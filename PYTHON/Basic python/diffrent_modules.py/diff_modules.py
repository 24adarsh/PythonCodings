
import math
print(math.factorial(5))
print(math.pi)

print('----------------------------------------------')

import datetime
mydate=datetime.date(2025,2,18)
print(mydate)
print(mydate.day)
print(mydate.month)
print(mydate.year)

today=datetime.datetime.today()
print(today.day)
print(today.month)
print(today.year)

print(datetime.datetime.now())

print('----------------------------------------------')

import datetime

start=datetime.datetime.now()

for i in range(1001):
    print(i)

end=datetime.datetime.now()

time=end-start
print(time)

print('----------------------------------------------')

import csv 
csv.DictReader()
