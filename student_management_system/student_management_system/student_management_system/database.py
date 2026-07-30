import sqlite3


# Database connection
def create_connection():
    conn = sqlite3.connect("students.db")
    return conn


# Create table
def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        roll_no INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        tamil INTEGER,
        english INTEGER,
        maths INTEGER
    )
    """)

    conn.commit()
    conn.close()


# Add student
def add_student(roll_no, name, age, tamil, english, maths):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students
        (roll_no, name, age, tamil, english, maths)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (roll_no, name, age, tamil, english, maths))

        conn.commit()
        print("Student Added Successfully")

    except sqlite3.IntegrityError:
        print("Roll Number Already Exists")

    finally:
        conn.close()


# View all students
def view_students():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if students:
        for student in students:
            print("----------------------------")
            print("Roll No :", student[0])
            print("Name    :", student[1])
            print("Age     :", student[2])
            print("Tamil   :", student[3])
            print("English :", student[4])
            print("Maths   :", student[5])
    else:
        print("No Students Found")

    conn.close()


# Search student
def search_student(roll_no):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll_no=?",
        (roll_no,)
    )

    student = cursor.fetchone()

    if student:
        print("----------------------------")
        print("Roll No :", student[0])
        print("Name    :", student[1])
        print("Age     :", student[2])
        print("Tamil   :", student[3])
        print("English :", student[4])
        print("Maths   :", student[5])
    else:
        print("Student Not Found")

    conn.close()


# Update student
def update_student(roll_no, name, age, tamil, english, maths):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET name=?,
        age=?,
        tamil=?,
        english=?,
        maths=?
    WHERE roll_no=?
    """,
    (name, age, tamil, english, maths, roll_no))

    if cursor.rowcount > 0:
        print("Student Updated Successfully")
    else:
        print("Student Not Found")

    conn.commit()
    conn.close()


# Delete student
def delete_student(roll_no):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE roll_no=?",
        (roll_no,)
    )

    if cursor.rowcount > 0:
        print("Student Deleted Successfully")
    else:
        print("Student Not Found")

    conn.commit()
    conn.close()
