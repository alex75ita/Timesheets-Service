import unittest
from unittest.mock import MagicMock

from core.employeesManager import EmployeesManager
from entities.employee import Employee
from providers.userProvider import UserProvider


class EmployeeManagerTest(unittest.TestCase):

    def test_ctor(self):
        provider = UserProvider()
        manager = EmployeesManager(provider)

        self.assertIsNotNone(manager)
        self.assertIsNotNone(manager.userFacade)

    def test_create(self):
        manager = self._getManagerInstance()

        firstName = "John"
        lastName = "Doe"
        employee = manager.create(firstName, lastName)

        self.assertIsNotNone(employee)
        self.assertEqual(firstName, employee.firstName)
        self.assertEqual(lastName, employee.lastName)

    def test_save_should_call_save_on_Facade(self):

        employee = self._getTestEmployee()

        #userFacadeMock = Mock(spec=UserFacade)

        provider = UserProvider()
        provider.save = MagicMock()
        manager = EmployeesManager(provider)
        manager.save(employee)

        # assert
        provider.save.asser_any_call()
        provider.save.assert_called_once_with(employee)

# private methods
    def _getManagerInstance(self):
        provider = UserProvider()
        manager = EmployeesManager(provider)
        return manager

    def _getTestEmployee(self):
        employee = Employee("John", "Doe")
        return employee
