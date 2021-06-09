# PYTHON ACCESS TUPLE ITEMS:
# Tuples are unchangeable or immutable
# you cannot change tuples values
# you have to convert the tuple into a list, change the list, and convert the list back into a tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# ADD ITEMS IN TUPLE: Just like workaround for changing a changing a tuple, you can convert it onto a list add your
# items and convert it back into a tuple

tuple1 = ("horse", "panner", "spider")
addTuple2 = list(tuple1)
addTuple2.append("Orange")
tuple1 = tuple(addTuple2)
print(tuple1)
# REMOVE ITEMS:
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for
# changing and adding tuple items:

tuple2 = ("joker", "inception", "avengers", "infinity-war")
removeItem2 = list(tuple2)
removeItem2.remove("joker")
tuple2 = tuple(removeItem2)
print(tuple2)