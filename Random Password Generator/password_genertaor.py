import random
import string
import pyperclip

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type must be selected.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def psw_len_strong(password):
    
    return len(password) >= 5  

def main():
    try:
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password and psw_len_strong(password):
            print(f"Generated Password: {password}")
            pyperclip.copy(password)
            print("Password copied to clipboard.")
        else:
            print("Password generation failed. Please ensure password strength must be greater then 5.")

    except ValueError:
        print("Error: Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
