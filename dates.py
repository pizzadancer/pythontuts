#to get current date and time we need to use the datetime library
from datetime import datetime, timedelta

#the now function returns currnt date and time
today = datetime.now()

print("Today is: " + str(today))

#You can use timedelta to add or reomve days, or weeks to a date
# one_day = timedelta(days=1)
# # print(one_day)
# yesterday = today - one_day
# print("Yesterday was: " + str(yesterday))

# one_week = timedelta(weeks=1)
# last_week = today - one_week
# print("Last week was: " + str(last_week))

print("Day: " + str(today.day))
print("Month: " + str(today.month))
print("Year: " + str(today.year))

print("Hour: " + str(today.hour))
print("Minute: " + str(today.minute))
print("Second: " + str(today.second))
