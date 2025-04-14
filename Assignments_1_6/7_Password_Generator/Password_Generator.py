import string
import random

def generate_password(name,digit):
    name = name
    chracters =name + string.ascii_letters +string.digits  + "!@#$%^&*"
    return name[:3] +"".join(random.choice(chracters) for i in range(digit))
name = input("Enter your name : ")
user_input =int( input("Enter the length of the password :" )
)
if user_input < 8:

    print("Password length should be at least 8 chracters.")
else:
    password = generate_password(name,user_input)
    print("Generate Password", password)
