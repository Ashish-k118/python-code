# kisi ek object ki multipul property or behaiver ko declear kr skte h

'''
class  ----> blue print of an object .
object ----> 


# class basic syntx-->

class class_name
"doc string"
consttructor (optionsl)
variable
methods

obj= class_name




class student:
    "student information"
    # name='Paradox'
    # age=21
    def __init__(self,name,age): # kisi bhi class ka object hold krta hai .
        self.name=name    # obj ka adresh hold karta hai
        self.age=age 
        
       # print(id(self)) # curent class ka curent adresh (refrence) ko hold kr ke rakhta hai .
       # print("consttructor callad....")
    def add(p,q):
        return p+q

obj=student("Paradoc,21")
print(id(obj))

obj2=student()
print(id(obj2))

print(dir(student))  # dender method ya magic
print(student.__doc__)
print(student.__dict__)
print(student.__base__)

print(obj)
print(obj.name)
print(obj.age)
x=obj.add(5,6)
print(x)




#  Obj ke sath agar koi value badal rahi ho to use ham inheritenc bolte hai 

instance variable

delclaration of isinstance variable
1. inside class
    1. in constructor
    2. in isinstance methods
2. outside class
    1. thorugh object (outside of the class)

    
colling : -->

1. in side class 
    use self
        1. constractr
        2. instance method
2. out-side class 
    use object


constrctor ka pahala paira metter self hota hai.







class student:
    "student information"
    def __init__(self,name,age): 
        self.name = name    
        self.age = age 
    def show_details(self):
        print(self.name)
        print(self.age)

obj=student("Paradox",21)
obj.show_details()
obj1=student("Ashish",21)
obj1.show_details()




class student:
    def __init__(self, name, age):   # declaration of instance variable
        self.name=name 
        self.age=age
        print(self.name)
    def add (self, school):    #  declaration
        self.school=school
    def show_detail(self):     # colling of declaration
        print(self.name)
        print(self.age)
        print(self.school)
        print(self.city)

obj=student("Paradox",21)
obj.add ('SHSC')
# obj.show_detail()
print(obj.name)    # colling
obj.city='bhopal'
obj.show_detail()



# static varible (class varible ) 
# :- jo object upar declare nhi hota hai use ham static ya phir class name bolte hai. 
# static value kabhi cheng nhi hoti hai. 

    1. declare (colling):
        1. in-side class 
            1. out-side method
            2. in-side constroctor
            3. in-side isinstance method     # through class name

        2. out-side class    #(through class name)

        

 
class student:
    "student infromation" 
    school= "SHSC"
    def _init_(self, name, age):
        self.name=name
        self.age=age
        student.city ="bhopal"
    def add_details(self):
        student.school_code=101
obj=student("Paradox",21)
student.principal="indra bahadur"





class student:
    school= "SHSC"
    def _init_(self):
        student.city ="bhopal"
        print(student.school)
    def add(self):
        student.code=101
        print(student.school)
        print(student.city)
    def show_details(self):
        print(student.code)
        print(student.principal)

obj=student()
student.principal='new123'
obj.add()
obj.show_details()
print(student.school)




class Student:
    "Student Information"
    school = "SHSC"                         # declaration of static variable in side class but outside of the mehtod.......
    def _init_(self,name,age):
        self.name = name
        self.age = age
        Student.city = "Bhopal"             # declaration of static variable inside constrctor.......
        print("Calling inside of Constructor = ",Student.school)               # calling of static variable.......
    def add_detail(self):
        Student.school_code=101             # declaration of static variable inside instance method.......
        print("Calling inside of instance method = ",Student.school)               # calling of static variable.......
        print("Calling inside of instance method = ",Student.city)                 # calling of static variable.......
    def show_detail(self):
        print(Student.school)
        print(Student.city)
        print(Student.school_code)
        print("Calling inside of instance method = ",Student.principal)
        
obj = Student("Paradox", 21)
print("My_City=",Student.city)
print("My_School=",Student.school)
obj.add_detail()
print("School_code=",Student.school_code)
Student.principal = "Indra Bahadur"        # declaration of static variable.......
obj.show_detail()









# local scop :

x=10
class student:
    x=50
    def add(self):
        print(x)
        x=20
        print(x)
obj=student
print(x)
obj.add()
print(x)





x=50                   # Global
class student :
    global x
    x='paradox'
    def add ():
        print(x)
        y=20
        print(y)
    def add1():
        print(x)
obj=student
obj.add()
obj.add1()
print(x)

'''



x=10
class cybrom:
    global x
    x=54
    def add():
        print(x)
        y=100
        print(y)
    def add1():
        print(x)
obj=cybrom
obj.add()
obj.add1()
print(x)
