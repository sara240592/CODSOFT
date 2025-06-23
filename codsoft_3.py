import random
import sys

def generate_password(password_length):
    """
    Generates a simple random password of a specified length
    """
    # Defines the pool of characters available for the password
    allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    # Check if the character set is empty
    if not allowed_characters:
        return "Error: No characters available for password generation."

    # Builds the password by randomly selecting characters
    new_password = ""
    for _ in range(password_length):
        new_password += random.choice(allowed_characters)
    
    return new_password

def main():
    """
    Main function to run the simple password generator application.
    Prompts for password length and displays the generated password.
    """
    print("\n--- Simple Python Password Generator ---")
    print("This tool creates basic random passwords.")
    print("--------------------------------------")

    while True:
        try:
            # Prompt user for password length
            input_length_str = input("Enter the desired password length (e.g., 8, 10, 12): ").strip()
            requested_length = int(input_length_str)

            if requested_length <= 0:
                print("Password length must be a positive number. Please enter a valid length.")
            else:
                # Generate and display the password
                generated_pwd = generate_password(requested_length)
                print(f"\nYour new simple password: {generated_pwd}")
                print("--------------------------------------")
                
                # Ask if the user wants another password
                continue_generating = input("Generate another password? (yes/no): ").strip().lower()
                if continue_generating != 'yes':
                    print("Exiting password generator. Have a great day!")
                    sys.exit() # Exit the program
        except ValueError:
            print("Invalid input. Please enter a whole number for the password length.")
        except KeyboardInterrupt:
            # Handle Ctrl+C to exit gracefully
            print("\nPassword generator interrupted. Exiting.")
            sys.exit()

if __name__ == "__main__":
    main()
