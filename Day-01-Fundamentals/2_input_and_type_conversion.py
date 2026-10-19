# input() gives me text, so I convert number input before doing maths.

name = input("What is your name? ").strip().title()

try:
    age = int(input("How old are you? "))
    height = float(input("Enter your height in metres (e.g. 1.65): "))

    print(f"\nHi, {name}!")
    print(f"Next year you will be {age + 1}.")
    print(f"Your height is {height} metres.")

    # A value can be converted to text for joining with other text.
    age_as_text = str(age)
    print("Your age as text is", age_as_text, "and its type is", type(age_as_text))
except ValueError:
    print("Please enter a whole number for age and a valid decimal for height.")

print("\nConversion examples:")
print(int("20"), type(int("20")))
print(float("3.5"), type(float("3.5")))
print(str(20), type(str(20)))

# Try entering 'abc' for age to test the error-handling path.