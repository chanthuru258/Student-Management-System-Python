from student_management_system.student import Student

students = []


def add_student():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    tamil = int(input("Enter Tamil Mark: "))
    english = int(input("Enter English Mark: "))
    maths = int(input("Enter Maths Mark: "))

    student = Student(roll_no, name, age, tamil, english, maths)
    students.append(student)

    print("\nStudent Added Successfully.\n")


def view_students():
    if len(students) == 0:
        print("\nNo Student Records Found.\n")
        return

    for student in students:
        student.display()


def search_student():
    roll = int(input("Enter Roll Number to Search: "))

    for student in students:
        if student.roll_no == roll:
            student.display()
            return

    print("Student Not Found.")


def update_student():
    roll = int(input("Enter Roll Number to Update: "))

    for student in students:
        if student.roll_no == roll:
            student.name = input("Enter New Name: ")
            student.age = int(input("Enter New Age: "))
            student.tamil = int(input("Enter Tamil Mark: "))
            student.english = int(input("Enter English Mark: "))
            student.maths = int(input("Enter Maths Mark: "))

            print("Student Updated Successfully.")
            return

    print("Student Not Found.")


def delete_student():
    roll = int(input("Enter Roll Number to Delete: "))

    for student in students:
        if student.roll_no == roll:
            students.remove(student)
            print("Student Deleted Successfully.")
            return

    print("Student Not Found.")
