import datetime
from os import X_OK
import time
import pytz

print(datetime.date(2021, 10, 7))
print(datetime.time(20, 10, 7))
print(datetime.date.today())
print(datetime.datetime(2020, 10, 11, 20, 10, 1, 999))
d1 = datetime.date(2021, 10, 7)
print(d1.weekday())
print(d1.isoweekday())
d2 = d1.replace(year=2022)
print(d2)
delta = datetime.timedelta(minutes=11, weeks=1, seconds=2, hours=44)
print(delta)
sh = pytz.timezone('Asia/Shanghai')
d_tz = datetime.datetime(2020, 10, 12, hour=8, tzinfo=sh)
print(d_tz.tzinfo)
print(d1.strftime('%b %d ， %Y'))

t2 = time.localtime()
t3 = time.gmtime()
print(t3)
print(t2)
t4 = time.mktime(t2)
print(t4)
t5 = time.asctime(t2)
print(t5)
import calendar

print(calendar.prcal(2021))
print(calendar.month(2022,9))
print(calendar.weekday(2021,10,8))
print(calendar.weekheader(4))



import numpy as np
w=np.arange(10000)
t=np.arange(10000)
c=w+pow(t,2)
print(c)
arr=np.arange(24).reshape(3,4,2)
print(arr)
print(bool(1))
print(np.arange(4,dtype=float))
print(np.arange(4,dtype='D'))
print(arr.size)
print(arr.ndim)
f=arr.flat
print(f)
for item in f:
    print(item)