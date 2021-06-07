# PYTHON - ADD LIST ITEMS:
# Append Items:
# to add an item to the end of the list we use append() method:
fruits = ['apple', 'grapes', 'cherry', 'litchi', 'tomato']
fruits.append('orange')
print(fruits)

# Extend List:
# to append elements from another list to the current list use the extend() method:
thisList = ['horse', 'cat', 'dogs']
morePets = ['turtle', 'goldfish', 'rabbit']
thisList.extend(morePets)
print(thisList)

# Add any Iterable :
thisTuple = ('kiwi', 'snake')
thisList.extend(thisTuple)
