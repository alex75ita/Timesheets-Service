from entities.employee import Employee


class EmployeesManager:

    def __init__(self, userFacade):
        self.userFacade = userFacade

    @staticmethod
    def create(firstName, lastName):
        employee = Employee(firstName, lastName)
        return employee

    def save(self, employee):
        """

        :type employee: Employee
        """
        self.userFacade.save(employee)