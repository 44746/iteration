number = int(input('Please enter a number: '))
print("Times table for {0}".format(number))
counter = 0
for count in range(12):
    counter = counter +1
    answer = counter*number
    print( "{0:2} * {1:2} = {2:3}".format(counter,number,answer))
