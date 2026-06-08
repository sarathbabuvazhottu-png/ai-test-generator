import pytest
from src.functions import add_numbers, divide_numbers, find_largest, validate_email, calculate_grade


# ============================================================
# Tests for add_numbers
# ============================================================

class TestAddNumbers:
    """Comprehensive tests for add_numbers function"""

    def test_add_two_positive_integers(self):
        """Test adding two positive integers"""
        assert add_numbers(2, 3) == 5

    def test_add_positive_and_negative(self):
        """Test adding a positive and negative number"""
        assert add_numbers(10, -4) == 6

    def test_add_two_negatives(self):
        """Test adding two negative numbers"""
        assert add_numbers(-5, -7) == -12

    def test_add_zeros(self):
        """Test adding zero to zero"""
        assert add_numbers(0, 0) == 0

    def test_add_zero_to_number(self):
        """Test adding zero to a number"""
        assert add_numbers(42, 0) == 42

    def test_add_floats(self):
        """Test adding two float numbers"""
        assert add_numbers(1.5, 2.5) == 4.0

    def test_add_large_numbers(self):
        """Test adding very large numbers"""
        assert add_numbers(1_000_000, 2_000_000) == 3_000_000

    def test_add_float_and_integer(self):
        """Test adding a float and an integer"""
        assert add_numbers(3.7, 2) == pytest.approx(5.7)

    def test_add_negative_and_zero(self):
        """Test adding a negative number and zero"""
        assert add_numbers(-10, 0) == -10

    def test_add_commutative(self):
        """Test that addition is commutative"""
        assert add_numbers(3, 7) == add_numbers(7, 3)


# ============================================================
# Tests for divide_numbers
# ============================================================

class TestDivideNumbers:
    """Comprehensive tests for divide_numbers function"""

    def test_divide_basic(self):
        """Test basic division"""
        assert divide_numbers(10, 2) == 5.0

    def test_divide_returns_float(self):
        """Test that division returns a float"""
        result = divide_numbers(7, 2)
        assert result == pytest.approx(3.5)

    def test_divide_by_one(self):
        """Test dividing by one returns the same number"""
        assert divide_numbers(99, 1) == 99.0

    def test_divide_negative_by_positive(self):
        """Test dividing negative by positive"""
        assert divide_numbers(-10, 2) == -5.0

    def test_divide_positive_by_negative(self):
        """Test dividing positive by negative"""
        assert divide_numbers(10, -2) == -5.0

    def test_divide_negative_by_negative(self):
        """Test dividing negative by negative gives positive"""
        assert divide_numbers(-10, -2) == 5.0

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number gives zero"""
        assert divide_numbers(0, 5) == 0.0

    def test_divide_by_zero_raises_value_error(self):
        """Test that dividing by zero raises ValueError"""
        with pytest.raises(ValueError):
            divide_numbers(10, 0)

    def test_divide_by_zero_error_message(self):
        """Test that the error message is correct when dividing by zero"""
        with pytest.raises(ValueError, match="Cannot divide by zero!"):
            divide_numbers(10, 0)

    def test_divide_float_by_float(self):
        """Test dividing floats"""
        assert divide_numbers(7.5, 2.5) == pytest.approx(3.0)

    def test_divide_large_numbers(self):
        """Test dividing large numbers"""
        assert divide_numbers(1_000_000, 1_000) == pytest.approx(1000.0)

    def test_divide_negative_zero_raises(self):
        """Test that dividing by negative zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero!"):
            divide_numbers(5, 0)


# ============================================================
# Tests for find_largest
# ============================================================

class TestFindLargest:
    """Comprehensive tests for find_largest function"""

    def test_find_largest_basic(self):
        """Test finding the largest in a simple list"""
        assert find_largest([1, 2, 3, 4, 5]) == 5

    def test_find_largest_with_negatives(self):
        """Test finding the largest when all numbers are negative"""
        assert find_largest([-10, -3, -7, -1]) == -1

    def test_find_largest_mixed(self):
        """Test finding the largest with mixed positive and negative numbers"""
        assert find_largest([-5, 0, 3, -2, 8]) == 8

    def test_find_largest_single_element(self):
        """Test finding the largest in a single-element list"""
        assert find_largest([42]) == 42

    def test_find_largest_all_same(self):
        """Test finding the largest when all elements are the same"""
        assert find_largest([7, 7, 7, 7]) == 7

    def test_find_largest_with_floats(self):
        """Test finding the largest with float values"""
        assert find_largest([1.1, 3.3, 2.2]) == pytest.approx(3.3)

    def test_find_largest_with_zero(self):
        """Test finding the largest when zero is included"""
        assert find_largest([0, -1, -2]) == 0

    def test_find_largest_large_list(self):
        """Test finding the largest in a large list"""
        numbers = list(range(1, 1001))
        assert find_largest(numbers) == 1000

    def test_find_largest_empty_list_raises_value_error(self):
        """Test that an empty list raises ValueError"""
        with pytest.raises(ValueError):
            find_largest([])

    def test_find_largest_empty_list_error_message(self):
        """Test that the error message is correct for empty list"""
        with pytest.raises(ValueError, match="List cannot be empty!"):
            find_largest([])

    def test_find_largest_unordered_list(self):
        """Test finding the largest in an unordered list"""
        assert find_largest([5, 1, 9, 3, 7]) == 9

    def test_find_largest_two_elements(self):
        """Test finding the largest in a two-element list"""
        assert find_largest([3, 99]) == 99


# ============================================================
# Tests for validate_email
# ============================================================

class TestValidateEmail:
    """Comprehensive tests for validate_email function"""

    # --- Valid emails ---
    def test_valid_basic_email(self):
        """Test a standard valid email"""
        assert validate_email("user@example.com") is True

    def test_valid_email_with_subdomain(self):
        """Test a valid email with a subdomain"""
        assert validate_email("user@mail.example.com") is True

    def test_valid_email_with_numbers(self):
        """Test a valid email with numbers"""
        assert validate_email("user123@domain.org") is True

    def test_valid_email_with_dots_in_local(self):
        """Test a valid email with dots in the local part"""
        assert validate_email("first.last@example.com") is True

    def test_valid_email_with_hyphens(self):
        """Test a valid email with hyphens"""
        assert validate_email("user-name@my-domain.com") is True

    def test_valid_email_uppercase(self):
        """Test a valid email with uppercase letters"""
        assert validate_email("User@Example.COM") is True

    # --- Invalid: Empty email ---
    def test_empty_email_is_invalid(self):
        """Test that an empty string is invalid"""
        assert validate_email("") is False

    # --- Invalid: Missing or multiple @ ---
    def test_no_at_sign_is_invalid(self):
        """Test that email without @ is invalid"""
        assert validate_email("userexample.com") is False

    def test_multiple_at_signs_is_invalid(self):
        """Test that email with multiple @ is invalid"""
        assert validate_email("user@@example.com") is False

    def test_two_at_signs_is_invalid(self):
        """Test another case of multiple @ signs"""
        assert validate_email("us@er@example.com") is False

    # --- Invalid: Empty local part ---
    def test_empty_local_part_is_invalid(self):
        """Test that email starting with @ is invalid"""
        assert validate_email("@gmail.com") is False

    # --- Invalid: Local starts with dot ---
    def test_local_starts_with_dot_is_invalid(self):
        """Test that local part starting with dot is invalid"""
        assert validate_email(".user@gmail.com") is False

    # --- Invalid: Empty domain ---
    def test_empty_domain_is_invalid(self):
        """Test that email with nothing after @ is invalid"""
        assert validate_email("user@") is False

    # --- Invalid: Domain starts with dot ---
    def test_domain_starts_with_dot_is_invalid(self):
        """Test that domain starting with a dot is invalid"""
        assert validate_email("user@.gmail.com") is False

    # --- Invalid: Domain ends with dot ---
    def test_domain_ends_with_dot_is_invalid(self):
        """Test that domain ending with a dot is invalid"""
        assert validate_email("user@gmail.") is False

    # --- Invalid: Domain has no dot ---
    def test_domain_has_no_dot_is_invalid(self):
        """Test that domain without a dot is invalid"""
        assert validate_email("user@gmailcom") is False

    # --- Additional edge cases ---
    def test_only_at_sign_is_invalid(self):
        """Test that a single @ sign is invalid"""
        assert validate_email("@") is False

    def test_dot_at_dot_is_invalid(self):
        """Test edge case with dots around @ sign"""
        assert validate_email(".@.") is False

    def test_valid_email_with_plus(self):
        """Test a valid email with plus sign in local part"""
        assert validate_email("user+tag@example.com") is True


# ============================================================
# Tests for calculate_grade
# ============================================================

class TestCalculateGrade:
    """Comprehensive tests for calculate_grade function"""

    # --- Grade A ---
    def test_score_100_is_A(self):
        """Test that score of 100 gives grade A"""
        assert calculate_grade(100) == "A"

    def test_score_90_is_A(self):
        """Test that score of 90 gives grade A"""
        assert calculate_grade(90) == "A"

    def test_score_95_is_A(self):
        """Test that score of 95 gives grade A"""
        assert calculate_grade(95) == "A"

    # --- Grade B ---
    def test_score_80_is_B(self):
        """Test that score of 80 gives grade B"""
        assert calculate_grade(80) == "B"

    def test_score_89_is_B(self):
        """Test that score of 89 gives grade B"""
        assert calculate_grade(89) == "B"

    def test_score_85_is_B(self):
        """Test that score of 85 gives grade B"""
        assert calculate_grade(85) == "B"

    # --- Grade C ---
    def test_score_70_is_C(self):
        """Test that score of 70 gives grade C"""
        assert calculate_grade(70) == "C"

    def test_score_79_is_C(self):
        """Test that score of 79 gives grade C"""
        assert calculate_grade(79) == "C"

    def test_score_75_is_C(self):
        """Test that score of 75 gives grade C"""
        assert calculate_grade(75) == "C"

    # --- Grade D ---
    def test_score_60_is_D(self):
        """Test that score of 60 gives grade D"""
        assert calculate_grade(60) == "D"

    def test_score_69_is_D(self):
        """Test that score of 69 gives grade D"""
        assert calculate_grade(69) == "D"

    def test_score_65_is_D(self):
        """Test that score of 65 gives grade D"""
        assert calculate_grade(65) == "D"

    # --- Grade F ---
    def test_score_0_is_F(self):
        """Test that score of 0 gives grade F"""
        assert calculate_grade(0) == "F"

    def test_score_59_is_F(self):
        """Test that score of 59 gives grade F"""
        assert calculate_grade(59) == "F"

    def test_score_30_is_F(self):
        """Test that score of 30 gives grade F"""
        assert calculate_grade(30) == "F"

    # --- Invalid scores ---
    def test_score_above_100_raises_value_error(self):
        """Test that score above 100 raises ValueError"""
        with pytest.raises(ValueError):
            calculate_grade(101)

    def test_score_below_0_raises_value_error(self):
        """Test that score below 0 raises ValueError"""
        with pytest.raises(ValueError):
            calculate_grade(-1)

    def test_score_above_100_error_message(self):
        """Test the error message for score above 100"""
        with pytest.raises(ValueError, match="Score must be between 0 and 100!"):
            calculate_grade(150)

    def test_score_below_0_error_message(self):
        """Test the error message for score below 0"""
        with pytest.raises(ValueError, match="Score must be between 0 and 100!"):
            calculate_grade(-10)

    def test_boundary_between_A_and_B(self):
        """Test boundary: 89 is B, 90 is A"""
        assert calculate_grade(89) == "B"
        assert calculate_grade(90) == "A"

    def test_boundary_between_B_and_C(self):
        """Test boundary: 79 is C, 80 is B"""
        assert calculate_grade(79) == "C"
        assert calculate_grade(80) == "B"

    def test_boundary_between_C_and_D(self):
        """Test boundary: 69 is D, 70 is C"""
        assert calculate_grade(69) == "D"
        assert calculate_grade(70) == "C"

    def test_boundary_between_D_and_F(self):
        """Test boundary: 59 is F, 60 is D"""
        assert calculate_grade(59) == "F"
        assert calculate_grade(60) == "D"