import random

def get_player_choice():
    """Get the player's choice"""
    choice = input("Rock, paper, or scissors? ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    """Get the computer's choice"""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    """Determine the winner"""
    if player_choice == computer_choice:
        return "tie"
    elif player_choice == "rock" and computer_choice == "scissors":
        return "player"
    elif player_choice == "paper" and computer_choice == "rock":
        return "player"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "player"
    else:
        return "computer"

def play_game():
    """Play the game"""
    print("Let's play rock, paper, scissors!")
    player_score = 0
    computer_score = 0
    for round_num in range(1, 6):
        print(f"Round {round_num}:")
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {player_choice}. The computer chose {computer_choice}.")
        winner = determine_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            player_score += 1
            print("You win!")
        else:
            computer_score += 1
            print("Computer wins!")
        print(f"Score: You {player_score}, Computer {computer_score}\n")
        
if __name__ == "__main__":
    play_game()
