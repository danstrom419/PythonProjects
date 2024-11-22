import random
import time

from colorama import Fore, Style

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
            (user == "scissors" and computer == "paper") or \
            (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    print(Fore.GREEN + "Welcome to Rock, Paper, Scissors!" + Style.RESET_ALL)
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    loading_animation()

    display_choices(user_choice, computer_choice)

    countdown(3)

    #print(f"\nYou chose: {user_choice}")
    #print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

def play_again():
    retry_choice = input("Play again? (Y/N): ").lower()
    while retry_choice not in ["Y", "y", "n", "N"]:
        print("Invalid choice! Please choose Y or N")
        retry_choice = input("Play again? (Y/N): ").lower()
    return retry_choice == "y"

def loading_animation():
    print("Rock, Paper, Sicssors...")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print() # moves to the next line after loading

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Result in {i}...", end="\r")
        time.sleep(1)
    print("Result!")

def animate_choice(choice):
    print("Your choice is...")
    for char in choice:
        print(char, end="", flush=True)
        time.sleep(0.5)
    print()

def display_choices(user_choice, compuer_choice):
    print("\n" * 100)
    print(Fore.CYAN + "Your Choice: " + Style.RESET_ALL + user_choice)
    print(Fore.MAGENTA + "Computer Choice: " + Style.RESET_ALL + compuer_choice)
    time.sleep(2)

if __name__ == "__main__":
    while True:
        play_game()
        if not play_again():
            print("\nThanks for playing!")
            break








