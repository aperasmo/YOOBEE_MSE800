class StringManipulator():
    def __init__(self, input_string): # Initialize with an input string
        self.input_string = input_string
    
    def find_character(self,char): # Find the index of a character in the string
        return  self.input_string.find(char)
        
    def get_length(self):   
        return len(self.input_string)

    def to_uppercase(self): #  Convert the string to uppercase
        return self.input_string.upper()

    def to_lowercase(input_string): #   
        return input_string.lower()

def main():

    # Example usage of StringManipulator
    manipulator = StringManipulator("hello world") # Initialize with a string
    print(f"Index of 'o': {manipulator.find_character('o')}") # Find the index of 'o' 
    print(f"Length of string: {manipulator.get_length()}") # Get the length of the strin
    print(f"Uppercase string: {manipulator.to_uppercase()}") # Convert the string to uppercase


if __name__ == "__main__":
    main()