# create empty list then append elements in list using for loop with range
l = []
for i in range(1,50):
    l.append(i)
print(l)

# create empty list then append even numbers in list using for loop with range
l1 = []
for i in range(2,50,2):
    l1.append(i)
print(l1)

# create empty list then append elements in list using list comprehension
x = [a for a in range(1,20)]
print(x)

# create empty list then append even numbers in list using list comprehension
y = [b for b in range(1,20) if b%2 == 0]
print(y)