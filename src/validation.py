"""
Validation Module for RUNPREDICT
Handles string normalization, prediction matching, and CLI input parsing.
"""

from typing import Optional, List


def normalize_output(text: str) -> str:
    """
    Normalizes printed output string for flexible comparison.
    Trims leading/trailing whitespace and normalizes line endings.
    """
    if text is None:
        return ""
    lines = [line.strip() for line in text.strip().splitlines() if line.strip() != ""]
    return "\n".join(lines)


def compare_predictions(user_prediction: str, actual_output: str) -> bool:
    """
    Compares normalized user prediction string against actual execution output string.
    """
    norm_user = normalize_output(user_prediction)
    norm_actual = normalize_output(actual_output)
    return norm_user == norm_actual


def parse_integer_input(input_str: str) -> Optional[int]:
    """Safely converts string to int."""
    if not input_str:
        return None
    try:
        return int(input_str.strip())
    except ValueError:
        return None
