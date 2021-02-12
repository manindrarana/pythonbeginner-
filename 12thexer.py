##program to get a new string from a given string where "ls" has been addded to the front .,if the given string is already
#begins  with "ls" then return the string unchanged


print(" - - - - - - - - - - - - - - - - - - - - -- - - - - - - - - - - -")

def new_string (str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    else:
        return  "likes" + str

print("manindra")
print(new_string("anu"))


##program to find weather a given number is odd or even and print an approprite mesage to the user

def is_oddoreven (n):
     mod = n % 2
     if mod > 0:
         print("it's an odd ")
     else:
         print("it's an even")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
number = int(input("enter the number : "))

print(is_oddoreven(number))

print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -s")