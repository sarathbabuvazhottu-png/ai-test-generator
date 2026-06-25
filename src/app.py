from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic
import os
import subprocess
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)


def build_prompt(code, style):
    if style == "basic":
        return f"""
        Write pytest unit tests for
        this Python code:
        {code}
        Return only complete working code.
        """
    elif style == "detailed":
        return f"""
        Write comprehensive pytest
        unit tests for this code:
        {code}
        Include normal, edge case
        and error handling tests.
        Return only complete working code.
        """
    elif style == "expert":
        return f"""
        You are a senior developer.
        Write ALL possible pytest tests
        for this Python code:
        {code}
        Return only complete working code.
        """


@app.route("/")
def index():
    return jsonify({
        "status": "running",
        "message": "AI Test Generator API Ready!"
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "running",
        "message": "AI Test Generator API Ready!"
    })


@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        code = data.get("code", "")
        style = data.get("style", "basic")

        if not code:
            return jsonify({
                "error": "No code provided!"
            }), 400

        prompt = build_prompt(code, style)

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        tests = response.content[0].text
        tests = tests.replace("```python", "")
        tests = tests.replace("```", "")
        tests = tests.strip()

        return jsonify({
            "success": True,
            "tests": tests,
            "style": style
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/run-tests", methods=["POST"])
def run_tests():
    try:
        data = request.json
        tests = data.get("tests", "")
        style = data.get("style", "basic")

        os.makedirs("generated_tests", exist_ok=True)
        test_file = f"generated_tests/test_web_{style}.py"

        with open(test_file, "w", encoding="utf-8") as f:
            f.write(tests)

        result = subprocess.run(
            [
                "python", "-m", "pytest",
                test_file,
                "--tb=short",
                "-v",
                "--no-header"
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout
        passed = 0
        failed = 0

        for line in output.split("\n"):
            if " PASSED" in line:
                passed += 1
            elif " FAILED" in line:
                failed += 1

        total = passed + failed
        pass_rate = str(round(
            (passed / total * 100)
            if total > 0 else 0, 1
        )) + "%"

        return jsonify({
            "success": True,
            "results": {
                "total": total,
                "passed": passed,
                "failed": failed,
                "pass_rate": pass_rate,
                "coverage": "N/A",
                "output": output[-2000:]
            }
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n🚀 Flask Starting on port {port}...")
    app.run(debug=False, host="0.0.0.0", port=port)