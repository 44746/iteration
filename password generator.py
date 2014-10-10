#George West
#10-10-14
#password generator
import random
import string
length = int(input("How long do you want your password: "))
list1 = ("")
while length > 0:
    
    choice =random.choice(string.ascii_letters + string.digits)
    list1 = list1 + choice
    length = length-1
    
print(list1)
