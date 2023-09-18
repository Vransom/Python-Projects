class School: #parent class
    name="San Diego State University" #parent attribute
    city="San Diego" #parent attribute

    def info(self): #parent method
        msg="\nThis school is: {}\nLocated in: {}".format(self.name,self.city)
        return msg

class Professor(School): #child class1
    professor_name="Dr. Smith" #child attribute
    teaches="Psychology" #child attribute
    username="professor@school.com"
    password="password"

    def ProfessorLogin(self): # child1 polymorphism
        prof_username=input("Enter username: ")
        prof_password=input("Enter password: ")
        if (prof_username==self.username and prof_password==self.password):
            print("Welcome, {}!".format(professor_name))
        else:
            print("Password or email is incorrect, please re-enter")
        
class Student(School): #child class2
    student_name="Victoria Ransom" #child attribute
    major="Business" #child attribute
    active_student=False #child attribute
    susername="victoriamransom@gmail.com"
    spassword="victoria123"

    def StudentLogin(self): #child2polymorphism
        student_username=input("Enter username: ")
        student_password=input("Enter password: ")
        if (student_username==self.susername and student_password==self.spassword):
            print("Welcome, {}!".format(student_name))
        else:
            print("Password or email is incorrect, please re-enter")


professor=Professor()
print(professor.ProfessorLogin())
    
    
