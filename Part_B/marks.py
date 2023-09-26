3
class Student:
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn
        self.marks = []

    def getMarks(self):
        for i in range(3):
            mark = float(input(f"Enter marks for subject {i + 1}: "))
            self.marks.append(mark)

    def display(self):
        total_marks = sum(self.marks)
        percentage = (total_marks / (3 * 100)) * 100
        print("\nScore Card:")
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Marks:", self.marks)
        print("Total Marks:", total_marks)
        print("Percentage:", percentage)

name = input("Enter student's name: ")
usn = input("Enter student's USN: ")
student = Student(name, usn)
student.getMarks()
student.display()
