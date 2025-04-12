import random

choices = ["rock","paper","scissors"]

player_choice = input("enter rock paper and scissrs").lower()

computer_choice = random.choice(choices)
if player_choice==computer_choice:
    print(f"dono ka chooice {player_choice} the its a tie! ")
elif player_choice == "rock" and computer_choice == "scissors":
    print(f"player win {player_choice} baets {computer_choice}")
elif player_choice == "paper" and computer_choice == "rock":
        print(f"player win {player_choice} baets {computer_choice}")
elif player_choice == "scissors" and computer_choice == "paper":
        print(f"player win {player_choice} baets {computer_choice}")

else:
              print(f"computer win {computer_choice} baets {player_choice}")

     

