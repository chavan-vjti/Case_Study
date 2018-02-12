from decimal import getcontext, Decimal

getcontext().prec = 100  # You can change this number upto nth decimal place, here n = 100

pi = Decimal(22) / Decimal(7)

print 'Value of \'pi\' upto 100th decimal place is ' + str(pi)  # For String concatenation pi is converted into string
