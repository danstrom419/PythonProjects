import random
import string

#sets the number of characters as an integer instead of string
length = int(input("# of characters must be greater than 8: "))

#requirements
while length < 8:
    print("Your password must include more than 8 characters")
    length = int(input("# of characters must be greater than 8: "))

#this creates a place for us to store our lists later on
character_options = ""

#prints options for people to choose
print('''Please select which characters you want:
          1. Letters
          2. Special
          3. Digits
          4. Exit''')

#user will choose their characters and the loop will conitnue until 4 is chosen
while True:
    player_choice = int(input("Choose characters: "))
    if player_choice == int("1"):
        character_options += string.ascii_letters
    elif player_choice == int("2"):
        character_options += string.punctuation
    elif player_choice == int("3"):
        character_options += string.digits
    elif player_choice == int("4"):
        break

#creates an list for us to store the characters in
password = []

#for each character we want in a password choose a random character from our chosen options
for i in range(length):
    random_character = random.choice(character_options)
    password.append(random_character)

#prints password
if __name__ == "__main__":
    print("\nYour password is " + "".join(password))





