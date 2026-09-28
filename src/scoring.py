"""
Scoring Module for RUNPREDICT
Manages score calculation, streak tracking, accuracy stats, and category performance summaries.
"""

from typing import Dict, Any, List


class ScoreTracker:
    """
    Tracks session score, streaks, and performance breakdown by CSE1021 category.
    """

    def __init__(self):
        self.total_score = 0
        self.streak = 0
        self.max_streak = 0
        self.total_solved = 0
        self.total_attempts = 0
        
        # Category breakdown stats: category -> {"correct": count, "total": count}
        self.category_stats: Dict[str, Dict[str, int]] = {
            "Basics": {"correct": 0, "total": 0},
            "Control Flow": {"correct": 0, "total": 0},
            "Algorithms": {"correct": 0, "total": 0},
            "Collections": {"correct": 0, "total": 0}
        }

    def record_prediction(self, category: str, is_correct: bool, used_hint: bool) -> int:
        """
        Records a prediction attempt.
        Returns the score gained in this round (+100, +50, or +0).
        """
        self.total_attempts += 1
        cat_key = category if category in self.category_stats else "Basics"
        self.category_stats[cat_key]["total"] += 1

        if is_correct:
            self.total_solved += 1
            self.streak += 1
            if self.streak > self.max_streak:
                self.max_streak = self.streak

            points = 50 if used_hint else 100
            self.total_score += points
            self.category_stats[cat_key]["correct"] += 1
            return points
        else:
            self.streak = 0
            return 0

    def get_accuracy(self) -> float:
        """Returns overall accuracy percentage."""
        if self.total_attempts == 0:
            return 0.0
        return (self.total_solved / self.total_attempts) * 100.0

    def get_performance_summary(self) -> Dict[str, Any]:
        """Returns detailed category performance statistics."""
        breakdown = {}
        for cat, stats in self.category_stats.items():
            tot = stats["total"]
            corr = stats["correct"]
            acc = (corr / tot * 100.0) if tot > 0 else 0.0
            breakdown[cat] = {
                "correct": corr,
                "total": tot,
                "accuracy": round(acc, 1)
            }

        return {
            "total_score": self.total_score,
            "streak": self.streak,
            "max_streak": self.max_streak,
            "total_attempts": self.total_attempts,
            "total_solved": self.total_solved,
            "overall_accuracy": round(self.get_accuracy(), 1),
            "category_breakdown": breakdown
        }
