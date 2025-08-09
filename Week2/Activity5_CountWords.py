class StringManipulator():
    def __init__(self, input_string):
        self.input_string = input_string
    
    def find_character(self,char):
        return  self.input_string.find(char)
        
    def get_length(self):
        return len(self.input_string)

    def to_uppercase(self):
        return self.input_string.upper()

    def to_lowercase(input_string):
        return input_string.lower()
    
    def count_words(self):
        """
        Count the number of words in the input string.
        
        Returns:
            int: The number of words in the input string
        """
        return len(self.input_string.split())

def main():

    #count words that user inputs
    input_str = input("Enter a string to count words: ")
    manipulator = StringManipulator(input_str)
    print(f"The numer of words that you entered is: {manipulator.count_words()}")



if __name__ == "__main__":
    main()