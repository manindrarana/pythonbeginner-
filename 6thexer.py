## program to accept the filename from the user nad print the extension of that

print("---------------------------------------------------------------")

name_file = input("----inout the filename----: ")

file_extension = name_file.split(".") #its means it splits from the .

print("The extension of the file is : " +repr(file_extension[-1])) #if you put -2 then it will print the filename not extension

#and repr is a python predifined ones that returns the string that holds a printable representation of an object


print("----------------------------------------------------------------")