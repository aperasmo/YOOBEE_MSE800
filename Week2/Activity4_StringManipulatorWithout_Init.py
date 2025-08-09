class StringManipulator:

    def find_character(input_string,char):  # This method finds the index of a character in the input string
        return input_string.find(char)
        
    def get_length(input_string): # This method returns the length of the input string
        return len(input_string)

    def to_uppercase(input_string): # This method converts the input string to uppercase
        return input_string.upper()

    def to_lowercase(input_string): #   
        return input_string.lower()
        
def main():
    
    input_str = "Hello World" # This is the input string 

    print(f"Index of 'o': {StringManipulator.find_character(input_str,'o')}") # Find the index of 'o'
    print(f"Length of string: {StringManipulator.get_length(input_str)}") # Get the length of the string
    print(f"Uppercase string: {StringManipulator.to_uppercase(input_str)}")# Convert the string to uppercase


if __name__ == "__main__":
    main()

    

    