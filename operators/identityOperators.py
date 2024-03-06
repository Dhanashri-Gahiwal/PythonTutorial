'''
identity operators
is = 'is' operator is same as '==' operator
is not = 'is not' operator is same as '!=' operator
--- identity operators are used to check equality ---
'''

a = 5
b = 5
c = 6

print(a is b)
print(a == b)
print(a is c)
print(a == c)
print(a is not b)
print(a != b)
print(a is not c)
print(a != c)