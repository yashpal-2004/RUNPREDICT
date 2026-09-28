# RUNPREDICT Architecture & System Design

This document details the modular architecture and state machine of **RUNPREDICT**.

---

## 1. Modular Architecture Diagram

```mermaid
graph TD
    Main[src/main.py CLI Interface] --> Gen[src/generator.py Generator]
    Main --> Pred[src/predictor.py Predictor]
    Main --> Score[src/scoring.py Scoring Engine]

    Gen --> Bank[(data/question_bank.json)]
    Gen --> Algo[src/algorithms.py Snippets]

    Pred --> Exec[src/executor.py Sandbox Execution]
    Pred --> Val[src/validation.py Output Comparison]

    Exec --> Trace[Execution Trace Table Generator]
```

---

## 2. Prediction Lifecycle Sequence

```mermaid
sequenceDiagram
    autonumber
    actor Player
    participant UI as main.py CLI
    participant Gen as generator.py
    participant Pred as predictor.py
    participant Exec as executor.py
    participant Score as scoring.py

    Player->>UI: Select Start Round
    UI->>Gen: Request Challenge (Level N)
    Gen-->>UI: Python Code Snippet & Hint
    UI->>Player: Render Code & Prompt Prediction
    Player->>UI: Enter Predicted Output
    UI->>Pred: Submit (Code, User Prediction, UsedHint)
    Pred->>Exec: Execute Code in Isolated Sandbox
    Exec-->>Pred: Actual Output & Trace History
    Pred->>Pred: Compare Predictions (Normalized String Match)
    Pred-->>UI: Verification Result (Correct/Incorrect + Trace Table)
    UI->>Score: Update Points, Streak, and Category Stats
    Score-->>UI: Updated Score Summary
    UI-->>Player: Display Actual Output, Result, and TRACE Table
```
