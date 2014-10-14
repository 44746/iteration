#George West
#14-10-14
#stars
number = int(input("How many stars do you want per row? "))
rows = int(input("How many rows do you want? "))
list1=''
for count in range(number):
    list1= list1 + '*'
for count in range(rows):
           print(list1)
