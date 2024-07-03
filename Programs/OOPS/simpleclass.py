class Vehicle:

    #attributes of class. Attributes are always public


    #contructor - called only once when object is created
    def __init__(self, c, w, n):
        self.colour = c
        self._wheel = w
        self.__name = n

    def run(self):
        print("vehicle runs ",self._wheel, self.__name, self.colour)

    # to compare the values of the object
    def __eq__(self, other):
        if isinstance(other, Vehicle):
            if other.colour == self.colour and other._wheel == self._wheel and other.__name == self.__name:
                return True
        return False

    # to print the values of the object
    def __str__(self) -> str:
        return f"{self.colour}({self._wheel}) {self.__name}"


#object
v = Vehicle("red",4,"car")
#v.run()
print("v ",v)

v1 = Vehicle("red",4,"car")

v1.run()
print("v is v1 ", v is v1)

print("v == v1 ", v == v1)
print("v eq v1 ", v.__eq__(v1))

v.colour = "blue"
v.run()

v1.run()

print("v == v1 ", v == v1)

print("v eq v1 ", v.__eq__(v1))

print(v is v1)

#print("vehicle colour ",Vehicle.colour)
