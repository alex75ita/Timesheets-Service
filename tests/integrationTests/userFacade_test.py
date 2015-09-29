from pathlib import _Accessor
import unittest
from facades.userFacade import UserFacade
from entities.employee import Employee
from pymongo.mongo_client import MongoClient


class userFacadeTests(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.userFacade = UserFacade()
        self.dbServer = "mongodb://localhost"
        self.dbPort = 27017
        self.dbName = "timesheets_test"
        #self.employeesCollectionName = "employees"

        client = MongoClient(self.dbServer, self.dbPort)
        db = client[self.dbName]
        db.employees.drop()

    def tearDown(self):
        print("tearDown")
        # delete database
        pass

    def test_save_should_create_record_in_database(self):
        employee = Employee("AAA", "CCC")
        self.userFacade.save(employee)
        #id = employee.Id
        #self.assertIsNotNone(id)
        #print(id)

        # Assert
        client = MongoClient(self.dbServer, self.dbPort)
        db = client[self.dbName]
        loaded_employee = db.employees.find_one({"firstName":"AAA"})
        self.assertIsNotNone(loaded_employee)

    def test_save_create_a_record_in_database(self):
        employee = Employee("AAA", "BBB")
        client = MongoClient(self.dbServer, self.dbPort)
        db = client[self.dbName]
        db.employees.insert_one(employee.toJson())

        # Assert
        loaded_employee = db.employees.find_one({"firstName":"AAA"})
        self.assertIsNotNone(loaded_employee)

    def test_connection(self):
        client = MongoClient(self.dbServer, self.dbPort)
        self.assertIsNotNone(client)

