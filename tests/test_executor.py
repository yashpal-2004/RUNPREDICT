import unittest
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.executor import execute_code_snippet, generate_execution_trace, format_trace_table
from src.validation import compare_predictions, normalize_output


class TestExecutorAndPredictor(unittest.TestCase):

    def test_execute_code_snippet(self):
        code = "x = 5\ny = 10\nprint(x + y)"
        res = execute_code_snippet(code)
        self.assertIsNone(res["error"])
        self.assertEqual(res["output"].strip(), "15")

    def test_compare_predictions(self):
        pred = " 15 \n"
        actual = "15\n"
        self.assertTrue(compare_predictions(pred, actual))

    def test_generate_execution_trace(self):
        code = "a = 1\nfor i in range(2):\n    a += i"
        trace = generate_execution_trace(code)
        self.assertTrue(len(trace) > 0)

        tbl = format_trace_table(trace)
        self.assertIn("a", tbl)


if __name__ == "__main__":
    unittest.main()
