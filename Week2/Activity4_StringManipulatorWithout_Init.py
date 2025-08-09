class StringManipulator:

    def find_character(input_string,char):
        return input_string.find(char)
        
    def get_length(input_string):
        return len(input_string)

    def to_uppercase(input_string):
        return input_string.upper()

    def to_lowercase(input_string):
        return input_string.lower()
        
def main():
    
    input_str = "Hello World" # This is the input string 

    print(f"Index of 'o': {StringManipulator.find_character(input_str,'o')}")
    print(f"Length of string: {StringManipulator.get_length(input_str)}")
    print(f"Uppercase string: {StringManipulator.to_uppercase(input_str)}")


if __name__ == "__main__":
    main()

    

    