# TUPLE: it is a collection which is ordered and unchangeable
# tuples are written with round brackets

thisTuple = ("apple", "banana", "cherry")
print(thisTuple)

# 1. tuple items are ordered, unchangeable, and allow duplicate values
# first item has index [0] and the second item has index [1]

# 2. tuples have a defined order and that order cannot be changed

# 3. tuples are unchangeable, we cannot add or remove items after the tuple has been created

# 4. Allow Duplicates:
# tuples are indexed, they can have items with the same value
Tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(Tuple1)

# Tuple Length:
Tuple2 = ('horse', 'dog', 'rabbit')
print(len(Tuple2))

# Create a Tuple with one item:
# You have to add a comma after the item, otherwise python will not recognise it as a tuple
Tuple3 = ('apple',)
print(type(Tuple3))

# Tuple Items - Data Types:
T1 = ('apple', 'banana', 'cherry')  # tuple made of strings
T2 = (1, 3, 5, 9, 2, 3)  # tuple made of integers
T3 = (True, False)  # tuple made of booleans
MixedTuple = ('mango', True, 123, False, 4.55)

# Tuple type() :
mytuple = ('apple', 'uganda', 'Strawberry')
print(type(mytuple))