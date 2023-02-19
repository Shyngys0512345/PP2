import datetime

current_date = datetime.datetime.now()
new_date = current_date - datetime.timedelta(days=5)
print("Five days ago from today was:", new_date)