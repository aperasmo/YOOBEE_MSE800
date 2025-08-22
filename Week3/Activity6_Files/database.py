import sqlite3

class Database:
    def __init__(self):
        self.db_name = "Week3/Activity6_Files/YB_MngSys.db" # Database file path
    
    def connect(self): # Create a connection to the SQLite database
        return sqlite3.connect(self.db_name)
    
    def create_tables(self): # Create necessary tables in the database
        print("Creating tables...")
        conn = self.connect()
        cursor = conn.cursor()
        
        # Student table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS student (
          student_id INTEGER PRIMARY KEY,
          name VARCHAR(100) NOT NULL,
          contact_number VARCHAR(100) NOT NULL,
          email VARCHAR(100) NOT NULL,
          status VARCHAR(50) NOT NULL
        )
        ''')
        
        # Lecturer table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturer (
          lecturer_id INTEGER PRIMARY KEY,
          name VARCHAR(100) NOT NULL,
          contact_number VARCHAR(100) NOT NULL,
          email VARCHAR(100) NOT NULL,
          department VARCHAR(100) NOT NULL
        )
        ''')
        
        # Course table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS course (
          course_id INTEGER PRIMARY KEY,
          course_code VARCHAR(20) NOT NULL,
          name VARCHAR(200) NOT NULL,
          credits INTEGER NOT NULL
        )
        ''')
        
        # Class table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS class (
          class_id INTEGER PRIMARY KEY,
          course_id INTEGER NOT NULL,
          lecturer_id INTEGER NOT NULL,
          term VARCHAR(20) NOT NULL,
          section TEXT NOT NULL,
          FOREIGN KEY (course_id) REFERENCES course(course_id),
          FOREIGN KEY (lecturer_id) REFERENCES lecturer(lecturer_id),
          UNIQUE(course_id, lecturer_id, term, section)
        )
        ''')
        
        # Student enrollments table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_enrollments (
          student_enrollments_id INTEGER PRIMARY KEY,
          student_id INTEGER NOT NULL,
          class_id INTEGER NOT NULL,
          enrolled_date TEXT NOT NULL,
          status TEXT NOT NULL,
          grade INTEGER,
          FOREIGN KEY (student_id) REFERENCES student(student_id),
          FOREIGN KEY (class_id) REFERENCES class(class_id)
        )
        ''')
        
        # Users table for login
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
          user_id INTEGER PRIMARY KEY,
          login TEXT NOT NULL UNIQUE,
          password TEXT NOT NULL,
          name TEXT NOT NULL,
          contact_number TEXT NOT NULL,
          status TEXT NOT NULL
        )
        ''')
        
        conn.commit()
        conn.close()
        print("Tables created!")