"""
Predictor Module for RUNPREDICT
Manages prediction submission, actual code execution invocation,
verification, and trace table formatting.
"""

from typing import Dict, Any, List
from src.executor import execute_code_snippet, generate_execution_trace, format_trace_table
from src.validation import compare_predictions, normalize_output


def process_prediction(
    code_str: str,
    user_prediction: str,
    used_hint: bool = False
) -> Dict[str, Any]:
    """
    Executes code_str, compares user prediction against actual output,
    and constructs execution trace.
    """
    exec_result = execute_code_snippet(code_str)
    actual_out = exec_result["output"]
    error = exec_result["error"]

    if error:
        is_correct = False
    else:
        is_correct = compare_predictions(user_prediction, actual_out)

    # Generate step-by-step variable trace table
    trace_history = generate_execution_trace(code_str)
    trace_table_str = format_trace_table(trace_history)

    return {
        "is_correct": is_correct,
        "user_prediction": normalize_output(user_prediction),
        "actual_output": normalize_output(actual_out),
        "raw_actual_output": actual_out,
        "error": error,
        "trace_table": trace_table_str,
        "used_hint": used_hint
    }
