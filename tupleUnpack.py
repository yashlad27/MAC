# UNPACKING A TUPLE:
# When we creat a tuple, we normally assign values to it. This is called "packing" tuple.

fruitsT = ("apple", "cherry", "orange")

# but in Python we are allowed to extract the values back into variables.
# this is called unpacking

(green, yellow, red) = fruitsT

print(green)
print(yellow)
print(red)

# USING ASTERISK *
# if the number of var is less than the number if values, you can add an * to the variable name and t
# the values will be assigned to the variables list:

fruitsT1 = ("apple", "orange", "horse", "dog", "rasberry", "chicken")

(fawn, violet, *magenta) = fruitsT1
print(fawn)
print(violet)
print(magenta)

# if the asterisk is added to another variable name than the last, python will assign values to the variable
# until the number of values left matches the number of variables left

(fawn, *violet, magenta) = fruitsT1
print(fawn, violet, magenta)
