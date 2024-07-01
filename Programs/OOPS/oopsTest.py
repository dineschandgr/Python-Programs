class Vehicle:

    #attributes of class. Attributes are always public
    colour = "red"
    wheel = "4"

    # Constructor
    def __init__(self, colour, wheel):
        self.colour = colour
        self.wheel = wheel

    def run(self):
        print("run ",self.colour, " ",self.wheel)

    def __str__(self):
        return f"{self.colour}({self.wheel})"

vehicle = Vehicle("yellow",3)
print("vehicle ",vehicle)
print(vehicle.__class__.colour)
print(vehicle.__class__.wheel)

print(vehicle.colour)
print(vehicle.wheel)
vehicle.run()
vehicle.colour = "blue"
print("vehicle ",vehicle)
del vehicle.colour
print("vehicle ",vehicle)
del vehicle
print("vehicle ",vehicle)

