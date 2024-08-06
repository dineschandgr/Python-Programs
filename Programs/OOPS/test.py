class Vehicle:

    #attributes
    wheel = 4
    colour = "red"
    # behaviour
    def run(self):
        # accessing protected data members
        print("Name: ", self.wheel)
        print("Colour: ", self.colour)

    # creating objects of the class


obj = Vehicle()
obj.run()
# calling public member
# functions of the class
obj1 = Vehicle()
obj1.run()