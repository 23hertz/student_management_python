# from students import Students   
from student_management import Student_management
from course_management import Course_management
class Manage:
    def __init__(self):
        self.student = Student_management()
        self.course = Course_management()

    def get_students_menu(self):                                 
        self.student.students_menu()

    def get_course_management(self):
        self.course.course_menu()
    
  






    
    # def course_management(self):
    #     while True:        
    #       self.course.course_option()
    #       print("Running course management system...")
          
    #       course_options = int(input('Select course activities'))

    #       if course_options == '1':
    #           self.course.view_courses()
    #       elif course_options == '2':
    #           self.course.add_course()
    #       else:
    #           print("Wrong")
              
              
              
              
              
    

