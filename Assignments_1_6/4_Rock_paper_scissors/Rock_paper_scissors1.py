import random
choices = ["rock", "paper","scissors"]

while True:
    user_choice = input("Choose Rock, Paper, or Scissors :  ").lower()

    if user_choice not in choices:
        print("Invalid choice! please enter only rock, paper, or scissor! ❌")
        continue

    computer_choices = random.choice(choices)
    print(f"computer chose: {computer_choices}")

    if user_choice == computer_choices:
        print("Match Draw! 🤝 both chose the same!")

    elif (user_choice == "rock" and computer_choices == "scissors")or\
         (user_choice == "paper" and computer_choices == "rock")or\
         (user_choice == "scissors" and computer_choices == "paper"):
        print("You Win 🎉")
    else:
        print("Computer Win! 🤔")

    play_again = input("Do you want to play again : ").lower()
    if play_again != "yes":
        print("Thanks for Playing! ✋")
        break



