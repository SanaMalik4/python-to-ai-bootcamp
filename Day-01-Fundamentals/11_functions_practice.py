# Functions let me reuse a task without rewriting the same code.

def greet():
    print("Welcome to my Python practice!")

greet()
greet()


def add(first_number, second_number):
    return first_number + second_number

answer = add(10, 20)
print("\n10 + 20 =", answer)


def greet_person(name="Student"):
    print(f"Hello, {name}!")

greet_person("Sana")
greet_person()


def introduce(name, age):
    return f"My name is {name}, and I am {age} years old."

print(introduce(age=20, name="Sana"))  # Keyword arguments can be named.


def check_pass(marks):
    if marks >= 50:
        return "Pass"
    return "Fail"

print("\n75 marks:", check_pass(75))
print("35 marks:", check_pass(35))


def calculate_average(numbers):
    if not numbers:
        return 0  # Avoid dividing by zero for an empty list.
    return sum(numbers) / len(numbers)

print("\nAverage:", round(calculate_average([70, 80, 90]), 2))
print("Empty-list average:", calculate_average([]))

# print() displays something; return lets another part of the program use it.
