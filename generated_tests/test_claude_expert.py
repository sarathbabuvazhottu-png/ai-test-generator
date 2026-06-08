import pytest
from src.functions import add_numbers, divide_numbers, find_largest, validate_email, calculate_grade


# ── add_numbers ──────────────────────────────────────────────────────────────

def test_add_positive_numbers():
    assert add_numbers(2, 3) == 5

def test_add_negative_numbers():
    assert add_numbers(-4, -6) == -10

def test_add_positive_and_negative():
    assert add_numbers(10, -3) == 7

def test_add_floats():
    assert add_numbers(1.5, 2.5) == 4.0

def test_add_zeros():
    assert add_numbers(0, 0) == 0


# ── divide_numbers ───────────────────────────────────────────────────────────

def test_divide_normal():
    assert divide_numbers(10, 2) == 5.0

def test_divide_returns_float():
    assert divide_numbers(7, 2) == 3.5

def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide_numbers(5, 0)

def test_divide_negative_numbers():
    assert divide_numbers(-9, 3) == -3.0

def test_divide_zero_numerator():
    assert divide_numbers(0, 5) == 0.0


# ── find_largest ─────────────────────────────────────────────────────────────

def test_find_largest_basic():
    assert find_largest([1, 2, 3]) == 3

def test_find_largest_single_element():
    assert find_largest([42]) == 42

def test_find_largest_negative_numbers():
    assert find_largest([-5, -1, -3]) == -1

def test_find_largest_empty_list_raises():
    with pytest.raises(ValueError, match="List cannot be empty!"):
        find_largest([])

def test_find_largest_duplicates():
    assert find_largest([5, 5, 5]) == 5


# ── validate_email ───────────────────────────────────────────────────────────

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


# ── calculate_grade ──────────────────────────────────────────────────────────

def test_grade_A():
    assert calculate_grade(95) == "A"

def test_grade_B():
    assert calculate_grade(85) == "B"

def test_grade_C():
    assert calculate_grade(75) == "C"

def test_grade_D():
    assert calculate_grade(65) == "D"

def test_grade_F():
    assert calculate_grade(50) == "F"

def test_grade_boundary_90_is_A():
    assert calculate_grade(90) == "A"

def test_grade_boundary_80_is_B():
    assert calculate_grade(80) == "B"

def test_grade_boundary_0_is_F():
    assert calculate_grade(0) == "F"

def test_grade_boundary_100_is_A():
    assert calculate_grade(100) == "A"

def test_grade_negative_raises():
    with pytest.raises(ValueError, match="Score must be between 0 and 100!"):
        calculate_grade(-1)

def test_grade_above_100_raises():
    with pytest.raises(ValueError, match="Score must be between 0 and 100!"):
        calculate_grade(101)