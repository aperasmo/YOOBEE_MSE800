from database import Database
from student_manager import StudentManager, LecturerManager, CourseManager, ClassManager, StudentEnrollmentManager, UserManager

class YOOBEESystem: # Main class to manage the Yoobee College system
    def __init__(self):
        self.db = Database()
        self.student_mgr = StudentManager()
        self.lecturer_mgr = LecturerManager()
        self.course_mgr = CourseManager()
        self.class_mgr = ClassManager()
        self.enrollment_mgr = StudentEnrollmentManager()
        self.user_mgr = UserManager()
    
    def setup(self):
        self.db.create_tables()
        # Create admin user if no users exist
        users = self.user_mgr.view_users()
        if len(users) == 0:
            self.user_mgr.add_user("admin", "password", "Admin", "555-0000", "A")   # Default admin credentials
            print("Default admin created: admin/password")
    
    def login(self):
        print("\n--- Login ---")
        username = input("Username: ")
        password = input("Password: ")
        
        if self.user_mgr.check_login(username, password):
            print("Login successful!")
            return True
        else:
            print("Login failed!")
            return False
    
    def show_main_menu(self):
        print("\n=== Yoobee College Management System ===")
        print("1. Manage Students")
        print("2. Manage Lecturers") 
        print("3. Manage Courses")
        print("4. Manage Classes")
        print("5. Manage Student Enrollments")
        print("6. Manage Users")
        print("7. Exit")
    
    def student_menu(self):
        while True:
            print("\n--- Student Management ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Back")
            
            choice = input("Choose option: ")
            
            if choice == "1":
                name = input("Name: ")
                contact_number = input("Contact Number: ")
                email = input("Email: ")
                status = input("Status (Active, Inactive, Graduated, Suspended): ")
                self.student_mgr.add_student(name, contact_number, email, status)
            
            elif choice == "2":
                students = self.student_mgr.view_students()
                print("\n--- Students ---")
                for student in students:
                    print(f"ID: {student[0]}, Name: {student[1]}, Contact: {student[2]}, Email: {student[3]}, Status: {student[4]}")
            
            elif choice == "3":
                students = self.student_mgr.view_students()
                for student in students:
                    print(f"ID: {student[0]}, Name: {student[1]}")
                
                student_id = int(input("Enter student ID to update: "))
                name = input("New name: ")
                contact_number = input("New contact number: ")
                email = input("New email: ")
                status = input("New status: ")
                self.student_mgr.update_student(student_id, name, contact_number, email, status)
            
            elif choice == "4":
                students = self.student_mgr.view_students()
                for student in students:
                    print(f"ID: {student[0]}, Name: {student[1]}")
                
                student_id = int(input("Enter student ID to delete: "))
                confirm = input("Are you sure? (y/n): ")
                if confirm.lower() == 'y':
                    self.student_mgr.delete_student(student_id)
            
            elif choice == "5": # Go back to main menu
                break
    
    def lecturer_menu(self):
        while True:
            print("\n--- Lecturer Management ---")
            print("1. Add Lecturer")
            print("2. View Lecturers")
            print("3. Delete Lecturer")
            print("4. Back")
            
            choice = input("Choose option: ")
            
            if choice == "1":
                name = input("Name: ")
                contact_number = input("Contact Number: ")
                email = input("Email: ")
                department = input("Department: ")
                self.lecturer_mgr.add_lecturer(name, contact_number, email, department)
            
            elif choice == "2":
                lecturers = self.lecturer_mgr.view_lecturers()
                print("\n--- Lecturers ---")
                for lecturer in lecturers:
                    print(f"ID: {lecturer[0]}, Name: {lecturer[1]}, Contact: {lecturer[2]}, Email: {lecturer[3]}, Department: {lecturer[4]}")
            
            elif choice == "3":
                lecturers = self.lecturer_mgr.view_lecturers()
                for lecturer in lecturers:
                    print(f"ID: {lecturer[0]}, Name: {lecturer[1]}")
                
                lecturer_id = int(input("Enter lecturer ID to delete: "))
                confirm = input("Are you sure? (y/n): ")
                if confirm.lower() == 'y':
                    self.lecturer_mgr.delete_lecturer(lecturer_id)
            
            elif choice == "4": # Go back to main menu
                break
    
    def course_menu(self):
        while True:
            print("\n--- Course Management ---")
            print("1. Add Course")
            print("2. View Courses")
            print("3. Delete Course")
            print("4. Back")
            
            choice = input("Choose option: ")
            
            if choice == "1":
                course_code = input("Course code (e.g., MSE800): ")
                name = input("Course name: ")
                credits = int(input("Credits: "))
                self.course_mgr.add_course(course_code, name, credits)
            
            elif choice == "2":
                courses = self.course_mgr.view_courses()
                print("\n--- Courses ---")
                for course in courses:
                    print(f"ID: {course[0]}, Code: {course[1]}, Name: {course[2]}, Credits: {course[3]}")
            
            elif choice == "3":
                courses = self.course_mgr.view_courses()
                for course in courses:
                    print(f"ID: {course[0]}, Code: {course[1]}, Name: {course[2]}")
                
                course_id = int(input("Enter course ID to delete: "))
                confirm = input("Are you sure? (y/n): ")
                if confirm.lower() == 'y':
                    self.course_mgr.delete_course(course_id)
            
            elif choice == "4": # Go back to main menu
                break
    
    def class_menu(self):
        while True:
            print("\n--- Class Management ---")
            print("1. Add Class")
            print("2. View Classes")
            print("3. Delete Class")
            print("4. Back")
            
            choice = input("Choose option: ")
            
            if choice == "1":
                # Show available courses and lecturers
                courses = self.course_mgr.view_courses()
                lecturers = self.lecturer_mgr.view_lecturers()
                
                print("\nAvailable Courses:")
                for course in courses:
                    print(f"ID: {course[0]}, Code: {course[1]}, Name: {course[2]}")
                
                print("\nAvailable Lecturers:")
                for lecturer in lecturers:
                    print(f"ID: {lecturer[0]}, Name: {lecturer[1]}")
                
                course_id = int(input("Course ID: "))
                lecturer_id = int(input("Lecturer ID: "))
                term = input("Term (e.g., 2025-S2): ")
                section = input("Section (A or B): ")
                self.class_mgr.add_class(course_id, lecturer_id, term, section)
            
            elif choice == "2":
                classes = self.class_mgr.view_classes()
                print("\n--- Classes ---")
                for cls in classes:
                    print(f"ID: {cls[0]}, Course: {cls[1]} - {cls[2]}, Lecturer: {cls[3]}, Term: {cls[4]}, Section: {cls[5]}")
            
            elif choice == "3":
                classes = self.class_mgr.view_classes()
                for cls in classes:
                    print(f"ID: {cls[0]}, Course: {cls[1]} - {cls[2]}, Term: {cls[4]}, Section: {cls[5]}")
                
                class_id = int(input("Enter class ID to delete: "))
                confirm = input("Are you sure? (y/n): ")
                if confirm.lower() == 'y':
                    self.class_mgr.delete_class(class_id)
            
            elif choice == "4": # Go back to main menu
                break
    
    def enrollment_menu(self):
        while True:
            print("\n--- Student Enrollment Management ---")
            print("1. Add Student Enrollment")
            print("2. View Student Enrollments")
            print("3. Delete Student Enrollment")
            print("4. Back")
            
            choice = input("Choose option: ")
            
            if choice == "1":
                # Show available students and classes
                students = self.student_mgr.view_students()
                classes = self.class_mgr.view_classes()
                
                print("\nAvailable Students:")
                for student in students:
                    print(f"ID: {student[0]}, Name: {student[1]}")
                
                print("\nAvailable Classes:")
                for cls in classes:
                    print(f"ID: {cls[0]}, Course: {cls[1]} - {cls[2]}, Term: {cls[4]}, Section: {cls[5]}")
                
                student_id = int(input("Student ID: "))
                class_id = int(input("Class ID: "))
                enrolled_date = input("Enrolled date (YYYY-MM-DD): ")
                status = input("Status (Enrolled, Completed, Withdrawn, Failed): ")
                grade = input("Grade (0-100 or press Enter for none): ")
                final_grade = int(grade) if grade else None
                self.enrollment_mgr.add_enrollment(student_id, class_id, enrolled_date, status, final_grade)
            
            elif choice == "2":
                enrollments = self.enrollment_mgr.view_enrollments()
                print("\n--- Student Enrollments ---")
                for enrollment in enrollments:
                    grade = enrollment[8] if enrollment[8] else "N/A"
                    print(f"ID: {enrollment[0]}, Student: {enrollment[1]}, Course: {enrollment[2]} - {enrollment[3]}, Term: {enrollment[4]}, Section: {enrollment[5]}, Enrolled: {enrollment[6]}, Status: {enrollment[7]}, Grade: {grade}")
            
            elif choice == "3": #
                enrollments = self.enrollment_mgr.view_enrollments()
                for enrollment in enrollments:
                    print(f"ID: {enrollment[0]}, Student: {enrollment[1]}, Course: {enrollment[2]}")
                
                enrollment_id = int(input("Enter enrollment ID to delete: "))
                confirm = input("Are you sure? (y/n): ")
                if confirm.lower() == 'y':
                    self.enrollment_mgr.delete_enrollment(enrollment_id)
            
            elif choice == "4": # Go back to main menu
                break
    
    def user_menu(self):
        while True:
            print("\n--- User Management ---")
            print("1. Add User")
            print("2. View Users")
            print("3. Back")
            
            choice = input("Choose option: ")
            
            if choice == "1":
                login = input("Login: ")
                password = input("Password: ")
                name = input("Name: ")
                contact = input("Contact: ")
                status = input("Status (A=Active, I=Inactive): ")
                self.user_mgr.add_user(login, password, name, contact, status)
            
            elif choice == "2":
                users = self.user_mgr.view_users()
                print("\n--- Users ---")
                for user in users:
                    print(f"ID: {user[0]}, Login: {user[1]}, Name: {user[3]}, Contact: {user[4]}, Status: {user[5]}")
            
            elif choice == "3": # Go back to main menu
                break
    
    def main(self):
        print("Welcome to Yoobee College Management System")
        self.setup() # Initialize the database and create tables
        
        # Login
        if not self.login(): # If login fails, exit the system
            print("Thank you for using YBCMS!")
            return
        
        # Main menu
        while True:
            self.show_main_menu()
            choice = input("Choose option: ")
            
            if choice == "1":
                self.student_menu()
            elif choice == "2":
                self.lecturer_menu()
            elif choice == "3":
                self.course_menu()
            elif choice == "4":
                self.class_menu()
            elif choice == "5":
                self.enrollment_menu()
            elif choice == "6":
                self.user_menu()
            elif choice == "7":
                print("Goodbye! System exiting...")
                break
            else:
                print("Invalid choice! Try again.")

# Run the program
if __name__ == "__main__":
    system = YOOBEESystem() # Create an instance of the system
    system.main()   # Start the main program 