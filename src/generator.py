import anthropic
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load your secret API keys
load_dotenv()

# Connect to Claude AI
claude_client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Connect to GPT-4
openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def build_prompt(code, style):
    """
    Builds the prompt for
    the given style!
    """
    if style == "basic":
        return f"""
        Write pytest unit tests for
        this Python code:

        {code}

        IMPORTANT RULES:
        - Use this import EXACTLY:
          from src.functions import add_numbers, divide_numbers, find_largest, validate_email, calculate_grade
        - Do NOT use 'from solution import'
        - Close all brackets properly
        - Return only complete working code
        Nothing else.
        """

    elif style == "detailed":
        return f"""
        Write comprehensive pytest
        unit tests for this code:

        {code}

        IMPORTANT RULES:
        - Use this import EXACTLY:
          from src.functions import add_numbers, divide_numbers, find_largest, validate_email, calculate_grade
        - Do NOT use 'from solution import'
        - Close all brackets properly
        - Return only complete working code

        Include:
        - Normal input tests
        - Edge case tests
        - Error handling tests
        - Maximum 20 test functions
        """

    elif style == "expert":
        return f"""
        You are a senior developer.
        Write ALL possible pytest tests
        for this Python code:

        {code}

        IMPORTANT RULES:
        - Use this import EXACTLY:
          from src.functions import add_numbers, divide_numbers, find_largest, validate_email, calculate_grade
        - Do NOT use 'from solution import'
        - Close all brackets properly
        - Return only complete working code
        - Maximum 25 test functions

        Think about:
        - What inputs could break this?
        - What edge cases exist?
        - What errors should be raised?
        - What boundary values matter?
        """


def generate_with_claude(code, style):
    """
    Sends code to Claude AI
    and gets tests back!
    """
    question = build_prompt(code, style)

    print(f"   Sending to Claude AI...")
    response = claude_client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8000,
        messages=[
            {"role": "user", "content": question}
        ]
    )

    return response.content[0].text


def generate_with_gpt4(code, style):
    """
    Sends code to GPT-4
    and gets tests back!
    """
    question = build_prompt(code, style)

    print(f"   Sending to GPT-4...")
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=8000,
        messages=[
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content


def clean_code(text):
    """
    Removes markdown formatting
    from AI response
    """
    text = text.replace("```python", "")
    text = text.replace("```", "")
    text = text.replace(
        "from solution import",
        "from src.functions import"
    )
    text = text.replace(
        "import solution",
        "from src.functions import add_numbers, divide_numbers, find_largest, validate_email, calculate_grade"
    )
    return text.strip()


def save_tests(tests, filename):
    """Saves generated tests to file"""
    path = f"generated_tests/{filename}"
    with open(path, "w", encoding="utf-8") as f:
        f.write(tests)
    print(f"   ✅ Saved: {filename}")


# ─────────────────────────────
# MAIN — Run everything here!
# ─────────────────────────────
if __name__ == "__main__":

    print("\n🤖 AI Test Generator Starting...")
    print("=" * 50)

    # Read your functions
    with open("src/functions.py", "r") as f:
        my_code = f.read()

    print("📄 Code loaded from src/functions.py")
    print("=" * 50)

    # Generate with CLAUDE
    print("\n🟣 Generating tests with CLAUDE AI...")
    print("-" * 50)
    for style in ["basic", "detailed", "expert"]:
        print(f"\n📝 Claude — {style} tests...")
        tests = generate_with_claude(my_code, style)
        clean = clean_code(tests)
        save_tests(clean, f"test_claude_{style}.py")

    # GPT-4 comparison coming soon!
    print("\n🟢 GPT-4 comparison — Coming Soon!")
    
    print("-" * 50)

    print("\n" + "=" * 50)
    print("🎉 Done! Check generated_tests folder!")
    print("=" * 50)