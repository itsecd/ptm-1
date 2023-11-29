from dataclasses import dataclass, field
from typing import List

from customer_data_access import CustomerMatches
from model_objects import Customer, ExternalCustomer, CustomerType



class ConflictException(Exception):
    pass


class CustomerSync:

    def __init__(self, customer_data_access):
        self.customer_data_access = customer_data_access

    def sync_with_data_layer(self, external_customer):
        customer_matches: CustomerMatches
        if external_customer.isCompany:
            customer_matches = self.load_company(external_customer)
        else:
            customer_matches = self.load_person(external_customer)

        customer = customer_matches.customer

        if customer is None:
            customer = Customer()
            customer.externalId = external_customer.externalId
            customer.masterExternalId = external_customer.externalId

        self.populate_fields(external_customer, customer)

        created = False
        if customer.internal_id is None:
            customer = self.create_customer(customer)
            created = True
        else:
            self.update_customer(customer)

        self.update_contact_info(external_customer, customer)

        if customer_matches.has_duplicates:
            for duplicate in customer_matches.duplicates:
                self.update_duplicate(external_customer, duplicate)

        self.update_relations(external_customer, customer)
        self.update_preferred_store(external_customer, customer)

        return created


    def update_relations(self, external_customer: ExternalCustomer, customer: Customer):
        consumer_shopping_lists = external_customer.shoppingLists
        for consumer_shopping_list in consumer_shopping_lists:
            self.customer_data_access.update_shopping_list(customer, consumer_shopping_list)


    def update_customer(self, customer):
        return self.customer_data_access.update_customer_record(customer)


    def update_duplicate(self, external_customer: ExternalCustomer, duplicate: Customer):
        if duplicate is None:
            duplicate = Customer()
            duplicate.externalId = external_customer.externalId
            duplicate.masterExternalId = external_customer.externalId

        duplicate.name = external_customer.name

        if duplicate.internalId is None:
            self.create_customer(duplicate)
        else:
            self.update_customer(duplicate)


    def update_preferred_store(self, external_customer: ExternalCustomer, customer: Customer):
        customer.preferredStore = external_customer.preferredStore


    def create_customer(self, customer) -> Customer:
        return self.customer_data_access.create_customer_record(customer)


    def populate_fields(self, external_customer: ExternalCustomer, customer: Customer):
        customer.name = external_customer.name
        if external_customer.isCompany:
            customer.companyNumber = external_customer.companyNumber
            customer.customerType = CustomerType.COMPANY
        else:
            customer.customerType = CustomerType.PERSON


    def update_contact_info(self, external_customer: ExternalCustomer, customer: Customer):
        customer.address = external_customer.postalAddress


    def load_company(self, external_customer) -> CustomerMatches:
        external_id = external_customer.externalId
        company_number = external_customer.companyNumber

        customer_matches = self.customer_data_access.load_company_customer(external_id, company_number)

        if customer_matches.customer is not None and CustomerType.COMPANY != customer_matches.customer.customerType:
            raise ConflictException("Existing customer for externalCustomer {externalId} already exists and is not a company")

        if "ExternalId" == customer_matches.matchTerm:
            customer_company_number = customer_matches.customer.companyNumber
            if company_number != customer_company_number:
                customer_matches.customer.masterExternalId = None
                customer_matches.add_duplicate(customer_matches.customer)
                customer_matches.customer = None
                customer_matches.matchTerm = None

        elif "CompanyNumber" == customer_matches.matchTerm:
            customer_external_id = customer_matches.customer.externalId
            if customer_external_id is not None and external_id != customer_external_id:
                raise ConflictException(f"Existing customer for externalCustomer {company_number} doesn't match external id {external_id} instead found {customer_external_id}")

            customer = customer_matches.customer
            customer.externalId = external_id
            customer.masterExternalId = external_id
            customer_matches.addDuplicate(None)

        return customer_matches


    def load_person(self, external_customer):
        external_id = external_customer.externalId

        customer_matches = self.customer_data_access.load_person_customer(external_id)

        if customer_matches.customer is not None:
            if CustomerType.PERSON != customer_matches.customer.customerType:
                raise ConflictException(f"Existing customer for externalCustomer {external_id} already exists and is not a person")

            if "ExternalId" != customer_matches.matchTerm:
                customer = customer_matches.customer
                customer.externalId = external_id
                customer.masterExternalId = external_id

        return customer_matches
