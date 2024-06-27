# overriding in python = same function name, same argument but in different class

# class
class Override1:

    def displayInfo(self):
        print("Welcome")

class Override2(Override1):

    def displayInfo(self):
        print("Hello World")
        super().displayInfo()

# object of Override2
obj = Override2()
obj.displayInfo()