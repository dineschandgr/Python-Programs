from datetime import datetime
from dateutil import tz

# tz_string = datetime.now(datetime.utcnow()).astimezone().tzname()
#
# print("datetime.now() :", tz_string)

NYC = tz.gettz('Europe / Berlin')
dt1 = datetime(2022, 5, 21, 12, 0)
dt2 = datetime(2022, 12, 21, 12, 0, tzinfo=NYC)

print("Naive Object :", dt1.tzname())
print("Aware Object :", dt2.tzname())

tz = tz.gettz('Australia/Melbourne')
now = datetime.now()

your_now = now.astimezone(tz)
print(your_now)