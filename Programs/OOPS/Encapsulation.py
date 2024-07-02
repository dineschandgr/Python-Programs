class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name

        # private member
        self.__salary = salary

    def get_salary(self):
        return self.__salary

# creating object of a class
emp = Employee('James', 100000)

# accessing private data members
print('Salary:', emp.get_salary())