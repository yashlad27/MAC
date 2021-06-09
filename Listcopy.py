# COPY LISTS:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# JOIN LISTS:
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list3 = list2 + list1

print(list3)

# another way is to append all the items of list1 into list2, one by one:

for x in list1:
    list2.append(x)

print(list1)