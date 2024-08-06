
from datetime import time

my_time = time(13, 24, 56)

print("Entered time", my_time)

# calling constructor with 1
# argument
my_time = time(minute=12)
print("\nTime with one argument", my_time)

# Calling constructor with
# 0 argument
my_time = time()
print("\nTime without argument", my_time)

Time = time(11, 34, 56, 00)

print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

Str = Time.isoformat()
print("String Representation:", Str)
print(type(Str))