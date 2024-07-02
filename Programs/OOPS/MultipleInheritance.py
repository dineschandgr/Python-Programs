class Vehicle():

    #name = "vehicle"

    def __init__(self, name):
        self.name = name
        print(name, "Is a vehicle")

    def run(self):
        print("vehicle can run")


class Passenger(Vehicle):

    def __init__(self, name):
        print(name, "can carry people")

        # Calling Parent class
        # Constructor
        super().__init__(name)

    def carry_passenger(self):
        print("carry passengers", self.name)


class Luggage(Vehicle):

    def __init__(self, name):
        print("carry luggage", name)
        self.name = name

        super().__init__(name)

    def carry_luggage(self):
        print("carry luggage", self.name)


class Truck(Passenger, Luggage):

    def __init__(self, name):
        super().__init__(name)

vehicle = Vehicle("vehcile")
truck = Truck("AshokLeyland")
truck.run()
truck.carry_luggage()


#Hybrid Inheritance - Diamond Problem
#Method Resolution Order (MRO)
class A:
    def age(self):
        print("Age is 21")


class B:
    def age(self):
        print("Age is 23")


class C(A, B):
    def age(self):
        super(C, self).age()


c = C()
print(C.__mro__)
print(c.age())
print(C.mro())