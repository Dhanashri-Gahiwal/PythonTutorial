# single inheritance

# class A (parent class)
class A:
    def displayA(self):
        print("Class A")

# class B (child class) class B inherits class A
class B(A):
    def displayB(self):
        print("Class B")

# object of class A called only class A methods
objA = A()
objA.displayA()

# object of class B called both class A & class B methods, bcz class B inhertis the methods of class A
objB = B()
objB.displayA()
objB.displayB()