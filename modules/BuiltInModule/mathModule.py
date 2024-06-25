# math module
import math

# cbrt() = cube root = returns the cube root
print(math.cbrt(27))

# ceil() = returns the greater value if the given number in float
print(math.ceil(10.2))

# fabs() = returns the absolute value, means it returns the positive value
print(math.fabs(-10))

# factorial() = it returns the factorial of given number
print(math.factorial(5))

# floor() = it returns smaller value if the given number in float  
print(math.floor(10.5))

# fsum() = returns the sum of list or tuple elements
l = [1,2,3,4,5] # list
print(math.fsum(l))

t = (1,2,3,4,5) # tuple
print(math.fsum(t))

# pi = returns the value of pi
print(math.pi)

# pow() = returns the power of given value
print(math.pow(2,3)) # 2^3 = 2*2*2 = 8
print(math.pow(2,2)) # 2^2 = 2*2 = 4

# prod() = returns the multiplication of list or tuple elements
l = [1,2,3,4,5] # list
print(math.prod(l))

t = (10,2,3,4,5) # tuple
print(math.prod(t))

# remainder() = returns the remainder (10/3 = 1)
print(math.remainder(10,3))

# sqrt() = returns the square root of given number
print(math.sqrt(81))
