from datetime import date


class Timesheet:

    def __init__(self, year, month, employee):
        self.year = year
        self.month = month
        self.employee = employee

    @staticmethod
    def create_from_data(data):
        assert isinstance(data, dict)
        assert data.__contains__("year")
        assert data.__contains__("month")
        assert data.__contains__("employee")

        return Timesheet(data["year"], data["month"], data["employee"])


