import unittest
from sum_calculator import add


class TestAddition(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_add_positive_and_negative(self):
        self.assertEqual(add(-5, 3), -2)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_add_decimal_numbers(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)


if __name__ == "__main__":
    unittest.main()