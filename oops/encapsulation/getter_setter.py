# getter setter methods in encapsulation = getter setter methods must be public in encapsulation

# class
class Demo:

    # constructor
    def __init__(self):
        self.__name = ""

    # setter method
    def setname(self,name):
        self.__name = name

    # getter method
    def getname(self):
        return self.__name

# object of Demo class 
obj = Demo()

# calling setter method
obj.setname("Dhanshri")

# calling getter method
print(obj.getname())