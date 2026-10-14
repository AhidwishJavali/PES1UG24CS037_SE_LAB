# Static analysis findings

Line numbers below refer to the original `parcel_tracker.py` and the *before* reports.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Shell command injection risk (Bandit B602, high) | Security | 55 | `pingHub` concatenated user-controlled input into a command and ran it with `shell=True`. | Removed the unused ping helper and its `subprocess` dependency. |
| Unsafe temporary file name (Bandit B306, medium) | Security | 50 | `tempfile.mktemp` can return a name that another process claims before it is opened. | Removed the unused helper and its `tempfile` dependency. |
| Mutable default argument (Pylint W0102) | Bug | 11 | `history=[]` reused one list across calls, so tracking IDs could leak between independent bookings. | Default to `None` and create a fresh list inside the function. |
| Overly broad exception (Pylint W0718) | Reliability | 37 | `except Exception` concealed unrelated programming errors while handling an unknown tracking ID. | Use `dict.get` and handle the missing parcel explicitly. |
| Predictable OTP (Bandit B311, low) | Security | 72 | `random.randint` is not intended for security-sensitive codes. | Generate the four digit OTP with `secrets.randbelow`. |
| Naming, docstrings, and formatting violations | Style | Multiple | CamelCase names, missing docstrings, spacing errors, and direct module-level execution reduced readability and tool scores. | Use snake_case, add docstrings, format consistently, and call the demo through a main guard. |

## Verification

The `*_report_before.txt` files preserve the initial tool findings. The `*_report_after.txt` files contain the final analysis. The final Bandit report has zero findings, Flake8 is clean, and Pylint reports 10.00/10.
