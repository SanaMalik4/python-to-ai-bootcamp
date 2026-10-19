# This mini-project combines lists, loops, conditions, and functions.

def analyze_marks(marks):
    if not marks:
        print("No marks were provided yet.")
        return None

    if any(mark < 0 or mark > 100 for mark in marks):
        print("Please use marks between 0 and 100.")
        return None

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"

    print("\nStudent Marks Report")
    print("--------------------")
    print("Marks:", marks)
    print("Number of subjects:", len(marks))
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Highest mark:", highest)
    print("Lowest mark:", lowest)
    print("Result:", result)

    return {
        "total": total,
        "average": round(average, 2),
        "highest": highest,
        "lowest": lowest,
        "result": result
    }


# Start with these sample marks, then try your own values.
student_marks = [78, 85, 42, 67, 90]
report = analyze_marks(student_marks)

print("\nReturned report dictionary:", report)

# Extra practice: uncomment these one at a time to test edge cases.
# analyze_marks([])
# analyze_marks([40, 45, 38])
# analyze_marks([100, 0, 75])
# analyze_marks([80, 105, 70])  # Invalid mark should be caught.
