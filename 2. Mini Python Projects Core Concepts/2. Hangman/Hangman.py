# Hangman game created by Sheikh Nafis. Try to save the innocent man by guessing the word before time runs out! 

import random

words_list = [
    # Countries
    "Brazil", "Canada", "Mexico", "Greece", "Sweden", "Turkey", "France", "Russia", "Taiwan", "Austria",
    
    # Fruits
    "Orange", "Banana", "Papaya", "Durian", "Tomato", "Lychees", "Coconut", "Plumcot", "Mangoes", "Jackfruit",
    
    # Foods
    "Burger", "Noodles", "Cereals", "Samosas", "Lasagna", "Crumpet", "Risotto", "Bagel", "Omelets", "Tortilla",
    
    # Animals
    "Giraffe", "Dolphin", "Rabbit", "Leopard", "Ostrich", "Beetles", "Cricket", "Buffalo", "Penguin", "Wombats",
    
    # Sports
    "Soccer", "Tennis", "Cricket", "Bowling", "Cycling", "Boxing", "Wrestle", "Running", "Hockey", "Rowboat",
    
    # Vehicles
    "Bicycle", "Scooter", "Airship", "Tramcar", "Subway", "Shuttle", "Freight", "Skate", "Trolley", "Cabinet",
    
    # Musical Instruments
    "Guitar", "Violin", "Drumset", "Flutes", "Trumpet", "Bagpipe", "Clarion", "Keybord", "Cellist", "Saxhorn",
    
    # Flowers
    "Dahlia", "Tulips", "Orchid", "Lobelia", "Daisies", "Marigold", "Primula", "Hyacinth", "Lilac", "Peonies",
    
    # Occupations
    "Teacher", "Engineer", "Plumber", "Nursing", "Artists", "Farmers", "Doctors", "Writers", "Soldier", "Sailors",
    
    # Elements
    "Oxygen", "Nitrogen", "Sulphur", "Calcium", "Carbon", "Silicon", "Helium", "Lithium", "Phosph", "Iron"
]

# Get the total number of items in the list of words
total_words_count = len(words_list)

# Choose a random index within the list's range
random_index = random.randint(0, total_words_count - 1)

# Select a random word from the list using the random index
selected_word = words_list[random_index]

# Get the length of the randomly selected word
selected_word_length = len(selected_word)
# print("Randomly chosen word:", selected_word)

hidden_word = "_" * selected_word_length
# Convert the hidden word into a list for easy letter replacement
hidden_word_list = list(hidden_word)

# Convert the selected word into a list of characters
selected_word_list = list(selected_word.lower())

# Raw strings (using the 'r' prefix) are used to avoid issues with escape sequences.
hangman = [r"""
 ____  
|/   | 
|   (_)
|    
|    
|    
|
|_____
""",
r"""
 ____  
|/   | 
|   (_)
|    | 
|    |    
|    
|
|_____
""",
r"""
 ____  
|/   | 
|   (_)
|   \| 
|    | 
|    
|
|_____
""",
r"""
 ____  
|/   | 
|   (_)
|   \|/
|    | 
|    
|
|_____
""",
r"""
 ____  
|/   | 
|   (_)
|   \|/
|    | 
|   / 
|
|_____
""",
r"""
 ____  
|/   | 
|   (_)
|   \|/
|    | 
|   / \
|
|_____
""",
r"""
 ____  
|/   | 
|   (_)
|   /|\
|    | 
|   | |
|
|_____
"""]

hangman_title = """
888                                                           
888                                                           
888                                                           
88888b.  8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888 "88b    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888  888.d888888888  888888  888888  888  888.d888888888  888 
888  888888  888888  888Y88b 888888  888  888888  888888  888 
888  888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                             888                              
                        Y8b d88P                              
                         "Y88P"       
"""

print(hangman_title)
print("In Hangman, you guess letters to figure out a hidden word. For every wrong guess, a part of a stick figure is drawn—guess the word before the man gets hanged!\n")

# Set the number of lives the player has
lives_remaining = 7
new_guessed_letters = set()
# Start the game loop
while lives_remaining > 0:
    # Prompt the player to guess a letter
    guessed_letter = input("Please guess a letter to save the innocent man\nYour guess: ").lower()
    print("\n")

    # Check if the letter has already been guessed
    if guessed_letter in new_guessed_letters:
        print(f"You've already guessed '{guessed_letter}'. Try a different letter.\n")
        print("Current progress:", "".join(hidden_word_list)) # hidden_word_list = ['_', '_', 'e', '_', 'l'] so the output will be __e_l
        continue # Skip the rest code and start over again

    # Add the guessed letter to the set of guessed letters
    new_guessed_letters.add(guessed_letter)

    # Check if the guessed letter is in the selected word
    if guessed_letter in selected_word_list:
        # Loop through each character in the selected word to find matches
        for index, letter in enumerate(selected_word_list): # 2, e = e
            if letter == guessed_letter:
                # Replace the corresponding underscore with the correct letter
                hidden_word_list[index] = guessed_letter
        
        print(f"Good guess! The letter '{guessed_letter}' is in the word.")
        # "".join() takes the list and joins them together using the empty string "" as a separator
        print("Current progress:", "".join(hidden_word_list)) # hidden_word_list = ['_', '_', 'e', '_', 'l'] so the output will be __e_l

        # Check if the player has guessed the entire word
        if '_' not in hidden_word_list:
            print("Congratulations! You've saved the innocent man!")
            break
    else:
        # The guessed letter is incorrect, so the player loses a life
        print(f"Wrong guess! The letter '{guessed_letter}' is not in the word.")
        lives_remaining -= 1

        if lives_remaining > 0:
            print(hangman[7 - lives_remaining - 1])
            print(f"Lives remaining: {lives_remaining}")
            # "".join() takes the list and joins them together using the empty string "" as a separator
            print("Current progress:", "".join(hidden_word_list)) # hidden_word_list = ['_', '_', 'e', '_', 'l'] so the output will be __e_l
        else:
            print(hangman[6])
            print("Game over! You couldn’t save the innocent man this time—better luck next time!")
            print("The hidden word is:", selected_word)
            break