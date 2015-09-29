import unittest
import tests.unitTests.employee_test
import tests.unitTests.timesheet_test
import tests.integrationTests.userFacade_test

if __name__ == '__main__':
    #unittest.main(warnings='ignore')

    modules = [
        tests.unitTests.employee_test,
        tests.unitTests.timesheet_test,
        tests.integrationTests.userFacade_test,
        # add test module here
    ]

    testSuite = unittest.TestSuite()
    for module in modules:
        testSuite.addTest(unittest.defaultTestLoader.loadTestsFromModule(module))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(testSuite)
