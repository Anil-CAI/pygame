import random

def get_user_choice():
    print("\nChoose Rock, Paper, or Scissors")
    choice = input("Your choice: ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        choice = input("Your choice: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"\nComputer chose: {computer}")
        print(determine_winner(user, computer))

        again = input("\nPlay again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

play_game()
