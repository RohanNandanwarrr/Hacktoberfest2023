# POLYMORPHISM WITH INHERITANCE :-

class Veh:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def get_details(self):
        print("Name is :",self.name)
        print("Color is :",self.color)
        print("Price is :",self.price)

    def max_Speed(self):
        print("Maximum speed limit is 100")

    def gear(self):
        print("gear change is 6")


class Car(Veh):
    def max_Speed(self):
        print("Maximum speed limit is 140")

    def gear(self):
        print("gear change is 8")

V1 = Veh("Truck","red",20000000)
V1.get_details()
V1.gear()
V1.max_Speed()

C1 = Car("Car","red",20000)
C1.get_details()
C1.gear()
C1.max_Speed()
