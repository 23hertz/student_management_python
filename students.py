import json
class Students:
        def __init__(self):
             self.students = []
             self.load_students()

        def get_input(self):
            get_name = input("Enter student name: ")
            get_gender = input("Enter student gender: ")
            get_course = input("Enter student course: ")

            
            student_data = {
                "name": get_name,
                "gender": get_gender,
                "course": get_course
            }
            return student_data
        
        def save_students(self):
            with open("students.json", "w") as file:
                json.dump(self.students, file, indent=4)

        def add_student(self):
            student = self.get_input()
            self.students.append(student)
            self.save_students()
            print("Student created successfully.")

        def view_student(self):
             if not self.students:
                print("No students found.")
             else:
                for index, student in enumerate(self.students, start=1):
                    print(f"\nStudent {index}")
                    print(f"Name: {student['name']}")
                    print(f"Gender: {student['gender']}")
                    print(f"Course: {student['course']}")        

        def update_student(self):
            if not self.students:
                print("No students to update.")
            else:
                self.view_student()
                try:
                    student_index = int(input("Enter the student number to update: "))
                    if 1 <= student_index <= len(self.students):
                        print(f"Updating information for Student {student_index}")
                        updated_student = self.get_input()
                        self.students[student_index - 1] = updated_student
                        self.save_students()
                        print("Student information updated successfully.")
                    else:
                        print("Invalid student number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid student number.")
    
        def delete_student(self):
            self.view_student()
            if not self.students:
                print("No students to delete.")
            else:
                try:
                     
                    student_index = int(input("Enter the student number to delete: "))
                    if 1 <= student_index <= len(self.students):
                        deleted_student = self.students.pop(student_index - 1)
                        self.save_students()
                        print(f"Student '{deleted_student['name']}' deleted successfully.")
                    else:
                        print("Invalid student number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid student number.")
        
        def load_students(self):
            try:
                with open("students.json", "r") as file:
                    self.students = json.load(file)
            except FileNotFoundError:
                self.students = []
        
    