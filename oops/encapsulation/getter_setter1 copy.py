# getter setter methods in encapsulation = getter setter methods must be public in encapsulation

# class
class Demo:

    # private variable
    __firstname = ""
    __lastname = ""

    # private method
    def __fullname(self):
        print(self.__firstname,self.__lastname)

    # setter method
    def setfullname(self,fname,lname):
        self.__firstname = fname
        self.__lastname = lname

    # getter method
    def getfullname(self):
        return self.__fullname()

# object of Demo class 
obj = Demo()

# calling setter method
obj.setfullname("Rahul","Gahiwal")

# calling getter method
obj.getfullname()