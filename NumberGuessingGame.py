import random

def start_game():
    while True:
        start = input("\nWanna play the Number Guessing Game? (Y/N): ").upper()
        if start == "Y":
            guesses = 0
            computer_number = random.randint(0, 1000)
            while True:
                try:
                    player_choice = int(input("\nPlease input a number between 0 and 1,000: "))
                    guesses += 1
                    if player_choice > computer_number:
                        print("Guess is to high try again.")
                    elif player_choice < computer_number:
                        print("Guess is to low try again.")
                    elif player_choice == computer_number:
                        print(f"You win congratulations, it took you {guesses} guesses!")
                        break
                except ValueError:
                    print("Invalid input please enter a number.")
        elif start == "N":
            print("You have quit")
            break
        else:
            print("Please enter a valid input.")

start_game()