import string
# counts the number of vowels in a word
def count_vowels():
    vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")
    vowel_total = 0
    user_choice = str(input("Write a phrase or word and the amount of vowels will be provided: "))
    for vowel in user_choice:
        if vowel in vowels:
            vowel_total += 1
    print(vowel_total)

# Palindrome checker
def check_palendrome():
    user_word = str(input("Check if your word is a palindrome: ")).lower().replace(" ", "")
    for char in string.punctuation:
        user_word = user_word.replace(char, "")
    reverse_word = user_word[::-1]
    if reverse_word == user_word:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

# Capitalize letter of first word
def capitalize_first():
    user_phrase = str(input("Enter A phrase and see each word capitalized: ")).title()
    print(user_phrase)

# Text analyzer that counts words, characters, and sentences
def text_analyzer():
    text = str(input("Please enter the text you would like analyzed: "))
    sentence_count = 0
    character_count = len(text)
    word_count = len(text.split())
    sentence_ender = ("!", "?", ".")
    for char in text:
        if char in sentence_ender:
            sentence_count += 1
    print(f"# of Sentences: {sentence_count}")
    print(f"# of Words: {word_count}")
    print(f"# of Character: {character_count}")

