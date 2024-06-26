import functools

import operator


#Map Reduce and Filter Operations in Python


#Syntax: map(fun, iterable)

# Function to return double of n

def double(n):
    return n * 2

# Using map to double all numbers
numbers = [5, 6, 7, 8]
result = map(double, numbers)
print(list(result))

fruits = ['apple', 'mango', 'orange', 'banana']
capital_fruits = []

for fruit in fruits:
    fruit_ = fruit.upper()
    capital_fruits.append(fruit_)

print(capital_fruits)

capital_fruits = list(map(str.upper, fruits))
print(capital_fruits)


#map with lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)

# initializing list
lis = [1, 3, 5, 6, 2]

#filter
#filter(function, iterable(s))



# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

print(functools.reduce(operator.add, lis))
print(functools.reduce(operator.mul, lis))


def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_A, fruit)

print(list(filter_object))


#filter using lambda
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)

print(list(filter_object))