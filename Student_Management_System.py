class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >=40:
            return "c"
        else:
            return "Fail"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grades: {self.calculate_grade()}")

# s1 = Student("Ankit",101,85)
# s1.display()

Students = [
    Student("Ankit",101,85),
    Student("Rahul",102,92),
    Student("Site",103,78)
]

top_student = Students[0]

for s in Students:
    if s.marks > top_student.marks:
        top_student = s

print("Top Scorer: ")
top_student.display()