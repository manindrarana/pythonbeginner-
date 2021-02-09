## program to print tthe documents(syntax description)
print("-------------------------------------------------------------------------")

print(abs(5))
print(abs.__doc__)

##program to print hte calendar of given month and a year (use calendar module) well this is quite interesting :-)

import calendar

year = int(input("«««« enter the year»»»»: "))

month = int(input("«««« eneter the month»»»»»:  "))

print("------------------------------------------------------------------------")

print(calendar.month(year,month))

print("------------------------------------------------------------------------")

print(calendar.calendar(year))

print("-----------------------------------------------------------------------")

