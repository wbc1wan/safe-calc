import unittest
import warnings
from unittest.mock import patch
from simpleeval import InvalidExpression, FunctionNotDefined, MultipleExpressions
from safe_calculator import evaluate_expression, main


class TestSafeCalculatorLogic(unittest.TestCase):

    def test_basic_operations(self):
        """Test normal arithmetic operations."""
        cases = [
            ("2 + 3", 5),
            ("7 - 4", 3),
            ("2 * 3", 6),
            ("10 / 4", 2.5),
            ("10 % 3", 1),
            ("10 // 3", 3),
            ("2 ** 3", 8),
        ]
        for expr, expected in cases:
            with self.subTest(expr=expr):
                self.assertEqual(evaluate_expression(expr), expected)

    def test_invalid_input(self):
        """Test invalid expressions trigger appropriate exceptions."""
        cases = ["2 +", "a + 3", "unknown_func(2)"]
        for expr in cases:
            with self.subTest(expr=expr):
                with self.assertRaises((InvalidExpression, FunctionNotDefined, NameError, SyntaxError)):
                    evaluate_expression(expr)

    def test_division_by_zero(self):
        """Test division by zero raises ZeroDivisionError."""
        for expr in ["10 / 0", "10 // 0", "10 % 0"]:
            with self.subTest(expr=expr):
                with self.assertRaises(ZeroDivisionError):
                    evaluate_expression(expr)

    def test_malicious_code(self):
        """Ensure code injection attempts raise InvalidExpression."""
        expr = "import os; os.system('ls')"
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=MultipleExpressions)
            with self.assertRaises(InvalidExpression):
                evaluate_expression(expr)


class TestSafeCalculatorCLI(unittest.TestCase):

    @patch("builtins.input")
    @patch("builtins.print")
    def test_exit_command(self, mock_print, mock_input):
        """Test that CLI handles 'exit' command correctly."""
        mock_input.side_effect = ["exit"]
        main()
        mock_print.assert_any_call("Safe Calculator — type 'exit' to quit.")
        mock_print.assert_any_call("Goodbye!")

    @patch("builtins.input")
    @patch("builtins.print")
    def test_valid_expression_output(self, mock_print, mock_input):
        """Test that CLI correctly prints the result of a valid expression."""
        mock_input.side_effect = ["2 + 3", "exit"]
        main()
        mock_print.assert_any_call("Result:", 5)

    @patch("builtins.input")
    @patch("builtins.print")
    def test_specific_error_printed(self, mock_print, mock_input):
        """Test CLI prints for known expression errors."""
        mock_input.side_effect = ["unknown_func(1)", "exit"]
        main()
        self.assertTrue(
            any(str(arg).startswith("Error: Invalid expression or operation")
                for call_args, _ in mock_print.call_args_list
                for arg in call_args),
            msg="CLI did not print expected specific error"
        )

    @patch("builtins.input")
    @patch("builtins.print")
    @patch("safe_calculator.evaluate_expression", side_effect=Exception("generic error"))
    def test_generic_error_printed(self, mock_eval, mock_print, mock_input):
        """Test CLI prints for generic exceptions."""
        mock_input.side_effect = ["anything", "exit"]
        main()
        self.assertTrue(
            any(str(arg).startswith("Error:")
                for call_args, _ in mock_print.call_args_list
                for arg in call_args),
            msg="CLI did not print expected generic error"
        )


if __name__ == "__main__":
    unittest.main()
