import subprocess
import json
import csv
import os
from datetime import datetime

def run_tests_for_style(style):
    """
    Runs pytest for one test file
    and returns the results!
    """
    print(f"   Running {style} tests...")

    test_file = f"generated_tests/test_{style}.py"

    # Run pytest and capture results
    result = subprocess.run(
        [
            "python", "-m", "pytest",
            test_file,
            "--tb=no",
            "-q",
            f"--cov=src/functions",
            "--cov-report=json",
            "--no-header"
        ],
        capture_output=True,
        text=True
    )

    # Get the output text
    output = result.stdout

    # Count passed and failed
    passed = 0
    failed = 0

    for line in output.split("\n"):
        if "passed" in line:
            # Extract number before "passed"
            parts = line.split()
            for i, word in enumerate(parts):
                if word == "passed":
                    passed = int(parts[i-1])
                if word == "failed":
                    failed = int(parts[i-1])

    # Get coverage percentage
    coverage = 0
    try:
        with open("coverage.json", "r") as f:
            cov_data = json.load(f)
            coverage = round(
                cov_data["totals"]["percent_covered"], 1
            )
    except:
        coverage = 0

    return {
        "style": style,
        "passed": passed,
        "failed": failed,
        "total": passed + failed,
        "pass_rate": f"{round((passed/(passed+failed)*100) if (passed+failed) > 0 else 0, 1)}%",
        "coverage": f"{coverage}%"
    }


def print_results_table(results):
    """
    Prints a nice results table
    in the terminal!
    """
    print("\n")
    print("=" * 60)
    print("   AI TEST GENERATOR — RESULTS TABLE")
    print("=" * 60)
    print(f"{'Style':<12} {'Passed':<10} {'Failed':<10} {'Pass Rate':<12} {'Coverage'}")
    print("-" * 60)

    for r in results:
        print(
            f"{r['style']:<12} "
            f"{r['passed']:<10} "
            f"{r['failed']:<10} "
            f"{r['pass_rate']:<12} "
            f"{r['coverage']}"
        )

    print("=" * 60)

    # Total summary
    total_passed = sum(r["passed"] for r in results)
    total_failed = sum(r["failed"] for r in results)
    total_tests  = sum(r["total"]  for r in results)

    print(f"\n📊 TOTAL TESTS:   {total_tests}")
    print(f"✅ TOTAL PASSED:  {total_passed}")
    print(f"❌ TOTAL FAILED:  {total_failed}")
    print(f"🎯 OVERALL RATE:  {round(total_passed/total_tests*100, 1)}%")
    print("=" * 60)


def save_results_to_csv(results):
    """
    Saves results to a CSV file
    So you can open in Excel!
    """
    # Create results folder if needed
    os.makedirs("results", exist_ok=True)

    # Create filename with today's date
    today = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"results/results_{today}.csv"

    # Write to CSV file
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "style", "passed", "failed",
            "total", "pass_rate", "coverage"
        ])
        writer.writeheader()
        writer.writerows(results)

    print(f"\n💾 Results saved to: {filename}")
    print(f"   Open in Excel to see the data!")
    return filename


# ─────────────────────────────
# MAIN — Run everything here!
# ─────────────────────────────
if __name__ == "__main__":

    print("\n📊 AI Test Evaluator Starting...")
    print("=" * 60)
    print("Measuring results for all 3 prompt styles...")
    print("=" * 60)

    # Run tests for all 3 styles
    all_results = []

    for style in ["basic", "detailed", "expert"]:
        result = run_tests_for_style(style)
        all_results.append(result)

    # Print the results table
    print_results_table(all_results)

    # Save to CSV file
    save_results_to_csv(all_results)

    print("\n🎉 Evaluation Complete!")
    print("=" * 60)