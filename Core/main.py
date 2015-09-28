import sys
from employeesManager import EmployeesManager


userFacade = None
employeesManager = EmployeesManager(userFacade)


def main():
    print("main")

    employee = employeesManager.create("Alessandro", "Piccione")
    employeesManager.save(employee)
    print("end")


if __name__ == "__main__":
    main()