#Using the attached text file, open, read, and write the complete information for the demo.txt. 
#Share the GitHub link here(with adding the screenshot of the result).


class ProcessTextFile:
    
    def file_reader(self,file_path):
     with open(file_path, "r") as file:
      content = file.read()
      print(f"contents of the file is {content} ")
  
    def write_into_file(self, additional_file_content, file_path):
        with open(file_path,"a") as file:
         file.write(additional_file_content)


if __name__ == "__main__":
 file_path = "demo.txt"
 file_read_writer = ProcessTextFile()
 file_read_writer.file_reader(file_path)
 file_read_writer.write_into_file("I over write the content of this file",file_path)
 file_read_writer.file_reader(file_path)