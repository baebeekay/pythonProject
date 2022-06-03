# Rock Paper Scissors Game
# importing the random module
import random

# list to hold options for rock, paper and scissors
options = ["R", "P", "S"]
# take input from user
player = input("Choose [R for rock], [P for Paper], [S for Scissors]: ")
# check is no input was given
while True:
    if player not in options:
        player = input("Please choose [R, P or S]: ")
    else:
        break
CPU = random.choice(options)
print(f"player  {[player]} : CPU {[CPU]}")
if player == CPU:
    # If it's a tie (the computer and player pick the same move), restart the game from step 3
    print(f"Both players selected {player}. It's a tie!")
    # take input from user
    player = input("Choose [R for rock], [P for Paper], [S for Scissors]: ")
    # check is no input was given
    while True:
        if player not in options:
            player = input("Please choose [R, P or S]: ")
        else:
            break
    CPU = random.choice(options)
    print(f"player  {[player]} : CPU {[CPU]}")
    if player == CPU:
        print(f"Both players selected {player}. It's a tie!")
        # take input from user
        player = input("Choose [R for rock], [P for Paper], [S for Scissors]: ")
        # check is no input was given
        while True:
            if player not in options:
                player = input("Please choose [R, P or S]: ")
            else:
                break
        CPU = random.choice(options)
        print(f"player  {[player]} : CPU {[CPU]}")
    elif player == "R":
        if CPU == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player == "P":
        if CPU == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player == "S":
        if CPU == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
elif player == "R":
        if CPU == "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
elif player == "P":
        if CPU == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
elif player == "S":
        if CPU == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")



