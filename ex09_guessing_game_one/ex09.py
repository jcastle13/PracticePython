import os
import random

os.system('clear')
print("***********************************************")
print("# Welcome to the guess Game!!!")
print("***********************************************\n")


while 1:
    print("1.\tPlay a Game.")
    print("2.\tQuit.")
    choice = int(input("Pick your options from above: "))

    if choice == 2:
        print("Have a great day, good bye :)")
        break

    elif choice == 1:
        os.system('clear')
        print("Let's begin playing the guessing game.")
        number = random.randint(1, 9)
        num_of_guess = 0
        while 1:
            guess = int(input("Make your guess: "))
    
            if guess == number:
                print("You've selected the correct number:", number, "!!!!")
                print("It only took you", num_of_guess, "guess.")
                break
            elif guess > number:
                print("The number you guessed is to high.")
            else:
                print("The number you guessed is to low.")
            num_of_guess += 1

    else:
        break
