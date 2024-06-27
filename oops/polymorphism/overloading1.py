# overloading in polymorphism = same function name, but different arguments in same class

# class
class Overload:

    # same method
    def add(self, a=None, b=None):
        if a!=None and b!=None:
            print(a + b)
        elif a!=None:
            print(a)
        else:
            print("Nothing to find")

# object of Overload class
obj = Overload()

obj.add()
obj.add(2)
obj.add(4,3)