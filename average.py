times = int(input("How many numbers do you want to be averaged: "))
total = 0
for count in range(times):
    num = int(input("Please enter a number: "))
    total = total + num
average = total/times
print("The average is {0}".format(average))
