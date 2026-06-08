import pytest
from src.functions import add_numbers, divide_numbers, find_largest, validate_email, calculate_grade


# Tests for add_numbers
class TestAddNumbers:
    def test_add_positive_numbers(self):
        assert add_numbers(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add_numbers(-2, -3) == -5

    def test_add_positive_and_negative(self):
        assert add_numbers(-2, 3) == 1

    def test_add_zeros(self):
        assert add_numbers(0, 0) == 0

    def test_add_floats(self):
        assert add_numbers(1.5, 2.5) == 4.0

    def test_add_large_numbers(self):
        assert add_numbers(1000000, 2000000) == 3000000

    def test_add_zero_and_number(self):
        assert add_numbers(0, 5) == 5


# Tests for divide_numbers
class TestDivideNumbers:
    def test_divide_positive_numbers(self):
        assert divide_numbers(10, 2) == 5.0

    def test_divide_negative_numbers(self):
        assert divide_numbers(-10, -2) == 5.0

    def test_divide_positive_by_negative(self):
        assert divide_numbers(10, -2) == -5.0

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError) as exc_info:
            divide_numbers(10, 0)
        assert "Cannot divide by zero!" in str(exc_info.value)

    def test_divide_zero_by_number(self):
        assert divide_numbers(0, 5) == 0.0

    def test_divide_floats(self):
        assert divide_numbers(7.5, 2.5) == 3.0

    def test_divide_returns_float(self):
        result = divide_numbers(10, 4)
        assert result == 2.5


# Tests for find_largest
class TestFindLargest:
    def test_find_largest_positive_numbers(self):
        assert find_largest([1, 2, 3, 4, 5]) == 5

    def test_find_largest_negative_numbers(self):
        assert find_largest([-1, -2, -3, -4, -5]) == -1

    def test_find_largest_mixed_numbers(self):
        assert find_largest([-10, 0, 10, 5]) == 10

    def test_find_largest_single_element(self):
        assert find_largest([42]) == 42

    def test_find_largest_empty_list_raises_error(self):
        with pytest.raises(ValueError) as exc_info:
            find_largest([])
        assert "List cannot be empty!" in str(exc_info.value)

    def test_find_largest_with_duplicates(self):
        assert find_largest([5, 5, 5, 5]) == 5

    def test_find_largest_with_floats(self):
        assert find_largest([1.1, 2.2, 3.3]) == 3.3


# Tests for validate_email
class TestValidateEmail:
    def test_valid_email(self):
        assert validate_email("sara@gmail.com") == True

    def test_empty_email(self):
        assert validate_email("") == False

    def test_missing_at_symbol(self):
        assert validate_email("sagmail.com") == False

    def test_multiple_at_symbols(self):
        assert validate_email("sa@ra@gmail.com") == False

    def test_missing_local_part(self):
        assert validate_email("@gmail.com") == False

    def test_local_starts_with_dot(self):
        assert validate_email(".sara@gmail.com") == False

    def test_missing_domain(self):
        assert validate_email("sara@") == False

    def test_domain_starts_with_dot(self):
        assert validate_email("sara@.gmail.com") == False

    def test_domain_ends_with_dot(self):
        assert validate_email("sara@gmail.") == False

    def test_domain_missing_dot(self):
        assert validate_email("sara@gmailcom") == False

    def test_valid_email_with_dots_in_local(self):
        assert validate_email("sara.smith@gmail.com") == True

    def test_valid_email_with_subdomain(self):
        assert validate_email("sara@mail.gmail.com") == True

    def test_valid_email_with_numbers(self):
        assert validate_email("sara123@gmail.com") == True


# Tests for calculate_grade
class TestCalculateGrade:
    def test_score_90_returns_A(self):
        assert calculate_grade(90) == "A"

    def test_score_100_returns_A(self):
        assert calculate_grade(100) == "A"

    def test_score_95_returns_A(self):
        assert calculate_grade(95) == "A"

    def test_score_80_returns_B(self):
        assert calculate_grade(80) == "B"

    def test_score_85_returns_B(self):
        assert calculate_grade(85) == "B"

    def test_score_70_returns_C(self):
        assert calculate_grade(70) == "C"

    def test_score_75_returns_C(self):
        assert calculate_grade(75) == "C"

    def test_score_60_returns_D(self):
        assert calculate_grade(60) == "D"

    def test_score_65_returns_D(self):
        assert calculate_grade(65) == "D"

    def test_score_59_returns_F(self):
        assert calculate_grade(59) == "F"

    def test_score_0_returns_F(self):
        assert calculate_grade(0) == "F"

    def test_negative_score_raises_error(self):
        with pytest.raises(ValueError) as exc_info:
            calculate_grade(-1)
        assert "Score must be between 0 and 100!" in str(exc_info.value)

    def test_score_above_100_raises_error(self):
        with pytest.raises(ValueError) as exc_info:
            calculate_grade(101)
        assert "Score must be between 0 and 100!" in str(exc_info.value)

    def test_score_89_returns_B(self):
        assert calculate_grade(89) == "B"

    def test_score_79_returns_C(self):
        assert calculate_grade(79) == "C"

    def test_score_69_returns_D(self):
        assert calculate_grade(69) == "D"