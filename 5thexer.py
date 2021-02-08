## program to accept the sequence of comma-separated numbers from the user and generate a list and tuple with those numbers

values = input("-----input some comma separated number-------: ")

lists = values.split(",")

print(lists)

tuple = tuple(lists)

print('List : ',lists)

print('Tuple : ',tuple)