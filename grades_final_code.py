from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    grades: list = field(default_factory=list)

    def add_grade(self, score: float) -> None:
        if score < 0 or score > 100:
            print("Invalid grade")  
            return
        self.grades.append(score)

    def average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades) 


def letter_grade(avg: float) -> str:
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F" 

grade_ranks: dict[str, int] = {
    "Maya": 1,
    "Leo": 2,
}

def top_student(students: list[Student]) -> Student:
    if not students:
        raise ValueError("students list is empty")
    return max(students, key=lambda s: s.average()) 


def parse_grade_line(line: str) -> tuple[str, float]:
    name, grade = line.split(",")
    grade_float = float(grade)
  
    if grade_float > 100 or grade_float < 0:
        raise ValueError(f"Grade out of valid range 0-100: {grade_float}")
    return name.strip(), grade_float


def main() -> None:
    maya = Student("Maya")
    leo = Student("Leo")
    sam = Student("Sam")
    sam.add_grade(100)

    maya.add_grade(95)
    maya.add_grade(105)
    leo.add_grade(40)

    print("letter_grade(55):", letter_grade(55))
    print("Maya avg:", maya.average())
    print("Leo avg:", leo.average())
    print("Top student:", top_student([maya, leo]).name)
    print("parse_grade_line('Ben,90'):", parse_grade_line("Ben,90"))
    print("Sam avg:", sam.average())
    print("Top student:", top_student([maya, leo, sam]).name)


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error (invalid value or state): {e}")
