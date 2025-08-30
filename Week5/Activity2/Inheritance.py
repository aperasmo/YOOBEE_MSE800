#Review the attached file and develop code that demonstrates the use of inheritance as a core feature in your OOP implementation. 
#Upload your code to GitHub and share the repository link, including a short comment that explains your understanding.
#Consider people in the University
# ▪ Students have: name, address, age, ID, academic record, etc.
# ▪ Academics have: name, address, age, ID, tax code, salary, etc.
# ▪ General staffs have: name, address, age, ID, tax code, pay rate, 


# This program shows how we can use inheritance in Python.
# We have a base class Person with common details like name, address, age, and ID.
# Then, we create Student and Academic classes that get these details from Person
# but also have their own special information.

class Person:
    def __init__(self, name, address, age, ID):
        # Initialize basic person details
        self.name = name
        self.address = address
        self.age = age
        self.ID = ID

    def display_info(self):
        # Show basic person information
        return f"Name: {self.name}, Address: {self.address}, Age: {self.age}, ID: {self.ID}"

class Student(Person):
    def __init__(self, name, address, age, ID, academic_record):
        # Use Person's __init__ to set common info
        super().__init__(name, address, age, ID)
        # Add student-specific info
        self.academic_record = academic_record

    def display_info(self):
        # Get the person info and add academic record
        base_info = super().display_info()
        return f"{base_info}, Academic Record: {self.academic_record}"

class Academic(Person):
    def __init__(self, name, address, age, ID, tax_code, salary):
        # Use Person's __init__ to set common info
        super().__init__(name, address, age, ID)
        # Add academic-specific info
        self.tax_code = tax_code
        self.salary = salary

    def display_info(self):
        # Get the person info and add tax code and salary
        base_info = super().display_info()
        return f"{base_info}, Tax Code: {self.tax_code}, Salary: {self.salary}"

if __name__ == "__main__":
    student = Student("Allan", "123 Flat Bush St", 20, "S123", "A+")
    academic = Academic("Dr. Vian", "MIT", 45, "A456", "TX789", 100000)

    print(student.display_info())
    print(academic.display_info())