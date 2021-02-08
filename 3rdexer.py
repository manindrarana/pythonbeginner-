### In here we do the the simple program to print the date and time


import datetime

c = datetime.datetime.now()

print("--------current date and tinme is---------")

print(c.strftime("%Y-%m-%d %H:%M:%S"))

print("------------------------------------------")



## program to accept radius of circle fro mthe user nad compute the area :

import math

pi = math.pi
print("-------------------------------------------------")
r = float(input("««««««Enter the radius»»»»: "))

print("r = "+ str(r))
Area = print(pi*r*r)
print("------------------------------------------------")

