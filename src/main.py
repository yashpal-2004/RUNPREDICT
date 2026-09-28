"""
RUNPREDICT - Main CLI Entrypoint
Interactive Python Program Output Predictor and Execution Simulator.
"""

import sys
import os
import time

# Add parent dir to path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from src.generator import generate_program_challenge
from src.predictor import process_prediction
from src.scoring import ScoreTracker
from src.validation import parse_integer_input


# ANSI Formatting
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_banner() -> None:
    """Prints the RUNPREDICT ASCII banner."""
    banner = f"""
{CYAN}{BOLD}╔══════════════════════════════════════╗
║          RUNPREDICT v1.0             ║
║       CSE1021 OUTPUT CHALLENGE       ║
╚══════════════════════════════════════╝{RESET}
{YELLOW}  Mental Python Code Execution Simulator{RESET}
"""
    print(banner)


def run_challenge_round(round_num: int, difficulty: int, score_tracker: ScoreTracker) -> None:
    """Runs a single prediction round."""
    challenge = generate_program_challenge(difficulty_level=difficulty)
    code_str = challenge["code"]
    category = challenge["category"]
    hint_text = challenge["hint"]

    diff_labels = {1: "EASY (Basics)", 2: "MEDIUM (Control Flow)", 3: "HARD (Algorithms)", 4: "EXPERT (Collections)"}
    diff_name = diff_labels.get(difficulty, "MEDIUM")

    print(f"\n{BOLD}ROUND {round_num:02d}{RESET} | Difficulty: {YELLOW}{diff_name}{RESET} | Category: {CYAN}{category}{RESET}")
    print("Predict what the following program will print:")
    print(f"{CYAN}----------------------------------------{RESET}")
    print(code_str)
    print(f"{CYAN}----------------------------------------{RESET}")

    print("\nOptions: Type your prediction, or type 'H' for a hint.")
    used_hint = False

    user_lines = []
    print("Your prediction (Enter empty line when done):")
    while True:
        try:
            line = input("> ")
            if line.strip().upper() == "H" and not used_hint:
                print(f"{YELLOW}[HINT]: {hint_text}{RESET}")
                used_hint = True
                continue
            if line == "":
                if user_lines:
                    break
                else:
                    # If empty on first input, re-prompt or treat as empty
                    break
            user_lines.append(line)
        except EOFError:
            break

    user_pred_str = "\n".join(user_lines)

    # Process prediction & execute code safely
    res = process_prediction(code_str, user_pred_str, used_hint=used_hint)

    print(f"\n{BOLD}ACTUAL OUTPUT{RESET}")
    print("─────────────")
    print(res["actual_output"] if res["actual_output"] else "(No stdout output)")
    print("─────────────")

    points_gained = score_tracker.record_prediction(category, res["is_correct"], used_hint)

    if res["is_correct"]:
        print(f"{GREEN}{BOLD}✓ CORRECT{RESET} (+{points_gained} pts)")
    else:
        print(f"{RED}{BOLD}✗ INCORRECT{RESET}")

    # Display execution TRACE table
    print(f"\n{BOLD}TRACE{RESET}")
    print("────────────────────────")
    print(res["trace_table"])

    print(f"\n{BOLD}Score Summary:{RESET}")
    print(f"  Points Gained  : +{points_gained}")
    print(f"  Current Streak : {YELLOW}{score_tracker.streak}{RESET}")
    print(f"  Total Score    : {GREEN}{score_tracker.total_score}{RESET}")
    print(f"  Overall Acc.   : {score_tracker.get_accuracy():.1f}%")

    input("\nPress Enter for next round...")


def display_performance_stats(score_tracker: ScoreTracker) -> None:
    """Displays category accuracy stats."""
    summary = score_tracker.get_performance_summary()
    print(f"\n{CYAN}{BOLD}--- YOUR PERFORMANCE STATISTICS ---{RESET}")
    print(f"  Total Programs Solved : {summary['total_solved']} / {summary['total_attempts']}")
    print(f"  Overall Accuracy      : {GREEN}{summary['overall_accuracy']}%{RESET}")
    print(f"  Best Streak Achieved  : {YELLOW}{summary['max_streak']}{RESET}")
    print(f"  Total Score Accumulated: {summary['total_score']} pts")
    print("\n  Category Breakdown:")
    for cat, stats in summary["category_breakdown"].items():
        print(f"    - {cat:<14}: {stats['accuracy']:>5.1f}% ({stats['correct']}/{stats['total']} solved)")

    input("\nPress Enter to return to main menu...")


def main() -> None:
    """Main CLI menu loop."""
    score_tracker = ScoreTracker()
    current_difficulty = 2
    round_counter = 1

    while True:
        print_banner()
        print(f"{BOLD}MAIN MENU:{RESET}")
        print(f"  {CYAN}[1]{RESET} Start Next Challenge Round (Round {round_counter})")
        print(f"  {CYAN}[2]{RESET} Set Difficulty Level (Current: Level {current_difficulty})")
        print(f"  {CYAN}[3]{RESET} View Performance & Category Stats")
        print(f"  {RED}[4]{RESET} Exit Program")
        print()

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            run_challenge_round(round_counter, current_difficulty, score_tracker)
            round_counter += 1
        elif choice == "2":
            print("\nSelect Difficulty Level:")
            print("  1 - EASY (Basics)")
            print("  2 - MEDIUM (Control Flow)")
            print("  3 - HARD (Algorithms)")
            print("  4 - EXPERT (Collections)")
            level_input = input("Enter level (1-4): ")
            lvl = parse_integer_input(level_input)
            if lvl and 1 <= lvl <= 4:
                current_difficulty = lvl
                print(f"{GREEN}Difficulty set to Level {current_difficulty}.{RESET}")
            else:
                print(f"{RED}Invalid level.{RESET}")
            time.sleep(1)
        elif choice == "3":
            display_performance_stats(score_tracker)
        elif choice == "4":
            print(f"\n{GREEN}Thank you for playing RUNPREDICT! Final Score: {score_tracker.total_score} pts{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}Invalid option.{RESET}")
            time.sleep(1)


if __name__ == "__main__":
    main()
