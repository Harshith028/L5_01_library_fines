# Lab 5: Static Code Analysis

## Issue Documentation

| Issue | Type | Line(s) in Original Code | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe `eval()` usage | Security — Medium | 45 | `eval()` can execute arbitrary Python expressions. | Replaced it with a restricted arithmetic evaluator using Python's AST module. |
| Bare exception handling | Security/Code Quality — Low | 21–22 | A bare `except` catches exceptions too broadly and silently ignores failures. | Caught specific exceptions and displayed an appropriate message. |
| Mutable default argument | Bug/Code Quality | 9 | The default list can be shared between function calls. | Changed `dates=[]` to `dates=None` and initialized the list inside the function. |
| Global state modification | Code Quality | 28, 35 | Functions modify global variables, making program state harder to manage. | Reviewed the global state usage; two global-statement warnings remain. |
| Missing docstrings | Code Quality | Multiple | Functions and the module lacked documentation. | Added module and function docstrings. |
| Unused import | Code Quality | 2 | The imported `os` module was not used. | Removed the unused import. |
| Incorrect function naming | Style | 27 | `renewBook` does not follow snake_case naming conventions. | Renamed the function to `renew_book` and updated its caller. |
| Unsafe file handling | Code Quality | 34, 39 | Files were opened without explicit encoding and context managers. | Added UTF-8 encoding and used `with open(...)`. |
| Long lines and missing newline | Style | 14, 31 and end of file | Lines exceeded the recommended length and the file lacked a final newline. | Reformatted long statements and added a final newline. |
| Insufficient input validation | Bug/Code Quality | 46 and main input handling | Negative overdue days and invalid input could produce incorrect results or errors. | Added validation for negative values and invalid input. |

## Verification

- Pylint score improved from 6.07/10 to 9.82/10.
- Bandit reported no issues in the latest scan.
- Flake8 produced no output after the formatting fixes.
- Two Pylint warnings about the `global` statement remain.

## Conclusion

Static code analysis helped identify security, code-quality, exception-handling, and formatting issues. Fixing these problems improved the safety, readability, and maintainability of the library fine management program.
