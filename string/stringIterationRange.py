str = "Welcome To Python "
print(str)

# len() function is used to find out the length of string
l = len(str)
print("length of '",str,"' =",l)

# string iterate with range 
for i in range(l):
    print(str[i])

# reverse string iterate with range 
str1 = str[-1::-1]
for i in range(l):
    print(str1[i])

# reverse string iterate another way
for i in range(l-1,-1,-1):
    print(str[i])