import datetime

mytime = datetime.time(2, 20)

print(mytime.minute)
print(mytime.hour)

print(mytime)
print(type(mytime))

today = datetime.date.today()
print(today)


mydatetime = datetime.datetime(2021, 10, 3, 14, 20, 1)
print(mydatetime)

mydatetime = mydatetime.replace(year=2020)
print(mydatetime)
