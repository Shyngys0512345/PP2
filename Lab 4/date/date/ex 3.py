import datetime

date = datetime.datetime.now()
new_date = date.replace(microsecond=0)
print("Datetime without microseconds:", new_date)