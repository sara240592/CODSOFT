import random
import sys

def play_game(user_score, computer_score):
    """
    This function will play a single round of Rock-Paper-Scissors against the computer.
    Updates the scores and returns them.
    """
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("\n--- Rock, Paper, Scissors! ---")
    print("Enter your choice: rock, paper, or scissors")
    print("------------------------------")

    while True:
        user_choice = input("Your choice: ").strip().lower()

        if user_choice in choices:
            break
        else:
            print("Wrong choice. Please enter 'rock', 'paper', or 'scissors'.")

    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    # Determine the winner and update scores
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("Congrats you win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    
    print(f"Current Score: You {user_score} - Computer {computer_score}")
    return user_score, computer_score

def main():
    """
    This is a main function to run the Rock-Paper-Scissors game with score tracking
    and a play-again option.
    """
    user_total_score = 0
    computer_total_score = 0

    while True:
        # Pass the current scores to the play_game function
        user_total_score, computer_total_score = play_game(user_total_score, computer_total_score)
        
        while True: # Loop to ensure valid 'yes'/'no' input for playing again
            play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
            if play_again == 'yes':
                break # Exit this inner loop, continue outer game loop
            elif play_again == 'no':
                print("\n--- Final Score ---")
                print(f"You: {user_total_score}")
                print(f"Computer: {computer_total_score}")
                print("Thanks for playing! Goodbye!")
                sys.exit() # Exit the program
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
        sys.exit()
