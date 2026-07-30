class Student:

    def __init__(self, roll_no, name, age, tamil, english, maths):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.tamil = tamil
        self.english = english
        self.maths = maths

    def total(self):
        return self.tamil + self.english + self.maths

    def average(self):
        return self.total() / 3

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("-" * 40)
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Tamil   :", self.tamil)
        print("English :", self.english)
        print("Maths   :", self.maths)
        print("Total   :", self.total())
        print("Average :", round(self.average(), 2))
        print("Grade   :", self.grade())
        print("-" * 40)
