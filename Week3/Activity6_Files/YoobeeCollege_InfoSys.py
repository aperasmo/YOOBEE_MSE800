from database import create_connection
import sqlite3

#ADD
def add_Student(name,contact_number,email,status):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO student (name, contact_number,email,status) VALUES (?, ?,?,?)", (name,contact_number,email,status))
        conn.commit()
        print(" Student added successfully.")
    except sqlite3.IntegrityError:
        print("Student ID must be unique.")
    conn.close()

def add_Course(course_code,name, credits):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO course (course_code,name, credits) VALUES (?, ?,?)", (course_code,name, credits))
        conn.commit()
        print(" Course added successfully.")
    except sqlite3.IntegrityError:
        print("Course must be unique.")
    conn.close()

def add_Lecturer(name,contact_number,email,department):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO lecturer (name,contact_number,email,department) VALUES (?, ?,?,?)", (name,contact_number,email,department))
        conn.commit()
        print(" Lecturer added successfully.")
    except sqlite3.IntegrityError:
        print("Lecturer must be unique.")
    conn.close()

def add_Class(course_id,lecturer_id,term,section):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO `class` (course_id,lecturer_id,term,section) VALUES (?, ?,?,?)", (course_id,lecturer_id,term,section))
        conn.commit()
        print(" Class added successfully.")
    except sqlite3.IntegrityError:
        print("Class must be unique.")
    conn.close()

def add_Student_enrollments(student_id,class_id,enrolled_date,status,grade):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO student_enrollments (student_id,class_id,enrolled_date,status,grade) VALUES (?, ?,?,?,?)", (student_id,class_id,enrolled_date,status,grade))
        conn.commit()
        print(" Student enrollment added successfully.")
    except sqlite3.IntegrityError:
        print("Student enrollment must be unique.")
    conn.close()

def add_user(login, password, name, contact_number, status):
    # Input validation
    if not login or len(login.strip()) == 0:
        print("Error: Login cannot be empty.")
        return False
    
    if len(login) > 20:
        print("Error: Login must be 20 characters or less.")
        return False
    
    if not password or len(password.strip()) == 0:
        print("Error: Password cannot be empty.")
        return False
    
    if len(password) > 20:
        print("Error: Password must be 20 characters or less.")
        return False
    
    if not name or len(name.strip()) == 0:
        print("Error: Name cannot be empty.")
        return False
    
    if len(name) > 100:
        print("Error: Name must be 100 characters or less.")
        return False
    
    if not contact_number or len(contact_number.strip()) == 0:
        print("Error: Contact number cannot be empty.")
        return False
    
    if len(contact_number) > 100:
        print("Error: Contact number must be 100 characters or less.")
        return False
    
    if status not in ['A', 'I', 'a', 'i']:
        print("Error: Status must be 'A' for active or 'I' for inactive.")
        return False
    
    # Convert status to uppercase for consistency
    status = status.upper()
    
    conn = create_connection()
    cursor = conn.cursor()
    try:
        # Check if login already exists
        cursor.execute("SELECT login FROM users WHERE login = ?", (login,))
        if cursor.fetchone():
            print(f"Error: Login '{login}' already exists. Please choose a different login.")
            return False
        
        # Insert new user
        cursor.execute("INSERT INTO users (login, password, name, contact_number, status) VALUES (?, ?, ?, ?, ?)", 
                      (login, password, name, contact_number, status))
        conn.commit()
        print(f"✅ User '{login}' added successfully.")
        return True
    except sqlite3.IntegrityError as e:
        print(f"Database error: {e}")
        return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

#VIEW
def view_Students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_Student(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_users(login,password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE login = ?  AND password = ?", (login, password))
    rows = cursor.fetchall()
    conn.close()
    if len(rows) == 0:
        print("No user found with the provided credentials.")
        return False
    return True

def delete_Student(stud_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE student_id = ?", (stud_id,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted.")

# Additional VIEW functions
def view_Courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_Lecturers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturer")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_Classes():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.class_id, co.course_code, co.name as course_name, 
               l.name as lecturer_name, c.term, c.section
        FROM `class` c
        JOIN course co ON c.course_id = co.course_id
        JOIN lecturer l ON c.lecturer_id = l.lecturer_id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_Student_enrollments():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT se.student_enrollments_id, s.name as student_name, 
               co.course_code, co.name as course_name, 
               se.enrolled_date, se.status, se.grade
        FROM student_enrollments se
        JOIN student s ON se.student_id = s.student_id
        JOIN `class` c ON se.class_id = c.class_id
        JOIN course co ON c.course_id = co.course_id
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows

# UPDATE functions
def update_Student(student_id, name, contact_number, email, status):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE student 
            SET name = ?, contact_number = ?, email = ?, status = ?
            WHERE student_id = ?
        """, (name, contact_number, email, status, student_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("✅ Student updated successfully.")
            return True
        else:
            print("❌ Student not found.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def update_user(user_id, login, password, name, contact_number, status):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE users 
            SET login = ?, password = ?, name = ?, contact_number = ?, status = ?
            WHERE user_id = ?
        """, (login, password, name, contact_number, status, user_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("✅ User updated successfully.")
            return True
        else:
            print("❌ User not found.")
            return False
    except sqlite3.IntegrityError:
        print("❌ Login already exists. Please choose a different login.")
        return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def update_Course(course_id, course_code, name, credits):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE course 
            SET course_code = ?, name = ?, credits = ?
            WHERE course_id = ?
        """, (course_code, name, credits, course_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("✅ Course updated successfully.")
            return True
        else:
            print("❌ Course not found.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def update_Lecturer(lecturer_id, name, contact_number, email, department):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE lecturer 
            SET name = ?, contact_number = ?, email = ?, department = ?
            WHERE lecturer_id = ?
        """, (name, contact_number, email, department, lecturer_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("✅ Lecturer updated successfully.")
            return True
        else:
            print("❌ Lecturer not found.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

# DELETE functions
def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("🗑️ User deleted successfully.")
            return True
        else:
            print("❌ User not found.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def delete_Course(course_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM course WHERE course_id = ?", (course_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("🗑️ Course deleted successfully.")
            return True
        else:
            print("❌ Course not found.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def delete_Lecturer(lecturer_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM lecturer WHERE lecturer_id = ?", (lecturer_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("🗑️ Lecturer deleted successfully.")
            return True
        else:
            print("❌ Lecturer not found.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def delete_Class(class_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM `class` WHERE class_id = ?", (class_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("🗑️ Class deleted successfully.")
            return True
        else:
            print("❌ Class not found.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def delete_Student_enrollment(enrollment_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM student_enrollments WHERE student_enrollments_id = ?", (enrollment_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("🗑️ Student enrollment deleted successfully.")
            return True
        else:
            print("❌ Student enrollment not found.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()
