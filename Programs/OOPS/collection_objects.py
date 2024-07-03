
from multipledispatch import dispatch

class Employee:

    __salary = 1000

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
        return f"{self.__name}({self.__salary})"

    def __eq__(self, other):
        if isinstance(other, Employee):
            if other.__name == self.__name and other.__salary == self.__salary:
                return True
        return False

    def __hash__(self):
        # hash(custom_object)
        return hash((self.__name, self.__salary))

# creating object of a class
emp = Employee('AAA')
print(emp.get_salary())

emp1 = Employee('James', 100000)
print(emp1.get_salary())

emp1.add_salary(15000.01)
print(emp1.get_salary())

emp2 = Employee('Roshan', 200000)
emp2.add_salary(20000.01,10000.50)
print(emp2.get_salary())

list = [emp, emp1, emp2]

for e in list:
    print(e)
    print(e)

emp3 = list[1]
print(" emp3 is emp", emp3 is emp)

list.append(emp3)

tuple_emp = (emp, emp1, emp2)

dict_emp =  {
    "emp" : emp,
    "emp1" : emp1,
    "emp2": emp2
}

print(dict_emp.get("emp1"))

emp5 = Employee('Roshan', 200000)
emp5.add_salary(20000.01,10000.50)

print("emp2 is emp5 ", emp2 is emp5)

emp_set = {emp, emp1, emp2, emp3, emp5, emp}
print("len is ",len(emp_set))

for e in emp_set:
    print("set values ",e)

dict_emp1 = {
    "emp": emp,
    "emp": emp1,
    "emp2": emp2
}

print("dict ",dict_emp1.get("emp"))