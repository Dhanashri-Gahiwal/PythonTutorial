# create a Demo class
class Demo:
    # variables
    x = 5
    y = 3

    # simple method
    def sum(self,a,b):
        print(a+b)

    # calling variables in method using self keyword
    def mul(self):
        result = self.x * self.y
        return result

obj = Demo()
obj.sum(10,20)
output = obj.mul()
print(output)