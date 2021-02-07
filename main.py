""" #### hello i am new at python i really like to push to github and gitlab even it is small little knowledge :)
      !!!!!LEts LEArn"""

character_name = "john"

character_age = "36"

""" printing the character nad name with + one """

print("the character name is "+character_name)
print("the character name age is "+character_age)

print("Hakuna\"MatATaTa")

phrase = "Hakuna maaTaTa"
print(phrase + " is cool")

print("manindra is cool \t\t\t\t\t manindra")

"""so lets talk about some predefined functions """
""" if you want to print in all the string to uppercase  """
print(phrase.upper())

"""  if you want to print all in lowercase"""
print(phrase.lower())

""" if you want check if the given variable is upper or not ????"""
print(phrase.isupper())

""" if ypu want to check if the given string is lower or not????"""
print(phrase.upper().isupper())

""" if you want to check the length of the string"""
print(len(phrase))

""" if you want to print the following index from the string  """
print(phrase[0])

""" if you want to get index of something """
print(phrase.index("u"))

""" if you want to replace the string with something """
print(phrase.replace("Hakuna","hekuna"))

""" working with the numbers easy in python rather than c """
print(2)
print(0.55)
print(54654.001)
print(-222)
print(3+15.5)

""" with division"""
print(8/8)

"""multiply"""
print(8*8)

"""with paranthesis"""
print(8*(4+5))

""" without paranthesis"""
print(8*4+5)

""" remainder giver"""
print(10%3)

"""create variable"""
my_num = 5
print(my_num)

"""to convert num to string"""
print(str(my_num)+ " is my favourite number ")

"""to get absolute value of the number """
my_secnum = -5
print(abs(my_secnum))

""" power function exponent one """
print(pow(my_num,2))

"""another one call as max (it returns the higher number )"""
print(max(44,24))

"""as well as max it also have min function"""
print(min(44,24))

"""function call as round which roundabouts the value (you can see the difference ::: ) """
print(round(33.4))
print(round(33.7))

"""you can also import the external code """
from math import *
newnum = 55

"""floor function chops the lowest number or can be saidit removes decimal pont"""
print(floor(3.7))

"""ceil functions just does opposite as floor"""
print(ceil(33.4))

"""sqrt return the sqrt of the number  """
print(sqrt(36))

"""getting input from the user """
name = input("«««««enter you name please»»»»»»: ")
age = input("«««««enter your age»»»»»: ")
print("hello "+ name + "!!!" + "and you are " + age)
