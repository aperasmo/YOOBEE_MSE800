import random as rnd

class WordGuessingGame:
    """A class to represent a word guessing game."""
    
    def __init__(self, word_list=None, max_attempts=3):
        """
        Initialize the word guessing game.
        
        Args:
            word_list (list): List of words to choose from
            max_attempts (int): Maximum number of incorrect attempts allowed
        """
        self.word_list = word_list or ["yoobee", "python", "software", "development", "programming", "javascript", "coding"]
        self.max_attempts = max_attempts
        self.reset_game()
    
    def reset_game(self):
        """Reset the game state for a new game."""
        self.word = self._select_random_word()
        self.guessed_letters = set()
        self.attempts_left = self.max_attempts
        self.game_over = False
        self.won = False
    
    def _select_random_word(self):
        """
        Select a random word from the word list.
        
        Returns:
            str: A random word in uppercase
        """
        return rnd.choice(self.word_list).upper()
    
    def display_current_word(self):
        """
        Display the current state of the guessed word.
        
        Returns:
            str: The word with guessed letters shown and unguessed letters as underscores
        """
        displayed = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed += letter
            else:
                displayed += "_"
        return displayed
    
    def is_word_completely_guessed(self):
        """
        Check if the word is completely guessed.
        
        Returns:
            bool: True if all letters have been guessed, False otherwise
        """
        return all(letter in self.guessed_letters for letter in self.word)
    
    def is_valid_guess(self, guess):
        """
        Validate the user's guess.
        
        Args:
            guess (str): The user's input
            
        Returns:
            tuple: (is_valid, error_message) -> stores multiple items in a single variable.
        """
        if not guess or len(guess) != 1:
            return False, "Please enter a single letter."
        
        if not guess.isalpha():
            return False, "Please enter a valid letter."
        
        if guess.upper() in self.guessed_letters:
            return False, "You already guessed that letter."
        
        return True, ""
    
    def make_guess(self, guess):
        """
        Process a letter guess.
        
        Args:
            guess (str): The guessed letter
            
        Returns:
            dict: Result of the guess with status and message
        """
        if self.game_over:
            return {"status": "game_over", "message": "Game is already over!"}
        
        guess = guess.upper()
        is_valid, error_message = self.is_valid_guess(guess)
        
        if not is_valid:
            return {"status": "invalid", "message": error_message}
        
        self.guessed_letters.add(guess)
        
        if guess in self.word:
            result = {"status": "correct", "message": "You matched a letter! Good Job! 👍"}
            
            # Check if word is completely guessed
            if self.is_word_completely_guessed():
                self.game_over = True
                self.won = True
                result["status"] = "won"
                result["message"] = f"🎉🥳👏\nCongratulations! 🏆 You've got the word correct: {self.word}\n🎉🥳👏"
        else:
            self.attempts_left -= 1
            result = {"status": "incorrect", "message": f"Wrong guess! ⚠️  You have {self.attempts_left} attempts left."}
            
            # Check if game is over
            if self.attempts_left <= 0:
                self.game_over = True
                result["status"] = "lost"
                result["message"] = f"Game over! The word was - {self.word} - better luck next time! 😢"
        
        return result
    
    def get_game_status(self):
        """
        Get the current game status.
        
        Returns:
            dict: Current game state information
        """
        return {
            "word_length": len(self.word),
            "current_display": self.display_current_word(),
            "attempts_left": self.attempts_left,
            "guessed_letters": sorted(list(self.guessed_letters)),
            "game_over": self.game_over,
            "won": self.won
        }
    
    def start_game(self):
        """Start and run the interactive word guessing game."""
        print("Welcome to the Word Guessing Game!")
        print(f"Try to guess the word. You have {self.max_attempts} attempts.")
        
        while not self.game_over:
            status = self.get_game_status()
            print(f"\nCurrent word is {status['word_length']} letters: {status['current_display']}")
            
            guess = input("Enter a letter: ")
            result = self.make_guess(guess)
            print(result["message"])
        
        # Ask if player wants to play again
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again == 'y':
            self.reset_game()
            self.start_game()
        else:
            print("Thank you for playing! Goodbye! 👋")

def main():
    """Main function to run the game."""
    try:
        game = WordGuessingGame() # Basic usage of the class
        game.start_game()   # using the start_game method to run the game interactively  
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()