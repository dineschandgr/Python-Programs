class Vehicle:

    #attributes of class. Attributes are always public
    colour = "red"
    wheel = "4"
    name = "car"

    # Args Constructor
    def __init__(self, colour, wheel):
        print("args constrcutor called")
        self.colour = colour
        self.wheel = wheel

    def run(self):
        print("colour {} name {}".format(self.colour,self.wheel))

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            if other.colour == self.colour and other.wheel == self.wheel:
                return True
        return False

    def __str__(self) -> str:
        return f"{self.colour}({self.wheel}) {self.name}"

vehicle = Vehicle("green",3)

print("vehicle ",isinstance(vehicle,Vehicle))


#class variables
print(vehicle.__class__.colour)
print(vehicle.__class__.wheel)

#instance variables
print(vehicle.colour)
print(vehicle.wheel)
vehicle.run()

vehicle1 = Vehicle("blue",4)
vehicle1.run()

print("vehicle == vehicle1 ",vehicle == vehicle1)

vehicle1.wheel = 3
vehicle1.colour = "green"

print("vehicle eq vehicle1 ",vehicle.__eq__(vehicle1))


vehicle.colour = "blue"
print("vehicle ",vehicle)
del vehicle.colour
print("vehicle ",vehicle)
del vehicle
#print("vehicle ",vehicle)

