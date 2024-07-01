class Mammal():

    def __init__(self, name):
        print(name, "Is a mammal")


class canFly(Mammal):

    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")

        # Calling Parent class
        # Constructor
        super().__init__(canFly_name)


class canSwim(Mammal):

    def __init__(self, canSwim_name):
        print(canSwim_name, "cannot swim")

        super().__init__(canSwim_name)


class Animal(canFly, canSwim):

    def __init__(self, name):
        super().__init__(name)



Carol = Animal("Dog")


#Hybrid Inheritance - Diamond Problem
#Method Resolution Order (MRO)
class A:
    def age(self):
        print("Age is 21")


class B:
    def age(self):
        print("Age is 23")


class C(A, B):
    def age(self):
        super(C, self).age()


c = C()
print(C.__mro__)
print(c.age())
print(C.mro())