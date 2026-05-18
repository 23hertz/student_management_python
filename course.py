import json


class Course:
    def __init__(self):
        self.courses = []
    

    def get_course(self):
        course_code = input("Enter course code: ")
        course_title = input("Enter course title: ")
        # course_info = f"{course_code}: {course_title}"
        # self.courses.append(course_info)

        course_data = {
            "course_code": course_code,
            "course_title": course_title    
        }
        return course_data

    def save_courses(self):
        with open("courses.json", "w") as file:
            json.dump(self.courses, file, indent=4)
        
    def add_course(self):
        course = self.get_course()
        self.courses.append(course)
        self.save_courses()
        print("Course added succcessfully.")

    def view_courses(self):
        if not self.courses:
            print("No course found.")
        else:
            for index, course in enumerate(self.courses, start=1):
                print(f"\nCourse {index}")
                print(f"Course Code: {course['course_code']}")
                print(f"Course Title: {course['course_title']}")    
    
    def update_course(self):
        if not self.courses:
            print("No courses to update.")
        else:
            self.view_courses()
            try:
                course_index = int(input("Enter the course number to update: "))
                if 1 <= course_index <= len(self.courses):
                    print(f"Updating information for Course {course_index}")
                    updated_course = self.get_course()
                    self.courses[course_index - 1] = updated_course
                    self.save_courses()
                    print("Course information updated successfully.")
                else:             
                    print("Invalid course number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid course number.")

    def delete_course(self):
        self.view_courses()
        if not self.courses:
            print("No course to delete.")
        else:
            try:
                course_index = int(input("Enter the course number to delete: "))
                if 1 <= course_index <= len(self.courses):
                    deleted_course = self.courses.pop(course_index - 1)
                    self.save_courses()
                    print(f"Course '{deleted_course['course_code']}' deleted successfully.")
                else:
                    print("Invalid course number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid course number.")

    def load_courses(self):
        try:
            with open("courses.json", "r") as file:
                self.courses = json.load(file)  
        except FileNotFoundError:
            self.courses = []