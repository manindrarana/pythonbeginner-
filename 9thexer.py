##program to calculate the number of days between two date
print(
    "--------------------------------------------------------------------------------------------------------"
)

from datetime import date

p_date = date(2021,1,12)

c_date = date(2021,1,29) #we can only do within a month not more than one month

adelta = c_date - p_date

print(str(adelta.days) + " days")

print("-----------------------------------------------------------------------------")

#program to get the volume of a sphere with radius 6
from math import pi

radius_sphere = float(input("««««enetr a radius»»»»»: "))

Volume_sphere = 4/3 *pi * radius_sphere**3

print("###The volume of the sphere is " + str(Volume_sphere) + " ####")

print(
      "-----------------------------------------------------------------------------------------------------")

