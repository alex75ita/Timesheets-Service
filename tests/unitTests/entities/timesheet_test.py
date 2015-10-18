import unittest
from datetime import date

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

    def test_addHoliday_should_create_the_item(self):

        # add a "holiday" item to the Timesheet of an employee
        year = 2015
        month = 10
        day = 3
        when = date(year, month, day)
        employee = Employee("a", "b")
        timesheet = Timesheet(2015, 10, employee)


        timesheet.addHoliday(when)

        self.assertIsNotNone(timesheet.items)
        self.assertEqual(len(timesheet.items), 1)