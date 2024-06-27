# encapsulation = in encapsulation, class must be contain private variables and private methods

# class
class Demo:

    # private variable
    __a = 10

    # private method
    def __display(self):
        print("Encapsulation")

    # constructor = automatically called after creating object, no needs to call through object
    def __init__(self):
        c = self.__a
        print(c)
        self.__display()

# object of Demo class
obj = Demo()
