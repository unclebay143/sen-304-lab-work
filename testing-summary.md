# Part B — Testing summary (SEN 304)

## Approach

- **Target:** `grades-final-code.py` (loaded by `test_grades_final.py` because the filename contains a hyphen).
- **Runner:** PyTest (`pytest -v`).
- **Black-box:** Equivalence classes (valid vs invalid grades, empty vs non-empty averages) and **boundary values** for `letter_grade` (edges at 60, 70, 80, 90 and just below).
- **White-box:** Tests chosen so **`add_grade`** (both branches), **`average`** (empty guard vs divide), **`parse_grade_line`** (valid path, `if` out-of-range, `float` errors), and **`top_student`** (empty vs non-empty) are exercised.

## How to run (use a venv on macOS / PEP 668 systems)

```bash
cd sen-304-lab-work
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -v test_grades_final.py
```

Optional coverage (whole project dir):

```bash
pytest -v test_grades_final.py --cov=. --cov-report=term-missing
```

## Tests at a glance

| Area | What is checked |
|------|------------------|
| `add_grade` | 0, 50, 100 stored; -1, 101, etc. rejected with message; list unchanged |
| `average` | Empty → 0.0; one / multiple grades |
| `letter_grade` | F/D/C/B/A band boundaries |
| `parse_grade_line` | Valid CSV; spaces; 150 / -1 raise; 0 and 100; bad text raises |
| `top_student` | Higher average wins; `[]` raises; single student |

## Challenges

- Importing a module whose file name is not a valid Python identifier required **`importlib.util.spec_from_file_location`** in the test module.
- `add_grade` prints on invalid input; tests use **`capsys`** to assert the message without failing on stderr noise.

## Screenshot

Capture the terminal after **`pytest -v`** (all **passed**) for submission.
