# create tuple
t = (10,20,10,40,60,10)
print(t)

# iterate tuple
for i in t:
    print(i)

# iterate tuple using range
l = len(t)
for i in range(l):
    print(t[i])

# count()
print(t.count(10))

# max()
print(max(t))

# min()
print(min(t))

# sum()
# sum(t) = 10+20+10+40+60+10 = 150
print(sum(t))

# sum(t,10) = sum(t) + 10 = 150+10 = 160
print(sum(t,10))

# index()
print(t.index(40))

# accessing tuple element
print(t[4]) 

