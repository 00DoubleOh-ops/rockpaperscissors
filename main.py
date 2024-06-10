import random

user_choice = (input("Please choose either rock, paper, or scissors: \n"))

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou Chose: {user_choice} and the computer chose {computer_action}.\n")

if user_choice == computer_action:
    print("It's a draw!")
elif user_choice == "rock":
    if computer_action == "scissors":
        print("Rock OBLITERATES scissors! You win!")
    else:
        print("Paper covers rock... Too bad!")
elif user_choice == "scissors":
    if computer_action == "paper":
        print("Paper gets cut up by scissors. You win!")
    else:
        print("Scissors get OBLITERATED by rock... Too bad!")
elif user_choice == "paper":
    if computer_action == "rock":
        print("Paper covers rock. You win!")
    else:
        print("Paper gets cut up by scissors... Too bad!")
else:
    print("You lose because you're are stupid")
