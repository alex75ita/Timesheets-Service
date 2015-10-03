import unittest

import tests.unitTests.entities.employee_test
from tests.unitTests.core import employeesManager_test
import tests.unitTests.entities.timesheet_test
import tests.integrationTests.userFacade_test

if __name__ == '__main__':
    #unittest.main(warnings='ignore')

    modules = [
        # unit tests
        tests.unitTests.entities.employee_test,
        tests.unitTests.entities.timesheet_test,
        tests.unitTests.core.employeesManager_test,
        # integration tests
        tests.integrationTests.userFacade_test,

        # add test module here
    ]

    testSuite = unittest.TestSuite()
    for module in modules:
        testSuite.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(testSuite)
