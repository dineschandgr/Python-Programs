class Vehicle:

    #attributes of class. Attributes are always public
    colour = "blue"
    wheel = "4"
    name = "vehicle"

    #contructor - called only once when object is created
    def __init__(self, c, w, n):
        self.colour = c
        self.wheel = w
        self.name = n

    def run(self):
        print("vehicle runs ",self.wheel, self.name, self.colour)

#object
v = Vehicle("red","4","car")
v.run()


v1 = Vehicle("brown",8,"truck")
v1.run()

print("vehicle colour ",Vehicle.colour)
