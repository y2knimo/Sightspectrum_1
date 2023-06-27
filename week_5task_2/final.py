
class Car:

    vehicle = 'car'

    def __init__(self, model):
        # Instance Variable
        self.model = model


    def setprice(self, price):
        self.price = price


    def getprice(self):
        return self.price


Audi = Car("R8")
Audi.setprice(1000000)
print(Audi.getprice())
