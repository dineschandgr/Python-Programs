from datetime import datetime, timedelta

# Using current time
ini_time_for_now = datetime.now()

# printing initial_date
print("initial_date", str(ini_time_for_now))

# Calculating future dates
# for two years
future_date_after_2yrs = ini_time_for_now + timedelta(days=730)

future_date_after_2days = ini_time_for_now + timedelta(days=2)

# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))

print("initial_date", str(ini_time_for_now))

# Some another datetime
new_final_time = ini_time_for_now + \
                 timedelta(days=2)

# printing new final_date
print("new_final_time", str(new_final_time))

# printing calculated past_dates
print('Time difference:', str(new_final_time -
                              ini_time_for_now))