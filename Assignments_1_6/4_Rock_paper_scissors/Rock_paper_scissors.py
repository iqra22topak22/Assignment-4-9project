import random

# Function to get the player's choice
def get_player_choice():
    choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please try again.")
        choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    return choice

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Running the game
if __name__ == "__main__":
    play_game()
