import sqlite3

def create_connection():
    conn = sqlite3.connect("students.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            stud_id INTEGER PRIMARY KEY AUTOINCREMENT,
            stud_name TEXT NOT NULL,
            stud_address TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()
