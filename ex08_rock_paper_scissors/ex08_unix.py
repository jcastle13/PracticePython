import os
import tty
import sys
import termios

os.system('clear')
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
        os.system('clear')
        print("Player 1 make your choice.")
        print("1.\tRock")
        print("2.\tPaper")
        print("3.\tScissor\n")
        player1 = int(input("Player 1 selection: "))
    
        os.system('clear')
        print("Player 2 make your choice.")
        print("1.\tRock")
        print("2.\tPaper")
        print("3.\tScissor\n")
        player2 = int(input("Player 2 selection: "))
    
        os.system('clear')
        # Figuring out the winner
        if player1 == 1 and player2 == 1:
            print("It is a TIE.")
            print("Press spacebar to continue")
            orig_settings = termios.tcgetattr(sys.stdin)
            tty.setraw(sys.stdin)
            x = 0
            while x != ' ': # ESC
                x=sys.stdin.read(1)[0]
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
            os.system('clear')
