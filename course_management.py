from course import Course
class Course_management:
    def __init__(self):
        self.courses = Course()
        self.course = [] 

    def select_course_menu(self):
        print("\nStudent Management System")
        print("1. View Courses")
        print("2. Add Course")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Back to Main Menu")
    
    def course_menu(self):
        while True:
            self.select_course_menu()
            choice = input("Select course options: ")

            if choice == '1':
                self.courses.view_courses()
            elif choice == '2':
                self.courses.add_course()
            elif choice == '3':
                self.courses.update_course()
            elif choice == '4':
                self.courses.delete_course()
            elif choice == '5':
                print("Returning to main menu")
                break
            else:
                print("Invalid choice. Please try again.")

