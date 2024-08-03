#course class===========

class Course:
    def __init__(self, course_name, course_id):
        self._course_name = course_name
        self._course_id = course_id
        
    @property
    def get_course_name(self):
        return self._course_name
    
    @property
    def get_course_id(self):
        return self._course_id
    
    def __str__(self):
        return f"Course Datails Below;\n Course Name: {self._course_name}\n Course Id: {self._course_id}"
    
    
    
    
    