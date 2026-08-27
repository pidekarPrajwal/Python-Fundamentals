"""
OOP
    - Object oriented programming langauge
    
    
    `Classes & objects
        Class is a blue print of object
        object is an instance of class

    For creating the class we have to use class keyword 
    EX:
        class Student:   # student is an class name (class name is start from upppercase)

"""



# EX

# Class {blueprint}
class Student :
    subject = "python" #properties
    college = "ABCED"
    year    = "2nd"

a= 10
stu1 = Student()

# we can create multple object for one class ( in all object stored same data )
stu2 = Student()
stu3 = Student()
print(stu1) #output: <__main__.Student object at 0x0000024F01245790>
print(stu1.subject) #output : Python


print(stu2) #output: <__main__.Student object at 0x0000024F01245790>
print(stu2.college) #output : Python


print(stu3) #output: <__main__.Student object at 0x0000024F01245790>
print(stu3.year) #output : Python

#stu1 is the instance of an student class  ( it can access whole student class) 
#stu2 is the instance of an student class 
#stu3 is the instance of an student class 





"""
Constructor
    __init_() Method - its also called constructor
    - for use to intialse our object
    
    
    - if we dont created a constructor then python created itself
    
    -self() 
        - stored the current instance of the class ( current obeject  )
    

"""
# Stored the name for object

class Students:
    
    def __init__(self , name):
        self.name = name
        
stu11 = Students("Rahul")
stu22 = Students("Raj")
stu33 = Students("Kunal")

print(stu11.name) 
# output : Rahul

print(stu22.name) 
# output :  Raj

print(stu33.name) 
# output : Kunal 



# In last class we dont use constructor so for every student name is same 
# now after use constructor we can give the name to that specific user




"""
Types of Constructor

    1 . Default   
    2 . Parameterized 
    
    
    
    1 . Default    
        In the constructor only self paramter present
        
    2 . Parameterized 
        In the constuctor more paramter with the self 
        
        '''
        In the Python we dont pass multiple paramters in one class 
        its not allowed in python 
        '''
"""




 



