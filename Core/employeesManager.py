from entities.employee import Employee

class EmployeesManager:

    def __init__(self, userFacade):
        self.userFacade = userFacade

    def create(self, firstName, lastName):
        employee = Employee(firstName, lastName)
        return employee

    def save(self, employee):
        """

        :type employee: Employee
        """
        self.userFacade.save(employee)