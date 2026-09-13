# LinuxPulse — Linux Application Health & Incident Monitoring System

Linux-oriented application health monitoring and incident classification platform using Python, FastAPI, SQLite, SQLAlchemy, Linux/Bash, HTML/CSS/JavaScript and REST APIs.

## Features
- CPU, memory, disk, process and port health collection
- Rule-based incident classification
- Incident history in SQLite
- Bash diagnostic health-check script
- REST API and browser dashboard
- Deterministic validation tests

## Run

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
python seed.py
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 and `/docs` for API documentation.

On Linux, run `bash scripts/health_check.sh` for CLI diagnostics.

## Validation
The classifier is deterministic so detection/classification benchmarks can be reproduced. Resume percentages should only be claimed after running the corresponding benchmark scenarios.
