#  Yoobee College Management System
Developing a small information system for Yoobee College. The database will store students, lecturers, the courses offered, and student enrollments.

The system will records:

Student enrollment – Identifies which student is registered in which class
Lecturers assignment – Specifies which lecturers teaches each class
Academic outcome – Records the student’s final result in the class


# STEP 1

### ACTORS
1. Students
2. Lecturers
3. System Admin/Users


## USE CASES
1. Manage Course ⟶ «include» from Schedule Class Offering
2. Schedule Class Offering ⟶ «include» to Assign Lecturer to Class
3. Assign Lecturer to Class
4. Manage Person ▸▸ generalizes to Manage Student and Manage Lecturer
5. Manage Student  
6. Manage Lecturer
7. Manage Enrollment ⟶ «include» Lookup Student, «include» Lookup Class
8. Lookup Student
9. Lookup Class
10. Record Grade «extend» Manage Enrollment
11. Update Enrollment Status «extend» Manage Enrollment
12  Manage Enrollment
13. View Class (Registrar, Lecturer)
14. View Student Academic Record (Student, Registrar)




# STEP 2

- This use case diagram illustrates the interactions between various actors and the system. Each actor represents a distinct role that interacts with the system to achieve specific goals. The diagram maps out the functionalities (use cases) the system provides and shows which actors are associated with each use case.

![Yoobee College Database Schema](2_usecase_diagram.png)

# STEP 3
- The use case diagram below represents the Yoobee College Management System. It shows how the actors—Student, Lecturer, and Admin—interact with the system and what each can accomplish. The diagram also highlights the relationships between use cases, including generalization to represent commmon behaviours between actors or use cases.

It also illustrates dependencies between use cases, where << include >> show the required functionality and << extend >> represents as optional. 
 
![Yoobee College Database Schema](3_usecase_diagram.png)



# WITH CONDITION
![Yoobee College Database Schema](4_usecase_diagram_with_condition.png)


## USE CASES BRIEF DESCRIPTION
![Yoobee College Database Schema](use_case_description.png)