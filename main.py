from core.employeesManager import EmployeesManager
from core.sender import Sender

userFacade = None
employeesManager = EmployeesManager(userFacade)


def main():
    print("main")

    try:
        sender = Sender()
        sender.testConnection()

    except:
        print("Some error occurs sending message.")
        raise

    return

    employee = employeesManager.create("John", "Doe")
    employeesManager.save(employee)
    print("end")


if __name__ == "__main__":
    main()
