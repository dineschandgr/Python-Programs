class Vehicle:

    #attributes of class. Attributes are always public


    #contructor - called only once when object is created
    def __init__(self, c, w, n):
        self.colour = c
        self._wheel = w
        self.__name = n

    def run(self):
        print("vehicle runs ",self._wheel, self.__name, self.colour)

#object
v = Vehicle("red",4,"car")
v.run()

v1 = Vehicle("brown",8,"truck")
v1.run()

v1.name = "aaa"
v1.run()

v1.name = "yellow"
v1.run()
#print("vehicle colour ",Vehicle.colour)
