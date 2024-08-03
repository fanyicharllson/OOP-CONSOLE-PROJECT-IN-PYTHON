#student class====================

class Student:
    def __init__(self, name, student_id, courses):
        self._name = name
        self._student_id = student_id
        self._courses = courses
    @property
    def get_name(self):
        return self._name
    @property
    def get_student_id(self):
        return self._student_id
    @property
    def get_courses(self):
        return self._courses
    
    
    def enroll_course(self, course):
        self._courses.append(course)
        print(f"\n\t{self._name} enrolled in {course}")
        
    
    def drop_course(self, course_name):
        for course in self._courses:
            if course == course_name:
                self._courses.remove(course)
                print(f"\n\t{self._name} dropped {course_name}")
                return
            print(f"{self._name} did not enrolled in {course_name}")
        
            
    
    def __str__(self):
        return f"{self._name} Information:\n Name: {self._name}\n Student ID: {self._student_id}\n Course: {self._courses}\n"     
    
    