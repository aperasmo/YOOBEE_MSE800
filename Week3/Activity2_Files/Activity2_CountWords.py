#Week3- Activity 2: count the words in the demo text file
#Develop a new project that reads demo.txt and returns the total number of words. 
#Share the GitHub repository link and a screenshot of the result.

class ProcessTextFile:
    def __init__(self, file_path):
        self.file_path = file_path    
# define the word count function
    def text_count_word(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            words_files = file_content.split()
            return len(words_files)

# main function
def main():
    file_path = "demo.txt"
    count_word = ProcessTextFile(file_path)
    print("Count of the words in file: ", count_word.text_count_word())

if __name__ == "__main__":
    main()