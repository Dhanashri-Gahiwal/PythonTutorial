# create a Demo class
class Demo:
    a = 10                    # variable
    def display(self):        # method
        print("Demo class")

demoObj = Demo()              # create object of Demo class

val = demoObj.a               # calling variable through demoObj object
print(val)

demoObj.display()             # calling method through demoObj object