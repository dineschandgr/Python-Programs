class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.__name = name

        # private member
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, newsal):
         self.__salary = newsal

    def __str__(self) -> str:
        return f"{self.__name}({self.__salary})"

# creating object of a class
emp = Employee('James', 100000)

# accessing private data members
print('Salary:', emp.get_salary())

emp.set_salary(20000)
print('Updated Salary:', emp.get_salary())

print(emp)