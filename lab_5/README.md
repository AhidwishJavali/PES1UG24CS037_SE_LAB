# Lab 5: Static Code Analysis — Courier & Parcel Tracking System

This parcel tracker demonstrates booking, status updates, tracking, courier checks, OTP generation, and shipping-cost calculation. The code has been reviewed with Pylint, Bandit, and Flake8.

## Set up on Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the demo and analysis

```powershell
python parcel_tracker.py
python -m pylint --persistent=n parcel_tracker.py
python -m bandit -r parcel_tracker.py
python -m flake8 parcel_tracker.py
```

The `*_report_before.txt` and `*_report_after.txt` files preserve the analysis before and after the fixes. See [issues.md](issues.md) for the findings and [reflection.md](reflection.md) for the reflection.
