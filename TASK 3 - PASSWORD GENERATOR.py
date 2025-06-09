import random
import sys

def generate_password(length):
    """
    Generates a simple random password of a specified length
    """
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    # Check if the character set is empty
    if not characters:
        return "Error: No characters available for password generation."

    generated_password = ""
    for _ in range(length):
        generated_password += random.choice(characters)
    
    return generated_password

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
            desired_length_str = input("Enter the desired password length (e.g., 8, 10, 12): ").strip()
            desired_length = int(desired_length_str)

            if desired_length <= 0:
                print("Password length must be a positive number. Please enter a valid length.")
            else:
                # Generate and display the password
                password = generate_password(desired_length)
                print(f"\nYour new simple password: {password}")
                print("--------------------------------------")
                
                # Ask if the user wants another password
                another_password = input("Generate another password? (yes/no): ").strip().lower()
                if another_password != 'yes':
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
