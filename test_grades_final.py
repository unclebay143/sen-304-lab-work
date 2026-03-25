"""
Part B — PyTest against grades_final_code.py.
Covers equivalence / boundary (black-box) and branch coverage (white-box) for the lab brief.
"""

from __future__ import annotations

import pytest

from grades_final_code import Student, letter_grade, parse_grade_line, top_student


# --- Student.add_grade (valid partition, invalid partition, boundaries) ---


@pytest.mark.parametrize(
    "score,expected_grades",
    [
        (0, [0]),
        (50, [50]),
        (100, [100]),
    ],
)
def test_add_grade_valid_equivalence(score: float, expected_grades: list) -> None:
    s = Student("Test")
    s.add_grade(score)
    assert s.grades == expected_grades


@pytest.mark.parametrize("score", [-0.01, -1, 101, 150])
def test_add_grade_invalid_rejected(score: float, capsys: pytest.CaptureFixture[str]) -> None:
    s = Student("Test")
    s.add_grade(80)
    s.add_grade(score)
    assert s.grades == [80]
    captured = capsys.readouterr()
    assert "Invalid grade" in captured.out


def test_add_grade_multiple_valid() -> None:
    s = Student("Test")
    s.add_grade(70)
    s.add_grade(85)
    assert s.grades == [70, 85]


# --- Student.average (empty path vs divide path) ---


def test_average_empty_returns_zero() -> None:
    assert Student("X").average() == 0.0


def test_average_single_grade() -> None:
    s = Student("X")
    s.add_grade(88)
    assert s.average() == 88.0


def test_average_multiple() -> None:
    s = Student("X")
    s.add_grade(80)
    s.add_grade(90)
    assert s.average() == 85.0


# --- letter_grade (boundary value analysis) ---


@pytest.mark.parametrize(
    "avg,expected",
    [
        (0, "F"),
        (59, "F"),
        (59.99, "F"),
        (60, "D"),
        (69.9, "D"),
        (70, "C"),
        (79.9, "C"),
        (80, "B"),
        (89.9, "B"),
        (90, "A"),
        (100, "A"),
    ],
)
def test_letter_grade_boundaries(avg: float, expected: str) -> None:
    assert letter_grade(avg) == expected


# --- parse_grade_line ---


def test_parse_grade_line_valid() -> None:
    assert parse_grade_line("Ada,88") == ("Ada", 88.0)


def test_parse_grade_line_whitespace_after_comma() -> None:
    assert parse_grade_line("Ada, 88") == ("Ada", 88.0)


def test_parse_grade_line_out_of_range_high() -> None:
    with pytest.raises(ValueError, match="out of valid range"):
        parse_grade_line("Ben,150")


def test_parse_grade_line_out_of_range_low() -> None:
    with pytest.raises(ValueError, match="out of valid range"):
        parse_grade_line("Ben,-1")


def test_parse_grade_line_boundary_zero() -> None:
    assert parse_grade_line("X,0") == ("X", 0.0)


def test_parse_grade_line_boundary_hundred() -> None:
    assert parse_grade_line("X,100") == ("X", 100.0)


def test_parse_grade_line_invalid_float() -> None:
    with pytest.raises(ValueError):
        parse_grade_line("Ada,notanumber")


# --- top_student ---


def test_top_student_picks_highest_average() -> None:
    a = Student("A")
    b = Student("B")
    a.add_grade(60)
    b.add_grade(90)
    assert top_student([a, b]).name == "B"


def test_top_student_empty_raises() -> None:
    with pytest.raises(ValueError, match="empty"):
        top_student([])


def test_top_student_single() -> None:
    s = Student("Only")
    s.add_grade(75)
    assert top_student([s]) is s
