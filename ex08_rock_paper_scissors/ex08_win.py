import os
import msvcrt



os.system('cls')
print("***********************************************")
print("Welcome to the Rock, Paper, & Scissors Game!!!!")
print("***********************************************\n")


while 1:
    print("1.\tPlay a Game.")
    print("2.\tQuit.")
    choice = int(input("Pick your options from above: "))
    
    if choice == 2:
        print("Have a great day, good bye :)")
        break
    
    if choice == 1:
        os.system('cls')
        print("Player 1 make your choice.")
        print("1.\tRock")
        print("2.\tPaper")
        print("3.\tScissor\n")
        player1 = int(input("Player 1 selection: "))
    
        os.system('cls')
        print("Player 2 make your choice.")
        print("1.\tRock")
        print("2.\tPaper")
        print("3.\tScissor\n")
        player2 = int(input("Player 2 selection: "))
    
        os.system('cls')
        # Figuring out the winner
        if player1 == 1 and player2 == 1:
            print("It is a TIE.")
            print("Press spacebar to continue")
            num = 0
            done = False
            while not done:
                if msvcrt.kbhit():
                    #temp = msvcrt.getch()
                    temp = msvcrt.getch().decode('utf-8')
                    if str(temp) == ' ':
                        print("You pressed",temp,"so now I will quit")
                        done = True
                        exit()
            os.system('cls')
