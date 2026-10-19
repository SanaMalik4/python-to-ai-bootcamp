# Sets keep unique values, so duplicates disappear.

attending_topics = {"Python", "AI", "Python", "Data"}
print("Unique topics:", attending_topics)
print("Has AI:", "AI" in attending_topics)

attending_topics.add("Machine Learning")
attending_topics.update(["Git", "Data"])
print("After adding topics:", attending_topics)

attending_topics.discard("Data")  # discard is safe if the item is missing.
print("After removing Data:", attending_topics)

python_group = {"Sana", "Ali", "Hira"}
ai_group = {"Ali", "Hira", "Usman"}
print("\nBoth groups:", python_group & ai_group)
print("Anyone in either group:", python_group | ai_group)
print("Only in Python group:", python_group - ai_group)

student_ids = [101, 102, 101, 103, 102]
unique_ids = set(student_ids)
print("\nIDs before:", student_ids)
print("Unique IDs:", unique_ids)

# An empty set is set(), because {} creates an empty dictionary.
empty_set = set()
print("Empty set:", empty_set)
