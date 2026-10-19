# A dictionary connects each key with a value.

student = {
    "name": "Sana",
    "age": 20,
    "gpa": 3.45,
    "is_enrolled": True
}

print("Student name:", student["name"])
print("GPA:", student.get("gpa"))
print("Missing city safely:", student.get("city"))

student["city"] = "Wah Cantt"  # Add a new key-value pair.
student["age"] = 21            # Update an existing value.
student.update({"gpa": 3.6, "course": "Python to AI Bootcamp"})

print("\nAll student details:")
for key, value in student.items():
    print(key, ":", value)

print("\nKeys:", list(student.keys()))
print("Values:", list(student.values()))
print("Number of fields:", len(student))

# Use get() when a key may not exist; direct indexing would raise KeyError.
print("City:", student.get("city", "Not provided"))

# A simple dictionary can also count repeated items.
topics = ["Python", "AI", "Python", "Loops", "AI", "Python"]
topic_counts = {}
for topic in topics:
    topic_counts[topic] = topic_counts.get(topic, 0) + 1
print("\nTopic counts:", topic_counts)
