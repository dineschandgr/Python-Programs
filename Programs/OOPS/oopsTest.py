class Vehicle:

    #attributes of class. Attributes are always public
    colour = "red"
    wheel = "4"
    name = "car"
    gear = "auto"

    # Args Constructor
    def __init__(self, colour, wheel):
        print("args constrcutor called")
        self.colour = colour
        self.wheel = wheel

    def run(self):
        print("colour {} name {}".format(self.colour,self.wheel))

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            if other.colour == self.colour and other.wheel == self.wheel and other.gear == self.gear:
                return True
        return False

    def __str__(self) -> str:
        return f" $$ {self.colour} $$ {self.wheel} $$ {self.name} $$ {self.gear}"

vehicle = Vehicle("green",3)

print("vehicle ",isinstance(vehicle,Vehicle))

#instance variables
print(vehicle.colour)
print(vehicle.wheel)
print("vehicle object ", vehicle)
vehicle.run()

vehicle1 = Vehicle("blue",4)
vehicle1.run()
print("vehicle1 ",vehicle1)
print("vehicle == vehicle1 ",vehicle == vehicle1)
vehicle2 = vehicle1
print("vehicle2 == vehicle1 ",vehicle2 == vehicle1)
vehicle3= vehicle2.colour = "cyan"

print("vehicle 1", vehicle1)
print("vehicle 3", vehicle2)

print("vehicle eq vehicle1 before",vehicle.__eq__(vehicle1))
vehicle.colour = "cyan"
vehicle.wheel = 4
print("vehicle", vehicle)
print("vehicle eq vehicle1 after",vehicle.__eq__(vehicle1))

print("vehicle ",vehicle)
del vehicle.colour
print("vehicle ",vehicle)
del vehicle
#print("vehicle ",vehicle)

list1 = [1,2,3]
list2 = [1,2,3]
print("eq ", list1.__eq__(list2))
print("== ", list1 == list2)
list1.append(4)
print("list1 ",list1)
print("list2 ",list2)