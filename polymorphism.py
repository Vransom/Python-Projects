class School: #parent class
    name="San Diego State University" #parent attribute
    city="San Diego" #parent attribute
    username="user@school.com"
    password="password3"

    def LoginInfo(self): #parent method
        enter_username=input("Enter username: ")
        enter_password=input("Enter password: ")
        if (enter_username==self.username and enter_password==self.password):
            print("Welcome, {}!".format(enter_username))
        else:
            print("Password or email is incorrect, please re-enter")

class Professor(School): #child class1
    professor_name="Dr. Smith" #child attribute
    teaches="Psychology" #child attribute
    username="professor@school.com"
    pincode="1234"

    def LoginInfo(self): # child1 polymorphism
        enter_username=input("Enter username: ")
        enter_pincode=input("Enter pincode: ")
        if (enter_username==self.username and enter_pincode==self.pincode):
            print("Welcome, {}!".format(enter_username))
        else:
            print("Password or email is incorrect, please re-enter")
        
class Student(School): #child class2
    student_name="Victoria Ransom" #child attribute
    major="Business" #child attribute
    active_student=False #child attribute
    username="victoriamransom@gmail.com"
    password="victoria123"
    DOB="12-4-1994"

    def LoginInfo(self): #child2polymorphism
        enter_username=input("Enter username: ")
        enter_password=input("Enter password: ")
        enter_DOB=input("Enter DOB: ")
        if (enter_username==self.username and enter_password==self.password and enter_DOB==self.DOB):
            print("Welcome, {}!".format(enter_username))
        else:
            print("Password or email is incorrect, please re-enter")


admin=School()
print(admin.LoginInfo())

professor=Professor()
print(professor.LoginInfo())

student=Student()
print(student.LoginInfo())




    
    
