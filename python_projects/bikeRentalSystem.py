# Bike Rental System
# class
class BikeShop:
    # constructor
    def __init__(self,stock):
        self.stock = stock

    def displayBikeStock(self):
        print("Available bike stock:",self.stock)

    def rentForBike(self,quantity):
        if quantity <= 0:
            print("Enter positive number or greater than 0")
        elif quantity > self.stock:
            print("Enter less number of quantity")
        else:
            print("Total Price",quantity*100)
            self.stock -= quantity
            print("Total bikes:",self.stock)

while True:
    bikeObj = BikeShop(100)

    choice = int(input(
        '''
        1 Display available stock of bike
        2 Total rent of bike
        3 Exit
        '''
    ) )

    if choice == 1:
        bikeObj.displayBikeStock()

    elif choice == 2:
        n = int(input("Enter quantity of bike: "))
        bikeObj.rentForBike(n)

    else:
        break