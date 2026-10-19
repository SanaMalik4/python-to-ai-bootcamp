# Change the marks to see a different grade.

marks = 78

if marks < 0 or marks > 100:
    print("Marks should be between 0 and 100.")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Needs improvement")

# A second example combines conditions.
attendance = 85
has_submitted_work = True

if attendance >= 75 and has_submitted_work:
    print("Eligible for the lab evaluation.")
else:
    print("Check the attendance or submission requirement.")

# Try marks values such as 90, 55, 0, 100, and 120.
