class StringManipulator():
    def __init__(self, input_string): # Initialize with an input string
        self.input_string = input_string
    
    def find_character(self,char): # Find the index of a character in the string
        return  self.input_string.find(char)
        
    def get_length(self):    # Get the length of the input string
        return len(self.input_string)

    def to_uppercase(self): #  Convert the string to uppercase
        return self.input_string.upper()

    def to_lowercase(input_string): # Convert the string to lowercase
        return input_string.lower()
    def count_words(self):  #Count the number of words in the input string.
        return len(self.input_string.split()) #return the number of words by splitting the string by spaces

def main():

    #count words that user inputs
    input_str = input("Enter a string to count words: ")
    manipulator = StringManipulator(input_str) # Initialize with a string
    print(f"The numer of words that you entered is: {manipulator.count_words()}") # Count the number of words


if __name__ == "__main__":
    main()    
