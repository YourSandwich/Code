## Time Only

import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

## Current Time and day
import datetime
datetime.datetime.now()
print(datetime.datetime.now())

# Selective
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.hour)
print(x.hour,x.minute)

# own time
x = datetime.datetime(2020, 5, 17)
print(x)

# Just the time
datetime.time()
print(datetime.time())

### stupid usage example

birth = datetime.datetime.now()
print("stop")
print('you was born at '+ str(birth) + ' and now your his son') ## str() is needed to declarate birth as a string(number) otherwise it wont work like in java

## makes the terminal not to close 

input()