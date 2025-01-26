import unittest
from calculator import button_click, calculate

class TestCalculator(unittest.TestCase):
    def test_square_root(self):
        """Test square root functionality."""
        # Simulate entering '√25'
        expression = button_click('√', '')  # Start with empty input and append '√'
        expression = button_click('2', expression)  # Append '2'
        expression = button_click('5', expression)  # Append '5'

        # Calculate the result
        result = calculate(expression)

        # Check if the result is correct (should be 5.0)
        self.assertEqual(result, '5.0')

    def test_invalid_square_root(self):
        """Test invalid square root input."""
        # Simulate entering '√-25'
        expression = button_click('√', '')  # Start with empty input and append '√'
        expression = button_click('-', expression)  # Append '-'
        expression = button_click('2', expression)  # Append '2'
        expression = button_click('5', expression)  # Append '5'

        # Calculate the result
        result = calculate(expression)

        # Check if the result is "Error" for invalid square root operation
        self.assertEqual(result, "Error")

if __name__ == '__main__':
    unittest.main()
