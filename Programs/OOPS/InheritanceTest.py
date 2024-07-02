#Single, Multilevel, Hierarchical, Multiple

# parent class
class Vehicle(object):

    # __init__ is known as the constructor
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def display(self):
        print(self.name)
        print(self.colour)

    def details(self):
        print("Vehicle name is {}".format(self.name))
        print("colour: {}".format(self.colour))


class Test(Vehicle):
  pass

# child class
class Car(Vehicle):

    def __init__(self, name, colour, type, wheel):
        self.type = type
        self.wheel = wheel

        # invoking the __init__ of the parent class
        super().__init__(name, colour)

    def details(self):
        print("Vehicle name is {}".format(self.name))
        print("colour: {}".format(self.colour))
        print("type: {}".format(self.type))
        print("wheel: {}".format(self.wheel))

# creation of an object variable or an instance
a = Car('Ferrari', "red", "car", 4)

# calling a function of the class Person using
# its instance
a.display()
a.details()

b = Test('Ferrari', "red")
b.details()