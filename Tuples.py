### Tuples and Immutability in Python

#### Hashability and Immutability
'''
In Python, hashable objects must be immutable because their hash value needs to remain constant throughout their lifetime. This is essential for two main reasons:

1. **Consistency**: Immutability ensures that the hash value of an object remains unchanged, allowing for reliable data retrieval in dictionaries and sets.
2. **Efficiency**:  Immutable objects allow hash tables to operate efficiently by avoiding the need for constant rehashing and checking, 
                    thus maintaining fast data access and management.
'''


#### Working with Tuples

print("\n \n")

# Creating and displaying tuples
a = ()
print(len(a))  # Output: 0

a = (1, 2, 3, 3)
print(a)  # Output: (1, 2, 3, 3)

# Single element tuple
b = (2)
print(b)  # Output: 2
print(type(b))  # Output: <class 'int'>

# Correct way to create a single element tuple
b = (3,)
print(b)  # Output: (3,)
print(type(b))  # Output: <class 'tuple'>

# Tuple with mixed data types
student = ("Marcy", 8, "History", 3.5)
print(student)  # Output: ('Marcy', 8, 'History', 3.5)

# Enumerating items in a tuple
for index, item in enumerate(student):
    print(f"{type(student)} is the type of storage and the item {item} and its index {index}. Item type: {type(item)}")
    print(student[index])
    # Uncomment the following line to see the error
    # student[index] = "nooo"

# Unpacking a tuple
student = ("Marcy", 8, "History")
name, age, subject = student
print(name, age, subject)

```

#### Returning Multiple Values

```python
# A function can return multiple values, which are automatically packed into a tuple.
def fun_begins():
    return "aaa", 4

scream, pitch = fun_begins()

print(scream)  # Output: aaa
print(pitch)   # Output: 4
```

---

