import sqlite3
from database import Database

class StudentManager:
    def __init__(self):
        self.db = Database()
    
    def add_student(self, name, contact_number, email, status):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO student (name, contact_number, email, status) VALUES (?, ?, ?, ?)", 
                          (name, contact_number, email, status))
            conn.commit()
            print("Student added!")
        except:
            print("Error adding student")
        conn.close()
    
    def view_students(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student")
        students = cursor.fetchall()
        conn.close()
        return students
    
    def update_student(self, student_id, name, contact_number, email, status):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE student SET name=?, contact_number=?, email=?, status=? WHERE student_id=?", 
                      (name, contact_number, email, status, student_id))
        conn.commit()
        conn.close()
        print("Student updated!")
    
    def delete_student(self, student_id):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE student_id=?", (student_id,))
        conn.commit()
        conn.close()
        print("Student deleted!")

class LecturerManager:
    def __init__(self):
        self.db = Database()
    
    def add_lecturer(self, name, contact_number, email, department):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO lecturer (name, contact_number, email, department) VALUES (?, ?, ?, ?)", 
                          (name, contact_number, email, department))
            conn.commit()
            print("Lecturer added!")
        except:
            print("Error adding lecturer")
        conn.close()
    
    def view_lecturers(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lecturer")
        lecturers = cursor.fetchall()
        conn.close()
        return lecturers
    
    def delete_lecturer(self, lecturer_id):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM lecturer WHERE lecturer_id=?", (lecturer_id,))
        conn.commit()
        conn.close()
        print("Lecturer deleted!")

class CourseManager:
    def __init__(self):
        self.db = Database()
    
    def add_course(self, course_code, name, credits):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO course (course_code, name, credits) VALUES (?, ?, ?)", 
                          (course_code, name, credits))
            conn.commit()
            print("Course added!")
        except:
            print("Error adding course")
        conn.close()
    
    def view_courses(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course")
        courses = cursor.fetchall()
        conn.close()
        return courses
    
    def delete_course(self, course_id):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM course WHERE course_id=?", (course_id,))
        conn.commit()
        conn.close()
        print("Course deleted!")

class ClassManager:
    def __init__(self):
        self.db = Database()
    
    def add_class(self, course_id, lecturer_id, term, section):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO class (course_id, lecturer_id, term, section) VALUES (?, ?, ?, ?)", 
                          (course_id, lecturer_id, term, section))
            conn.commit()
            print("Class added!")
        except:
            print("Error adding class")
        conn.close()
    
    def view_classes(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT cl.class_id, c.course_code, c.name, l.name, cl.term, cl.section
            FROM class cl
            JOIN course c ON cl.course_id = c.course_id
            JOIN lecturer l ON cl.lecturer_id = l.lecturer_id
        """)
        classes = cursor.fetchall()
        conn.close()
        return classes
    
    def delete_class(self, class_id):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM class WHERE class_id=?", (class_id,))
        conn.commit()
        conn.close()
        print("Class deleted!")

class StudentEnrollmentManager:
    def __init__(self):
        self.db = Database()
    
    def add_enrollment(self, student_id, class_id, enrolled_date, status, grade=None):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO student_enrollments (student_id, class_id, enrolled_date, status, grade) VALUES (?, ?, ?, ?, ?)", 
                          (student_id, class_id, enrolled_date, status, grade))
            conn.commit()
            print("Student enrollment added!")
        except:
            print("Error adding enrollment")
        conn.close()
    
    def view_enrollments(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT se.student_enrollments_id, s.name, c.course_code, c.name, cl.term, cl.section, se.enrolled_date, se.status, se.grade
            FROM student_enrollments se
            JOIN student s ON se.student_id = s.student_id
            JOIN class cl ON se.class_id = cl.class_id
            JOIN course c ON cl.course_id = c.course_id
        """)
        enrollments = cursor.fetchall()
        conn.close()
        return enrollments
    
    def delete_enrollment(self, enrollment_id):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student_enrollments WHERE student_enrollments_id=?", (enrollment_id,))
        conn.commit()
        conn.close()
        print("Student enrollment deleted!")

class UserManager:
    def __init__(self):
        self.db = Database()
    
    def add_user(self, login, password, name, contact, status):
        conn = self.db.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (login, password, name, contact_number, status) VALUES (?, ?, ?, ?, ?)", 
                          (login, password, name, contact, status))
            conn.commit()
            print("User added!")
            return True
        except:
            print("Error - login already exists!")
            return False
        finally:
            conn.close()
    
    def view_users(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        return users
    
    def check_login(self, login, password):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE login=? AND password=?", (login, password))
        user = cursor.fetchone()
        conn.close()
        return user is not None