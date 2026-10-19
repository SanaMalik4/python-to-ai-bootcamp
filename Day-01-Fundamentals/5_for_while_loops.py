# for loops are useful when I know which values I want to visit.

print("Count from 1 to 5:")
for number in range(1, 6):
    print(number)

print("\nCount by twos:")
for number in range(0, 11, 2):
    print(number)

print("\nSkip 2 and stop before 5:")
for number in range(1, 6):
    if number == 2:
        continue
    if number == 5:
        break
    print(number)

# A while loop keeps going while its condition is true.
print("\nWhile loop:")
count = 1
while count <= 3:
    print("Count is", count)
    count += 1  # Without this update, the loop would never finish.

# Small practice: add the numbers from 1 through 5.
total = 0
for number in range(1, 6):
    total += number
print("\nSum from 1 to 5:", total)
