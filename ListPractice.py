# function that removes duplicates from list
def remove_duplicate():
        grocery_list = ["Apples", "Bananas", "Apples", "Grapes", "Mango", "Milk", "Ham", "Eggs"]
        grocery_list.sort()
        unique_grocery_list = list(set(grocery_list))
        unique_grocery_list.sort()
        print(unique_grocery_list)

# function that reports the smallest and largest elements
def reportsmall_large():
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(f"The largest number is: {max(numbers)}" )
        print(f"The smallest number is: {min(numbers)}")

# simple search function that searches for a specific element
def simple_search(first, target):
        # loop is saying go through each index and item in the list one by one adn see if it matches target
        for index, item in enumerate(first):
                if item == target:
                        return index
        return -1

my_numbers = [0, 1, 2, -10, 50, 60, 100, 20]
target_value = 50

result = simple_search(my_numbers, target_value)

if result != -1:
        print(f"Value {target_value} found at index {result}")
else:
        print(f"Value {target_value} not found")

# function that removes negative numbers and doubles positive ones
def math_function():
        number_list = [0, -1, -2, -4, 50, 60, 70 , 88, 95, -100, 2, 4]
        doubles_list = [x*2 for x in number_list if x >= 0]
        print(number_list)
        print(doubles_list)
math_function()



