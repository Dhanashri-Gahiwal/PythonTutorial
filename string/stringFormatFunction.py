# empty placeholder
str1 = "Welcome to {}".format("Python")
print(str1)

# named indexes
str2 = "Welcome to {course}".format(course = "Java")
print(str2)

# number indexes
str3 = "Welcome to {1} {0}".format("language","Java")
print(str3)

# size(length of string)
# {:20} = indicates the size of character. by default it takes the space in right side
str4 = "{:20}".format("Python")
print(str4)

# {a:>20} = it takes the space in left side of characters
str5 = "{a:>20}".format(a = "Python")
print(str5)

# {a:<20} = it takes the space in right side of characters
str6 = "{a:<20}".format(a = "Python")
print(str6)

# {a:^20} = it takes the equal space in both side of characters
str7 = "{a:^20}".format(a = "Python")
print(str7)