from decimal import getcontext, Decimal
from math import sin, radians

getcontext().prec = 100  # You can change this number up to nth decimal place, here decimal places = 100
n = float(100)          # Value of n here is the small and finite segment which circle constitute of
angle_value = sin(radians(360/(2*n)))
pi = Decimal(n) * Decimal(angle_value)
print pi
