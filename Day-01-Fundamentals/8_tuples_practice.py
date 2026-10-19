# A tuple is ordered like a list, but its items cannot be reassigned.

coordinates = (10, 20)
print("Coordinates:", coordinates)
print("X coordinate:", coordinates[0])
print("Tuple length:", len(coordinates))

point = (4, 7)
x, y = point  # Tuple unpacking puts each value into a variable.
print("Unpacked x:", x)
print("Unpacked y:", y)

repeated_values = (1, 2, 1, 3, 1)
print("How many ones:", repeated_values.count(1))
print("Index of 2:", repeated_values.index(2))

# A tuple can contain a list; that inner list can still be changed.
mixed_tuple = ("Python", ["beginner", "practice"])
mixed_tuple[1].append("projects")
print("Tuple with updated inner list:", mixed_tuple)

# This would fail because tuple positions cannot be reassigned:
# coordinates[0] = 99
