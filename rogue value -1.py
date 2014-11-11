num = 0
total = 0
count = 0
while num >= 0:
    num = int(input("Please enter a number: "))
    if num >=0:
        total = total + num
        count = count +1
average = total/count
print("You entered {0} numbers, the average of those numbers is {1}".format(count,average))


