#welcome to my humble code
# -------------------------------
# Section 1: Greeting Messages
# -------------------------------

greetings = ["Hello", "Bonjour", "Hola"]

for greeting in greetings:
    print(f"{greeting}, World!")

# -------------------------------
# Section 2: Abuse Messages
# -------------------------------

abuse = ["Boooo", "Mooooo", "Duck", "NOOOO"]

for swear in abuse:
    print(f"\n\n  {swear}, You!!!!!!")

# -------------------------------
# Section 3: Type Conversion
# -------------------------------

num = 42
y = type(num)

print(f"        {num}  {y} {float(num)}   {type(float(num))}")

# -------------------------------
# Section 4: String Handling
# -------------------------------

name = "Chatrapati"
x = type(name)

print(f"  {name}  {x}")

for char in name:
    print(f"\n   {char}   {type(char)}")

# Iterate with index and value
for index, value in enumerate(name):
    print(f"Index: {index}, Value: {value}")

# -------------------------------
# Section 5: Decimal Type Usage
# -------------------------------

from decimal import Decimal 

roll_no = 23000
z = Decimal(roll_no / 33.3)

print(f"  \n {z}  {type(z)}")
print(f" {float(z)}  {type(float(z))}")
print(f" {int(z)}   {type(int(z))}")

# -------------------------------
# Section 6: Math Module Examples
# -------------------------------

import math

print("\n \n    \n         math.floor(-23.11) : ", math.floor(-23.11))
print("math.floor(300.16) : ", math.floor(300.16))
print("math.floor(300.72) : ", math.floor(300.72))

print("math.ceil(300.72) :", math.ceil(300.72))  # Corrected from math.ceiling

print("round(-23.11) : ", round(-23.11))
print("round(300.16) : ", round(300.16))
print("round(300.72) :", round(300.72))

# -------------------------------
# Section 7: String Stripping
# -------------------------------

my_string = "   Hello World!   "
print(f"\n            >{my_string.lstrip()}<")
print(f"?{my_string.strip()}?")

my_string = "Hello World!,,,"
print(my_string.strip(","))

# -------------------------------
# Section 8: Replacing Substrings
# -------------------------------

my_string1 = "   Hello World!   "
name1 = "looooe"
greet = my_string1.replace("World", name1)
print(greet)

# -------------------------------
# Section 9: Interactive Username Replacement
# -------------------------------

for i in range(2):
    username = input('Greetings user, please enter your username: ')
    my_string2 = "   Hello World!   "
    greet = my_string2.replace("World", username)
    print(greet)


# -------------------------------
# Section 10: String Formatting
# -------------------------------

# Define variables
name2 = "Nina"
userno = 1001

# Old-style string formatting using % operator
print("\n   Hello, my name is %s" % name2)

# New-style string formatting using str.format()
print("Hello, my name is {name}".format(name=name2))

# Using str.format() with named placeholders
print("Hello, my user number is {userno}".format(userno=userno))

# Combining multiple placeholders in str.format()
print("Get out!! {userno} {name}".format(userno=userno, name=name2))



# -------------------------------
# Section 11: List Operations and Methods
# -------------------------------

# Empty list examples
print(list())
print([])
print(type(list()))
print(type([]))

# List string manipulation
names = ["Nina", "Max", "Jane"]
names2 = ["You", "Live", "Once"]
print(len(names))

for i in range(len(names)):
    print("before change")
    print(f" {names[i]} index is: {i}")
    names[i] = names2[i]
    print("after change:")
    print(f" {names[i]} index is: {i}")

# Sorting and modifying lists
lottery_numbers = [1, 4, 32423, 2, 45, 11]
print(sorted(lottery_numbers, reverse=True))  # Sorted in descending order

names2 = ["You", "Live", "Once"]
print(sorted(names2, reverse=True))  # Sorted in descending order

lottery_numbers1 = [5, 1, 8, 3]
lottery_numbers1.sort()  # Sorts the list in place
print(lottery_numbers1)  # Prints the sorted list

# List modification
names2.insert(3, "Mike")
print(names2)

names2.append("doooo")
print(names2)

lottery_numbers1.extend(lottery_numbers)
print(lottery_numbers1)

# Membership testing and list methods
ans = "You" in names2
print(ans)

ans2 = 3 in lottery_numbers1
print(ans2)

print(names2.count("Nina"))  # Count occurrences of "Nina"

print(names2.index("Mike"))  # Find index of "Mike"
names2.remove("Mike")  # Remove the first occurrence of "Mike"
print(names2)

names2.pop()  # Remove and return the last item
print(names2)
