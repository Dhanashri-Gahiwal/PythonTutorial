# convert string into list using split function
str1 = "Welcome to Python Programming"
l = str1.split()
print(l)

# take string input from user and convert it into list
list1 = []
for i in range(1,4):
    st = input("Enter string:"+str(i)+":")
    list1.append(st)
print(list1)
