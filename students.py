import json
class Students:
        def __init__(self):
             self.students = []
             self.load_students()

        def get_input(self):
            get_name = input("Enter student name: ")
            if not get_name.strip():
                print("Name cannot be empty. Please try again.")
                return self.get_input()
            elif any(char.isdigit() for char in get_name):
                print("Name cannot contain numbers. Please try again.")
                return self.get_input()
            elif any(not char.isalpha() and not char.isspace() for char in get_name):
                print("Name cannot contain special characters. Please try again.")
                return self.get_input()
            elif len(get_name) < 2:
                print("Name must be at least 2 characters long. Please try again.")
                return self.get_input() 
            elif len(get_name) > 50:
                print("Name cannot be longer than 50 characters. Please try again.")
                return self.get_input()
            elif get_name.isspace():
                print("Name cannot be just whitespace. Please try again.")
                return self.get_input()
            elif get_name.lower() in ["admin", "root", "superuser"]:
                print("Name cannot be a reserved word. Please try again.")
                return self.get_input()
            elif get_name.lower() in ["null", "undefined", "none"]:
                print("Name cannot be a null value. Please try again.")
                return self.get_input()
            elif get_name.lower() in ["test", "testing"]:
                print("Name cannot be a test value. Please try again.")
                return self.get_input()
            elif get_name.lower() in ["example", "sample"]:
                print("Name cannot be an example value. Please try again.")
                return self.get_input()
            elif get_name.lower() in ["unknown", "anonymous"]:
                print("Name cannot be an unknown value. Please try again.")
                return self.get_input()
            elif get_name.lower() in ["default", "placeholder"]:
                print("Name cannot be a default value. Please try again.")
                return self.get_input()
            elif get_name.lower() in ["user", "username"]:
                print("Name cannot be a generic user value. Please try again.")
                return self.get_input()
            elif get_name.lower() in ["guest", "visitor"]:
                print("Name cannot be a guest value. Please try again.")
                return self.get_input()
            elif get_name.lower() in ["admin", "administrator"]:
                print("Name cannot be an administrator value. Please try again.")
                return self.get_input() 
          
            get_gender = input("Enter student gender: ")
            if not get_gender.strip():
                print("Gender cannot be empty. Please try again.")
                return self.get_input() 
            elif get_gender.lower() not in ["male", "female"]:
                print("Gender must be 'male' or 'female '. Please try again.")
                return self.get_input()     
            elif get_gender.isspace():
                print("Gender cannot be just whitespace. Please try again.")
                return self.get_input() 
            elif get_gender.lower() in ["unknown", "unspecified"]:
                print("Gender cannot be an unknown value. Please try again.")
                return self.get_input() 
            elif get_gender.lower() in ["other", "non-binary"]:
                print("Gender cannot be a non-binary value. Please try again.")
                return self.get_input() 
          

            get_course = input("Enter student course: ")
            if not get_course.strip():
                print("Course cannot be empty. Please try again.")
                return self.get_input() 
            elif get_course.lower() not in ["english", "math", "science", "history", "art"]:
                print("Course must be one of the following: English, Math, Science, History, Art. Please try again.")
                return self.get_input()
            elif any(char.isdigit() for char in get_course):
                print("Course cannot contain numbers. Please try again.")
                return self.get_input() 
            elif any(not char.isalpha() and not char.isspace() for char in get_course):
                print("Course cannot contain special characters. Please try again.")
                return self.get_input() 
            elif len(get_course) < 2:
                print("Course must be at least 2 characters long. Please try again.")
                return self.get_input() 
            elif len(get_course) > 50:
                print("Course cannot be longer than 50 characters. Please try again.")
                return self.get_input() 
            elif get_course.isspace():
                print("Course cannot be just whitespace. Please try again.")
                return self.get_input() 
            elif get_course.lower() in ["admin", "root", "superuser"]:
                print("Course cannot be a reserved word. Please try again.")
                return self.get_input() 
            elif get_course.lower() in ["null", "undefined", "none"]:
                print("Course cannot be a null value. Please try again.")
                return self.get_input() 
            elif get_course.lower() in ["test", "testing"]:
                print("Course cannot be a test value. Please try again.")
                return self.get_input() 
            elif get_course.lower() in ["example", "sample"]:
                print("Course cannot be an example value. Please try again.")
                return self.get_input() 
            elif get_course.lower() in ["unknown", "anonymous"]:
                print("Course cannot be an unknown value. Please try again.")
                return self.get_input() 
            elif get_course.lower() in ["default", "placeholder"]:
                print("Course cannot be a default value. Please try again.")
                return self.get_input() 
            elif get_course.lower() in ["user", "username"]:
                print("Course cannot be a generic user value. Please try again.")
                return self.get_input() 
            elif get_course.lower() in ["guest", "visitor"]:
                print("Course cannot be a guest value. Please try again.")
                return self.get_input() 
            elif get_course.lower() in ["admin", "administrator"]:
                print("Course cannot be an administrator value. Please try again")
                return self.get_input()
       

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
        
    