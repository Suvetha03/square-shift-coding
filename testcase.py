import unittest
import helper_functions


class MyTestCase(unittest.TestCase):
    def testPrime1(self):
        result = helper_functions.isPrime(15)
        self.assertEqual(result, 0)

    def testPrime2(self):
        result = helper_functions.isPrime(7)
        self.assertEqual(result, 1)

    def testPrime3(self):
        result = helper_functions.isPrime(6)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
