import unittest

class Test_PrimeNumbers(unittest.TestCase):

    def setUp(self):
        print("Test initialization for test:", self._testMethodName)

    def tearDown(self):
        print("Test completion for test:", self._testMethodName)

    def test_Is_prime_odd_number(self):
        print("verify odd number is prime or not")
        self.assertTrue(self.is_prime(5))

    def test_is_prime_even_number(self):
        print("verify even number is prime or not")
        self.assertFalse(self.is_prime(40))

    def test_is_negative_number(self):
        print("verify negative number is prime or not")
        self.assertFalse(self.is_prime(-3))

    def is_prime(self, number):
        """"Check whether number is prime or not"""
        if number < 0:
            return False
        if number in [0, 1]:
            return False
        if number >= 2:
            for num in range(2, number):
                if number % num == 0:
                    return False
        return True
if __name__ == "__main__":
    unittest.main()
