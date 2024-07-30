---

### Working with Sets in Python

#### Basic Set Information
'''
A set is a mutable datatype that allows you to store only immutable types in an unsorted manner. 
Sets are mutable but do not support indexing or sorting due to their unordered nature.

'''
# Initializing an empty dictionary and checking its type
my_dic = {}
print(type(my_dic))  # Output: <class 'dict'>

# Initializing an empty tuple and checking its type
my_set = ()
print(type(my_set))  # Output: <class 'tuple'>

# Correct way to initialize an empty set
my_set = set()
print(type(my_set))  # Output: <class 'set'>

# Checking the type of an empty list
my_list = []
print(type(my_list))  # Output: <class 'list'>
```

#### Creating and Using Sets

```python
# Initializing a set with duplicate values (duplicates are removed)
num = {3, 4, 4, 22, 4}
print(num)  # Output: {3, 4, 22}

# Example of an invalid set (sets cannot contain lists)
# Uncomment the following line to see the error
# narcosis = {[3, 4, 5, 4], [4.5]}  # TypeError: unhashable type: 'list'

# Initializing and displaying sets
num = {2, 5, 6}
print(num)  # Output: {2, 5, 6}

# De-duplicating a list using a set
names = ['Nina', 'Max', 'Nina']
print(set(names))  # Output: {'Nina', 'Max'}

# Working with sets
my_set = {1, "a", 2, "b", 3, "cat"}
print(my_set)  # Output: {1, 2, 3, 'a', 'b', 'cat'}

my_set = {1, 3, "a", 2, "b", "cat"}
print(my_set)  # Output: {1, 2, 3, 'a', 'b', 'cat'}
```

#### Set Operations

```python
# Union of two sets
res1 = my_set.union(num)
res3 = my_set | num
print(f"{res1} this is union result")  # Output: {1, 2, 3, 'a', 'b', 'cat', 5, 6}
print(f"{res3} this is union result")  # Output: {1, 2, 3, 'a', 'b', 'cat', 5, 6}

# Intersection of two sets
res2 = my_set.intersection(num)
res4 = my_set & num
print(f"{res2} this is intersection result")  # Output: {1, 2, 3}
print(f"{res4} this is intersection result")  # Output: {1, 2, 3}
```

#### Sorting and Modifying Sets

```python
# Sorting a set by converting it to a list
my_set = {"a", "b", "cat", "dog", "red"}
print(sorted(my_set))  # Output: ['a', 'b', 'cat', 'dog', 'red']

# Adding and removing items from a set
colors = {"Red", "Green", "Blue"}
colors.add("Orange")
print(colors)  # Output: {'Red', 'Green', 'Blue', 'Orange'}

colors.discard("Red")
print(colors)  # Output: {'Green', 'Blue', 'Orange'}

# Adding multiple items to a set
colors = {"Red", "Green"}
numbers = {1, 3, 5}
colors.update(numbers)
print(colors)  # Output: {1, 3, 5, 'Green', 'Red'}

# Adding items from a string (iterates over each character)
hello = "Hello"
colors.update(hello)
print(colors)  # Output: {1, 3, 5, 'Green', 'Red', 'H', 'e', 'l', 'o'}
```

---
