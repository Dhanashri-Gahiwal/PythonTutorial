# multiple inheritance

# class A (parent class)
class A:
    def displayA(self):
        print("Class A")

# class B (parent class)
class B:
    def displayB(self):
        print("Class B")

# class C (child class) class C inherits class A & class B
class C(A,B):
    def displayC(self):
        print("Class C")

# object of class A called only class A methods
objA = A()
objA.displayA()

# object of class B called only class B methods
objB = B()
objB.displayB()

# object of class C called class A, class B & class C methods, bcz class C inhertis the methods of class A & class B
objC = C()
objC.displayA()
objC.displayB()
objC.displayC()