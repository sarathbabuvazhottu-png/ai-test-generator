import pytest
from src.functions import add_numbers, divide_numbers, find_largest, validate_email, calculate_grade


# ─────────────────────────────────────────
# Tests for add_numbers
# ─────────────────────────────────────────

def test_add_numbers_positive():
    assert add_numbers(2, 3) == 5

def test_add_numbers_negative():
    assert add_numbers(-1, -4) == -5

def test_add_numbers_mixed():
    assert add_numbers(-3, 7) == 4

def test_add_numbers_zeros():
    assert add_numbers(0, 0) == 0

def test_add_numbers_floats():
    assert add_numbers(1.5, 2.5) == 4.0

def test_add_numbers_large():
    assert add_numbers(1000000, 2000000) == 3000000


# ─────────────────────────────────────────
# Tests for divide_numbers
# ─────────────────────────────────────────

def test_divide_numbers_basic():
    assert divide_numbers(10, 2) == 5.0

def test_divide_numbers_float_result():
    assert divide_numbers(7, 2) == 3.5

def test_divide_numbers_negative():
    assert divide_numbers(-9, 3) == -3.0

def test_divide_numbers_both_negative():
    assert divide_numbers(-9, -3) == 3.0

def test_divide_numbers_zero_numerator():
    assert divide_numbers(0, 5) == 0.0

def test_divide_numbers_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide_numbers(10, 0)

def test_divide_numbers_float_inputs():
    assert divide_numbers(5.0, 2.0) == 2.5


# ─────────────────────────────────────────
# Tests for find_largest
# ─────────────────────────────────────────

def test_find_largest_basic():
    assert find_largest([1, 2, 3]) == 3

def test_find_largest_single_element():
    assert find_largest([42]) == 42

def test_find_largest_negative_numbers():
    assert find_largest([-5, -1, -3]) == -1

def test_find_largest_mixed_numbers():
    assert find_largest([-10, 0, 10]) == 10

def test_find_largest_duplicates():
    assert find_largest([4, 4, 4]) == 4

def test_find_largest_floats():
    assert find_largest([1.1, 2.2, 3.3]) == 3.3

def test_find_largest_empty_list_raises():
    with pytest.raises(ValueError, match="List cannot be empty!"):
        find_largest([])

def test_find_largest_large_list():
    assert find_largest(list(range(1000))) == 999


# ─────────────────────────────────────────
# Tests for validate_email
# ─────────────────────────────────────────

def test_validate_email_valid():
    assert validate_email("user@example.com") is True

def test_validate_email_valid_subdomain():
    assert validate_email("user@mail.example.com") is True

def test_validate_email_empty_string():
    assert validate_email("") is False

def test_validate_email_no_at_symbol():
    assert validate_email("usergmail.com") is False

def test_validate_email_multiple_at_symbols():
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

def test_validate_email_valid_with_dots_in_local():
    assert validate_email("first.last@example.com") is True

def test_validate_email_valid_with_numbers():
    assert validate_email("user123@domain.org") is True


# ─────────────────────────────────────────
# Tests for calculate_grade
# ─────────────────────────────────────────

def test_calculate_grade_a():
    assert calculate_grade(95) == "A"

def test_calculate_grade_a_boundary():
    assert calculate_grade(90) == "A"

def test_calculate_grade_b():
    assert calculate_grade(85) == "B"

def test_calculate_grade_b_boundary():
    assert calculate_grade(80) == "B"

def test_calculate_grade_c():
    assert calculate_grade(75) == "C"

def test_calculate_grade_c_boundary():
    assert calculate_grade(70) == "C"

def test_calculate_grade_d():
    assert calculate_grade(65) == "D"

def test_calculate_grade_d_boundary():
    assert calculate_grade(60) == "D"

def test_calculate_grade_f():
    assert calculate_grade(50) == "F"

def test_calculate_grade_f_zero():
    assert calculate_grade(0) == "F"

def test_calculate_grade_perfect_score():
    assert calculate_grade(100) == "A"

def test_calculate_grade_negative_raises():
    with pytest.raises(ValueError, match="Score must be between 0 and 100!"):
        calculate_grade(-1)

def test_calculate_grade_above_100_raises():
    with pytest.raises(ValueError, match="Score must be between 0 and 100!"):
        calculate_grade(101)

def test_calculate_grade_just_below_a():
    assert calculate_grade(89) == "B"

def test_calculate_grade_just_below_b():
    assert calculate_grade(79) == "C"