# first way to import module and use functions
import userDfinedModules

# call sum() function
addition = userDfinedModules.sum(20,30)
print(addition)

# call mul() function
multiplication = userDfinedModules.mul(20,30)
print(multiplication)

# call sub() function
subtraction = userDfinedModules.sub(40,30)
print(subtraction)

# ------------------------------------------------------------------------------------

# second way to import module and use functions by using alias
import userDfinedModules as m

# call sum() function
addition = m.sum(20,30)
print(addition)

# call mul() function
multiplication = m.mul(20,30)
print(multiplication)

# call sub() function
subtraction = m.sub(40,30)
print(subtraction)

# ------------------------------------------------------------------------------------

# third way to import module and use functions
from userDfinedModules import sum, sub, mul

# call sum() function
addition = sum(20,30)
print(addition)

# call mul() function
multiplication = mul(20,30)
print(multiplication)

# call sub() function
subtraction = sub(40,30)
print(subtraction)

# ------------------------------------------------------------------------------------

# fourth way to import module and use functions
from userDfinedModules import *

# call sum() function
addition = sum(20,30)
print(addition)

# call mul() function
multiplication = mul(20,30)
print(multiplication)

# call sub() function
subtraction = sub(40,30)
print(subtraction)

# ------------------------------------------------------------------------------------