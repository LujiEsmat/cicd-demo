from calculator import add

def test_add():
    actual = add(5, 3)
    expected = 8

    assert actual == expected
    aimport unittest[cite: 2]

from calculator import calculate[cite: 2]


class TestCalculator(unittest.TestCase):[cite: 2]

    # Addition tests
    def test_addition_positive_numbers(self):[cite: 2]
        self.assertEqual(calculate(5, 3, "+"), 8)[cite: 2]

    def test_addition_negative_numbers(self):[cite: 2]
        self.assertEqual(calculate(-5, -3, "+"), -8)[cite: 2]

    def test_addition_positive_and_negative(self):[cite: 2]
        self.assertEqual(calculate(-5, 3, "+"), -2)[cite: 2]

    def test_addition_with_zero(self):[cite: 2]
        self.assertEqual(calculate(5, 0, "+"), 5)[cite: 2]

    def test_addition_decimal_numbers(self):[cite: 2]
        self.assertAlmostEqual(calculate(1.5, 2.5, "+"), 4.0)[cite: 2]

    # Subtraction tests
    def test_subtraction_positive_numbers(self):[cite: 2]
        self.assertEqual(calculate(8, 3, "-"), 5)[cite: 2]

    def test_subtraction_result_is_negative(self):[cite: 2]
        self.assertEqual(calculate(3, 8, "-"), -5)[cite: 2]

    def test_subtraction_negative_numbers(self):[cite: 2]
        self.assertEqual(calculate(-3, -8, "-"), 5)[cite: 2]

    def test_subtraction_with_zero(self):[cite: 2]
        self.assertEqual(calculate(5, 0, "-"), 5)[cite: 2]

    def test_subtraction_decimal_numbers(self):[cite: 2]
        self.assertAlmostEqual(calculate(2.5, 1.5, "-"), 1.0)[cite: 2]

    # Multiplication tests
    def test_multiplication_positive_numbers(self):[cite: 2]
        self.assertEqual(calculate(4, 3, "*"), 12)[cite: 2]

    def test_multiplication_negative_numbers(self):[cite: 2]
        self.assertEqual(calculate(-4, 3, "*"), -12)[cite: 2]

    def test_multiplication_with_zero(self):[cite: 2]
        self.assertEqual(calculate(10, 0, "*"), 0)[cite: 2]

    def test_multiplication_decimal_numbers(self):[cite: 2]
        self.assertAlmostEqual(calculate(1.5, 2, "*"), 3.0)[cite: 2]

    # Division tests
    def test_division_exact_result(self):[cite: 2]
        self.assertEqual(calculate(8, 2, "/"), 4)[cite: 2]

    def test_division_decimal_result(self):[cite: 2]
        self.assertEqual(calculate(7, 2, "/"), 3.5)[cite: 2]

    def test_division_negative_number(self):[cite: 2]
        self.assertEqual(calculate(-8, 2, "/"), -4)[cite: 2]

    def test_division_by_zero_raises_error(self):[cite: 2]
        with self.assertRaises(ZeroDivisionError):[cite: 2]
            calculate(10, 0, "/")[cite: 2]

    # Invalid operations and inputs "Negative Testing"
    def test_unsupported_operation_raises_error(self):[cite: 2]
        with self.assertRaises(ValueError):[cite: 2]
            calculate(5, 2, "//")[cite: 2]

    def test_empty_operation_raises_error(self):[cite: 2]
        with self.assertRaises(ValueError):[cite: 2]
            calculate(5, 2, "")[cite: 2]

    def test_string_operand_raises_error(self):[cite: 2]
        with self.assertRaises(TypeError):[cite: 2]
            calculate("5", 2, "+")[cite: 2]

    def test_none_operand_raises_error(self):[cite: 2]
        with self.assertRaises(TypeError):[cite: 2]
            calculate(None, 2, "+")[cite: 2]

    def test_boolean_operand_raises_error(self):[cite: 2]
        with self.assertRaises(TypeError):[cite: 2]
            calculate(True, 2, "+")[cite: 2]


if __name__ == "__main__":[cite: 2]
    unittest.main()[cite: 2]