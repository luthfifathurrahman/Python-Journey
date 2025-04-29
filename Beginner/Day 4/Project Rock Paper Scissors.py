import random

option = ["rock", "paper", "scissors"]
computer_choice = random.choice(option)
player_choice = int(input("what do you choose? Type 0 for rock, type 1 for paper, type 2 for Scissors: "))

if player_choice < 0 or player_choice > 2:
    print("invalid input, player lose.")
else:
    player_option = option[player_choice]
    print(f"player choose: {player_option}")
    print(f"computer choose: {computer_choice}")
    if player_option == "rock" and computer_choice == "scissors":
        print("player win")
    elif player_option == "scissors" and computer_choice == "paper":
        print("player win")
    elif player_option == "paper" and computer_choice == "rock":
        print("player win")
    elif player_option == computer_choice:
        print("Draw")
    else:
        print("player lose")
