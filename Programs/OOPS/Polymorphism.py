class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks")

my_animal = Dog()
my_animal.make_sound()  # Calls the overridden method in the Dog class
my_animal = Animal()
my_animal.make_sound()

#duck typing
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def perform_flight(obj):
    obj.fly()

sparrow = Sparrow()
airplane = Airplane()

perform_flight(sparrow)  # Output: Sparrow flies
perform_flight(airplane)  # Output: Airplane flies


# parametric polymorphism
from typing import TypeVar

T = TypeVar('T')

def print_item(item: T):
    print(item)

print_item(42)         # Works with integers
print_item("Hello")    # Works with strings

