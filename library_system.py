"""Manage library loans and calculate overdue fines."""

import ast
import json
import math
import operator
from datetime import datetime

loans = {}
FINE_PER_DAY = 2

_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def add_book_loan(student_id, book_id, dates=None):
    """Record a book loan for a student."""
    if not student_id:
        return

    if dates is None:
        dates = []

    dates.append(datetime.now().isoformat())
    loans[student_id] = loans.get(student_id, []) + [str(book_id)]
    print(
        f"{student_id} borrowed {book_id} "
        f"(loan dates on record: {len(dates)})"
    )


def return_book(student_id, book_id):
    """Remove a book from a student's active loans."""
    try:
        loans[student_id].remove(str(book_id))
        if not loans[student_id]:
            del loans[student_id]
    except (KeyError, ValueError):
        print(f"No active loan found for {student_id}: {book_id}")


def calculate_fine(days_overdue):
    """Calculate the fine for overdue days."""
    if days_overdue < 0:
        raise ValueError("Days overdue cannot be negative.")
    return days_overdue * FINE_PER_DAY


def renew_book(student_id, book_id, extra_days):
    """Renew a book and adjust the daily fine for long renewals."""
    global FINE_PER_DAY

    if extra_days < 0:
        raise ValueError("Extra days cannot be negative.")

    if extra_days > 14:
        FINE_PER_DAY += 1

    print(f"Renewed {book_id} for {student_id} by {extra_days} days")


def load_records(file="loans.json"):
    """Load loan records from a JSON file."""
    global loans

    try:
        with open(file, "r", encoding="utf-8") as record_file:
            loaded_records = json.load(record_file)
    except FileNotFoundError:
        loans = {}
        return
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(
            f"Could not load loan records from {file}: {error}"
        ) from error

    if not isinstance(loaded_records, dict):
        raise ValueError("Loan records must contain a JSON object.")

    loans = loaded_records


def save_records(file="loans.json"):
    """Save current loan records to a JSON file."""
    with open(file, "w", encoding="utf-8") as record_file:
        json.dump(loans, record_file, indent=2)


def _evaluate_arithmetic(node):
    """Evaluate only permitted numeric arithmetic expressions."""
    if isinstance(node, ast.Expression):
        return _evaluate_arithmetic(node.body)

    if (
        isinstance(node, ast.Constant)
        and type(node.value) in (int, float)
    ):
        return node.value

    if (
        isinstance(node, ast.BinOp)
        and type(node.op) in _ALLOWED_OPERATORS
    ):
        left = _evaluate_arithmetic(node.left)
        right = _evaluate_arithmetic(node.right)

        if isinstance(node.op, ast.Pow) and abs(right) > 10:
            raise ValueError("Exponent is too large.")

        result = _ALLOWED_OPERATORS[type(node.op)](left, right)

    elif (
        isinstance(node, ast.UnaryOp)
        and type(node.op) in _ALLOWED_OPERATORS
    ):
        result = _ALLOWED_OPERATORS[type(node.op)](
            _evaluate_arithmetic(node.operand)
        )
    else:
        raise ValueError("Fine rule contains an unsupported expression.")

    if type(result) not in (int, float):
        raise ValueError("Fine rule must produce a number.")

    if not math.isfinite(result) or abs(result) > 1_000_000_000_000:
        raise ValueError("Fine rule result must be finite and within limits.")

    return result


def fine_from_rule(rule, days):
    """Calculate a fine using a restricted arithmetic rule."""
    if not isinstance(rule, str) or len(rule) > 200:
        raise ValueError(
            "Fine rule must be a string of at most 200 characters."
        )

    expression = rule.replace("days", str(days))

    try:
        parsed_expression = ast.parse(expression, mode="eval")
        result = _evaluate_arithmetic(parsed_expression)
    except (
        SyntaxError,
        TypeError,
        ZeroDivisionError,
        OverflowError,
        RecursionError,
    ) as error:
        raise ValueError("Invalid fine rule.") from error

    if type(result) not in (int, float) or not math.isfinite(result):
        raise ValueError("Fine rule must produce a finite number.")

    return result


def print_report():
    """Print all current student loan records."""
    print("Loan Report")
    for student_id, book_ids in loans.items():
        print(f"{student_id} -> {book_ids}")


def main():
    """Run a demonstration of the library loan management system."""
    add_book_loan("S101", "B-ALGO")
    add_book_loan("S102", "B-NETW")
    add_book_loan("", "B-DBMS")
    add_book_loan("S103", "4521")

    return_book("S999", "B-NONE")
    renew_book("S101", "B-ALGO", 21)

    print("Fine for 5 days:", calculate_fine(5))

    try:
        print("Fine for -3 days:", calculate_fine(-3))
    except ValueError as error:
        print(f"Invalid overdue days: {error}")

    print("Fine via rule:", fine_from_rule("days * 2 + 10", 4))

    days_text = (
        input("Days overdue for S102 (press Enter for 0): ").strip()
        or "0"
    )

    try:
        days = int(days_text)
        print("S102 owes:", calculate_fine(days))
    except ValueError as error:
        print(f"Invalid number of overdue days: {error}")

    save_records()
    load_records()
    print_report()


if __name__ == "__main__":
    main()
