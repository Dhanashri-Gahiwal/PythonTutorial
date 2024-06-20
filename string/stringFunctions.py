str = "Welcome to Python"
print("original string :",str)

# lower() function is used to convert string into lower case
print("lower :",str.lower())

# upper() function is used to convert string into upper case
print("upper :",str.upper())

# title() function is used to convert each word's first letter in capital
print("title :",str.title())

# capitalize() function is used to convert first word's first letter in capital
print("capitalize :",str.capitalize())

# -----------------------------------------------------------------------------------------------

# find() function returns the index number of given string
print(str.find('o'))
print(str.find('ho'))

# finds the given string start from index 6
print(str.find('o',6))

# index() function returns the index number of given string
print(str.index('o'))
print(str.index('ho'))

# finds the given string start from index 6
print(str.index('o',6))

# difference between find() & index()
# it returns -1 bcz 'x' is not found in string
print(str.find('x'))
# it shows error bcz 'x' is not found in string
# print(str.index('x'))

# -----------------------------------------------------------------------------------------------
str1 = "hello"
str2 = "123"
str3 = "hello123"
str4 = "hello@123"

# isalpha() function returns true if given string contains only alphabets
print("------isalpha() start------")
print(str1,":",str1.isalpha())
print(str2,":",str2.isalpha())
print(str3,":",str3.isalpha())
print(str4,":",str4.isalpha())
print("------isalpha() end------")

# isdigit() function returns true if given string contains only digits
print("------isdigit() start------")
print(str1,":",str1.isdigit())
print(str2,":",str2.isdigit())
print(str3,":",str3.isdigit())
print(str4,":",str4.isdigit())
print("------isdigit() end------")

# isalnum() function returns true if given string contains only digits or only alphabets or only both digits & alphabets
print("------isalnum() start------")
print(str1,":",str1.isalnum())
print(str2,":",str2.isalnum())
print(str3,":",str3.isalnum())
print(str4,":",str4.isalnum())
print("------isalnum() end------")

# -----------------------------------------------------------------------------------------------
# chr() = takes an integer and returns string character
# chr(98) returns the ascii character value
print(chr(98),type(chr(98)))

# ord() = takes a single character and returns an integer
# ord('y') returns the ascii number
print(ord('y'),type(ord('y')))