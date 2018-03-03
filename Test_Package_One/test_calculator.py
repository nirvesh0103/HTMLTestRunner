import unittest
import time

class Test_Calculator(unittest.TestCase):

    def setUp(self):
        pass

    def test_addition(self):
        """ Verify the addition is working."""
        numberslist = [1, 5, 47, 56, 24]
        add = 0
        for num in numberslist:
            add += num
        addition, mul = self.calculation(1,5,47,56,24, addition=True)
        self.assertEqual(add, addition, "addition not working")

    def test_mutliplication(self):
        """ Verify the multiplication is working."""
        numberslist = [16,16]
        mul = 1
        for num in numberslist:
            mul *= num
        add, multiplication = self.calculation(16,16, multiplication =True)
        self.assertEqual(mul, multiplication, "multiplication not working")

    def tearDown(self):
        pass

    def calculation(self, *numbers, addition = None, multiplication = None):
        num_addition = 0
        # time.sleep(2)
        if addition == True:
            for num in numbers:
                num_addition += num
            print("Addition: ", num_addition)
        num_multiplication = 1
        if multiplication == True:
            for num in numbers:
                num_multiplication *= num
            print("Multiplication: ", num_multiplication)
        return num_addition, num_multiplication

if __name__ == '__main__':
    unittest.main()
