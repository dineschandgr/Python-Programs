
from multipledispatch import dispatch

class Employee:
    __bonus = 0

    # constructor
    @dispatch(str)
    def __init__(self, name):
        # public data member
        print("1 arg constructor")
        self.__name = name

    @dispatch(str,int)
    def __init__(self, name, salary):

        print("2 args constructor")
        # public data member
        self.__name = name

        # private member
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    @dispatch(float)
    def add_salary(self, bonus):
        print("arg 1 salary")
        self.__salary += bonus

    @dispatch(float, float)
    def add_salary(self, bonus, incentives):
        print("arg 1 salary")
        self.__salary += bonus + incentives

    def set_salary(self, newsal):
         self.__salary = newsal

    def __str__(self) -> str:
        return f"{self.__name}({self.__salary} {self.__bonus})"

# creating object of a class
emp = Employee('AAA')

emp.salary = 3000000000
print(emp.get_salary())

emp1 = Employee('James', 100000)
print(emp1.get_salary())
emp1.name = "hello"
print(emp1)

emp1.add_salary(15000.01)
print(emp1.get_salary())

emp2 = Employee('Roshan', 200000)
emp2.add_salary(20000.01,10000.50)
print(emp2.get_salary())