""" #### hello i am new at python i really like to push to github and gitlab even it is small little knowledge :)
      !!!!!LEts LEArn"""

#character_name = "john"

#character_age = "36"

#""" printing the character nad name with + one """

#print("the character name is "+character_name)
#print("the character name age is "+character_age)

#print("Hakuna\"MatATaTa")

#phrase = "Hakuna maaTaTa"
#print(phrase + " is cool")

#print("manindra is cool \t\t\t\t\t manindra")

#"""so lets talk about some predefined functions """
#""" if you want to print in all the string to uppercase  """
#print(phrase.upper())

#"""  if you want to print all in lowercase"""
#print(phrase.lower())

#""" if you want check if the given variable is upper or not ????"""
#print(phrase.isupper())

#""" if ypu want to check if the given string is lower or not????"""
#print(phrase.upper().isupper())

#""" if you want to check the length of the string"""
#print(len(phrase))

""" if you want to print the following index from the string  """
#print(phrase[0])

""" if you want to get index of something """
#print(phrase.index("u"))

""" if you want to replace the string with something """
#print(phrase.replace("Hakuna","hekuna"))


#""" working with the numbers easy in python rather than c """
print(2)
print(0.55)
print(54654.001)
print(-222)
print(3+15.5)

#""" with division"""
print(8/8)

#"""multiply"""
print(8*8)

#"""with paranthesis"""
print(8*(4+5))

#""" without paranthesis"""
print(8*4+5)

#""" remainder giver"""
print(10%3)

#"""create variable"""
my_num = 5
print(my_num)

#"""to convert num to string"""
print(str(my_num)+ " is my favourite number ")

#"""to get absolute value of the number """
my_secnum = -5
print(abs(my_secnum))

#""" power function exponent one """
print(pow(my_num,2))

#"""another one call as max (it returns the higher number )"""
print(max(44,24))

#"""as well as max it also have min function"""
#print(min(44,24))

#"""function call as round which roundabouts the value (you can see the difference ::: ) """
#print(round(33.4))
#print(round(33.7))

#"""you can also import the external code """
#from math import *
#newnum = 55

#"""floor function chops the lowest number or can be saidit removes decimal pont"""
#print(floor(3.7))

#"""ceil functions just does opposite as floor"""
#print(ceil(33.4))

#""""sqrt return the sqrt of the number  """
#print(sqrt(36))



#"""getting input from the user """

""""

name = input("«««««enter you name please»»»»»»: ")

age = input("«««««enter your age»»»»»: ")

print("hello "+ name + "!!!" + "and you are " + age)

"""

#""" remember whatever you make user input always it is in strings so you have to convert the string to int or float you want"""

""" n_num = input("enter a number please: ")

n1_num = input("enter another number : ")

result = float(n_num) + float(n1_num)

print(result) """



#"""mad libs game """


""""
color = input("enter you favourite color: ")

plural_noun = input("enter any plural noun: ")

fav_person = input("enter any name you like: ")

print("««««ROSES ARE "+ color)

print(plural_noun + " is blue")

print("««««i love " + fav_person)

"""

#Working with list (can be called as structure)

enemies = [ "mike" , "mcaaren" , "starboy" , "hakata" , "bishop" ]

print(enemies)

# enemies index [0]

print(enemies[0])

#enemies print from index [-1]

print(enemies[-1])

#enemies print form index 2 to 3

print(enemies[1:3])  #to three but prints only upto two

#change the list names

enemies[1] = "jake"

print(enemies)

## so lets talk about list function

favnumbers = [4,5,6,7,8,9,1,0]

#so what about the extend function

enemies.extend(favnumbers)

print(enemies)

#we can also append the individual data on it like :

enemies.append("manindra")

print(enemies)

#so we can also use isnert func to insert the data in th middle of indexes like

enemies.insert(1,"manindra")

print(enemies)

#we can also remove enemies

enemies.remove("jake")

print(enemies)

#we can aslo use the clear fun to remove like

# enemies.clear()


##we also have pop func what it does is that it pops out the last element of the list

enemies.pop()

print(enemies)

#so we can also check if the typed name is on the list

print(enemies.index("mike"))

#so we can also count the index where it lies

print(enemies.count("manindra"))

#we can also use sort fun to sort the list in ascending order

newlists = ["a","e","f","h","i","t","y","u","z","x"]

newlists.sort()

print(newlists)

#we can also sort the numbers like

print(favnumbers)

favnumbers.sort()

print(favnumbers)

#we can also use the reverse function to make from bottom to top or from last to first like

favnumbers.reverse()

print(favnumbers)

#there's also one thing we can copy the list from one lsit ot another

#so make a new list of one and copy it to another like

enemiesreal = enemies.copy()

print(enemiesreal)

## Tuples lets start

#tuple start with () small bracket whre as list start with []

#tuples cannot be changed or modified like

varia = (5,6)

print(varia[0])

print(varia[1])

#tuple can be created as list of tuples like

coord = [(5,6,) , (7,8) , (9,10)]

## So function started !!!

#to use funstion use def keyword

#so one more thing in python that yo see the line gap in code say_Hi and code wtitten after

#it should be done or it automatically does by the ide


def say_Hi(name,age) :
    print("hello!! " + name + ",you are " + age )

say_Hi("manindra","19")
say_Hi("motto","100")

##the same way we can also use like

def say_hello(name,age) :
    print("««HI»»» " + name + ", you are "+ str(age) ) #if you dont want to use double quote in number use string in here

say_hello("manindra",19)

say_hello("motto",100)



