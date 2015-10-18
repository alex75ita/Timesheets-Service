import unittest

import providers.userProvider_test

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
        providers.userProvider_test,
        tests.integrationTests.consumers.consumer_test,

        # add test module here
    ]

    testSuite = unittest.TestSuite()
    for module in modules:
        testSuite.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(testSuite)
