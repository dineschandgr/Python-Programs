#Generator Function

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)

#x is the generator object
x = simpleGeneratorFun()
print(next(x))
print("hello")
print(next(x))

print("final ",next(x))

# generator expression
generator_exp = (i * 5 for i in range(5) if i%2 == 0)

for i in generator_exp:
    print(i)

# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


print("\nUsing for in loop")
for i in fib(5):
    print(i)


