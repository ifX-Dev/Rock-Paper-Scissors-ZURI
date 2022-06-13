import random
from tkinter import Y

while True:
    player_option = input("Enter a choice (R, P, S): ")
    options = ["R", "P", "S"]
    CPU_option = random.choice(options)


    if player_option not in options:
        print(f"\nInvalid Input, Try again...\n")
        continue
    else:
        print(f"\nPlayer {player_option}, CPU {CPU_option}.\n")
    

    if player_option == CPU_option:
        print(f"It's a tie. Try again...\n")
        continue
    elif player_option == "R":
        if CPU_option == "S":
            print("Rock beats scissors! Player wins!")
        else:
            print("Paper beats rock! CPU wins!")
    elif player_option == "P":
        if CPU_option == "R":
            print("Paper beats rock! Player wins!")
        else:
            print("Scissors beats paper! CPU wins!")
    elif player_option == "S":
        if CPU_option == "P":
            print("Scissors beats paper! Player wins!")
        else:
            print("Rock beats scissors! CPU wins!")


    again = input("Play again? (y/n): ")

    if again != "y":
        break