from unittest import TestCase
from datetime import date

# Importing the functions from input_util
from input_util import get_int, get_int_range, get_date


class TestInputUtils(TestCase):
    """Testing cases for input utility functions."""

    # Testing get_int() function
    def test_get_int_valid_number(self):
        """Testing get_int with valid integer string."""
        self.assertEqual(get_int("5"), 5)
        self.assertEqual(get_int("0"), 0)
        self.assertEqual(get_int("-10"), -10)
        self.assertEqual(get_int("123456"), 123456)

    def test_get_int_invalid_number(self):
        """Testing get_int with invalid input."""
        self.assertIsNone(get_int("abc"))
        self.assertIsNone(get_int("12.34"))
        self.assertIsNone(get_int(""))
        self.assertIsNone(get_int("123abc"))

    # Testing get_int_range() function
    def test_get_int_range_valid_within_range(self):
        """Testing get_int_range with valid number within range."""
        self.assertEqual(get_int_range("3", 1, 5), 3)
        self.assertEqual(get_int_range("1", 1, 10), 1)  # Lower bound
        self.assertEqual(get_int_range("10", 1, 10), 10)  # Upper bound

    def test_get_int_range_valid_outside_range(self):
        """Testing get_int_range with valid number outside range."""
        self.assertIsNone(get_int_range("0", 1, 5))  # Below range
        self.assertIsNone(get_int_range("6", 1, 5))  # Above range
        self.assertIsNone(get_int_range("-1", 1, 5))  # Negative below range

    def test_get_int_range_invalid_input(self):
        """Testing get_int_range with invalid input."""
        self.assertIsNone(get_int_range("abc", 1, 5))
        self.assertIsNone(get_int_range("", 1, 5))
        self.assertIsNone(get_int_range("12.34", 1, 5))

    # Testing get_date() function
    def test_get_date_valid_date(self):
        """Testing get_date with valid date string."""
        expected_date = date(2025, 10, 30)
        self.assertEqual(get_date("10/30/2025"), expected_date)

        # Testing with leading zeros
        self.assertEqual(get_date("01/01/2024"), date(2024, 1, 1))
        self.assertEqual(get_date("12/31/2023"), date(2023, 12, 31))

    def test_get_date_invalid_year_length(self):
        """Testing get_date with invalid year length."""
        self.assertIsNone(get_date("10/30/25"))  # 2-digit year
        self.assertIsNone(get_date("10/30/20256"))  # 5-digit year

    def test_get_date_invalid_month_day_length(self):
        """Testing get_date with invalid month/day length."""
        self.assertIsNone(get_date("9/25/2025"))  # Single digit month
        self.assertIsNone(get_date("09/2/2025"))  # Single digit day
        self.assertIsNone(get_date("009/025/2025"))  # Triple digits

    def test_get_date_invalid_format(self):
        """Testing get_date with invalid format."""
        self.assertIsNone(get_date("2025/10/30"))  # Wrong order
        self.assertIsNone(get_date("30-10-2025"))  # Wrong separators
        self.assertIsNone(get_date("10.30.2025"))  # Wrong separators

    def test_get_date_invalid_separators(self):
        """Testing get_date with invalid separator placement."""
        self.assertIsNone(get_date("10-30/2025"))  # Mixed separators
        self.assertIsNone(get_date("10/30-2025"))  # Mixed separators
        self.assertIsNone(get_date("10 30 2025"))  # Space separators

    def test_get_date_invalid_characters(self):
        """Testing get_date with non-numeric characters."""
        self.assertIsNone(get_date("aa/bb/cccc"))  # All letters
        self.assertIsNone(get_date("1a/30/2025"))  # Letter in month
        self.assertIsNone(get_date("10/3b/2025"))  # Letter in day
        self.assertIsNone(get_date("10/30/2o25"))  # Letter in year

    def test_get_date_invalid_month_values(self):
        """Test get_date with invalid month values."""
        self.assertIsNone(get_date("13/30/2025"))  # Month > 12
        self.assertIsNone(get_date("00/30/2025"))  # Month = 0
        self.assertIsNone(get_date("-1/30/2025"))  # Negative month

    def test_get_date_invalid_day_values(self):
        """Testing get_date with invalid day values."""
        self.assertIsNone(get_date("10/32/2025"))  # Day > 31 for Oct
        self.assertIsNone(get_date("02/30/2025"))  # Day > 28/29 for Feb
        self.assertIsNone(get_date("10/00/2025"))  # Day = 0
        self.assertIsNone(get_date("10/-1/2025"))  # Negative day

    def test_get_date_valid_edge_cases(self):
        """Testing get_date with edge case valid dates."""
        # Leap year
        self.assertEqual(get_date("02/29/2024"), date(2024, 2, 29))
        # Non-leap year Feb 28
        self.assertEqual(get_date("02/28/2023"), date(2023, 2, 28))