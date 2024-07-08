class Vehicle(object):

    #name = "vehicle"

    def __init__(self, name):
        self.name = name
        print(name, "Is a vehicle")

    def run(self):
        print("vehicle can run ",self.name)

class Car(Vehicle):

    def __init__(self, name):
        print(name, "can carry people")

        # Calling Parent class
        # Constructor
        super().__init__(name)

    def carry_passenger(self):
        print("carry passengers", self.name)

class ElectricCar(Car):

    def __init__(self, battery, name):
        self.battery = battery

        # Calling Parent class
        # Constructor
        super().__init__(name)

    def run_ev(self):
        print("ev ",self.name,self.battery)

ev = ElectricCar("500kv","Comet")
ev.run()
ev.run_ev()