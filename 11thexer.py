##program to test weather a number is within 100 of 1000 or 2000
print("------------------------------------------------------------")
def near_thousand (n):
    return ((abs(1000-n) <= 100 or (abs(2000-n) <= 100)))
print(near_thousand(1000))
print(near_thousand(2000))
print(near_thousand(500))

print("-------------------------------------------------------------")


##program to calcuate the sum of three given numbers if the value is equals then return three times of their sum

print("------------------------------")
def sum_thrice(x,y,z):
    sum = x + y + z

    if x == y == z:
        sum = sum * 3
    return sum

print(sum_thrice(1,2,3))
print(sum_thrice(3,3,3))

print("------------------------------")