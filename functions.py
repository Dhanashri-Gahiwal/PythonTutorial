# simple function
# define function
def printData():
    print("Hello World!")

# calling function
printData()

# ------------------------------------------------------------------------------------------

# function with argument
# single argument
def cube(x):
    print(x*x*x)

cube(5)

# 2 arguments
def subtract(a,b):
    print(a-b)

subtract(20,10)

# argument with default value
def sum(a=10,b=5):
    print(a+b)

sum(5)   # a=5, b=5
sum(25,30) # a=25, b=30
sum() # a=10, b=5

n = 9
m = 2
sum(n,m) # n=9=a, m=2=b

# ------------------------------------------------------------------------------------------

# return type function
def multi(x,y):
    return x*y, 4*y, x*5

print(multi(2,3))