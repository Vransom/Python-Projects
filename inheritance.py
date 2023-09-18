class School: #parent class
    name="San Diego State University" #parent attribute
    city="San Diego" #parent attribute

class Professor(School): #child class1
    professor_name="Dr. Smith" #child attribute
    teaches="Psychology" #child attribute

class Student(School): #child class2
    student_name="Victoria Ransom" #child attribute
    major="Business" #child attribute
    active_student=False #child attribute
    
    
