class Vehicle:
    licenseCode = ""
    seriaCode=""
    def TurnOnAirConditioner(self):
        print("Turn on : Air")
class car(Vehicle):
    pass
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1 =car()
car1.TurnOnAirConditioner()
Pickup1=Pickup()
Pickup1.TurnOnAirConditioner()
Van1 = Van()
Van1.TurnOnAirConditioner()
EstateCar1=EstateCar()
EstateCar1.TurnOnAirConditioner()