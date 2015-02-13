import random
guessed = False
number  = random.randint(0,101)
noOfTurns = 0
while guessed != True:
    noOfTurns = noOfTurns + 1
    userGuess = int(input('Please enter a number: '))
    if userGuess == number:
        guessed = True
    elif userGuess > number:
        print('The number you guessed was too high')
    else:
        print('The number you guessed is too low')
print('you took {0} turns to guess the number'.format(noOfTurns))
print('The number was {0}'.format(number))
