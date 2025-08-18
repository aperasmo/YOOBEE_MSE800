from database import create_connection
import sqlite3

def add_Student(name, address):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO students (stud_name, stud_address) VALUES (?, ?)", (name, address))
        conn.commit()
        print(" Student added successfully.")
    except sqlite3.IntegrityError:
        print(" address must be unique.")
    conn.close()

def view_Students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_Student(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE stud_name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_Student(stud_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (stud_id,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted.")
