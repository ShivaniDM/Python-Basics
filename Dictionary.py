# Creating a dictionary with items
my_dict = {1: "jooo", 4: "goo"}

# Accessing a value using its key
print(my_dict[4])  # Output: goo

# Attempting to access a non-existent key will raise a KeyError
# print(my_dict[2])  # Uncommenting this will raise KeyError

# Dictionary with keys and values
nums = {1: "one", 2: "two", 3: "three"}
print(len(nums))  # Output: 3
print(nums[1])    # Output: one

# Using the get method to avoid KeyError
print(nums.get(1))         # Output: one
print(nums.get(4, "default"))  # Output: default


# Adding and modifying key-value pairs
nums[8] = "eight"
print(nums)  # Output: {1: 'one', 2: 'two', 3: 'three', 8: 'eight'}

# Removing a key-value pair
del nums[1]
print(nums)  # Output: {2: 'two', 3: 'three', 8: 'eight'}

# Checking if a key exists in the dictionary
print(f"{8 in nums}")  # Output: True

# Overwriting a value
nums[8] = "oops, overwritten"
print(nums)  # Output: {2: 'two', 3: 'three', 8: 'oops, overwritten'}

# Merging dictionaries
colors = {"r": "Red", "g": "Green"}
numbers = {1: "one", 2: "two"}
colors.update(numbers)
print(colors)  # Output: {'r': 'Red', 'g': 'Green', 1: 'one', 2: 'two'}

# Updating values in a dictionary
colors = {"Green": ["Spinach"]}
colors["Green"].append("Apples")
print(colors)  # Output: {'Green': ['Spinach', 'Apples']}

# Dictionary methods
print(colors.items())   # Output: dict_items([('Green', ['Spinach', 'Apples'])])
print(colors.keys())    # Output: dict_keys(['Green'])
print(colors.values())  # Output: dict_values([['Spinach', 'Apples']])
