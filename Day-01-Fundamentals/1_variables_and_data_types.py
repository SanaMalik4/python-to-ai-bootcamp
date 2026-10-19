# I am trying different kinds of values and checking their types.

student_name = "Sana"
age = 20
gpa = 3.51
is_enrolled = True
project_result = None

print("Student:", student_name)
print("Age:", age)
print("GPA:", gpa)
print("Enrolled:", is_enrolled)
print("Project result:", project_result)

print("\nTypes:")
print(type(student_name))   # str
print(type(age))            # int
print(type(gpa))            # float
print(type(is_enrolled))    # bool
print(type(project_result)) # NoneType

# Python variables can be updated to hold a different type.
score = 10
print("\nBefore update:", score, type(score))
score = "ten"
print("After update:", score, type(score))

# Names are case-sensitive, so these are two different variables.
topic = "Python"
Topic = "AI"
print("\nLowercase topic:", topic)
print("Uppercase Topic:", Topic)
