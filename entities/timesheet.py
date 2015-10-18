from datetime import date

from entities.item import Item, Holiday, Permit


class Timesheet:

    def __init__(self, year, month, employee):
        self.year = year
        self.month = month
        self.employee = employee
        self.items = []

    @staticmethod
    def create_from_data(data):
        assert isinstance(data, dict)
        assert data.__contains__("year")
        assert data.__contains__("month")
        assert data.__contains__("employee")

        return Timesheet(data["year"], data["month"], data["employee"])

    def addItem(self, item):
        assert isinstance(item, Item)

        self.items.append(item)

    def addHoliday(self, when):
        """
        Add a holiday on item list
        :param when: date object
        """
        assert isinstance(when, date)

        item = Holiday(when)
        self.items.append(item)

    def addPermit(self, when, hours):
        assert isinstance(when, date)

        item = Permit(when, hours)
        self.items.append(item)