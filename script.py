# Password Checker

from pathlib import Path

score = 0
lowercase_flag = False
uppercase_flag = False
digit_flag = False
special_character_flag = False
common_passwords = []
prev_char = None
consecutive_character_flag = False
consecutive_character_counter = 0

file_path = Path(__file__).resolve().parent / "common_passwords.txt"

try:
    with file_path.open("r", encoding="utf-8") as file:
        common_passwords = {line.rstrip("\r\n").lower() for line in file}
except FileNotFoundError:
    print(f"The file is missing: {file_path}")
    common_passwords = set()

password = input("What is the password that you would like to check?: ")

if len(password) >= 8: 
    score += 1

for char in password:
    if char == prev_char:
        consecutive_character_counter += 1
    else:
        consecutive_character_counter = 1
    if consecutive_character_counter == 3:
        consecutive_character_flag = True
    if char.islower():
        lowercase_flag = True
    if char.isupper():
        uppercase_flag = True
    if char.isdigit():
        digit_flag = True
    if not char.isalnum() and not char.isspace():
        special_character_flag = True
    prev_char = char

if lowercase_flag:
    score += 1

if uppercase_flag:
    score += 1

if digit_flag:
    score += 1

if special_character_flag:
    score += 1

if score <= 1:
    rating = "Very Weak"
elif score == 2:
    rating = "Weak"
elif score == 3:
    rating = "Moderate"
elif score == 4:
    rating = "Strong"
elif score == 5:
    rating = "Very Strong"

print(f"Password Score: {score}/5")
print(f"Password Rating: {rating}")

print()

if not lowercase_flag:
    print("Add a lowercase letter.")

if not uppercase_flag:
    print("Add an uppercase letter.")

if not digit_flag:
    print("Add a number.")

if not special_character_flag:
    print("Add a special character.")

if len(password) < 8:
    print("Make the password 8 characters or more.")

if password.lower() in common_passwords:
    print("Warning! Password is too generic.")

if consecutive_character_flag:
    print("Warning! Three or more identical characters in a row.")