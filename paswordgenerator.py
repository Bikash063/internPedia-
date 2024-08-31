import secrets
import string
import pyperclip  # Ensure you have the pyperclip module installed

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    """Generate a secure random password based on user preferences."""
    if not (use_uppercase or use_lowercase or use_digits or use_symbols):
        raise ValueError("At least one character type must be selected.")
    
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    """Get user preferences for password generation."""
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return length, use_uppercase, use_lowercase, use_digits, use_symbols

def main():
    print("Secure Random Password Generator")
    print("===============================")

    while True:
        length, use_uppercase, use_lowercase, use_digits, use_symbols = get_user_preferences()

        try:
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
            print(f"\nGenerated Password: {password}")

            copy_to_clipboard = input("Copy password to clipboard? (y/n): ").lower() == 'y'
            if copy_to_clipboard:
                pyperclip.copy(password)
                print("Password copied to clipboard.")

            another = input("\nGenerate another password? (y/n): ").lower()
            if another != 'y':
                break
        except ValueError as e:
            print(f"Error: {e}")
            continue

    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()
