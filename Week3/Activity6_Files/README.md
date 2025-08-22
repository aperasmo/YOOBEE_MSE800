#  Yoobee College Management System

Welcome to the Yoobee College Management System! This is a simple system program that helps to manage records - from keeping track of students and teachers to organizing classes,subject and section.

## What Does This System Do?

 Instead of having stacks of paper everywhere, everything is stored neatly in a computer database. Here's what it can handle:

- **Students**: Keep track of who's studying at the college
- **Lecturers**: Manage information about teachers and staff
- **Courses**: Organize what subjects are being taught (like Math, English, etc.)
- **Classes**: Schedule when and where courses happen
- **Enrollments**: Track which students are taking which classes and their grades
- **Users**: Control who can access and use this system

##  How Is It Built?

The system is made up of several Python files that work together - using sqlite3 as the Database:

### Main Files:
- **`main.py`** -  It's where you interact with the system
- **`database.py`** - This creates and manages the digital filing cabinet (database)
- **`student_manager.py`** - This handles all the behind-the-scenes work for managing data
- **`YB_MngSys.db`** -  the main database

### The Database:
The system uses SQLite, which is like having a super-organized digital filing cabinet with these folders:

1. **Student Folder** - Contains student ID, name, contact info, email, and status
2. **Lecturer Folder** - Contains teacher ID, name, contact info, email, and department
3. **Course Folder** - Contains course ID, course code (like "MSE800"), name, and credit hours
4. **Class Folder** - Contains class ID, which course it is, who teaches it, what term, and section
5. **Enrollment Folder** - Contains enrollment ID, which student, which class, when they enrolled, status, and grade
6. **Users Folder** - Contains login information for people who can use the system

##  How to Get Started

### What You Need:
- A computer with Python installed
- The ability to run Python programs

### Step 1: Run the Program
1. Open your command prompt or terminal
2. Navigate to the folder containing the files
3. Type: `python main.py`
4. Press Enter

### Step 2: Login
- **Username**: `admin`
- **Password**: `password`
(The system creates this default admin account automatically the first time you run it!)

## How to Use the System

Once you're logged in, you'll see a main menu with 7 options. Here's what each one does:

### 1. Manage Students
This is where you handle everything about students:

- **Add Student**: Register a new student
  - You'll need: Name, phone number, email, and status
  - Status examples: Active, Inactive, Graduated, Suspended
- **View Students**: See a list of all students
- **Update Student**: Change a student's information
- **Delete Student**: Remove a student from the system (be careful!)

### 2 Manage Lecturers
This handles teacher information:

- **Add Lecturer**: Register a new teacher
  - You'll need: Name, phone number, email, and department
- **View Lecturers**: See all teachers
- **Delete Lecturer**: Remove a teacher (be careful!)

### 3. Manage Courses
This is for the subjects taught at the college:

- **Add Course**: Create a new subject
  - You'll need: Course code (like "MSE800"), course name, and credit hours
- **View Courses**: See all available courses
- **Delete Course**: Remove a course

### 4. Manage Classes
This schedules when courses actually happen:

- **Add Class**: Schedule a course
  - You'll need to pick: Which course, which teacher, what term (like "2025-S2"), and section (A or B)
- **View Classes**: See all scheduled classes
- **Delete Class**: Cancel a class

### 5. Manage Student Enrollments
This tracks which students are taking which classes:

- **Add Enrollment**: Sign up a student for a class
  - You'll need: Which student, which class, enrollment date, status, and grade (optional)
  - Status examples: Enrolled, Completed, Withdrawn, Failed
  - Grades: 0-100 or leave blank
- **Update Enrollments**: Update the Status and Grade of the Students
- **View Enrollments**: See who's taking what
- **Delete Enrollment**: Remove a student from a class

### 6. Manage Users
This controls who can use the system:

- **Add User**: Create a new login account
  - You'll need: Username, password, full name, contact info, and status (A=Active, I=Inactive)
- **View Users**: See all user accounts

### 7. Exit
This closes the program safely.

## Tips for Using the System

### Do This:
-  Always add courses and lecturers before creating classes
-  Make sure students and classes exist before creating enrollments
-  Use consistent naming (like always using "Active" instead of mixing "active" and "Active")
-  Double-check before deleting anything - there's no undo!

### Avoid This:
-  Don't delete courses that have active classes
-  Don't delete students who are enrolled in classes
-  Don't use special characters in names or codes
-  Don't forget to create user accounts for people who need access

## Common Tasks

### Adding a New Student to a Class:
1. Go to "Manage Students" → Add the student
2. Go to "Manage Courses" → Make sure the course exists
3. Go to "Manage Lecturers" → Make sure the teacher exists
4. Go to "Manage Classes" → Create the class (links course + teacher + schedule)
5. Go to "Manage Student Enrollments" → Enroll the student in the class

### Setting Up a New Semester:
1. Add any new courses for the semester
2. Add any new lecturers
3. Create classes for each course (with term like "2025-S1")
4. Enroll students in their classes

## Troubleshooting

### "Login failed!"
- Make sure you're using valid users
- Check for extra spaces or typos

### "Error adding ..."
- Make sure you're not trying to add duplicate information
- Check that you've filled in all required fields
- For classes and enrollments, make sure the related records exist first

### "No ... available"
- You need to add the basic records first (students, courses, lecturers) before you can create relationships (classes, enrollments)

### Program won't start
- Make sure Python is installed
- Make sure you're in the right folder
- Check that all the Python files are in the same folder

## File Structure

```
YB College System/
├── main.py              (The main program - start here!)
├── database.py          (Creates and manages the database)
├── student_manager.py   (Handles all the data operations)
└── YB_MngSys.db       (The database file - created automatically)
```