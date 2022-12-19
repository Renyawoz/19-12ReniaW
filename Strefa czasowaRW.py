import calendar as c
import time

from arrow import arrow

print(c.calendar(2022))
print(c.month(1979,6))
print(c.firstweekday())

local_time = time.ctime()
print(local_time)
time_str = time.strftime("dziś jest %d, miesiac to %m, roku %Y")
time_str2 = time.strftime("mamy godzinę %H, minut %M")
time.sleep(5)
print(time_str)
print(time_str2)


print(arrow.now())



