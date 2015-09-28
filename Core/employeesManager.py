from employee import Employee

__author__ = 'alex'


class EmployeesManager:

    def __init__(self, userFacade):
        self.userFacade = userFacade

    def create(self, firstName, lastName):
        employee = Employee(firstName, lastName)
        return employee

    def save(self,f,):
        """

        :type employee: Employee
        """
        self.userFacade.save(employee)