from students import Students   

class Manage:
    def __init__(self):
        self.student = Students()

    def select_option(self):
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Back to Main Menu")
    
    def student_management(self):
         while True:
            self.select_option()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.student.add_student()
            elif choice == '2':
                self.student.view_student()
            elif choice == '3':
                self.student.update_student()
            elif choice == '4':
                self.student.delete_student()
            elif choice == '5':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice. Please try again.")    

    
    def course_management(self):
        print("Running course management system...")
    

