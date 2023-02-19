import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday's date was:", yesterday)
print("Today's date is:", today)
print("Tomorrow's date will be:", tomorrow)

