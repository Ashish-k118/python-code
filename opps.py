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

'''


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