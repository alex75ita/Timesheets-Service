import unittest
from tests.unitTests.core import employeesManager_test
from tests.unitTests.entities import item_test, timesheet_test, employee_test
from tests.unitTests.consumers import addItemConsumer_test

import tests.integrationTests.userFacade_test
from tests.integrationTests.consumers import consumer_test


if __name__ == '__main__':
    #unittest.main(warnings='ignore')

    modules = [
        # unit tests
        tests.unitTests.entities.employee_test,
        tests.unitTests.entities.timesheet_test,
        tests.unitTests.entities.item_test,
        tests.unitTests.core.employeesManager_test,
        tests.unitTests.consumers.addItemConsumer_test,

        # integration tests
        tests.integrationTests.userFacade_test,
        tests.integrationTests.consumers.consumer_test,

        # add test module here
    ]

    testSuite = unittest.TestSuite()
    for module in modules:
        testSuite.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(testSuite)
