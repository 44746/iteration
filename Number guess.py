#George West
import random
guess = int(input("Please enter your guess: "))
num= random.randint(1,100)32
while guess != num:
        if guess > num:
            print("Too high")
        elif guess < num:
            print("Too low")
        guess = int(input("Please enter your guess: "))
print("spot on")
