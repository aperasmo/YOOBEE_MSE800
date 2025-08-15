#Week 2 - Activity 6 : Develop a basic HR project using OO
#You are tasked with developing a simple program for the Human Resources (HR) department to store and display basic employee information, including each employee’s name, salary, and job title.
#Requirements:
#Create at least two Employee objects with different data.
#Call the display_info() method to show each employee’s details.
#Call the give_raise() method to increase an employee’s salary and display the updated amount.

 

# Week2/HR_Project.py
class Employee:
    def __init__(self, name, salary, job_title): #  Initialize the employee with name, salary, and job title
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def display_info(self): #   Display the employee's information
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:.2f}")
        print(f"Job Title: {self.job_title}")

    def give_raise(self, amount): #   Increase the employee's salary by a specified amount
        self.salary += amount
        print(f"{self.name}'s new salary after raise is: ${self.salary:.2f}")
def main():
    # Create two Employee objects with different data
    employee1 = Employee("Allan Erasmo", 60000, "Software Engineer")
    employee2 = Employee("Vito Erasmo", 70000, "Data Scientist")

    # Display each employee's information
    print("Employee 1 Information:")
    employee1.display_info()
    print("\nEmployee 2 Information:")
    employee2.display_info()

    # Give a raise to each employee and display the updated salary
    print("\nGiving raises...")
    employee1.give_raise(5000)
    employee2.give_raise(7000)

if __name__ == "__main__":
    main()  
