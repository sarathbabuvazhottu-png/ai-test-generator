# These are the Python functions
# that AI will generate tests for!

def add_numbers(a, b):
    """Adds two numbers together"""
    return a + b


def divide_numbers(a, b):
    """Divides a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def find_largest(numbers):
    """Finds largest number in list"""
    if not numbers:
        raise ValueError("List cannot be empty!")
    return max(numbers)
def validate_email(email):
    """Checks if email format is valid"""

    # Rule 1 — Cannot be empty
    if len(email) == 0:
        return False

    # Rule 2 — Must have exactly ONE @
    if email.count("@") != 1:
        return False

    # Split into 2 parts
    local = email.split("@")[0]   # BEFORE @
    domain = email.split("@")[1]  # AFTER @

    # Rule 3 — Local part cannot be empty
    # Catches @gmail.com
    if len(local) == 0:
        return False

    # Rule 4 — Local cannot start with dot
    # Catches .@gmail.com
    if local.startswith("."):
        return False

    # Rule 5 — Domain cannot be empty
    # Catches sara@
    if len(domain) == 0:
        return False

    # Rule 6 — Domain cannot start with dot
    # Catches sara@.gmail.com
    if domain.startswith("."):
        return False

    # Rule 7 — Domain cannot end with dot
    # Catches sara@gmail.
    if domain.endswith("."):
        return False

    # Rule 8 — Domain must have a dot
    # Catches sara@gmailcom
    if "." not in domain:
        return False

    # ALL rules passed!
    return True





def calculate_grade(score):
    """Returns grade based on score"""
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100!")
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"