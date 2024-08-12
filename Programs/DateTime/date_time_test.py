from datetime import datetime

# Initializing constructor
a = datetime(1999, 12, 12)
print(a)

# Initializing constructor
# with time parameters as well
a = datetime(1999, 12, 12, 12, 12, 12, 342380)
print(a)

print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

today = datetime.now()

print("Current date and time is", today)

string = datetime.isoformat(today)
print(string)
print(type(string))

# Getting Datetime from timestamp
# https://www.epochconverter.com/
date_time = datetime.fromtimestamp(1912165969)
print("Datetime from timestamp:", date_time)