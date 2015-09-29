import unittest
from entities.timesheet import Timesheet
from entities.employee import Employee


class TimesheetTest(unittest.TestCase):

    def test_ctor(self):
        year = 2015
        month = 9
        firstName = "John"
        lastName = "Doe"
        employee = Employee(firstName, lastName)
        timesheet = Timesheet(2015, 9, employee)
        self.assertIsNotNone(timesheet)
        self.assertEqual(year, timesheet.year)
        self.assertEqual(month, timesheet.month)
        self.assertIsNotNone(timesheet.employee)
        self.assertEqual(firstName, timesheet.employee.firstName)
        self.assertEqual(lastName, timesheet.employee.lastName)

    def test_create_from_data(self):
        year = 2015
        month = 9
        firstName = "John"
        lastName = "Doe"
        employee = Employee(firstName, lastName)
        data = {
            "year": year,
            "month": month,
            "employee": employee,
        }

        timesheet = Timesheet.create_from_data(data)

        self.assertIsNotNone(timesheet)