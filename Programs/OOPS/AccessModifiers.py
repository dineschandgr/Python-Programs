
from multipledispatch import dispatch

class Employee:
    # private member
    __bonus = 200
    # protected member
    _salary = 300
    # public member
    incentive = 100

    @dispatch(int, int, int)
    def __init__(self, bonus, salary, incentive):
        print("3 args constructor")
        self.__bonus = bonus
        self._salary = salary
        self.incentive = incentive

    @dispatch(int, int)
    def __init__(self, salary, incentive):
        # public data member
        print("2 args constructor")
        self._salary = salary
        self.incentive = incentive

    def get_salary(self):
        return self._salary

    def __str__(self) -> str:
        return f"({self.__bonus} : {self._salary} : {self.incentive})"

class Intern(Employee):

    def __init__(self, salary, incentive):
        super().__init__(salary, incentive)

    def __str__(self) -> str:
        return f"({self._salary} {self.incentive})"


emp = Employee(10000,20000,5000)
emp._salary = 222222
print("employee ",emp)

intern = Intern(8000,500)
print("intern ",intern)