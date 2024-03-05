'''
bitwise operators
&(and)
|(or)
^(xor)
--- bitwise operators performs with binary numbers ---
--- bin() function is used to check the binary number ---

binary number format            | truth table
2^3 | 2^2 | 2^1 | 2^0           | true = 1, false = 0
=8  | =4  | =2  | =1            | -----------------------
----------------------          | A | B | A&B | A|B | A^B
 0  |  0  |  0  |  0   = 0      | -----------------------
 0  |  0  |  0  |  1   = 1      | 0 | 0 |  0  |  0  |  0
 0  |  0  |  1  |  0   = 2      | 0 | 1 |  0  |  1  |  1
 0  |  0  |  1  |  1   = 3      | 1 | 0 |  0  |  1  |  1
 0  |  1  |  0  |  0   = 4      | 1 | 1 |  1  |  1  |  0
 0  |  1  |  0  |  1   = 5
 0  |  1  |  1  |  0   = 6
 0  |  1  |  1  |  1   = 7
 1  |  0  |  0  |  0   = 8
 1  |  0  |  0  |  1   = 9
 1  |  0  |  1  |  0   = 10
 1  |  0  |  1  |  1   = 11
 1  |  1  |  0  |  0   = 12
 1  |  1  |  0  |  1   = 13
 1  |  1  |  1  |  0   = 14
 1  |  1  |  1  |  1   = 15

'''

a = 10
b = 8
print("binary number of a:",bin(a))
print("binary number of b:",bin(b))
print(a&b,"binary number of a&b:",bin(a&b))
print(a|b,"binary number of a|b:",bin(a|b))
print(a^b,"binary number of a^b:",bin(a^b))