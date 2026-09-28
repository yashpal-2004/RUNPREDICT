import unittest
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.scoring import ScoreTracker


class TestScoring(unittest.TestCase):

    def test_score_tracker_points(self):
        st = ScoreTracker()
        pts1 = st.record_prediction(category="Control Flow", is_correct=True, used_hint=False)
        self.assertEqual(pts1, 100)
        self.assertEqual(st.streak, 1)

        pts2 = st.record_prediction(category="Control Flow", is_correct=True, used_hint=True)
        self.assertEqual(pts2, 50)
        self.assertEqual(st.streak, 2)
        self.assertEqual(st.total_score, 150)

    def test_score_tracker_miss_reset(self):
        st = ScoreTracker()
        st.record_prediction("Basics", is_correct=True, used_hint=False)
        self.assertEqual(st.streak, 1)

        st.record_prediction("Basics", is_correct=False, used_hint=False)
        self.assertEqual(st.streak, 0)
        self.assertEqual(st.max_streak, 1)
        self.assertEqual(st.get_accuracy(), 50.0)


if __name__ == "__main__":
    unittest.main()
