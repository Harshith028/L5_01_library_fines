# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing it. It helps identify potential bugs, security vulnerabilities, and coding-style violations.

## 2. What is the purpose of Pylint, Bandit, and Flake8?

- **Pylint:** Identifies code-quality problems, potential bugs, and poor programming practices.
- **Bandit:** Detects common security vulnerabilities in Python code.
- **Flake8:** Checks Python code for formatting and PEP 8 style violations.

## 3. What issues did you identify and fix?

I corrected the mutable default argument, replaced bare exception handling, removed unsafe `eval()` usage, added docstrings, improved file handling, removed an unused import, and corrected formatting and naming conventions.

## 4. How did static analysis improve the program?

Static analysis helped improve code readability, maintainability, exception handling, input validation, and security. Bandit reported no issues, and Flake8 produced no output after the fixes.

## 5. What did you learn from this lab?

I learned that different static analysis tools identify different categories of problems. Using multiple tools helps improve code quality and security before the program is deployed.
