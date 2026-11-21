import random

user_wins = 0
computer_wins = 0

while user_wins < 3 and computer_wins < 3:
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices).lower()
    print(f"User chooses {user_choice} " + f"Computer chooses {computer_choice}")

    if user_choice == "paper" and computer_choice == "rock" or user_choice == "rock" and computer_choice == "scissors" or user_choice == "scissors" and computer_choice == "paper":
        winner = "Player"

    elif user_choice == computer_choice:
        winner = "Tie"
        
    else:
        winner = "Computer"

    if winner == "Player":
        user_wins += 1
        print("Player Wins")
    elif winner == "Computer":
        computer_wins += 1
        print("Computer Wins")
    else:
        print("Tied")


if user_wins > computer_wins:
    print("Player wins the game!")
else:
    print("Computer Wins the game")


