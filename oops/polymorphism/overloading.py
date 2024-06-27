# overloading in polymorphism = same function name, but different arguments in same class

# class
class Overload:

    # same method
    def displayInfo(self, a):
        print(a)

    # same method
    def displayInfo(self,name=""):
        print(name)

# object of Overload class
obj = Overload()

obj.displayInfo(10)

obj.displayInfo("Rajesh")





