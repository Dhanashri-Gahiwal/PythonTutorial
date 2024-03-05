'''
Data types : 
Numerical
    integer(immutable data type)
    float(immutable data type)
    complex number(immutable data type)
Sequence
    string(immutable data type)
    list(mutable data type)
    tuple(immutable data type)
Dictionary(mutable data type)
Set(immutable data type)
--- mutable means changeable and immutable means not changeable ---
--- type() function is used to check the data type of variable
'''
int1 = 2
print(int1,type(int1))

float1 = 2.2
print(float1,type(float1))

cmplx = 2+3j
print(cmplx,type(cmplx))

str = "Hello"
print(str,type(str))

l1 = [1,2.2,3+4j,'a']
print(l1,type(l1))

t1 = (1,2.2,3+4j,'a')
print(t1,type(t1))

s1 = {1,2,3,4}
print(s1,type(s1))

d1 = {"name":"Dhanshri","age":26}
print(d1,type(d1))