# convert string into list without list comprehension
str = "Programming"
l = []
for i in str:
    l.append(i)
print(l)

# convert string into list with list comprehension
str1 = "Language"
l1 = [m for m in str1]
print(l1)