from pathlib import _Accessor
import unittest
from facades.userFacade import UserFacade
from entities.employee import Employee
from pymongo.mongo_client import MongoClient

configuration = dict(server="localhost", port=27017, database="timesheets_test")


class userFacadeTests(unittest.TestCase):

    def setUp(self):
        self.userFacade = UserFacade(configuration)

        # clean database
        client = MongoClient(configuration["server"], configuration["port"])
        db = client[configuration["database"]]
        db.employees.drop()

    def tearDown(self):
        # delete database
        pass

    def test_connection(self):
        client = MongoClient(configuration["server"], configuration["port"])
        self.assertIsNotNone(client)

    def test_ctor_when_empty(self):
        facade = UserFacade()
        self.assertIsNotNone(facade.configuration)
        self.assertIn("server", facade.configuration)
        self.assertIn("port", facade.configuration)
        self.assertIn("database", facade.configuration)

    def test_ctor_when_configuration_is_passed(self):
        conf = dict(server="localhost", port=27017, database="Timesheets_test")
        facade = UserFacade(configuration=conf)
        self.assertIsNotNone(facade.configuration)
        self.assertIn("server", facade.configuration)
        self.assertIn("port", facade.configuration)
        self.assertIn("database", facade.configuration)
        self.assertEqual(conf["server"], facade.configuration["server"])
        self.assertEqual(conf["port"], facade.configuration["port"])
        self.assertEqual(conf["database"], facade.configuration["database"])

    def test_save_should_create_record_in_database(self):
        firstName = "AAA"
        employee = Employee(firstName, "CCC")
        self.userFacade.save(employee)

        # Assert
        client = MongoClient(configuration["server"], configuration["port"])
        db = client[configuration["database"]]
        loaded_employee = db.employees.find_one({"firstName": firstName})
        self.assertIsNotNone(loaded_employee)
        self.assertIn("firstName", loaded_employee)
        self.assertEqual(firstName, loaded_employee["firstName"])



