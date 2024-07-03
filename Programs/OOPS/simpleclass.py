class Vehicle:

    #attributes of class. Attributes are always public


    #contructor - called only once when object is created
    def __init__(self, c, w, n):
        self.colour = c
        self._wheel = w
        self.__name = n

    def run(self):
        print("vehicle runs ",self._wheel, self.__name, self.colour)

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            if other.colour == self.colour and other._wheel == self._wheel and other.__name == self.__name:
                return True
        return False

#object
v = Vehicle("red",4,"car")
v.run()

v1 = Vehicle("red",4,"car")
v1.run()

print("v == v1 ", v == v1)

print("v eq v1 ", v.__eq__(v1))

v1.name = "aaa"
v1.run()

v1.name = "yellow"
v1.run()
#print("vehicle colour ",Vehicle.colour)
