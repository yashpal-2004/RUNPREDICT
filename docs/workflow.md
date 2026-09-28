# RUNPREDICT Operational Workflow

## 1. Challenge Generation Flow
1. Difficulty selection determines target category (Basics, Control Flow, Algorithms, Collections).
2. `generator.py` loads templates from `question_bank.json` or invokes procedural code generators in `algorithms.py`.
3. Numerical parameters, variables, and iteration ranges are parameterized using pseudo-random generation.

## 2. Prediction & Trace Flow
1. The student reads the generated code snippet and inputs their prediction.
2. `executor.py` runs `exec()` inside an isolated scope with stdout captured via `io.StringIO`.
3. `sys.settrace()` monitors frame variables line by line to compile the step-by-step execution trace table (`TRACE`).
4. Normalized string comparison verifies if the student's prediction matches the exact printed output.
5. Score and category accuracy statistics update in real time.
