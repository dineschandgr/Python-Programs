

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
#print(C.mro())