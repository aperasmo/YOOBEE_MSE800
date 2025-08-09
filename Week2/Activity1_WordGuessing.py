import random as rnd    

# Define the word list
word_to_guess = ["yoobee", "python", "software", "development", "programming", "javascript", "coding"]
# Function to select a random word
def random_word(word_to_guess): 
    return rnd.choice(word_to_guess).upper()  # Convert to uppercase for consistency    
# Function to display the current state of the guessed word
def display_word(word, guessed_letters):
    displayed = ""
    # Go through each letter in the word
    for letter in word:
        if letter in guessed_letters:
            displayed += letter  # Show the letter if it's been guessed
        else:
            displayed += "_"    # Hide the letter if it hasn't been guessed

    return displayed
# Function to check if the word is completely guessed
def is_word_guessed(word, guessed_letters): # Check if all letters in the word have been guessed
    word = word.upper()  # Ensure the word is in uppercase
    return all(letter in guessed_letters for letter in word) #  Check if all letters in the word are in the guessed letters set
# Function to play the word guessing game
def start_game():    
    word = random_word(word_to_guess) # Select a random word from the list
    guessed_letters = set() # Use a set to store guessed letters
    attempts = 3  # Number of attempts allowed
    print("Welcome to the Word Guessing Game!")
    print("Try to guess the word. You have", attempts, "attempts.")
    
    while attempts > 0:
        print(f"\nCurrent word is {len(word.strip())} letters: {display_word(word, guessed_letters)}")# Display the current state of the word
        guess_letter = input("Enter a letter: ").upper()
        
        if len(guess_letter) != 1 or not guess_letter:  # Check if input is a single letter
            print("Please enter a single letter.")
            continue
        
        if guess_letter in guessed_letters: # Check if the letter has already been guessed      
            print("You already guessed that letter.")   
            continue
        
        guessed_letters.add(guess_letter)  # Add the guessed letter to the set
        
        if guess_letter in word: # Check if the guessed letter is in the word
            print("You macthed a letter! Good Job! 👍")
        else:
            attempts -= 1   # Reduce attempts if the guess is incorrect
            print(f"Wrong guess! ⚠️  You have {attempts} attempts left.")
    
        if is_word_guessed(word, guessed_letters):
            print("\n🎉🥳👏")
            print("Congratulations! 🏆 You've get the word correct: ", word.upper())
            print("🎉🥳👏")
            return
    
    print(f"\nGame over! The word was - {word} - better luck next time! 😢")
if __name__ == "__main__":
    try:
        start_game()
    except Exception as e:
        print("An error occurred:", e)