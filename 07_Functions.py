"""
Function in Python
    Blocks of statment that perform specific task ..!
    
"""
# Simple Hello world print function
def hello(): # def is keyword it use to start a funciton #hello() is function name 
    print("Hello world ")       # inner part of function
    

hello()  # function call - excuted function and print : Hello World
hello()  # we can call function many times 
            # we dont have to write the same fucntion again and again just call fucntion we will get same output





# Paramterizised function

def sum(a, b):  #a and b is paramater / variables 
    print( a ,"+", b, "= " ,  a+b)


def minus(a, b):  #a and b is paramater / variables 
    c = a - b
    return c   # if you write return keyword 
# that you have to called the fucntion using print statment 
# because after executing task the fucntion returns values not print 



# when sum() function call that you have to pass the paramter for a & b in that parathesis

sum(4 , 5 )  #a=4 , b=5 actual values / arguments 
    # output : 4 + 5 = 9

sum(121 , 235) # a=121 , b =235 
    # output : 121 + 235 = 356
    
    
#minus
print(minus(121 , 90)) #a=121 , b=90
    #output : 31 

print(minus( 231  , 123)) #a=231 , b=123
    #output : 108
    
    
    
    
# ---calculate Avg Function----

def cal_avg( a , b, c):   #a=2 , b=2 , c=2
    sum = a + b + c      #2 +2 + 2 = 6
    return sum/3     # 6 / 3    = 2.0



print(cal_avg(2,2,2))
    #output : 2.0
    
    

# Default paramter 
    #if user does not pass the value then the function get automatically define value
    
# EX:

def cal_sum( a , b=2):   # if user pass a = 6 and not passing b then it automatically get b= 2
    return a + b 

#non-default value will be first and default value will be in the last
# if you write default function in start it get error 
    # Ex : def cal_sum ( a = 2 , b)
        #----ERROR-----


print(cal_sum(6)) #user pass a = 6 but not b then it b = 2 (default )
    #output : 8
    
print(cal_sum(6 , 5)) # if pass both value then do not get default value
    # output : 11
    
    
    
    
    




"""
Types in Fucntions

    1 . Built in Function 
        - Default function of python 
            EX: print() , input() , range() , type() , 
            
    2 . USer Defined function 
        - Write by codder / developer
            EX : sum() , minus () , cal_sum() ...etc
"""


"""
Lambda Function
    Not use for complex operations
    
        Ex : lambda a, b , c, d : Expresssion 
                no of parametes     calcultion or operation like a + b +c +d =  it return value 

"""

# EXAMPLE  : 
sum = lambda a ,b : a+b
print(sum(5,6))
    #output : 11


avg  = lambda a ,b  : (a+b)/2
print(avg(5,6))
    #output : 5.5s