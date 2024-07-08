class Vehicle(object):

    #name = "vehicle"

    def __init__(self, name):
        self.name = name
        print(name, "Is a vehicle")

    def run(self):
        print("vehicle can run")

class test():
    def __init__(self, test):
        self.test = test
        print("test class constructor ",test)

class Passenger(Vehicle):

    def __init__(self, name):
        print(name, "can carry people")

        # Calling Parent class
        # Constructor
        super().__init__(name)

    def carry_passenger(self):
        print("carry passengers", self.name)


class HeavyDuty(Vehicle):

    def __init__(self, name):
        print("carry luggage constructor", name)
        self.name = name

        super().__init__(name)

    def carry_luggage(self):
        print("carry luggage", self.name)


class Truck(Passenger, HeavyDuty, test):

    def __init__(self, name):
        super().__init__(name)

vehicle = Vehicle("vehicle")
passenger = Passenger("passenger")
heavy_duty = HeavyDuty("heavyduty")
truck = Truck("truck")
truck.run()
truck.carry_luggage()
print("method resolution order",Truck.mro())
print("method resolution order",Vehicle.mro())
