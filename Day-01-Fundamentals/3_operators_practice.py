# I am testing the operators with small numbers so the results are easy to check.

a = 10
b = 3

print("Arithmetic")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)       # Regular division gives a float.
print("a // b =", a // b)     # Floor division.
print("a % b =", a % b)       # Remainder.
print("a ** b =", a ** b)     # Power.

print("\nComparison")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= 10:", a >= 10)
print("b <= 2:", b <= 2)

print("\nLogical")
print("a > 5 and b < 5:", a > 5 and b < 5)
print("a < 5 or b == 3:", a < 5 or b == 3)
print("not (a == 10):", not (a == 10))

print("\nMembership")
languages = ["Python", "Java", "C++"]
print("'Python' in languages:", "Python" in languages)
print("'Ruby' not in languages:", "Ruby" not in languages)

print("\nAssignment operators")
counter = 5
counter += 2
print("After += 2:", counter)
counter -= 1
print("After -= 1:", counter)
counter *= 3
print("After *= 3:", counter)

print("\nIdentity")
nothing = None
print("nothing is None:", nothing is None)
print("nothing is not None:", nothing is not None)

# '==' checks whether values are equal; 'is' checks whether they are the same object.
first_list = [1, 2]
second_list = [1, 2]
same_list = first_list
print("first_list == second_list:", first_list == second_list)
print("first_list is second_list:", first_list is second_list)
print("first_list is same_list:", first_list is same_list)
