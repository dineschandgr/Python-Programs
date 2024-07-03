class Employee:
    # constructor

    # def __init__(self, name):
    #     # public data member
    #     print("1 arg constructor")
    #     self.__name = name


    def __init__(self, name, salary = None):

        print("2 args constructor")
        # public data member
        self.__name = name
        self.__salary = salary

        # private member
        self.__salary = salary


    # def get_salary(self):
    #     return self.__salary


    def get_salary(self, salary = None):
        print("arg 1 salary ",salary)
        return self.__salary

    def set_salary(self, newsal):
         self.__salary = newsal

    def __str__(self) -> str:
        return f"{self.__name}({self.__salary})"


e1 = Employee("test")
print("e1 sal ",e1.get_salary())

e2 = Employee("test",10000)
print("e2 sal ",e2.get_salary(1000))
