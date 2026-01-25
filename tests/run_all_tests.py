#!/usr/bin/env python3
"""
Master Test Runner for Personal AI Employee
Runs all Bronze and Silver Tier tests and reports results.
"""

import subprocess
import sys
import os

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def run_command(cmd):
    """Run a command and return its result."""
    try:
        result = subprocess.run(cmd, shell=False, capture_output=True, text=True, encoding='utf-8', errors='replace')
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)


def run_bronze_tests():
    """Run Bronze Tier tests."""
    print("Running Bronze Tier tests...")
    cmd = [sys.executable, "tests/bronze_tier_test.py"]
    returncode, stdout, stderr = run_command(cmd)

    print(stdout)
    if stderr:
        print("STDERR:", stderr)

    # Parse results
    if "Bronze Tier: " in stdout:
        parts = stdout.split("Bronze Tier: ")[1].split(" ")[0].split("/")
        if len(parts) == 2:
            passed, total = int(parts[0]), int(parts[1])
            return passed, total
    return 0, 7  # Default to 0/7 if parsing fails


def run_silver_tests():
    """Run Silver Tier tests."""
    print("\nRunning Silver Tier tests...")
    cmd = [sys.executable, "tests/silver_tier_test.py"]
    returncode, stdout, stderr = run_command(cmd)

    print(stdout)
    if stderr:
        print("STDERR:", stderr)

    # Parse results
    if "Silver Tier: " in stdout:
        parts = stdout.split("Silver Tier: ")[1].split(" ")[0].split("/")
        if len(parts) == 2:
            passed, total = int(parts[0]), int(parts[1])
            return passed, total
    return 0, 8  # Default to 0/8 if parsing fails


def main():
    """Run all tests and report results."""
    print("=== RUNNING COMPLETE TEST SUITE ===\n")

    print("=== BRONZE TIER TESTS ===")
    bronze_passed, bronze_total = run_bronze_tests()

    print("\n=== SILVER TIER TESTS ===")
    silver_passed, silver_total = run_silver_tests()

    # Calculate totals
    total_passed = bronze_passed + silver_passed
    total_tests = bronze_total + silver_total

    print("\n=== OVERALL RESULT ===")
    print(f"Bronze Tier: {bronze_passed}/{bronze_total} PASSED {'PASSED' if bronze_passed == bronze_total else 'FAILED'}")
    print(f"Silver Tier: {silver_passed}/{silver_total} PASSED {'PASSED' if silver_passed == silver_total else 'FAILED'}")
    print(f"Total: {total_passed}/{total_tests} PASSED {'PASSED' if total_passed == total_tests else 'FAILED'}")

    if total_passed == total_tests:
        print("\nSYSTEM FULLY FUNCTIONAL - READY FOR PRODUCTION!")
        return 0
    else:
        print(f"\n{total_tests - total_passed} TESTS FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(main())