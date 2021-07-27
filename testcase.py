import main, helper_functions, aeroplaneSeating
import unittest


class MyTestCase(unittest.TestCase):
    def testPrime(self):
        result = helper_functions.isPrime(3)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
