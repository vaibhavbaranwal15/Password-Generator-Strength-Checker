import random
import string

# Random to generate a password 
def generate_strong_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password = password + random.choice(characters)

    return password

# Random generated password to check password strength
def check_the_generated_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if any(char.isupper() for char in password):
        strength += 1

    if any(char.islower() for char in password):
        strength += 1

    if any(char.isdigit() for char in password):
        strength += 1

    if any(char in string.punctuation for char in password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength <= 4:
        return "Medium"
    else:
        return "Strong"


# Main Program
length = int(input("Enter the length of password = "))

password = generate_strong_password(length)

print("\nGenerate Password:", password)
print("Password Strength:", check_the_generated_password_strength(password))