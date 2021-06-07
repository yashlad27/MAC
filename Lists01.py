# PYTHON LISTS:
# lists are used to store multiple items in a single variable.
# list are one of the 4 built-in data types
# the other three are Tuple, Set and dictionary

thisList = ["apple", "banana", "cherry"]
print(thisList)

# List Items: items are ordered, changeable and allow duplicate values.
# list items are indexed, the first item has index [0], the second item has index [1] etc.

# length of a list can be easily calculated using the len() function:
print(len(thisList))

# List items: can include all types of python data types.
L1 = ['apple', 'orange', 'watermelon']  # list made of strings.
L2 = [1, 6, 9, 20, 44]  # list made up of integers.
L3 = [True, False, True]  # list made up of booleans.

# list can also contain different data types:
L4 = ['apple', True, 55, 'male', False, 22.3]

# type() function is used to define objects with the data type 'list':
print(type(thisList))
print(type(L1))

# List : a collection which is ordered and changeable. allows duplicate members.
# Tuple : is a collection which is ordered and unchangeable. allows duplicate members.
# Set : is a collection which is unordered and not indexed. No duplicate members.
# Dictionary : is a collection which is ordered and changeable. no duplicate members.