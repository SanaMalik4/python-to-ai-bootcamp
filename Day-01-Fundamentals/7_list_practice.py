# A list is ordered and changeable, and it can contain duplicate values.

skills = ["Python", "SQL", "AI", "Python"]
print("Starting skills:", skills)
print("First skill:", skills[0])
print("Last skill:", skills[-1])
print("Number of items:", len(skills))
print("Contains SQL:", "SQL" in skills)

skills[1] = "Pandas"
skills.append("Machine Learning")
skills.extend(["Git", "NumPy"])
skills.insert(1, "HTML")
print("\nAfter adding and updating:", skills)

skills.remove("AI")
removed_skill = skills.pop()  # Removes and returns the last item.
print("After removing AI and popping last item:", skills)
print("Popped item:", removed_skill)

numbers = [8, 3, 10, 1, 3]
print("\nNumbers:", numbers)
print("Sorted copy:", sorted(numbers))
print("Original is still:", numbers)
numbers.sort()
print("After numbers.sort():", numbers)
print("How many 3s:", numbers.count(3))
print("Index of 8:", numbers.index(8))

# Try adding another skill and see how the list changes.
