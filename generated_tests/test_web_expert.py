import pytest


# ============================================================
# Source code with bugs (as described)
# ============================================================

def add_numbers(a, b):
    return a - b  # Bug 1: should be a + b


def divide_numbers(a, b):
    return a / b  # Bug 2: no zero check


def find_largest(numbers):
    return min(numbers)  # Bug 3: should be max


def calculate_grade(score):
    if score >= 90:
        return "B"  # Bug 4: should be "A"
    elif score >= 80:
        return "A"  # Bug 4: should be "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ============================================================
# Tests for add_numbers (Bug 1)
# ============================================================

class TestAddNumbers:

    def test_add_two_positive_numbers(self):
        """2 + 3 should return 5, but returns -1 due to bug"""
        result = add_numbers(2, 3)
        assert result == 5, f"Expected 5 but got {result}"

    def test_add_zero_and_positive(self):
        """0 + 5 should return 5"""
        result = add_numbers(0, 5)
        assert result == 5

    def test_add_positive_and_zero(self):
        """5 + 0 should return 5"""
        result = add_numbers(5, 0)
        assert result == 5

    def test_add_two_zeros(self):
        """0 + 0 should return 0"""
        result = add_numbers(0, 0)
        assert result == 0

    def test_add_negative_numbers(self):
        """-2 + -3 should return -5"""
        result = add_numbers(-2, -3)
        assert result == -5

    def test_add_positive_and_negative(self):
        """5 + (-3) should return 2"""
        result = add_numbers(5, -3)
        assert result == 2

    def test_add_negative_and_positive(self):
        """-3 + 5 should return 2"""
        result = add_numbers(-3, 5)
        assert result == 2

    def test_add_large_numbers(self):
        """1000 + 2000 should return 3000"""
        result = add_numbers(1000, 2000)
        assert result == 3000

    def test_add_floats(self):
        """1.5 + 2.5 should return 4.0"""
        result = add_numbers(1.5, 2.5)
        assert result == pytest.approx(4.0)

    def test_add_float_and_int(self):
        """1.5 + 2 should return 3.5"""
        result = add_numbers(1.5, 2)
        assert result == pytest.approx(3.5)

    def test_add_commutativity_fails_due_to_bug(self):
        """Due to bug, add_numbers(2,3) != add_numbers(3,2)"""
        # This test documents that commutativity is broken
        result_a = add_numbers(2, 3)
        result_b = add_numbers(3, 2)
        # Correct behavior: both should be 5
        assert result_a == 5
        assert result_b == 5

    def test_add_returns_not_subtraction(self):
        """Explicitly verify that result is NOT a - b"""
        a, b = 10, 4
        result = add_numbers(a, b)
        assert result != a - b, "Function is incorrectly returning a - b"
        assert result == a + b

    def test_add_equal_numbers(self):
        """3 + 3 should return 6"""
        result = add_numbers(3, 3)
        assert result == 6

    def test_add_very_small_floats(self):
        """0.1 + 0.2 should be approximately 0.3"""
        result = add_numbers(0.1, 0.2)
        assert result == pytest.approx(0.3)


# ============================================================
# Tests for divide_numbers (Bug 2)
# ============================================================

class TestDivideNumbers:

    def test_divide_basic(self):
        """10 / 2 should return 5.0"""
        result = divide_numbers(10, 2)
        assert result == 5.0

    def test_divide_by_zero_raises_exception(self):
        """Dividing by zero should raise ZeroDivisionError or ValueError"""
        with pytest.raises((ZeroDivisionError, ValueError)):
            divide_numbers(10, 0)

    def test_divide_zero_by_zero_raises_exception(self):
        """0 / 0 should raise an exception"""
        with pytest.raises((ZeroDivisionError, ValueError)):
            divide_numbers(0, 0)

    def test_divide_negative_by_zero_raises_exception(self):
        """-5 / 0 should raise an exception"""
        with pytest.raises((ZeroDivisionError, ValueError)):
            divide_numbers(-5, 0)

    def test_divide_float_by_zero_raises_exception(self):
        """3.14 / 0 should raise an exception"""
        with pytest.raises((ZeroDivisionError, ValueError)):
            divide_numbers(3.14, 0)

    def test_divide_positive_numbers(self):
        """9 / 3 should return 3.0"""
        result = divide_numbers(9, 3)
        assert result == 3.0

    def test_divide_results_in_float(self):
        """7 / 2 should return 3.5"""
        result = divide_numbers(7, 2)
        assert result == pytest.approx(3.5)

    def test_divide_negative_numbers(self):
        """-10 / 2 should return -5.0"""
        result = divide_numbers(-10, 2)
        assert result == -5.0

    def test_divide_negative_by_negative(self):
        """-10 / -2 should return 5.0"""
        result = divide_numbers(-10, -2)
        assert result == 5.0

    def test_divide_zero_by_positive(self):
        """0 / 5 should return 0.0"""
        result = divide_numbers(0, 5)
        assert result == 0.0

    def test_divide_large_numbers(self):
        """1000000 / 1000 should return 1000.0"""
        result = divide_numbers(1000000, 1000)
        assert result == pytest.approx(1000.0)

    def test_divide_small_numbers(self):
        """1 / 1000 should return 0.001"""
        result = divide_numbers(1, 1000)
        assert result == pytest.approx(0.001)

    def test_divide_by_one(self):
        """Any number divided by 1 should return itself"""
        result = divide_numbers(42, 1)
        assert result == pytest.approx(42.0)

    def test_divide_by_itself(self):
        """Any non-zero number divided by itself should return 1"""
        result = divide_numbers(7, 7)
        assert result == pytest.approx(1.0)

    def test_divide_does_not_crash_on_zero(self):
        """Ensure the function handles division by zero gracefully"""
        try:
            result = divide_numbers(5, 0)
            # If it doesn't raise, it must return a meaningful value or infinity
            assert result is not None
        except (ZeroDivisionError, ValueError):
            pass  # This is acceptable behavior
        except Exception as e:
            pytest.fail(f"Unexpected exception type raised: {type(e).__name__}: {e}")


# ============================================================
# Tests for find_largest (Bug 3)
# ============================================================

class TestFindLargest:

    def test_find_largest_basic(self):
        """[1, 5, 3] should return 5, not 1"""
        result = find_largest([1, 5, 3])
        assert result == 5, f"Expected 5 but got {result}"

    def test_find_largest_single_element(self):
        """[42] should return 42"""
        result = find_largest([42])
        assert result == 42

    def test_find_largest_all_same(self):
        """[3, 3, 3] should return 3"""
        result = find_largest([3, 3, 3])
        assert result == 3

    def test_find_largest_sorted_ascending(self):
        """[1, 2, 3, 4, 5] should return 5"""
        result = find_largest([1, 2, 3, 4, 5])
        assert result == 5

    def test_find_largest_sorted_descending(self):
        """[5, 4, 3, 2, 1] should return 5"""
        result = find_largest([5, 4, 3, 2, 1])
        assert result == 5

    def test_find_largest_with_negatives(self):
        """[-1, -5, -3] should return -1"""
        result = find_largest([-1, -5, -3])
        assert result == -1

    def test_find_largest_mixed_positive_negative(self):
        """[-10, 0, 10] should return 10"""
        result = find_largest([-10, 0, 10])
        assert result == 10

    def test_find_largest_with_zero(self):
        """[0, 1, 2] should return 2"""
        result = find_largest([0, 1, 2])
        assert result == 2

    def test_find_largest_large_list(self):
        """Large list should still find maximum"""
        numbers = list(range(1, 1001))
        result = find_largest(numbers)
        assert result == 1000

    def test_find_largest_with_duplicates(self):
        """[3, 1, 4, 1, 5, 9, 2, 6, 5] should return 9"""
        result = find_largest([3, 1, 4, 1, 5, 9, 2, 6, 5])
        assert result == 9

    def test_find_largest_returns_max_not_min(self):
        """Explicitly verify result is max, not min"""
        numbers = [1, 5, 3]
        result = find_largest(numbers)
        assert result == max(numbers), f"Expected {max(numbers)} but got {result}"
        assert result != min(numbers), "Function incorrectly returns minimum"

    def test_find_largest_floats(self):
        """[1.1, 2.2, 3.3] should return 3.3"""
        result = find_largest([1.1, 2.2, 3.3])
        assert result == pytest.approx(3.3)

    def test_find_largest_two_elements(self):
        """[10, 20] should return 20"""
        result = find_largest([10, 20])
        assert result == 20

    def test_find_largest_two_elements_reversed(self):
        """[20, 10] should return 20"""
        result = find_largest([20, 10])
        assert result == 20

    def test_find_largest_all_negative_numbers(self):
        """[-100, -50, -200] should return -50"""
        result = find_largest([-100, -50, -200])
        assert result == -50

    def test_find_largest_with_very_large_number(self):
        """Should handle very large numbers"""
        numbers = [1, 999999999, 2]
        result = find_largest(numbers)
        assert result == 999999999


# ============================================================
# Tests for calculate_grade (Bug 4)
# ============================================================

class TestCalculateGrade:

    # --- A grade tests ---
    def test_grade_a_score_95(self):
        """Score 95 should return 'A', not 'B'"""
        result = calculate_grade(95)
        assert result == "A", f"Expected 'A' but got '{result}'"

    def test_grade_a_score_90(self):
        """Score 90 (boundary) should return 'A'"""
        result = calculate_grade(90)
        assert result == "A"

    def test_grade_a_score_100(self):
        """Score 100 should return 'A'"""
        result = calculate_grade(100)
        assert result == "A"

    def test_grade_a_score_99(self):
        """Score 99 should return 'A'"""
        result = calculate_grade(99)
        assert result == "A"

    def test_grade_a_score_91(self):
        """Score 91 should return 'A'"""
        result = calculate_grade(91)
        assert result == "A"

    # --- B grade tests ---
    def test_grade_b_score_85(self):
        """Score 85 should return 'B'"""
        result = calculate_grade(85)
        assert result == "B", f"Expected 'B' but got '{result}'"

    def test_grade_b_score_80(self):
        """Score 80 (boundary) should return 'B'"""
        result = calculate_grade(80)
        assert result == "B"

    def test_grade_b_score_89(self):
        """Score 89 should return 'B'"""
        result = calculate_grade(89)
        assert result == "B"

    def test_grade_b_score_81(self):
        """Score 81 should return 'B'"""
        result = calculate_grade(81)
        assert result == "B"

    # --- C grade tests ---
    def test_grade_c_score_75(self):
        """Score 75 should return 'C'"""
        result = calculate_grade(75)
        assert result == "C"

    def test_grade_c_score_70(self):
        """Score 70 (boundary) should return 'C'"""
        result = calculate_grade(70)
        assert result == "C"

    def test_grade_c_score_79(self):
        """Score 79 should return 'C'"""
        result = calculate_grade(79)
        assert result == "C"

    def test_grade_c_score_71(self):
        """Score 71 should return 'C'"""
        result = calculate_grade(71)
        assert result == "C"

    # --- D grade tests ---
    def test_grade_d_score_65(self):
        """Score 65 should return 'D'"""
        result = calculate_grade(65)
        assert result == "D"

    def test_grade_d_score_60(self):
        """Score 60 (boundary) should return 'D'"""
        result = calculate_grade(60)
        assert result == "D"

    def test_grade_d_score_69(self):
        """Score 69 should return 'D'"""
        result = calculate_grade(69)
        assert result == "D"

    def test_grade_d_score_61(self):
        """Score 61 should return 'D'"""
        result = calculate_grade(61)
        assert result == "D"

    # --- F grade tests ---
    def test_grade_f_score_50(self):
        """Score 50 should return 'F'"""
        result = calculate_grade(50)
        assert result == "F"

    def test_grade_f_score_0(self):
        """Score 0 should return 'F'"""
        result = calculate_grade(0)
        assert result == "F"

    def test_grade_f_score_59(self):
        """Score 59 (just below D boundary) should return 'F'"""
        result = calculate_grade(59)
        assert result == "F"

    def test_grade_f_negative_score(self):
        """Negative score should return 'F'"""
        result = calculate_grade(-10)
        assert result == "F"

    # --- Boundary swap bug tests ---
    def test_grade_a_is_not_b(self):
        """Score >= 90 must NOT return 'B'"""
        result = calculate_grade(95)
        assert result != "B", "Bug detected: A and B grades are swapped"

    def test_grade_b_is_not_a(self):
        """Score in 80-89 range must NOT return 'A'"""
        result = calculate_grade(85)
        assert result != "A", "Bug detected: A and B grades are swapped"

    def test_grade_boundary_89(self):
        """Score 89 should return 'B', not 'A'"""
        result = calculate_grade(89)
        assert result == "B"
        assert result != "A"

    def test_grade_boundary_90_vs_89(self):
        """Score 90 should return higher grade than score 89"""
        grade_90 = calculate_grade(90)
        grade_89 = calculate_grade(89)
        assert grade_90 == "A"
        assert grade_89 == "B"
        assert grade_90 != grade_89

    def test_grade_all_letters_correct(self):
        """Parameterized check for all grade boundaries"""
        test_cases = [
            (100, "A"),
            (95, "A"),
            (90, "A"),
            (89, "B"),
            (85, "B"),
            (80, "B"),
            (79, "C"),
            (75, "C"),
            (70, "C"),
            (69, "D"),
            (65, "D"),
            (60, "D"),
            (59, "F"),
            (50, "F"),
            (0, "F"),
        ]
        for score, expected in test_cases:
            result = calculate_grade(score)
            assert result == expected, (
                f"Score {score}: expected '{expected}' but got '{result}'"
            )


# ============================================================
# Parametrized tests for all functions
# ============================================================

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (1, 1, 2),
    (-1, -1, -2),
    (10, -5, 5),
    (-5, 10, 5),
    (100, 200, 300),
    (0, 100, 100),
    (100, 0, 100),
])
def test_add_numbers_parametrized(a, b, expected):
    assert add_numbers(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (0, 5, 0.0),
    (-10, 2, -5.0),
    (-10, -2, 5.0),
    (7, 2, 3.5),
    (1, 4, 0.25),
])
def test_divide_numbers_parametrized(a, b, expected):
    assert divide_numbers(a, b) == pytest.approx(expected)


@pytest.mark.parametrize("a", [0, 1, -1, 100, -100])
def test_divide_by_zero_parametrized(a):
    with pytest.raises((ZeroDivisionError, ValueError)):
        divide_numbers(a, 0)


@pytest.mark.parametrize("numbers, expected", [
    ([1, 5, 3], 5),
    ([5, 4, 3, 2, 1], 5),
    ([-1, -5, -3], -1),
    ([0], 0),
    ([100, 1, 50], 100),
    ([1, 2, 3, 4, 5], 5),
    ([-10, 0, 10], 10),
])
def test_find_largest_parametrized(numbers, expected):
    assert find_largest(numbers) == expected


@pytest.mark.parametrize("score, expected_grade", [
    (100, "A"),
    (95, "A"),
    (90, "A"),
    (89, "B"),
    (80, "B"),
    (79, "C"),
    (70, "C"),
    (69, "D"),
    (60, "D"),
    (59, "F"),
    (0, "F"),
])
def test_calculate_grade_parametrized(score, expected_grade):
    assert calculate_grade(score) == expected_grade