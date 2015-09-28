import unittest
import tests.unitTests.employee_test

if __name__ == '__main__':
    #unittest.main(warnings='ignore')

    testSuite = unittest.defaultTestLoader.loadTestsFromModule(tests.unitTests.employee_test)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(testSuite)
