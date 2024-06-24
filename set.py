# create set
s = {10,20,30,40}
print(s)

# iterate set
for i in s:
    print(i)

# add() = add element in tuple randomly
s.add(50)
print(s)

# pop() = delete any element in tuple randomly
p = s.pop()
print(p)
print(s)

# remove() = if the item to remove doesn't exist, it will show an error
s.remove(10)
print(s)
# s.remove(80)
print(s)

# discard() = if the item to remove doesn't exist, it will not show an error
s.discard(20)
print(s)
s.discard(80)
print(s)

# clear() = it returns = set()
s.clear()
print(s)

# update()
s1 = {11,22,33,44,55}
l1 = [66,77,55,11]
s1.update(l1)
print(s1)

# set() = use for convert into set
# convert list into set
l = [1,2,3,4]
s = set(l)
print(s)

# convert tuple into set
t = (11,21,31,41)
s = set(t)
print(s)