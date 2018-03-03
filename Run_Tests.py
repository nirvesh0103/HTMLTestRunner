import HTMLTestRunner
import unittest
from unittest import TestLoader
from Test_Package_2 import *
from unittest import TestResult
from Test_Package_One import test_calculator, test_primenumbers
from Test_Package_One.test_primenumbers import *
from Test_Package_One.test_calculator import *

class run_tests(object):

    def main(self):
        loader = TestLoader()
        suite = unittest.TestSuite()

        print(loader.loadTestsFromModule(test_calculator))
        print(loader.loadTestsFromModule(test_primenumbers))

        print(loader.loadTestsFromTestCase(Test_Calculator))
        print(loader.loadTestsFromTestCase(Test_PrimeNumbers))

        suite.addTests(loader.loadTestsFromModule(test_primenumbers))

        loader.discover("Test_Package_One","test*.py")
        suite.addTests(loader.discover("Test_Package_One"))
        runner = unittest.TextTestRunner()
        runner.run(suite)

    def HTMLMain(self):
        loader = TestLoader()
        package_list = ["Test_Package_2","Test_Package_One"]

        for package in package_list:
            print("package: ", package)
            suite = unittest.TestSuite()
            suite.addTests(loader.discover(package, "test_*.py", top_level_dir="../"))
            file_name = package + '_report.html'
            print(file_name)
            output = open(file_name, 'wb')
            runner = HTMLTestRunner.HTMLTestRunner(stream=output, verbosity=1, appVersion="1.1", dirTestScreenshots=None, title="Test report for module: "+package)
            runner.run(suite)

if __name__ == "__main__":
    run_tests().HTMLMain()
