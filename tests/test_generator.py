import unittest
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.generator import generate_program_challenge, load_question_bank


class TestGenerator(unittest.TestCase):

    def test_question_bank_loading(self):
        bank = load_question_bank()
        self.assertIn("level_1_basics", bank)
        self.assertIn("level_2_control_flow", bank)

    def test_generate_program_challenge_levels(self):
        for lvl in range(1, 5):
            ch = generate_program_challenge(difficulty_level=lvl)
            self.assertIn("code", ch)
            self.assertIn("category", ch)
            self.assertIn("hint", ch)
            self.assertTrue(len(ch["code"]) > 0)


if __name__ == "__main__":
    unittest.main()
