from abc import ABC, abstractmethod


class democlass(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return

    def method2(self):
        print("concrete method")


class concreteclass(democlass):
    def method1(self):
        super().method1()
        return


obj = concreteclass()
obj.method1()
obj.method2()


class Shape(ABC):
        @abstractmethod
        def area(self):
            pass
        @abstractmethod
        def perimeter(self):
            pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return  self.length * self.breadth
    def perimeter(self):
        return  (self.length +  self.breadth) * 2

def print_shape(shape):
    print(shape.area())
    print(shape.perimeter())


circle = Circle(10)
print_shape(circle)

rectange = Rectangle(10,20)
print_shape(rectange)