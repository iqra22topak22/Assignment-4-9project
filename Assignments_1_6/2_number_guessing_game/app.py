
import random

print("Socho ek secret number 1 sy 100 ke beech 😏")
user_input = int(input("Apna secret number likho (computer isko guess kry ga): "))

low = 1
high = 100
computer_number = random.randint(low, high)

while True:
    print(f"Computer ka guess: {computer_number}")
    feedback = input("Kya yah guess sahi hai? (bara/chota/sahi): ").lower()

    if feedback == "sahi":
        print("Yay! 🎉 Computer ne sahi guess kr liya! ✅")
        break
    elif feedback == "chota":
        low = computer_number + 1
    elif feedback == "bara":
        high = computer_number - 1
    else:
        print("Galat input! Sirf 'bara', 'chota', ya 'sahi' likho.")
        continue

   
    if low > high:
        print("Hmm... Lagta hai aap feedback mein kuch galti kar rahe ho 😅")
        break

    computer_number = random.randint(low, high)
