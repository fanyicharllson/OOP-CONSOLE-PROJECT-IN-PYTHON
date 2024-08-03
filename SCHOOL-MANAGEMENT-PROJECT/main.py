#main.py==========

from student import Student
from course import Course
from teacher import Teacher
from school import School

#creating student instance
student1 = Student("Sam", "S001", ["ICT", "Math", "English"])
student2 = Student("Enna", "S002", ["Computer Science", "Math", "Geography"])
student3 = Student("Peter", "S003", ["History", "Economics", "Literature"])

#student1 enrollingfor a course
student1.enroll_course("Economics")

#printing info about courses
print(student1)

#drop course
student1.drop_course("Math")
print(student1)

#creating course instance
course1 = Course("Math", "C001")
course2 = Course("Computer Science", "C002")
course3 = Course("History", "C003")
course4 = Course("Economics", "C004")


#creating teacher instance
teacher1 = Teacher("George", "T001", ["ICT", "Math", "English"]) 
teacher2 = Teacher("John", "T002", ["Computer Science", "Math", "Geography"]) 
teacher3 = Teacher("Kenneth", "T003",["History", "Economics", "Literature"] ) 
teacher4 = Teacher("Daneal", "T004", ["Civics", "Citizenship", "Moral Education"]) 

#displaying teacher  information
print(teacher2)

#adding course to teacher
teacher1.add_teacher_course("Moral Education")
print(teacher1)

#removing course from teacher
teacher4.remove_teacher_course("Citizenship")
print(teacher4)


#creating school instance
school = School()

#adding student to  school
school.addStudent(student1)
school.addStudent(student2)
school.addStudent(student3)

#removing student from school
school.removeStudent("Peter")

#adding teacher to school
school.addTeacher(teacher1)
school.addTeacher(teacher2)
school.addTeacher(teacher3)
school.addTeacher(teacher4)

#removing teacher from school
school.removeTeacher("John")

#adding course to school
school.addCourse(course1)
school.addCourse(course2)
school.addCourse(course3)
school.addCourse(course4)

#removing course from school
school.removeCourse("Math")

