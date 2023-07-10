import random

computer_choices = ["rock","paper", "scissors"]

game_round = 0

def game( user_action , computer_action):
    if user_action == computer_action:
        print(f"Both players doth select {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Stone smithers dagger! Thou claims victory!")
        else:
            print("Parchment covers stone! Wallow in despair.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! Thou claims victory!")
        else:
            print("Dagger cuts parchment! Wallow in despair.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Dagger cuts parchment! Thou claims victory!")
        else:
            print("Stone smithers dagger! Wallow in despair.")

user = input("What thou pickest? :")


while game_round < 3:
    game(user.lower(),random.choice(computer_choices))
    game_round += 1
    break



