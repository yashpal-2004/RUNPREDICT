# RUNPREDICT - Problem Statement & Project Specifications

## 1. Project Title
**RUNPREDICT: A Randomized Python Program Output Prediction and Execution Simulator**

---

## 2. Problem Statement & Motivation
In introductory computer science courses (such as CSE1021), students frequently struggle with mentally tracing program execution and predicting console output. Traditional static problem sets present static code snippets that lead to answer memorization rather than deep algorithmic comprehension.

**RUNPREDICT** solves this by acting as an interactive simulation engine that:
1. Dynamically generates randomized code instances from parameterized algorithm templates across 4 difficulty levels.
2. Executes generated Python code snippets inside a controlled, isolated execution sandbox.
3. Compares student predictions against actual outputs.
4. Generates step-by-step variable execution trace tables (`TRACE`), illustrating variable mutations loop-by-loop.

---

## 3. Question Categories & Syllabus Mapping (CSE1021 Alignment)

| Category / Level | Topics Covered | Code Snippet Examples |
| :--- | :--- | :--- |
| **Level 1 — Basics** | Variables, arithmetic, operator precedence, I/O | Swapping, expression evaluation, type casting |
| **Level 2 — Control Flow** | `if/elif/else`, `for`, `while`, nested loops | Loop accumulators, conditional skips, range steps |
| **Level 3 — Algorithms** | Counting, summation, factorial, Fibonacci, reverse, GCD, prime factors | Euclidean loop, prime factor loop, iterative Fibonacci |
| **Level 4 — Collections** | Lists, tuples, sets, dictionaries, duplicate removal, max/min | Unique item filters, dictionary counter maps, list slicing |

---

## 4. Key Functional Features

1. **Random Program Generator**: Parameterizes variable names, initial values, iteration bounds, and operations so every round presents a unique snippet.
2. **Safe Sandbox Execution Engine**: Executes generated code safely, capturing stdout while isolating system environment.
3. **Algorithm Variable Trace Mode**: Generates a tabular execution trace showing variable values ($i, x, y, \dots$) at each step.
4. **Adaptive Scoring & Performance Analytics**:
   - Correct Prediction: **+100 points**
   - Correct After Hint: **+50 points**
   - Incorrect Prediction: **+0 points**
   - Category performance breakdown (% accuracy per category).
