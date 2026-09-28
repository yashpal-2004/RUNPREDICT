"""
Generator Module for RUNPREDICT
Generates randomized, parameterized Python code snippets across 4 difficulty levels.
"""

import json
import os
import random
from typing import Dict, Any, Tuple
from src.algorithms import (
    generate_loop_accumulator_code,
    generate_summation_code,
    generate_dedup_code,
    generate_gcd_code
)


DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
BANK_FILE = os.path.join(DATA_DIR, "question_bank.json")


def load_question_bank() -> Dict[str, Any]:
    """Loads the question bank JSON configuration."""
    if not os.path.exists(BANK_FILE):
        return {}
    try:
        with open(BANK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def generate_program_challenge(difficulty_level: int = 1) -> Dict[str, Any]:
    """
    Generates a dynamic Python code challenge for the target difficulty level (1 to 4).
    Returns dictionary with: code, category, hint, level.
    """
    bank = load_question_bank()
    level_key_map = {
        1: "level_1_basics",
        2: "level_2_control_flow",
        3: "level_3_algorithms",
        4: "level_4_collections"
    }

    key = level_key_map.get(difficulty_level, "level_1_basics")
    templates = bank.get(key, [])

    # 50% chance to generate algorithmic procedural code or template parameterization
    use_procedural = random.choice([True, False])

    if use_procedural or not templates:
        if difficulty_level == 1:
            code, cat = generate_loop_accumulator_code()
            hint = "Track variable updates loop by loop."
        elif difficulty_level == 2:
            code, cat = generate_summation_code()
            hint = "Calculates the sum of numbers from 1 to n."
        elif difficulty_level == 3:
            code, cat = generate_gcd_code()
            hint = "Euclid's algorithm computes the Greatest Common Divisor."
        else:
            code, cat = generate_dedup_code()
            hint = "Removes duplicate elements while preserving order."

        return {
            "code": code,
            "category": cat,
            "difficulty": difficulty_level,
            "hint": hint
        }

    # Parameterize template from JSON bank
    tpl_entry = random.choice(templates)
    template_str = tpl_entry["template"]
    param_ranges = tpl_entry.get("param_ranges", {})

    params = {}
    for param_name, bounds in param_ranges.items():
        if isinstance(bounds, list) and len(bounds) == 2 and isinstance(bounds[0], int):
            params[param_name] = random.randint(bounds[0], bounds[1])
        elif isinstance(bounds, list):
            params[param_name] = random.choice(bounds)
        else:
            params[param_name] = bounds

    try:
        code_str = template_str.format(**params)
    except Exception:
        code_str, _ = generate_loop_accumulator_code()

    return {
        "code": code_str,
        "category": tpl_entry.get("category", "Basics"),
        "difficulty": difficulty_level,
        "hint": tpl_entry.get("hint", "Analyze variable assignments carefully.")
    }
