## i started doing practices to build an algorith and good knowledge development in python syntax

# start with the small :)

#lets BeGIN!!!!

print("--------------------------------------------------------")
num = int (input( "««««ENTER THE NUMBER»»»»»»: "))

check = int (input("«««««ENTER THE NUMBER TO BE DIVIDED BY»»»»: "))

if num % 4 == 0:
    print(num,"is a multiple of 4") #if the number mod 4 equals to zero

if num % 2 ==0:
    print(num,"is an even number ")

else:
    print(num,"is an odd number")

if num % check == 0:
    print(num,"divides evenly by",check)

else:
    print(num,"doesn't divide evenly by",check)

print("-------------------------------------------------------")