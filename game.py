import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (1 rock, 2 paper, 3 scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(choices)
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

def main():
    play_game()
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
        play_game()

if __name__ == "__main__":
    main()
