import unittest
from math_1 import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator(4,2)

    def tearDown(self) -> None:
        pass

    def test_add(self):
        self.assertEqual((self.calc.add()), 6)
    
    def test_sub(self):
        self.assertEqual(self.calc.sub(), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(),8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(), 2)


if __name__ == '__main__':
    unittest.main()