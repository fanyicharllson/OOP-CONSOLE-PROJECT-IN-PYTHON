#teacher class=====
class Teacher:
    def __init__(self, teacher_name, teacher_id, teacherCourse):
        self._teacher_name = teacher_name
        self._teacher_id = teacher_id
        self._teacherCourses = teacherCourse
   
    
    @property
    def get_teacher_name(self):
        return self._teacher_name
    
    @property
    def get_teacher_id(self):
        return self._teacher_id
    
    @property
    def get_teacherCourses(self):
        return self._teacherCourses
    
    #adding teacher courses
    def add_teacher_course(self, course):
        self._teacherCourses.append(course)
        print(f"\n\t Mr.{self._teacher_name} added the course {course}.")
        
        
    #remove teacher courses
    def remove_teacher_course(self, teacher_course):
        for course in self._teacherCourses:
            if course == teacher_course:
                self._teacherCourses.remove(course)
                print(f"\n\t {self._teacher_name}  removed the course {teacher_course}")  
                return
            print(f"\n\t No such course {teacher_course} found!") 
        
        
    
    def __str__(self):
        return f"\n\n\tMr. {self._teacher_name} Infomation:\n Teacher Name: {self._teacher_name}\n Teacher Id: {self._teacher_id}\n Teacher's Courses: {self._teacherCourses}\n"    
    