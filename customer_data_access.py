from dataclasses import dataclass, field
from typing import List

from model_objects import Customer, ShoppingList, CustomerType, Address


class CustomerMatches:
    def __init__(self):
        self.matchTerm = None
        self.customer = None
        self.duplicates = []

    def has_duplicates(self):
        return self.duplicates

    def add_duplicate(self, duplicate):
        self.duplicates.append(duplicate)


class CustomerDataAccess:
    def __init__(self, db):
        self.customer_data_layer = CustomerDataLayer(db)

    def load_company_customer(self, external_id, company_number):
        matches = CustomerMatches()
        match_by_external_id: Customer = self.customer_data_layer.find_by_external_id(external_id)
        if match_by_external_id is not None:
            matches.customer = match_by_external_id
            matches.matchTerm = "ExternalId"
            match_by_master_id: Customer = self.customer_data_layer.find_by_master_external_id(external_id)
            if match_by_master_id is not None:
                matches.add_duplicate(match_by_master_id)
        else:
            match_by_company_number: Customer = self.customer_data_layer.find_by_company_number(company_number)
            if match_by_company_number is not None:
                matches.customer = match_by_company_number
                matches.matchTerm = "CompanyNumber"

        return matches

    def load_person_customer(self, external_id):
        matches = CustomerMatches()
        match_by_personal_number: Customer = self.customer_data_layer.find_by_external_id(external_id)
        matches.customer = match_by_personal_number
        if match_by_personal_number is not None:
            matches.matchTerm = "ExternalId"
        return matches

    def update_customer_record(self, customer):
        self.customer_data_layer.update_customer_record(customer)

    def create_customer_record(self, customer):
        return self.customer_data_layer.create_customer_record(customer)

    def update_shopping_list(self, customer: Customer, shopping_list: ShoppingList):
        customer.addShoppingList(shopping_list)
        self.customer_data_layer.update_shopping_list(shopping_list)
        self.customer_data_layer.update_customer_record(customer)


class CustomerDataLayer:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def find_by_external_id(self, external_id):
        self.cursor.execute(
            'SELECT internalId, externalId, masterExternalId, name, customerType, companyNumber FROM customers WHERE externalId=?',
            (external_id,))
        customer = self._customer_from_sql_select_fields(self.cursor.fetchone())
        return customer

    def _find_address_id(self, customer):
        self.cursor.execute('SELECT addressId FROM customers WHERE internalId=?', (customer.internal_id,))
        (address_id,) = self.cursor.fetchone()
        if address_id:
            return int(address_id)
        return None

    def _customer_from_sql_select_fields(self, fields):
        if not fields:
            return None

        customer = Customer(internalId=fields[0], externalId=fields[1], masterExternalId=fields[2], name=fields[3],
                        customerType=CustomerType(fields[4]), companyNumber=fields[5])
        address_id = self._find_address_id(customer)
        if address_id:
            self.cursor.execute('SELECT street, city, postalCode FROM addresses WHERE addressId=?',
                                          (address_id, ))
            addresses = self.cursor.fetchone()
            if addresses:
                (street, city, postalCode) = addresses
                address = Address(street, city, postalCode)
                customer.address = address
        self.cursor.execute('SELECT shoppinglistId FROM customer_shoppinglists WHERE customerId=?', (customer.internal_id,))
        shoppinglists = self.cursor.fetchall()
        for sl in shoppinglists:
            self.cursor.execute('SELECT products FROM shoppinglists WHERE shoppinglistId=?', (sl[0],))
            products_as_str = self.cursor.fetchone()
            products = products_as_str[0].split(", ")
            customer.addShoppingList(ShoppingList(products))
        return customer

    def find_by_master_external_id(self, master_external_id):
        self.cursor.execute(
            'SELECT internalId, externalId, masterExternalId, name, customerType, companyNumber FROM customers WHERE masterExternalId=?',
            (master_external_id,))
        return self._customer_from_sql_select_fields(self.cursor.fetchone())

    def find_by_company_number(self, company_number):
        self.cursor.execute(
            'SELECT internalId, externalId, masterExternalId, name, customerType, companyNumber FROM customers WHERE companyNumber=?',
            (company_number,))
        return self._customer_from_sql_select_fields(self.cursor.fetchone())

    def create_customer_record(self, customer):
        customer.internal_id = self._nextid("customers")
        self.cursor.execute('INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?);', (
            customer.internal_id, customer.externalId, customer.masterExternalId, customer.name, customer.customerType.value,
            customer.companyNumber, None))
        if customer.address:
            address_id = self._nextid("addresses")
            self.cursor.execute('INSERT INTO addresses VALUES (?, ?, ?, ?)', (
                address_id, customer.address.street, customer.address.city, customer.address.postalCode))
            self.cursor.execute('UPDATE customers set addressId=? WHERE internalId=?', (address_id, customer.internal_id))

        if customer.shoppingLists:
            for sl in customer.shoppingLists:
                data = ", ".join(sl)
                self.cursor.execute('SELECT shoppinglistId FROM shoppinglists WHERE products=?', (data,))
                shoppinglist_id = self.cursor.fetchone()
                if not shoppinglist_id:
                    shoppinglist_id = self._nextid("shoppinglists")
                    self.cursor.execute('INSERT INTO shoppinglists VALUES (?, ?)', (shoppinglist_id, data))
                self.cursor.execute('INSERT INTO customer_shoppinglists VALUES (?, ?)', (customer.internal_id, shoppinglist_id))
        self.conn.commit()
        return customer

    def _nextid(self, tablename):
        self.cursor.execute(f'SELECT MAX(ROWID) AS max_id FROM {tablename};')
        (id,) = self.cursor.fetchone()
        if id:
            return int(id) + 1
        else:
            return 1

    def update_customer_record(self, customer):
        self.cursor.execute(
            'Update customers set externalId=?, masterExternalId=?, name=?, customerType=?, companyNumber=? WHERE internalId=?',
            (customer.externalId, customer.masterExternalId, customer.name, customer.customerType.value,
                customer.companyNumber, customer.internal_id))
        if customer.address:
            address_id = self._find_address_id(customer)
            if not address_id:
                address_id = self._nextid("addresses")
                self.cursor.execute('INSERT INTO addresses VALUES (?, ?, ?, ?)', (address_id, customer.address.street, customer.address.city, customer.address.postalCode))
                self.cursor.execute('UPDATE customers set addressId=? WHERE internalId=?', (address_id, customer.internal_id))

        self.cursor.execute('DELETE FROM customer_shoppinglists WHERE customerId=?', (customer.internal_id,))
        if customer.shoppingLists:
            for sl in customer.shoppingLists:
                products = ", ".join(sl.products)
                self.cursor.execute('SELECT shoppinglistId FROM shoppinglists WHERE products=?', (products,))
                shopping_list_ids = self.cursor.fetchone()
                if shopping_list_ids is not None:
                    (shoppinglist_id,) = shopping_list_ids
                    self.cursor.execute('INSERT INTO customer_shoppinglists VALUES (?, ?)',
                                        (customer.internal_id, shoppinglist_id))
                else:
                    shoppinglist_id = self._nextid("shoppinglists")
                    self.cursor.execute('INSERT INTO shoppinglists VALUES (?, ?)', (shoppinglist_id, products))
                    self.cursor.execute('INSERT INTO customer_shoppinglists VALUES (?, ?)', (customer.internal_id, shoppinglist_id))

        self.conn.commit()

    def update_shopping_list(self, shopping_list):
        pass
