# Strings are text sequences; indexes start at zero.

message = "Python to AI"
print("Original:", message)
print("First character:", message[0])
print("Last character:", message[-1])
print("First six characters:", message[0:6])
print("From index 7 onward:", message[7:])
print("Every second character:", message[::2])
print("Length:", len(message))
print("'AI' is in message:", "AI" in message)

print("\nString methods")
messy_name = "  sana malik  "
print("strip:", messy_name.strip())
print("title:", messy_name.strip().title())
print("upper:", message.upper())
print("lower:", message.lower())
print("replace:", message.replace("AI", "Machine Learning"))
print("split:", "Python,SQL,AI".split(","))
print("join:", " - ".join(["Python", "SQL", "AI"]))
print("startswith:", message.startswith("Python"))
print("endswith:", message.endswith("AI"))
print("isalpha:", "Python".isalpha())
print("isdigit:", "123".isdigit())

# String methods return a new string; the original stays the same.
print("\nOriginal name is still:", repr(messy_name))

# Strings are immutable. This would raise an error if uncommented:
# message[0] = "J"
