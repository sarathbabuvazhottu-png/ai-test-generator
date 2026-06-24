import pytest
from unittest.mock import patch
import math


# Assuming the functions are in a module called 'math_operations'
# For testing purposes, we'll define them inline or import them

def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# ==================== ADD NUMBERS TESTS ====================

class TestAddNumbers:
    
    # Basic positive integers
    def test_add_two_positive_integers(self):
        assert add_numbers(2, 3) == 5

    def test_add_zero_and_positive(self):
        assert add_numbers(0, 5) == 5

    def test_add_positive_and_zero(self):
        assert add_numbers(5, 0) == 5

    def test_add_two_zeros(self):
        assert add_numbers(0, 0) == 0

    # Negative numbers
    def test_add_two_negative_integers(self):
        assert add_numbers(-2, -3) == -5

    def test_add_negative_and_positive(self):
        assert add_numbers(-2, 3) == 1

    def test_add_positive_and_negative(self):
        assert add_numbers(3, -2) == 1

    def test_add_negative_and_zero(self):
        assert add_numbers(-5, 0) == -5

    def test_add_zero_and_negative(self):
        assert add_numbers(0, -5) == -5

    # Floats
    def test_add_two_floats(self):
        assert add_numbers(1.5, 2.5) == 4.0

    def test_add_float_and_integer(self):
        assert add_numbers(1.5, 2) == 3.5

    def test_add_integer_and_float(self):
        assert add_numbers(2, 1.5) == 3.5

    def test_add_negative_floats(self):
        assert add_numbers(-1.5, -2.5) == -4.0

    def test_add_float_precision(self):
        result = add_numbers(0.1, 0.2)
        assert result == pytest.approx(0.3)

    # Large numbers
    def test_add_large_numbers(self):
        assert add_numbers(1000000, 2000000) == 3000000

    def test_add_very_large_numbers(self):
        assert add_numbers(10**18, 10**18) == 2 * 10**18

    # Strings (Python allows + for strings)
    def test_add_two_strings(self):
        assert add_numbers("hello", " world") == "hello world"

    def test_add_empty_strings(self):
        assert add_numbers("", "") == ""

    def test_add_string_and_empty_string(self):
        assert add_numbers("hello", "") == "hello"

    # Lists (Python allows + for lists)
    def test_add_two_lists(self):
        assert add_numbers([1, 2], [3, 4]) == [1, 2, 3, 4]

    def test_add_empty_lists(self):
        assert add_numbers([], []) == []

    def test_add_list_and_empty_list(self):
        assert add_numbers([1, 2], []) == [1, 2]

    # Return type checks
    def test_add_integers_returns_integer(self):
        result = add_numbers(2, 3)
        assert isinstance(result, int)

    def test_add_floats_returns_float(self):
        result = add_numbers(2.0, 3.0)
        assert isinstance(result, float)

    def test_add_int_and_float_returns_float(self):
        result = add_numbers(2, 3.0)
        assert isinstance(result, float)

    # Commutativity
    def test_add_is_commutative(self):
        assert add_numbers(3, 5) == add_numbers(5, 3)

    def test_add_negative_is_commutative(self):
        assert add_numbers(-3, 5) == add_numbers(5, -3)

    # Special float values
    def test_add_infinity(self):
        assert add_numbers(float('inf'), 1) == float('inf')

    def test_add_negative_infinity(self):
        assert add_numbers(float('-inf'), 1) == float('-inf')

    def test_add_nan(self):
        result = add_numbers(float('nan'), 1)
        assert math.isnan(result)

    # Complex numbers
    def test_add_complex_numbers(self):
        assert add_numbers(1+2j, 3+4j) == 4+6j

    # Boolean (bool is subclass of int in Python)
    def test_add_booleans(self):
        assert add_numbers(True, True) == 2

    def test_add_bool_and_int(self):
        assert add_numbers(True, 5) == 6

    def test_add_false_and_int(self):
        assert add_numbers(False, 5) == 5

    # TypeError cases
    def test_add_int_and_string_raises_type_error(self):
        with pytest.raises(TypeError):
            add_numbers(1, "string")

    def test_add_string_and_int_raises_type_error(self):
        with pytest.raises(TypeError):
            add_numbers("string", 1)

    def test_add_none_raises_type_error(self):
        with pytest.raises(TypeError):
            add_numbers(None, 1)

    def test_add_list_and_int_raises_type_error(self):
        with pytest.raises(TypeError):
            add_numbers([1, 2], 3)

    # Identity property
    def test_add_identity_property(self):
        assert add_numbers(5, 0) == 5

    # Negative result
    def test_add_results_in_negative(self):
        assert add_numbers(3, -5) == -2

    # Tuples
    def test_add_tuples(self):
        assert add_numbers((1, 2), (3, 4)) == (1, 2, 3, 4)


# ==================== DIVIDE NUMBERS TESTS ====================

class TestDivideNumbers:

    # Basic division
    def test_divide_two_positive_integers(self):
        assert divide_numbers(10, 2) == 5.0

    def test_divide_returns_float(self):
        result = divide_numbers(10, 2)
        assert isinstance(result, float)

    def test_divide_positive_by_one(self):
        assert divide_numbers(5, 1) == 5.0

    def test_divide_negative_by_one(self):
        assert divide_numbers(-5, 1) == -5.0

    def test_divide_zero_by_positive(self):
        assert divide_numbers(0, 5) == 0.0

    def test_divide_zero_by_negative(self):
        assert divide_numbers(0, -5) == 0.0

    # Division by zero
    def test_divide_by_zero_raises_value_error(self):
        with pytest.raises(ValueError):
            divide_numbers(5, 0)

    def test_divide_by_zero_error_message(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide_numbers(5, 0)

    def test_divide_zero_by_zero_raises_value_error(self):
        with pytest.raises(ValueError):
            divide_numbers(0, 0)

    def test_divide_negative_by_zero_raises_value_error(self):
        with pytest.raises(ValueError):
            divide_numbers(-5, 0)

    def test_divide_float_by_zero_raises_value_error(self):
        with pytest.raises(ValueError):
            divide_numbers(5.0, 0)

    def test_divide_by_zero_float_raises_value_error(self):
        with pytest.raises(ValueError):
            divide_numbers(5, 0.0)

    # Negative numbers
    def test_divide_negative_by_positive(self):
        assert divide_numbers(-10, 2) == -5.0

    def test_divide_positive_by_negative(self):
        assert divide_numbers(10, -2) == -5.0

    def test_divide_negative_by_negative(self):
        assert divide_numbers(-10, -2) == 5.0

    # Floats
    def test_divide_floats(self):
        assert divide_numbers(5.0, 2.0) == 2.5

    def test_divide_float_by_integer(self):
        assert divide_numbers(5.0, 2) == 2.5

    def test_divide_integer_by_float(self):
        assert divide_numbers(5, 2.0) == 2.5

    def test_divide_float_precision(self):
        result = divide_numbers(1.0, 3.0)
        assert result == pytest.approx(0.3333333333333333)

    # Large numbers
    def test_divide_large_numbers(self):
        assert divide_numbers(10**18, 10**9) == pytest.approx(10**9)

    def test_divide_small_numbers(self):
        result = divide_numbers(0.001, 0.01)
        assert result == pytest.approx(0.1)

    # Fractions
    def test_divide_results_in_fraction(self):
        assert divide_numbers(1, 2) == 0.5

    def test_divide_results_in_one(self):
        assert divide_numbers(5, 5) == 1.0

    def test_divide_results_in_less_than_one(self):
        assert divide_numbers(1, 4) == 0.25

    # Special float values
    def test_divide_infinity_by_positive(self):
        assert divide_numbers(float('inf'), 2) == float('inf')

    def test_divide_positive_by_infinity(self):
        assert divide_numbers(1, float('inf')) == 0.0

    def test_divide_negative_infinity(self):
        assert divide_numbers(float('-inf'), 2) == float('-inf')

    def test_divide_nan(self):
        result = divide_numbers(float('nan'), 2)
        assert math.isnan(result)

    # Boolean
    def test_divide_true_by_true(self):
        assert divide_numbers(True, True) == 1.0

    def test_divide_false_by_true(self):
        assert divide_numbers(False, True) == 0.0

    def test_divide_true_by_false_raises_value_error(self):
        with pytest.raises(ValueError):
            divide_numbers(True, False)

    def test_divide_int_by_true(self):
        assert divide_numbers(10, True) == 10.0

    # TypeError cases
    def test_divide_string_raises_type_error(self):
        with pytest.raises(TypeError):
            divide_numbers("10", 2)

    def test_divide_none_raises_type_error(self):
        with pytest.raises(TypeError):
            divide_numbers(None, 2)

    def test_divide_by_none_raises_type_error(self):
        with pytest.raises(TypeError):
            divide_numbers(2, None)

    def test_divide_list_raises_type_error(self):
        with pytest.raises(TypeError):
            divide_numbers([10], 2)

    # Complex numbers
    def test_divide_complex_numbers(self):
        result = divide_numbers(4+2j, 2)
        assert result == 2+1j

    # Exact results
    def test_divide_exact_result(self):
        assert divide_numbers(9, 3) == 3.0

    def test_divide_by_itself(self):
        assert divide_numbers(7, 7) == 1.0

    # Negative zero edge case
    def test_divide_by_negative_zero_float_raises_value_error(self):
        with pytest.raises(ValueError):
            divide_numbers(5, -0)

    # Very small divisor
    def test_divide_by_very_small_number(self):
        result = divide_numbers(1, 1e-10)
        assert result == pytest.approx(1e10)

    # Error is specifically ValueError and not other exceptions
    def test_divide_by_zero_is_value_error_not_zero_division_error(self):
        with pytest.raises(ValueError) as exc_info:
            divide_numbers(5, 0)
        assert type(exc_info.value) == ValueError

    def test_divide_error_message_exact(self):
        with pytest.raises(ValueError) as exc_info:
            divide_numbers(5, 0)
        assert str(exc_info.value) == "Cannot divide by zero"


# ==================== PARAMETRIZED TESTS ====================

class TestAddNumbersParametrized:

    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),
        (0, 0, 0),
        (-1, -2, -3),
        (-1, 2, 1),
        (1, -2, -1),
        (100, 200, 300),
        (0, 5, 5),
        (5, 0, 5),
        (1.5, 2.5, 4.0),
        (-1.5, 1.5, 0.0),
    ])
    def test_add_parametrized(self, a, b, expected):
        assert add_numbers(a, b) == expected

    @pytest.mark.parametrize("a, b", [
        (1, "string"),
        ("string", 1),
        (None, 1),
        (1, None),
        ([1], 1),
        (1, [1]),
    ])
    def test_add_type_error_parametrized(self, a, b):
        with pytest.raises(TypeError):
            add_numbers(a, b)


class TestDivideNumbersParametrized:

    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5.0),
        (9, 3, 3.0),
        (1, 2, 0.5),
        (-10, 2, -5.0),
        (10, -2, -5.0),
        (-10, -2, 5.0),
        (0, 5, 0.0),
        (100, 10, 10.0),
        (7, 7, 1.0),
        (1, 4, 0.25),
    ])
    def test_divide_parametrized(self, a, b, expected):
        assert divide_numbers(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize("a", [0, 1, -1, 100, -100, 0.5, -0.5])
    def test_divide_by_zero_always_raises(self, a):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide_numbers(a, 0)


# ==================== INTEGRATION / COMBINED TESTS ====================

class TestCombinedOperations:

    def test_add_then_divide(self):
        result = divide_numbers(add_numbers(4, 6), 2)
        assert result == 5.0

    def test_divide_then_add(self):
        result = add_numbers(divide_numbers(10, 2), divide_numbers(6, 3))
        assert result == 7.0

    def test_add_results_used_in_division(self):
        a = add_numbers(3, 7)  # 10
        b = add_numbers(1, 1)  # 2
        assert divide_numbers(a, b) == 5.0

    def test_divide_result_used_in_addition(self):
        a = divide_numbers(10, 2)  # 5.0
        b = divide_numbers(6, 3)   # 2.0
        assert add_numbers(a, b) == 7.0

    def test_chain_multiple_adds(self):
        result = add_numbers(add_numbers(1, 2), add_numbers(3, 4))
        assert result == 10

    def test_chain_multiple_divides(self):
        result = divide_numbers(divide_numbers(100, 10), 2)
        assert result == 5.0