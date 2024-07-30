def my_function_1():
    print("Hello World")

def my_function_2(fname):
    print(fname + " args")

# arbitary args
def my_function_3(*args):
    print((args))

def addition(*args):
    sum = 0
    for ele in args:
        sum += ele
    print("unlimited sum ", sum)

def my_function_4(child3, child2, child1):
    print(child1, child2, child3)

# keyword args
def my_function_5(**fruit):
    print("fruits" + fruit["lname"])
    print("type", type(fruit))

# default params
def my_function_6(country="Norway"):
    print(country)
    return "hello"

# pass collections
# pass by reference
def my_function_7(fruits):
    for x in fruits:
        print("fruit ", x)
    fruits.append("Pomo")


my_function_1()
addition(10, 20, 30, 40, 50)
my_function_2("hello")
my_function_2("welcome")
my_function_3("welcome", "hello", "world")
my_function_4(child1="Emil", child2="Tobias", child3="Linus")
my_function_5(fname="apple", lname="banana")
my_function_6()
country = my_function_6("India")
print(country)
list1 = ["Apple", "Banana", "Mango"]
my_function_7(list1.copy())
print(list1)

# lambda function - anonymous
# lambda arguments : expression

def addition(a):
    return a + 10

x = addition(10)
print("function ", x)

x = lambda a: a + 10

print("lambda", x(5))
print("lambda", x(10))

x = lambda a, b: a * b
print(x(5, 6))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

def myfunc(n):
    return lambda a: a * n

double = myfunc(2)

print(double(11))

triple = myfunc(3)
print(triple(11))
