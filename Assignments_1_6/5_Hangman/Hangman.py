
import random
# Word list
word_list = ["python", "hangman", "challenge", "programming", "computer"]
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
        display += " "
    return display


def hangman():
    word = random.choice(word_list)
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("\nWelcome to Hangman!")
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Guessed Letters: {' '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")

        guess = input("Enter the letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess.")
            attempts -= 1

        
        if "_" not in display_word(word, guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")

hangman()
