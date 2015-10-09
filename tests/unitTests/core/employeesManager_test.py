import unittest
from unittest.mock import MagicMock
from core.employeesManager import EmployeesManager
from entities.employee import Employee
from facades.userFacade import UserFacade


class EmployeeManagerTest(unittest.TestCase):

    def test_ctor(self):
        userFacade_ = UserFacade()
        manager = EmployeesManager(userFacade_)

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

        userFacade_ = UserFacade()
        userFacade_.save = MagicMock()
        manager = EmployeesManager(userFacade_)
        manager.save(employee)

        # assert
        userFacade_.save.asser_any_call()
        userFacade_.save.assert_called_once_with(employee)

# private methods
    def _getManagerInstance(self):
        userFacade = UserFacade()
        manager = EmployeesManager(userFacade)
        return manager

    def _getTestEmployee(self):
        employee = Employee("John", "Doe")
        return employee
