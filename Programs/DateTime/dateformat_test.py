from datetime import datetime as dt, datetime

# Getting current date and time
now = dt.now()
print("Without formatting", now)

# Example 1
s = now.strftime("%A %m %-Y")
print('\nExample 1:', s)

# Example 2
s = now.strftime("%a %-m %y")
print('\nExample 2:', s)

# Example 3
s = now.strftime("%-I %p %S")
print('\nExample 3:', s)

# Example 4
s = now.strftime("%H:%M:%S")
print('\nExample 4:', s)

time_data = ["25/05/99 02:35:8.023", "26/05/99 12:45:0.003",
             "27/05/99 07:35:5.523", "28/05/99 05:15:55.523"]

# format the string in the given format : day/month/year
# hours/minutes/seconds-micro seconds
format_data = "%d/%m/%y %H:%M:%S.%f"

# Using strptime with datetime we will format string
# into datetime
for i in time_data:
    print(datetime.strptime(i, format_data))
