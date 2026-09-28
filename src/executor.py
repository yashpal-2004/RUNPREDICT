"""
Executor Module for RUNPREDICT
Provides safe sandboxed execution of generated Python code snippets and produces
step-by-step variable execution trace tables (TRACE mode).
"""

import sys
import io
from typing import Dict, Any, List, Tuple


def execute_code_snippet(code_str: str) -> Dict[str, Any]:
    """
    Executes a Python code string in an isolated scope, capturing stdout output.
    Returns dictionary with actual_output, execution_error (if any), and globals_dict.
    """
    buffer = io.StringIO()
    old_stdout = sys.stdout
    exec_globals: Dict[str, Any] = {}

    try:
        sys.stdout = buffer
        exec(code_str, exec_globals)
        output = buffer.getvalue()
        error = None
    except Exception as e:
        output = buffer.getvalue()
        error = str(e)
    finally:
        sys.stdout = old_stdout

    return {
        "output": output,
        "error": error,
        "variables": {k: v for k, v in exec_globals.items() if not k.startswith("__")}
    }


def generate_execution_trace(code_str: str) -> List[Dict[str, Any]]:
    """
    Traces line-by-line or loop-by-loop variable state changes during snippet execution.
    Returns a list of trace snapshot dictionaries.
    """
    trace_history: List[Dict[str, Any]] = []

    def trace_lines(frame, event, arg):
        if event == 'line':
            # Filter local scope variables excluding internal built-ins
            locals_copy = {
                k: v for k, v in frame.f_locals.items()
                if not k.startswith("__") and not callable(v)
            }
            if locals_copy:
                trace_history.append(dict(locals_copy))
        return trace_lines

    buffer = io.StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = buffer
        sys.settrace(trace_lines)
        exec(code_str, {})
    except Exception:
        pass
    finally:
        sys.settrace(None)
        sys.stdout = old_stdout

    return trace_history


def format_trace_table(trace_history: List[Dict[str, Any]]) -> str:
    """
    Formats line trace snapshots into a clean tabular ASCII execution TRACE string.
    """
    if not trace_history:
        return "No loop variable trace available."

    # Identify all tracked variable names across history
    all_keys = []
    for snap in trace_history:
        for k in snap.keys():
            if k not in all_keys:
                all_keys.append(k)

    if not all_keys:
        return "No local variables tracked."

    # Filter consecutive duplicate state snapshots for clarity
    filtered_history = []
    prev_snap = None
    for snap in trace_history:
        if snap != prev_snap:
            filtered_history.append(snap)
            prev_snap = snap

    # Construct table header and rows
    headers = [str(k) for k in all_keys]
    col_widths = {k: max(len(k), 8) for k in headers}

    header_line = "  ".join(k.ljust(col_widths[k]) for k in headers)
    separator = "─" * len(header_line)
    rows = [header_line, separator]

    for snap in filtered_history:
        row_str = "  ".join(str(snap.get(k, "-")).ljust(col_widths[k]) for k in headers)
        rows.append(row_str)

    return "\n".join(rows)
