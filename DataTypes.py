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
