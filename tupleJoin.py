# Join two Tuple:
# to join two tuples you can use + operator (or more tuples)

tuple1 = ("ab", "bc", "cd")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples:

fruits = ("rasberry", "blueberry", "blackberry")
mytuple = fruits * 2
print(mytuple)

# TUPLE METHODS :
# Python has 2 inbuilt methods that you can use on tuples:
# 1. count()
tuple4 = (1, 1, 33, 3, 7, 9, 10, 11, 1, 4, 4, 7, 1, 1)
x = tuple4.count(1)
print(x)

# 2. Index()
tuple5 = (1, 3, 4, 3, 2, 1, 8, 9, 1, 1, 3)
y = tuple5.index(1)
print(y)
