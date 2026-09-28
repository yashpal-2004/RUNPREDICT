# RUNPREDICT: Program Output Predictor & Execution Simulator

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**RUNPREDICT** is an interactive, randomized Python program output prediction and execution simulator built for CSE1021. The system presents generated code snippets, prompts students to predict the printed output, safely executes the snippet in a sandboxed runtime environment, and outputs step-by-step variable execution trace tables (`TRACE`).

---

## Key Features

- **Random Program Generator**: Dynamically parameterizes variables, loop bounds, and operators across 4 difficulty tiers so no two rounds are identical.
- **Safe Sandboxed Execution**: Executes generated Python code snippets in a safe environment, capturing `stdout` output while isolating system context.
- **Algorithm Trace Mode (`TRACE`)**: Renders loop-by-loop variable state change tables ($i, x, y$) allowing students to visualize exact variable mutations.
- **Dynamic Category Stats & Scoring**:
  - Correct Prediction: **+100 points**
  - Correct After Hint: **+50 points**
  - Streak multipliers & category accuracy breakdowns (% accuracy across Basics, Control Flow, Algorithms, and Collections).

---

## Directory Structure

```text
RUNPREDICT/
├── src/
│   ├── main.py           # Interactive CLI menu entrypoint
│   ├── generator.py      # Code snippet & template generator
│   ├── executor.py       # Safe execution sandbox & TRACE generator
│   ├── predictor.py      # Output verification engine
│   ├── algorithms.py     # Algorithmic code generators
│   ├── scoring.py        # Score, streak & performance tracker
│   └── validation.py     # Input normalization & validation
├── data/
│   └── question_bank.json# Parameterized code templates across 4 levels
├── tests/
│   ├── test_generator.py
│   ├── test_executor.py
│   └── test_scoring.py
├── docs/
│   ├── architecture.md   # System architecture diagrams
│   └── workflow.md       # Program lifecycle workflow
├── README.md             # Project documentation
├── statement.md          # Academic problem statement & syllabus mapping
└── requirements.txt      # Dependencies
```

---

## Running the Application

### 1. Launch RUNPREDICT
Navigate into the `RUNPREDICT` directory and start `main.py`:

```bash
cd RUNPREDICT
python src/main.py
```

### 2. Run Test Suite
Execute unit tests using Python's built-in `unittest`:

```bash
cd RUNPREDICT
python -m unittest discover tests
```

---

## CSE1021 Syllabus Alignment

- **Level 1 (Basics)**: Variables, arithmetic operations, operator precedence, I/O.
- **Level 2 (Control Flow)**: `if/elif/else`, `for`, `while`, nested loops.
- **Level 3 (Algorithms)**: Summation, factorial, Fibonacci, reverse, Euclidean GCD.
- **Level 4 (Collections)**: Lists, tuples, sets, dictionaries, duplicate filters, frequency counters.
