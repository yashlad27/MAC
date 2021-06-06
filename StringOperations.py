# 1.slicing : Specify the start index and the end index, seperated by a colon, to return a part of the string.
b = "hello World"
print(b[2:5])
# note: first character has index 0

# slice from start: by leaving out the start index, the range will start at the first char
x = "Yash Lad"
print(x[:6])

# slice to the end: by leaving out the end index, the range will go to end:
o = "ChhayaLad"
print(o[4:])


# NEGATIVE INDEXING: start from the end of the string
g = "Hello World"
print(g[-4:-1])

# 2. Modify strings:

# a) Upper case :
a = "yash lad"
print(a.upper())

# b) Lower case:
p = "YASH LAD"
print(p.lower())

# c) Remove whitespace:
# strip() method remvoes any whitespace from the beginning or the end
m = "  Yash  lad  "
print(m.strip())

# d) Replace string:
# the replace() method replaces a string with another string.
s = "Icy Igloo goes rounf and round"
print(s.replace("f", "d"))

# Split string:
# split() splits the string into substrings if it finds instances of the seperator:
k = "hello, world"
print(k.split(","))
print((k.split("r")))

# 3. STRING CONCATENATION:
# to concatenate, or combine two strings you use the + operator
r = "hello"
q = "guest"
# l = r + q
print(r+q)

# to add space between a sentence:
print(r + " " + q)

# 4. FORMAT STRINGS:
# the format() method takes the passed arguments, formats them and places them in string where the placeholders {} are:

age = 666
txt = "My name is Yash and my age is {}"
print(txt.format(age))
# the format() method takes unlimited amount of arguments, and are placed into the respective placeholders:

quantity = 9
itemno = 555
priceNo = 59.420
myOrder = "I want {} of these many pieces of {} for {} dollars"

print(myOrder.format(quantity, itemno, priceNo))

