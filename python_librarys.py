'''STANDARD LIBRARYS'''
#calender
import calendar
yy=int(input("enter your year"))
mm=int(input("enter your month"))
print(calendar.month(yy,mm))


import calendar
yy=2024
print(calendar.calendar(yy))

'''MATH'''
import math
print("the value is",math.pi)


# types of import
import math as m
print(m.pi)

# from
from math import pi
print(pi)

# all
from math import *
print("The value of pi is",pi)
