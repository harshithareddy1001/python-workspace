class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []  # association: teacher has students

    def add_student(self, student):
        if student.marks < 20:
            print(f"Cannot add {student.name}, marks too low ({student.marks})")
        else:
            self.students.append(student)

    def get_strength(self):
        return len(self.students)

    def count_distinction(self):
        return sum(1 for s in self.students if s.marks >= 75)

    def display_students_desc(self):
        
        def get_marks(student):
            return student.marks

        sorted_students = self.students[:]
        sorted_students.sort(key=get_marks, reverse=True)

        print(f"\n{self.name} teaches the following students (sorted by marks):\n")
        for s in sorted_students:
            s.show_details()
            print("----")


class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def get_classification(self):
        if self.marks >= 75:
            return "Distinction"
        elif self.marks >= 60:
            return "First Class"
        elif self.marks >= 50:
            return "Second Class"
        elif self.marks >= 35:
            return "Pass Class"
        else:
            return "Fail"

    def show_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Result: {self.get_classification()}")


# Example usage
teacher = Teacher("Dr. Smith")

# Add students (one below 20 will be restricted)
teacher.add_student(Student(101, "Alice", 82))
teacher.add_student(Student(102, "Bob", 55))
teacher.add_student(Student(103, "Charlie", 15))  # Should not be added
teacher.add_student(Student(104, "David", 65))
teacher.add_student(Student(105, "Eve", 78))

# Display all students in descending order of marks
teacher.display_students_desc()

# Show total strength
print(f"\nTotal strength of class: {teacher.get_strength()}")

# Count students with Distinction
print(f"Number of students with Distinction: {teacher.count_distinction()}")
