import datetime

str_date1 = input("Enter the first date in Y-W-D:")
str_date2 = input("Enter the second date in Y-W-D:")
date1 = datetime.datetime.strptime(str_date1, "%Y-%m-%d")
date2 = datetime.datetime.strptime(str_date2, "%Y-%m-%d")
difference = abs((date2 -date1).total_seconds())
print(difference)
