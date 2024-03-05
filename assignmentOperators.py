'''
 Assignment operators
 equal to(=)
addition(+=)
subtraction(-=)
multiplication(*=)
division(/=) : It returns the answer in float
modulus(%=)
exponent(**=)
floor division(//=) : It returns the answer in integer
'''
x = 5
y = 2
z = 10

print(x)
print(y)
print(z)

x += y
print("addition:",x)

x -= y
print("subtraction:",x)

x *= y
print("multiplication:",x)

x /= y
print("division:",x)

z //= y
print("floor division:",z)

z %= y
print("modulus:",z)

y **= 3
print("exponent:",y) 
