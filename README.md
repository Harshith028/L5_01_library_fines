# Lab 5: Static Code Analysis — Library Fine and Book Renewal System

## Overview

This project demonstrates static code analysis on a Python-based library loan management system. The program records book loans, handles book returns and renewals, calculates overdue fines, and saves loan records to a JSON file.

The original program contained code-quality, security, and style issues. Pylint, Bandit, and Flake8 were used to identify these issues and improve the code.

## Objectives

- Understand the purpose of static code analysis.
- Identify potential bugs, security vulnerabilities, and style violations.
- Use Pylint, Bandit, and Flake8 to analyze Python code.
- Fix at least four identified issues.
- Verify the fixes by rerunning the analysis tools.
- Improve code readability, security, and maintainability.

## Project Structure

```text
L5_01_library_fines/
├── library_system.py
├── loans.json
├── pylint_report.txt
├── bandit_report.txt
├── flake8_report.txt
├── issues.md
├── reflection.md
├── README.md
└── .gitignore
```

The `venv/` directory contains the local Python virtual environment and is not required as part of the source submission.

## Requirements

- Python 3
- Pylint
- Bandit
- Flake8

## Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
source venv/bin/activate
```

Install the required tools:

```bash
python -m pip install pylint bandit flake8
```

If PowerShell blocks environment activation, the tools can be run directly through the virtual environment's Python executable.

## Running the Program

Run the library system:

```bash
python library_system.py
```

The program demonstrates:
- Adding book loans for students.
- Returning books and handling missing loans.
- Renewing books.
- Calculating overdue fines.
- Evaluating restricted arithmetic fine rules.
- Saving and loading loan records.
- Displaying a loan report.

The program asks for the number of overdue days. Press Enter to use the default value of zero, or enter a non-negative integer.

Loan records are saved in `loans.json`.

## Static Code Analysis

Run each analysis tool and save its output:

### 1. Pylint

```bash
pylint library_system.py > pylint_report.txt
```

Pylint identifies code-quality issues, potential bugs, naming problems, and missing documentation.

### 2. Bandit

```bash
bandit -r library_system.py > bandit_report.txt
```

Bandit identifies common security vulnerabilities and unsafe coding patterns.

### 3. Flake8

```bash
flake8 library_system.py > flake8_report.txt
```

Flake8 checks Python formatting and PEP 8 style violations.

## Issues Identified and Fixes

The original source code contained several issues, including:

- A mutable default argument.
- Bare exception handling.
- Unsafe use of `eval()`.
- An unused import.
- Missing module and function docstrings.
- File operations without explicit encoding and context managers.
- A function name that did not follow snake_case.
- Long lines and formatting violations.
- Insufficient validation of negative overdue days.

The corrected program addresses these issues through safer arithmetic evaluation, specific exception handling, improved file management, input validation, documentation, and consistent formatting.

The issue table in `issues.md` records the findings, their types and line numbers, descriptions, and fix approaches.

## Analysis Results

The latest recorded analysis results are:

| Tool | Result |
|---|---|
| Pylint | 9.82/10 |
| Bandit | No issues identified |
| Flake8 | No output; no style violations reported |

Pylint still reports two warnings related to the use of the `global` statement. These are documented rather than being represented as fully resolved.

## Deliverables

1. `library_system.py` — corrected Python program.
2. `issues.md` — documented issues and fixes.
3. `reflection.md` — answers to the lab reflection questions.

The three report files are retained as supporting evidence of the static analysis process.

## Conclusion

This lab demonstrates how static analysis tools can improve Python code quality, security, readability, and maintainability. Using Pylint, Bandit, and Flake8 together helped identify different categories of issues and verify the improvements made to the library loan management system.
