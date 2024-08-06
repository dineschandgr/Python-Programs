import functools

import operator


#Map Reduce and Filter Operations in Python


#Syntax: map(fun, iterable)

# Function to return double of n

def double(n):
    return n * 2

# Using map to double all numbers
numbers = [5, 6, 7, 8]

result_list = []
for i in numbers:
    result_list.append(double(i))

print("result is ",result_list)
result = map(double, numbers)
print("result ",list(result))

fruits = ['apple', 'mango', 'orange', 'banana']
capital_fruits = []

for fruit in fruits:
    fruit_ = fruit.upper()
    capital_fruits.append(fruit_)

print(capital_fruits)

capital_fruits = map(str.upper, fruits)
print(list(capital_fruits))


def lambda_test(str):
    return str.upper()

#lambda
x = lambda string: string.upper()
print("lambda output ", x("hello"))


#map with lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [7, 8, 9]

result = map(lambda x, y, z: x + y - z, numbers1, numbers2, numbers3)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


#Reduce

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

print(functools.reduce(operator.add, lis))
print(functools.reduce(operator.mul, lis))


#filter
#filter(function, iterable(s))

def starts_with_A(s):
    return s[0] == "A"

fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_A, fruits)
print(type(filter_object))
print(list(filter_object))


#filter using lambda
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)

print(list(filter_object))

student = [30 , 40 , 44 , 50 , 60 , 80, 90, 97]

pass_students = filter(lambda mark: mark > 50, student)
print("pass students ", list(pass_students))

o_students = filter(lambda mark: mark >= 90, student)
print("O students ", list(o_students))