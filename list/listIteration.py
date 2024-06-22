# create list
l = [1,2,'a','b',3.4,6.8]
print(l)

# iterate list without range
for i in l:
    print(i)

# iterate list with range
length = len(l)
print(length)
for i in range(length):
    print(l[i])

# iterate list in reverse with range
for i in range(length-1,-1,-1):
    print(l[i])

# iterate list in reverse without range
l1 = l[-1::-1]
for i in l1:
    print(i)