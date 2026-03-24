# Debugging report

## 1st Run and Debug

**What happened:**  
Python failed while **compiling** the file (before any breakpoints in `main`).

**Error:**  
```
SyntaxError: expected ':'` at `grades_buggy.py`, 
line 18 — `def letter_grade(avg: float) -> str
```

**Cause:**  
A function header must end with a colon. The line was missing `:`.

**Fix:** 
Change to:

```python
def letter_grade(avg: float) -> str:
```

**Screenshot (1st run)**
![](/screenshots/1.png)

---

## 2nd Run and Debug

**What happened:**  
Starting the debugger **loads the module**. When Python executes `@dataclass` on `Student`, it rejects the field default `grades: list = []` (Python 3.11+).

**Error:**  

```
Exception has occurred: ValueError
mutable default <class 'list'> for field grades is not allowed: use default_factory
  File "/Users/unclebigbay/Desktop/1234/projects/miva/sen-304-lab-work/grades_buggy.py", line 4, in <module>
    @dataclass
     ^^^^^^^^^
ValueError: mutable default <class 'list'> for field grades is not allowed: use default_factory
```

**Cause:**  
A mutable default (`[]`) on a dataclass field is not allowed; each instance needs its own list via a **factory**.

**Fix:**  
Import `field` and use `default_factory=list`:

```python
from dataclasses import dataclass, field
# ...
grades: list = field(default_factory=list)
```

**Screenshot (2nd run)**
![](/screenshots/2.png)

---

## 3rd Run and Debug

**What happened:**  
`main` runs through `add_grade`, `parse_grade_line`, and the average **print** lines. When `top_student([maya, leo])` runs (line 66), execution stops on the line that uses an undefined name.

**Error:**   
`NameError: name 'grade_ranks' is not defined`

**Traceback (terminal / debugger):**

```text
Exception has occurred: NameError
name 'grade_ranks' is not defined
  File ".../grades_buggy.py", line 39, in top_student
    rank = grade_ranks[top.name]
           ^^^^^^^^^^^
  File ".../grades_buggy.py", line 66, in <module>
    print("Top student:", top_student([maya, leo]).name)
                          ~~~~~~~~~~~^^^^^^^^^^^^^
NameError: name 'grade_ranks' is not defined
```

**Cause:**   
`grade_ranks` is never defined in the module, so the name does not exist at runtime.

**Fix:**   
**Declare** `grade_ranks` in an above `top_student` as a mapping from student **name** to rank. Then `rank = grade_ranks[top.name]` resolves correctly. Add an entry for every `Student.name` to avoid `KeyError`.

```python
grade_ranks: dict[str, int] = {
    "Maya": 1,
    "Leo": 2,
}


def top_student(students: list[Student])
```

**Debugger:** 

With **Uncaught Exceptions** enabled, the IDE pauses at line 39; **Locals** show `top` and `students` (e.g. Maya still has grades including the invalid 105 in the buggy version).

### Screenshot (3rd run)
![](/screenshots/3.png)