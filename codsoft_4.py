import random
import sys

def play_round(player_score, ai_score):
    """
    Plays a single round of Rock-Paper-Scissors against the computer.
    Updates the scores and returns them.
    """
    options = ["rock", "paper", "scissors"]
    ai_choice = random.choice(options)

    print("\n--- Rock, Paper, Scissors! ---")
    print("Enter your move: rock, paper, or scissors")
    print("------------------------------")

    while True:
        player_move = input("Your move: ").strip().lower()

        if player_move in options:
            break
        else:
            print("Invalid move. Please enter 'rock', 'paper', or 'scissors'.")

    print(f"\nYou chose: {player_move.capitalize()}")
    print(f"Computer chose: {ai_choice.capitalize()}")

    # Determine the winner and update scores
    if player_move == ai_choice:
        print("It's a tie!")
    elif (player_move == "rock" and ai_choice == "scissors") or \
         (player_move == "paper" and ai_choice == "rock") or \
         (player_move == "scissors" and ai_choice == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        ai_score += 1
    
    print(f"Current Score: You {player_score} - Computer {ai_score}")
    return player_score, ai_score

def run_game():
    """
    Main function to run the Rock-Paper-Scissors game with score tracking
    and a play-again option.
    """
    player_overall_score = 0
    computer_overall_score = 0

    while True:
        # Pass the current scores to the play_round function
        player_overall_score, computer_overall_score = play_round(player_overall_score, computer_overall_score)
        
        while True: # Loop to ensure valid 'yes'/'no' input for playing again
            play_another = input("\nDo you want to play another round? (yes/no): ").strip().lower()
            if play_another == 'yes':
                break # Exit this inner loop, continue outer game loop
            elif play_another == 'no':
                print("\n--- Final Score ---")
                print(f"You: {player_overall_score}")
                print(f"Computer: {computer_overall_score}")
                print("Thanks for playing! Goodbye!")
                sys.exit() # Exit the program
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    try:
        run_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
        sys.exit()
