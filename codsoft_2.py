def add(num1, num2):
    """Calculates the sum of two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Calculates the difference between two numbers."""
    return num1 - num2

def multiply(num1, num2):
    """Calculates the product of two numbers."""
    return num1 * num2

def divide(num1, num2):
    """Performs division of two numbers, handling zero as a divisor."""
    if num2 == 0:
        return "Oops! Division by zero is not allowed." # Handles division by zero
    return num1 / num2

def main():
    """Simple calculator program."""
    print("\n--- Welcome to Your Simple Calculator! ---")
    print("Choose an arithmetic operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("----------------------------------------")

    while True: # Loop to allow multiple calculations
        operation_choice = input("Enter your choice (1, 2, 3, or 4): ").strip()

        if operation_choice in ('1', '2', '3', '4'):
            try:
                first_number = float(input("Please enter the first number: "))
                second_number = float(input("Please enter the second number: "))
            except ValueError: # Catches non-numeric input
                print("Invalid input. Kindly enter numerical values for your calculations.")
                continue # Loop back to ask for choice again

            if operation_choice == '1':
                print(f"Result: {first_number} + {second_number} = {add(first_number, second_number)}")
            elif operation_choice == '2':
                print(f"Result: {first_number} - {second_number} = {subtract(first_number, second_number)}")
            elif operation_choice == '3':
                print(f"Result: {first_number} * {second_number} = {multiply(first_number, second_number)}")
            elif operation_choice == '4':
                calculation_result = divide(first_number, second_number)
                print(f"Result: {first_number} / {second_number} = {calculation_result}")
            
            # Offer to perform another calculation
            continue_calculating = input("You wants another calculation? (yes/no): ").strip().lower()
            if continue_calculating != 'yes':
                print("Thank you for using the calculator. Exiting now!")
                break # End the program
        else:
            print("That's not a valid option. Pick a number from 1 to 4.")

if __name__ == "__main__":
    main() # Runs the main calculator program
