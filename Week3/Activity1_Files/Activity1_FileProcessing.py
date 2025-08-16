#Using the attached text file, open, read, and write the complete information for the demo.txt. 
#Share the GitHub link here(with adding the screenshot of the result).


class ProcessTextFile: # Class to handle file processing operations
    def __init__(self, file_path): # Initialize with the file path
        self.file_path = file_path

    def file_reader(self,file_path): # Read the contents of the file
     with open(self.file_path, 'r', encoding='utf-8') as file: # Open the file in read mode with UTF-8 encoding
      content = file.read()
      print(f"contents of the file is {content} ")
  
    def write_into_file(self, additional_content, file_path): # Write additional content to the file
        with open(file_path,"a") as file:
         file.write(additional_content)
    

if __name__ == "__main__":
 file_path = "demo.txt" #   Specify the path to the demo.txt file
 file_manipulator = ProcessTextFile(file_path) # Create an instance of ProcessTextFile
 file_manipulator.file_reader(file_path) # Read the file contents
 file_manipulator.write_into_file("**************************************\nI APPEND SOME TEXT HERE IN DEMO FILE",file_path) # Write additional content to the file
 file_manipulator.file_reader(file_path) # Read the file contents again to show the updated content

 