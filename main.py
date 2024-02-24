import random
import string
import os
from datetime import datetime

def generate_password(length, include_capital, unique_keywords, include_special):
    characters = string.ascii_lowercase
    if include_capital:
        characters += string.ascii_uppercase
    if include_special:
        characters += string.punctuation
    if unique_keywords:
        characters = ''.join(set(characters))
    
    password = []
    for _ in range(length):
        password.append(random.choice(characters))
    
    if include_capital:
        password[random.randint(0, length-1)] = random.choice(string.ascii_uppercase)
    if include_special:
        password[random.randint(0, length-1)] = random.choice(string.punctuation)
    if not unique_keywords:
        random.shuffle(password)
    
    return ''.join(password)

def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['y', 'n']:
            return user_input
        print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the number of characters for each password: "))
    include_capital = get_yes_no_input("Include capital letters? (y/n): ") == 'y'
    include_special = get_yes_no_input("Include special characters? (y/n): ") == 'y'
    unique_keywords = get_yes_no_input("Include unique keywords? (y/n): ") == 'y'

    if include_capital == 'n' and include_special == 'n' and unique_keywords == 'n':
        print("At least one of capital letters, special characters, or unique keywords must be included.")
        return


    print("\nGenerated Passwords:")
    passwords = []
    for i in range(num_passwords):
        password = generate_password(length, include_capital, unique_keywords, include_special)
        passwords.append(password)
        print(f"[{i+1}] : {password}")

    filename = "passwords.txt"
    mode = 'a' if os.path.exists(filename) else 'w'
    with open(filename, mode) as f:
        if mode == 'w':
            f.write(datetime.now().strftime("%d/%m/%Y") + "\n")
        for i, password in enumerate(passwords):
            f.write(f"[{i+1}] : {password}\n")
    print(f"\nPasswords saved to {filename}, in this folder")

if __name__ == "__main__":
    main()
