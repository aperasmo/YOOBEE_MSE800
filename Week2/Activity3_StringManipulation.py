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

def main():

    # Example usage of StringManipulator
    manipulator = StringManipulator("hello world") 
    print(f"Index of 'o': {manipulator.find_character('o')}")
    print(f"Length of string: {manipulator.get_length()}")
    print(f"Uppercase string: {manipulator.to_uppercase()}")


if __name__ == "__main__":
    main()