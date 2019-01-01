import unittest
from recursion import *


class TestRecurion(unittest.TestCase):

    def test_factorial(self):
        # Testing the factorial of 5
        expected = 5*4*3*2*1
        actual = factorial(5)
        self.assertEqual(expected, actual, "Something is wrong with our factorial")


if __name__ == '__main__':
    unittest.main()
