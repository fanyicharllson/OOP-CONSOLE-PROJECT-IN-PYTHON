#school class===========
class School:
    name = "THE COLLEGE UNIVERSITY"
    
    def __init__(self):
        self.studentDatabase = []
        self.teacherDatabase = []
        self.courseDatabase = []
    
    #adding student to school
    def addStudent(self, student):
        self.studentDatabase.append(student)
        print("\n\t Student added to school")
    
    #removing student from school
    def removeStudent(self, student_name):
        for student in self.studentDatabase:
            if student._name == student_name:
                self.studentDatabase.remove(student)
                print(f"\n\t {student._name} removed from school!")
                return
            print(f"\n\t No such student in {School.name}")
    
    #adding teacher to school
    def addTeacher(self, teacher):
        self.teacherDatabase.append(teacher)
        print("\n\t Teacher added to school")
    
    #removing teacher from school
    def removeTeacher(self, teacher_name):
        for teacher in self.teacherDatabase:
            if teacher._teacher_name  == teacher_name:
                self.teacherDatabase.remove(teacher)
                print(f"\n\t {teacher._teacher_name } removed from {School.name}")
                return
            print("No such teacher found!")
    
    #adding course to school
    def addCourse(self, course):
        self.courseDatabase.append(course)
        print("\n\t Course added to school")
    
    #removing course from school
    def removeCourse(self, course_name):
        for course in self.courseDatabase:
            if course._course_name == course_name:
                self.courseDatabase.remove(course)
                print(f"\n\t {course._course_name} removed from school!")
                return
            print("No course found to be remove!")
                        
                
                       
    