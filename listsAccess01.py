# PYTHON - ACCESS LIST ITEMS:
# first item of list has index zero:
# List items are indexed and you can access them by referring to the index number:
L1 = ['apple', 'horse', 'whale']
print(L1[1])

# Negative indexing:
# negative meaning starts from the end:
# -1 refers to the last item, -2 refers to the second last item
L2 = [1, 6, 44, 'horse', 'chicken', True]
print(L2[-4])
print(L2[-1])

# Range of indexes:
# You can specify a range of indexed by specifying where to start and where to end the range.
# when specifying a range, the return value will be a new list with the specified items.
L3 = [3, 'camel', 'dog', False, 33.44, 'Yellow']
print(L3[-5:-3])
print(L3[2:4])

# check if item exists:
L4 = ['open', True, 77.9, 'red', False]
if 'open' in L4:
    print("Yes, the word open is in L4")