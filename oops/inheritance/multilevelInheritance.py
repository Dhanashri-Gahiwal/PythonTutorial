# multilevel inheritance

# class A (parent class)
class A:
    def displayA(self):
        print("Class A")

# class B (parent class and child class of class A) class B inherits class A
class B(A):
    def displayB(self):
        print("Class B")

# class C (child class of class B) class C inherits class B
class C(B):
    def displayC(self):
        print("Class C")

# object of class A called only class A methods
objA = A()
objA.displayA()

# object of class B called both class A & class B methods, bcz class B inhertis the methods of class A
objB = B()
objB.displayA()
objB.displayB()

# object of class C called both class A, class B & class C methods, bcz class C inhertis the methods of class B and class B inhertis the methods of class A
objC = C()
objC.displayA()
objC.displayB()
objC.displayC()