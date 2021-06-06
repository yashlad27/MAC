# BOOLEAN VALUES:
# Represents one of two values : True or False

# Evaluate:
print(10 > 9)
print(10 == 9)
print(10 <= 9)

# when you run a condition in an if statement:

a = 200
b = 44

if b > a:
    print("b is greater than a: F")
else:
    print("a is greater than b: T")

# Evaluate Values and variables:
# the bool() func allows to evaluate any value, and give a true or false value:
# evaluate a string and an int:
print(bool("Hello"))
print(bool(13))

x = "Hello"
y = 18

print(bool(x))
print(bool(y))

# note: 1. any string is true, except EMPTY strings.
# 2. any number is True except zero.
# 3. Any list, tuple, set and dictionary are True, Except EMPTY ones.

def myFunction():
    return True
print(myFunction())