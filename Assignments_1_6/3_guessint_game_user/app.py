import random
print("computer ny ek secert number socha hai 🧠 ab use guess karo! 🔢 ")
secret_number = random.randint(1, 10)
# print(secret_number)

while True:
  user_input = int(input("apna andaza lagao (1-10): "))
  
  if user_input == secret_number:
    print("congrats! 🎉 tum ny sahi guess kar liya! ✅")
    break
  elif user_input < secret_number:
    print("bara socho! ⬆")
  elif user_input > secret_number:
    print("choto number select kro! ⬇")