import random

def get_random_word():
    word_list = ["about",
    "other",
    "which",
    "their",
    "there",
    "first",
    "would",
    "these",
    "click",
    "price",
    "state",
    "email",
    "world",
    "music",
    "after",
    "video",
    "where",
    "books",
    "links",
    "years",
    "order",
    "items",
    "group",
    "under",
    "games",
    "could",
    "great",
    "hotel",
    "store",
    "terms",
    "right",
    "local",
    "those",
    "using",
    "phone",
    "forum",
    "based",
    "black",
    "check",
    "index",
    "being",
    "women",
    "today",
    "south",
    "pages",
    "found",
    "house",
    "photo",
    "power",
    "while",
    "three",
    "total",
    "place",
    "think",
    "north",
    "posts",
    "media",
    "since",
    "guide",
    "board",
    "white",
    "small",
    "times",
    "sites",
    "level",
    "hours",
    "image",
    "title",
    "shall",
    "class",
    "still",
    "money",
    "every",
    "visit",
    "tools",
    "reply",
    "value",
    "press",
    "learn",
    "print",
    "stock",
    "point",
    "sales",
    "large",
    "table",
    "start",
    "model",
    "human",
    "movie",
    "march",
    "yahoo",
    "going",
    "study",
    "staff",
    "again",
    "april",
    "never",
    "users",
    "topic",
    "below"]

    word = random.sample(word_list, 1)
    return word[0]

def print_gallows(number_of_incorrect_guesses):
    if number_of_incorrect_guesses == 0:
        print("""
--------|
|       
|      
|       
|      
|
|
----------
""")

    elif number_of_incorrect_guesses == 1:
        print("""
--------|
|       O
|      
|       
|      
|
|
----------
""")

    elif number_of_incorrect_guesses == 2:
        print("""
--------|
|       O
|       |
|       |
|      
|
|
----------
""")

    elif number_of_incorrect_guesses == 3:
        print("""
--------|
|       O
|      \\|
|       |
|      
|
|
----------
""")

    elif number_of_incorrect_guesses == 4:
        print("""
--------|
|       O
|      \\|/
|       |
|      
|
|
----------
        """)

    elif number_of_incorrect_guesses == 5:
        print("""
--------|
|       O
|      \\|/
|       |
|      /
|
|
----------
        """)

    elif number_of_incorrect_guesses == 6:
        print("""
--------|
|       O
|      \\|/
|       |
|      / \\
|
|
----------
        """)

def has_person_been_hanged(number_of_incorrect_guesses):
    return number_of_incorrect_guesses == 6

def has_the_word_been_guessed(hidden_word, letters_guessed):
    for letter in hidden_word:
        if letter not in letters_guessed:
            return False
    return True

def display_hidden_word(hidden_word, letters_guessed):
    for letter in hidden_word:
        if letter in letters_guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def get_letter_guess(letters_guessed):
    print(f'You have already guessed {letters_guessed}')
    guess = input("Enter a letter")
    while len(guess) != 1 or guess in letters_guessed:
        print("invalid guess")
        guess = input("Enter a letter")
    letters_guessed.append(guess)
    return guess


play_again = 'y'
while play_again == 'y':

    letters_guessed = []
    hidden_word = get_random_word()
    number_of_incorrect_guesses = 0

    while not has_the_word_been_guessed(hidden_word, letters_guessed) \
            and not has_person_been_hanged(number_of_incorrect_guesses):
        display_hidden_word(hidden_word, letters_guessed)
        guess = get_letter_guess(letters_guessed)

        if guess not in hidden_word:
            number_of_incorrect_guesses += 1

        print_gallows(number_of_incorrect_guesses)

    print(f"the word was: {hidden_word}")

    play_again = input("Do you want to play again y/n").lower()