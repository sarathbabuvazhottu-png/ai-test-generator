import pytest
from src.functions import add_numbers, divide_numbers, find_largest, validate_email, calculate_grade


# ─────────────────────────────────────────────
# add_numbers
# ─────────────────────────────────────────────

def test_add_numbers_positive():
    assert add_numbers(3, 4) == 7

def test_add_numbers_negative():
    assert add_numbers(-2, -5) == -7

def test_add_numbers_mixed():
    assert add_numbers(-10, 10) == 0

def test_add_numbers_floats():
    assert add_numbers(1.5, 2.5) == pytest.approx(4.0)

def test_add_numbers_zeros():
    assert add_numbers(0, 0) == 0


# ─────────────────────────────────────────────
# divide_numbers
# ─────────────────────────────────────────────

def test_divide_numbers_normal():
    assert divide_numbers(10, 2) == 5.0

def test_divide_numbers_floats():
    assert divide_numbers(7, 2) == pytest.approx(3.5)

def test_divide_numbers_negative():
    assert divide_numbers(-9, 3) == -3.0

def test_divide_numbers_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_numbers(5, 0)


# ─────────────────────────────────────────────
# find_largest
# ─────────────────────────────────────────────

def test_find_largest_normal():
    assert find_largest([3, 1, 4, 1, 5, 9, 2]) == 9

def test_find_largest_single_element():
    assert find_largest([42]) == 42

def test_find_largest_negatives():
    assert find_largest([-7, -3, -15]) == -3

def test_find_largest_empty_list():
    with pytest.raises(ValueError, match="List cannot be empty"):
        find_largest([])


# ─────────────────────────────────────────────
# validate_email
# ─────────────────────────────────────────────

def test_validate_email_valid():
    assert validate_email("user@example.com") is True

def test_validate_email_empty():
    assert validate_email("") is False

def test_validate_email_no_at_sign():
    assert validate_email("usergmail.com") is False

def test_validate_email_multiple_at_signs():
    assert validate_email("user@@gmail.com") is False

def test_validate_email_no_local_part():
    assert validate_email("@gmail.com") is False

def test_validate_email_local_starts_with_dot():
    assert validate_email(".user@gmail.com") is False

def test_validate_email_no_domain():
    assert validate_email("user@") is False

def test_validate_email_domain_starts_with_dot():
    assert validate_email("user@.gmail.com") is False

def test_validate_email_domain_ends_with_dot():
    assert validate_email("user@gmail.") is False

def test_validate_email_domain_no_dot():
    assert validate_email("user@gmailcom") is False


# ─────────────────────────────────────────────
# calculate_grade
# ─────────────────────────────────────────────

def test_calculate_grade_a():
    assert calculate_grade(95) == "A"

def test_calculate_grade_b():
    assert calculate_grade(85) == "B"

def test_calculate_grade_c():
    assert calculate_grade(75) == "C"

def test_calculate_grade_d():
    assert calculate_grade(65) == "D"

def test_calculate_grade_f():
    assert calculate_grade(55) == "F"

def test_calculate_grade_boundary_a():
    assert calculate_grade(90) == "A"

def test_calculate_grade_boundary_b():
    assert calculate_grade(80) == "B"

def test_calculate_grade_score_zero():
    assert calculate_grade(0) == "F"

def test_calculate_grade_score_100():
    assert calculate_grade(100) == "A"

def test_calculate_grade_below_zero():
    with pytest.raises(ValueError, match="Score must be between 0 and 100"):
        calculate_grade(-1)

def test_calculate_grade_above_100():
    with pytest.raises(ValueError, match="Score must be between 0 and 100"):
        calculate_grade(101)