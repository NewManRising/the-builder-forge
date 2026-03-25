"""
Debugging practice - this script has an intentional bug.
Use the debugger to find it.
"""


def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average


def process_scores(scores):
    passing = []
    failing = []
    for score in scores:
        if score >= 70:
            passing.append(score)
        else:
            failing.append(score)
    return passing, failing


def main():
    test_scores = [85, 92, 67, 73, 55, 88, 91, 42, 78, 60]

    avg = calculate_average(test_scores)
    print(f"Class average: {avg}")

    passing, failing = process_scores(test_scores)
    print(f"Passing: {len(passing)} students")
    print(f"Failing: {len(failing)} students")

    empty_scores = []
    empty_avg = calculate_average(empty_scores)
    print(f"Empty average: {empty_avg}")


if __name__ == "__main__":
    main()
