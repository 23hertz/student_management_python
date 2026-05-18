from manage import Manage

class Index:
    def __init__(self):
        self.manage = Manage()

    def select_option(self):
        print("\nPlease select an option:")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Exit")

    def options(self):
            while True:
               self.select_option()
               choice = input("Enter your choice: ")

               if choice == '1':
                    self.manage.get_students_menu()

               elif choice == '2':
                    self.manage.get_course_management()

               elif choice == '3':
                    print("Exiting the program. Goodbye!")
                    break
               else:
                     print("Invalid choice. Please try again.")        

if __name__ == "__main__":
    app = Index()
    app.options()