import unittest
from entities.employee import Employee


class EmployeeTest(unittest.TestCase):

    def Setup(self):
        pass

    def tearDown(self):
        pass

    def test_ctor(self):
        firstName = "John"
        lastName = "Doe"
        employee = Employee(firstName, lastName)
        self.assertEqual(firstName, employee.firstName, "firstName is not as expected")
        self.assertEqual(lastName, employee.lastName)

    def test_toJson(self):
        firstName = "John"
        lastName = "Doe"
        employee = Employee(firstName=firstName, lastName=lastName)
        doc = employee.toJson()
        self.assertIsNotNone(doc)
        self.assertIsInstance(doc, dict)
        self.assertIn("firstName", doc)
        self.assertEqual(firstName, doc["firstName"])
        self.assertIn("lastName", doc)
        self.assertEqual(lastName, doc["lastName"])
