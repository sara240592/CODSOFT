def add(x, y):
    """Calculates the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Calculates the difference between two numbers."""
    return x - y

def multiply(x, y):
    """Calculates the product of two numbers."""
    return x * y

def divide(x, y):
    """Performs division of two numbers, handling zero as a divisor."""
    if y == 0:
        return "Oops! Division by zero is not allowed."
    return x / y

def main():
    """Simple calculator program."""
    print("\n--- Welcome to Your Simple Calculator! ---")
    print("Choose an arithmetic operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("----------------------------------------")

    while True:
        operation_choice = input("Enter your choice (1, 2, 3, or 4): ").strip()

        if operation_choice in ('1', '2', '3', '4'):
            try:
                first_number = float(input("Please enter the first number: "))
                second_number = float(input("Please enter the second number: "))
            except ValueError:
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
            continue_calculating = input("Would you like to do another calculation? (yes/no): ").strip().lower()
            if continue_calculating != 'yes':
                print("Thank you for using the calculator. Exiting now!")
                break # End the program
        else:
            print("That's not a valid option. Please pick a number from 1 to 4.")

if __name__ == "__main__":
    main()
