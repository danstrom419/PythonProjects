# Calculator
def menu():
    while True:
        try:
            user_choice = int(input("\nThis is a simple calculator:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Quit\nEnter Choice Here: "))
            if user_choice == 1:
                num_choice1 = int(input("Please enter the first number you would like to add: "))
                num_choice2 = int(input("Please enter the second number you would like to add: "))
                print(f"\nYour answer is {(num_choice1 + num_choice2)}")
            elif user_choice == 2:
                num_choice1 = int(input("Please enter the first number you would like to subtract: "))
                num_choice2 = int(input("Please enter the second number you would like to subtract: "))
                print(f"\nYour answer is {(num_choice1 - num_choice2)}")
            elif user_choice == 3:
                num_choice1 = int(input("Please enter the first number you would like to multiply: "))
                num_choice2 = int(input("Please enter the second number you would like to multiply: "))
                print(f"\nYour answer is {(num_choice1 * num_choice2)}")
            elif user_choice == 4:
                num_choice1 = int(input("Please enter the first number you would like to divide: "))
                num_choice2 = int(input("Please enter the second number you would like to divide: "))
                while num_choice2 == 0:
                    num_choice2 = int(input("Cannot divide by 0 please input another number: "))
                print(f"\nYour answer is {(num_choice1 / num_choice2)}")
            elif user_choice == 5:
                break
            else:
                print("Invalid input. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
menu()

