import random

while True:
    user_action = input("Enter a choice (rock, paper or scissors):")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, The computer chose {computer_action}.\n")

    if user_action == computer_action:
        print (f"Both chose {user_action}, tie!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes Scissors, You won!")
        else:
            print("Paper covers Rock, You lost...")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers Rock, You won!")
        else:
            print ("Scissors cut paper, You lost...")
    elif user_action == "scissors":
        if computer_action == "paper":
            print ("Scissors cut Paper, You win!")
        else:
            print ("Rock smashes Scissors, You lost...")