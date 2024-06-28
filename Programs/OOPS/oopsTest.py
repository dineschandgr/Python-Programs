class Vehicle:
    colour = "red"
    wheel = "4"

    # Instance attribute
    def __init__(self, colour, wheel):
        self.colour = colour
        self.wheel = wheel

    def run(self):
        print("run ",self.colour, " ",self.wheel)

vehicle = Vehicle("yellow",3)
print(vehicle.__class__.colour)
print(vehicle.__class__.wheel)

print(vehicle.colour)
print(vehicle.wheel)
vehicle.run()