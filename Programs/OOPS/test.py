class Geek:
    # protected data members
    _name = "R2J"
    _roll = 1706256

    # public member function
    def displayNameAndRoll(self):
        # accessing protected data members
        print("Name: ", self._name)
        print("Roll: ", self._roll)

    # creating objects of the class


obj = Geek()

# calling public member
# functions of the class
obj.displayNameAndRoll()