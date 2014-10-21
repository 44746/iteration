run = True
while run == True:
    number = int(input("Please enter a number: "))
    times = int(input("How many times do you want it printed: "))
    for count in range(times):
        print(number)
    again = input("Do you want to run it again: ")
    if again == "n":
        run = False
