from database import create_table
from student_manager import add_Student, view_Students, search_Student, delete_Student

def menu():
    print("\n==== Student Manager ====")
    print("1. Add Students")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. Delete Student by ID")
    print("5. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter Address: ")
            add_Student(name, email)
        elif choice == '2':
            Students = view_Students()
            for Student in Students:
                print(Student)
        elif choice == '3':
            name = input("Enter name to search: ")
            Students = search_Student(name)
            for Student in Students:
                print(Student)
        elif choice == '4':
            Student_id = int(input("Enter Student ID to delete: "))
            delete_Student(Student_id)
        elif choice == '5':
            print("See Yah!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
