#George West
#17-10-14
#n factorial
number=int(input("Please enter a number: "))
total = 1
while number !=0:
    total = total*number
    number = number-1   
print("The total is {0}".format(total))
