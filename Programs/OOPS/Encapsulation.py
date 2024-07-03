
from multipledispatch import dispatch

class Employee:
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
        self.__salary = salary

        # private member
        self.__salary = salary

    @dispatch()
    def get_salary(self):
        return self.__salary

    @dispatch(int)
    def get_salary(self, salary):
        print("arg 1 salary")
        return self.__salary

    def set_salary(self, newsal):
         self.__salary = newsal

    def __str__(self) -> str:
        return f"{self.__name}({self.__salary})"

# creating object of a class
emp = Employee('AAA')
emp1 = Employee('James', 100000)
print(emp1.get_salary())
print(emp1.get_salary(10000))
