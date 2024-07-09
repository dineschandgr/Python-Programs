x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


try:
  x = "hello"

  if not type(x) is int:
    raise TypeError("Only integers are allowed")
except Exception as e:
  print(f"Caught error: {repr(e)}")


try:
  x = "hello"

  if not type(x) is int:
    raise TypeError("Only integers are allowed")
except TypeError as e:
  print("Typo Error", repr(e))
except Exception as e:
  print(f"Caught error: {repr(e)}")


def divide_by_zero():
  return 1 / 0  # will fail and raise a ZeroDivisionError

try:
    divide_by_zero()
    raise Exception("My custom exception.")
except ValueError as e:
    print(f"Caught value error: {repr(e)}")
except Exception as e:
    print(f"Caught custom exception: {repr(e)}")


#Exception Arguments

try:
    raise Exception("My custom exception.", 1, "a", True)
except Exception as e:
    print(e.args) # will print (1, "a", True)


#Custom Exception Class

class MyValueError(ValueError):
  """ Raise when a custom value error occurs."""


def divide_by_zero():
  return 1 / 0  # will fail and raise a ZeroDivisionError

  class MyValueError(ValueError):
    """ Raise when a custom value error occurs."""


def divide_by_zero():
  return 1 / 0  # will fail and raise a ZeroDivisionError

class MyValueError(ValueError):
    """ Raise when a custom value error occurs."""


def divide_by_zero():
  return 1 / 0  # will fail and raise a ZeroDivisionError


try:
  raise MyValueError("My custom exception.")
  divide_by_zero()
except MyValueError as e:
  print(f"Caught custom value error: {repr(e)}")
except ValueError as e:
  print(f"Caught built-in value error: {repr(e)}")


#Chaining Exceptions

def example():
  try:
    int('N/A')
  except ValueError as e:
    raise RuntimeError('A parsing error occurred') from e

example()


