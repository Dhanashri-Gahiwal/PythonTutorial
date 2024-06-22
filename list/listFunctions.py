# delete element from list
# del = returns only list. it takes index number
l1 = [1,5,3,7,9]
print(l1)
del l1[2]
print(l1)

# pop() = returns deleted element and also returns list. it takes index number
l2 = [1,5,3,8,9]
print(l2)
p = l2.pop(1)
print(p)
print(l2)

# remove() = returns only list. it takes value
l3 = [20,50,30,80,90]
print(l3)
l3.remove(80)
print(l3)

# clear() = returns empty list
l4 = [1,20,31,42,90,6]
print(l4)
l4.clear()
print(l4)

# -----------------------------------------------------------------------------------
# update list element
l5 = [10,20,31,42,90,6]
print(l5)
l5[0] = 44
print(l5)

# -----------------------------------------------------------------------------------
# add element in existing list
# insert() = you can add element in any index number. it takes 2 arguments 1st arg is index number 2nd arg is value
list1 = ["anu","sonu"]
print(list1)

# it add in first index number
list1.insert(1,"monu")
print(list1)

# if you give out of index number, it will add in last position
list1.insert(10,"teju")
print(list1)

# append() = elements always added in last position.It takes only one argument, this arg is value. you can add other list in existing list.
list2 = ["om","sai"]
print(list2)
list2.append("ram")
print(list2)

z = ["krish","shree"]
list2.append(z)
print(list2)

# extend() = It takes only one argument, this arg is list. you can add other list in existing list. list extends always in last position.
list3 = ["divisha","aarav"]
print(list3)
y = ["vedika","vedant"]
list3.extend(y)
print(list3)

# -----------------------------------------------------------------------------------
newList = [10,50,90,10,45,23,10]
print(newList)
newList1 = ["python","c","java","php","c","cpp"]
print(newList1)

# sort() = sorting elements in ascendind order
newList.sort()
print(newList)
newList1.sort()
print(newList1)

# reverse() = reverse list
newList.reverse()
print(newList)
newList1.reverse()
print(newList1)

# max() = get max element in given list
n3 = max(newList)
print(n3)
m3 = max(newList1)
print(m3)

# min() = get min element in given list
n4 = min(newList)
print(n4)
m4 = min(newList1)
print(m4)

# count() = it counts the specific elements how many times comes in list
n5 = newList.count(10)
print(n5)
m5 = newList1.count("c")
print(m5)

# index() = it takes one argument as a value and returns index number
n6 = newList.index(45)
print(n6)
m6 = newList1.index("php")
print(m6)