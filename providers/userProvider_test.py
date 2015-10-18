import unittest

from providers.userProvider import UserProvider
from entities.employee import Employee
from pymongo.mongo_client import MongoClient

configuration = dict(server="localhost", port=27017, database="timesheets_test")


class UserFacadeTest(unittest.TestCase):

    def setUp(self):
        self.userFacade = UserProvider(configuration)

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
        provider = UserProvider()
        self.assertIsNotNone(provider.configuration)
        self.assertIn("server", provider.configuration)
        self.assertIn("port", provider.configuration)
        self.assertIn("database", provider.configuration)

    def test_ctor_when_configuration_is_passed(self):
        conf = dict(server="localhost", port=27017, database="Timesheets_test")
        provider = UserProvider(configuration=conf)
        self.assertIsNotNone(provider.configuration)
        self.assertIn("server", provider.configuration)
        self.assertIn("port", provider.configuration)
        self.assertIn("database", provider.configuration)
        self.assertEqual(conf["server"], provider.configuration["server"])
        self.assertEqual(conf["port"], provider.configuration["port"])
        self.assertEqual(conf["database"], provider.configuration["database"])

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



