from dataclasses import dataclass, field
from typing import List

from model_objects import Customer, ShoppingList, CustomerType, Address


class CustomerMatches:
    def __init__(self):
        self.matchTerm = None
        self.customer = None
        self.duplicates = []

    def has_duplicates(self) -> bool:
        return self.duplicates

    def add_duplicate(self, duplicate):
        self.duplicates.append(duplicate)


class CustomerDataAccess:
    def __init__(self, db):
        self.customerDataLayer = customer_data_layer(db)

    def load_company_customer(self, externalId, companyNumber) -> CustomerMatches:
        """Loads a company customer from the database based on
           the external ID or company number."""
        matches = customer_matches()
        matchByExternalId: Customer = 
                                     self.customerDataLayer.find_by_external_id(externalId)
        if matchByExternalId is not None:
            matches.customer = matchByExternalId
            matches.matchTerm = "ExternalId"
            matchByMasterId: Customer = 
                                       self.customerDataLayer.find_by_master_external_id(externalId)
            if matchByMasterId is not None:
                matches.add_duplicate(matchByMasterId)
        else:
            matchByCompanyNumber: Customer = 
                                            self.customerDataLayer.find_by_company_number(companyNumber)
            if matchByCompanyNumber is not None:
                matches.customer = matchByCompanyNumber
                matches.matchTerm = "CompanyNumber"

        return matches

    def load_person_customer(self, externalId) -> CustomerMatches:
        """ Loads a person customer from the database based on the external ID."""
        matches = customer_matches()
        matchByPersonalNumber: Customer = 
                                         self.customerDataLayer.find_by_external_id(externalId)
        matches.customer = matchByPersonalNumber
        if matchByPersonalNumber is not None:
            matches.matchTerm = "ExternalId"
        return matches

    def update_customer_record(self, customer):
        self.customerDataLayer.update_customer_record(customer)

    def create_customer_record(self, customer) -> int:
        return self.customerDataLayer.create_customer_record(customer)

    def update_shopping_list(self, customer: Customer, shoppingList: ShoppingList):
        customer.addShoppingList(shoppingList)
        self.customerDataLayer.update_shopping_list(shoppingList)
        self.customerDataLayer.update_customer_record(customer)


class customer_data_layer:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = self.conn.cursor()

    def find_by_external_id(self, externalId) -> Customer:
        """Finds a customer in the database based on the external ID."""
        self.cursor.execute(
                           'SELECT internalId, externalId, masterExternalId, name, customerType, companyNumber FROM customers WHERE externalId=?',
                           (externalId, ))
        customer = self._customer_from_sql_select_fields(self.cursor.fetchone())
        return customer

    def _find_address_id(self, customer) -> int:
        """Finds the address ID for a customer in the database."""
        self.cursor.execute('SELECT addressId FROM customers WHERE internalId=?', (customer.internalId,))
        (addressId,) = self.cursor.fetchone()
        if addressId:
            return int(addressId)
        return None

    def _customer_from_sql_select_fields(self, fields) -> Optional[Customer]:
        """Converts SQL select fields into a Customer object."""
        if not fields:
            return None

        customer = Customer(internalId=fields[0], externalId=fields[1], 
                           masterExternalId=fields[2], name=fields[3],
                           customerType=CustomerType(fields[4]), companyNumber=fields[5])
        addressId = self._find_address_id(customer)
        if addressId:
            self.cursor.execute(
                               'SELECT street, city, postalCode FROM addresses WHERE addressId=?',
                               (addressId, ))
            addresses = self.cursor.fetchone()
            if addresses:
                (street, city, postalCode) = addresses
                address = Address(street, city, postalCode)
                customer.address = address
        self.cursor.execute(
                           'SELECT shoppinglistId FROM customer_shoppinglists WHERE customerId=?', 
                           (customer.internalId,))
        shoppinglists = self.cursor.fetchall()
        for sl in shoppinglists:
            self.cursor.execute(
                              'SELECT products FROM shoppinglists WHERE shoppinglistId=?', 
                              (sl[0],))
            products_as_str = self.cursor.fetchone()
            products = products_as_str[0].split(", ")
            customer.addShoppingList(ShoppingList(products))
        return customer

    def find_by_master_external_id(self, masterExternalId) -> Optional[Customer]:
        self.cursor.execute(
                           'SELECT internalId, externalId, masterExternalId, name, customerType, companyNumber FROM customers WHERE masterExternalId=?',
                           (masterExternalId,))
        return self._customer_from_sql_select_fields(self.cursor.fetchone())

    def find_by_company_number(self, companyNumber) -> Optional[Customer]:
        self.cursor.execute(
                           'SELECT internalId, externalId, masterExternalId, name, customerType, companyNumber FROM customers WHERE companyNumber=?',
                           (companyNumber,))
        return self._customer_from_sql_select_fields(self.cursor.fetchone())

    def create_customer_record(self, customer) -> Customer:
        """Creates a new customer record in the database."""
        customer.internalId = self._next_id("customers")
        self.cursor.execute('INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?);', (
                            customer.internalId, customer.externalId, customer.masterExternalId, 
                            customer.name, customer.customerType.value, customer.companyNumber, None))
        if customer.address:
            addressId = self._next_id("addresses")
            self.cursor.execute('INSERT INTO addresses VALUES (?, ?, ?, ?)', (
                               addressId, customer.address.street, customer.address.city, 
                               customer.address.postalCode))
            self.cursor.execute('UPDATE customers set addressId=? WHERE internalId=?', 
                               (addressId, customer.internalId))

        if customer.shoppingLists:
            for sl in customer.shoppingLists:
                data = ", ".join(sl)
                self.cursor.execute(
                                   'SELECT shoppinglistId FROM shoppinglists WHERE products=?', (data,))
                shoppinglistId = self.cursor.fetchone()
                if not shoppinglistId:
                    shoppinglistId = self._next_id("shoppinglists")
                    self.cursor.execute('INSERT INTO shoppinglists VALUES (?, ?)', 
                                       (shoppinglistId, data))
                self.cursor.execute('INSERT INTO customer_shoppinglists VALUES (?, ?)',
                                   (customer.internalId, shoppinglistId))
        self.conn.commit()
        return customer

    def _next_id(self, tablename) -> int:
        """Retrieves the next available ID for a given table."""
        self.cursor.execute(f'SELECT MAX(ROWID) AS max_id FROM {tablename};')
        (id,) = self.cursor.fetchone()
        if id:
            return int(id) + 1
        else:
            return 1

    def update_customer_record(self, customer):
        """Updates a customer record in the database."""
        self.cursor.execute(
                           'Update customers set externalId=?, masterExternalId=?, name=?, customerType=?, companyNumber=? WHERE internalId=?',
                           (customer.externalId, customer.masterExternalId, customer.name, 
                           customer.customerType.value, customer.companyNumber, customer.internalId))
        if customer.address:
            addressId = self._find_address_id(customer)
            if not addressId:
                addressId = self._next_id("addresses")
                self.cursor.execute(
                                   'INSERT INTO addresses VALUES (?, ?, ?, ?)', 
                                   (addressId, customer.address.street, customer.address.city, 
                    customer.address.postalCode))
                self.cursor.execute(
                                   'UPDATE customers set addressId=? WHERE internalId=?', 
                                   (addressId, customer.internalId))

        self.cursor.execute('DELETE FROM customer_shoppinglists WHERE customerId=?', 
            (customer.internalId,))
        if customer.shoppingLists:
            for sl in customer.shoppingLists:
                products = ", ".join(sl.products)
                self.cursor.execute('SELECT shoppinglistId FROM shoppinglists WHERE products=?', 
                                   (products,))
                shoppinglistIds = self.cursor.fetchone()
                if shoppinglistIds is not None:
                    (shoppinglistId,) = shoppinglistIds
                    self.cursor.execute('INSERT INTO customer_shoppinglists VALUES (?, ?)',
                                       (customer.internalId, shoppinglistId))
                else:
                    shoppinglistId = self._next_id("shoppinglists")
                    self.cursor.execute('INSERT INTO shoppinglists VALUES (?, ?)', (shoppinglistId, products))
                    self.cursor.execute('INSERT INTO customer_shoppinglists VALUES (?, ?)', (customer.internalId, shoppinglistId))

        self.conn.commit()

    def update_shopping_list(self, shoppingList):
        pass