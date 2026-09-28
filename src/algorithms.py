"""
Algorithms Module for RUNPREDICT
Provides code generation algorithms and dynamic Python code templates.
"""

import random
from typing import Dict, Any, Tuple


def generate_loop_accumulator_code() -> Tuple[str, str]:
    """Generates a dynamic loop accumulator code snippet."""
    x_init = random.randint(1, 5)
    y_init = random.randint(5, 15)
    steps = random.randint(2, 4)
    dec = random.randint(1, 2)

    code = (
        f"x = {x_init}\n"
        f"y = {y_init}\n\n"
        f"for i in range({steps}):\n"
        f"    x = x + i\n"
        f"    y = y - {dec}\n\n"
        f"print(x)\n"
        f"print(y)"
    )
    category = "Control Flow"
    return code, category


def generate_summation_code() -> Tuple[str, str]:
    """Generates dynamic summation code snippet."""
    n = random.randint(3, 6)
    code = (
        f"n = {n}\n"
        f"total = 0\n\n"
        f"for i in range(1, n + 1):\n"
        f"    total += i\n\n"
        f"print(total)"
    )
    return code, "Algorithms"


def generate_dedup_code() -> Tuple[str, str]:
    """Generates dynamic list duplicate removal code snippet."""
    base_nums = random.choice([
        [3, 7, 3, 2, 7, 9],
        [1, 5, 2, 5, 1, 8],
        [4, 4, 2, 9, 2, 1]
    ])
    code = (
        f"numbers = {base_nums}\n\n"
        f"result = []\n"
        f"for x in numbers:\n"
        f"    if x not in result:\n"
        f"        result.append(x)\n\n"
        f"print(result)"
    )
    return code, "Collections"


def generate_gcd_code() -> Tuple[str, str]:
    """Generates dynamic Euclidean GCD snippet."""
    mult = random.randint(2, 6)
    a_val = random.randint(3, 8) * mult
    b_val = random.randint(2, 5) * mult

    code = (
        f"a = {a_val}\n"
        f"b = {b_val}\n\n"
        f"while b != 0:\n"
        f"    a, b = b, a % b\n\n"
        f"print(a)"
    )
    return code, "Algorithms"
