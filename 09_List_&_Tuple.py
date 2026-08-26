"""
List in Python 
    * mutable sequence of values ( it can be change)
        --list is like an Arry

"""
# EX
marks = [98,89,69,87,88] #--for list we use [square brackets]
# idx  = 0  1  2   3  4

print(marks)          #output : [98, 89, 69, 87, 88]
print(len(marks))     #output : 5
print(marks[3])       #output : 87


# in list we can stored multiple data types data
# Ex
info = ["student" , 98, 47, 54, 69, 87 , 96.55 , "male"]



"""
In List we can perfrom Slicing ....
            list[strt_idx : end_idx  ]  -- end_idx not included [ if you pass 5 then it get the word is 4 ]
    Example :
        like word =  
            info = ["student" , 98, 47, 54, 69, 87 , 96.55 , "male"]
            #           0       1   2   3   4   5      6        7     in idx 2 - 47 , idx 7 -"male" 
    
        str[ 2 : 4]             : output - [47 , 54]    


"""

"""

List methods : 
    1.  l.append(val)               --Add one element at the end
    2.  l.insert(idx , value)       --insert element at idx
    3.  l.sort()                    --arranges in increasing order
    4.  l.reverse()                 --reverse order
"""

# EX : 

nums = [ 1 , 2 , 3 ]


nums.append(4)   #adding one element at end.
print(nums)      #output : [ 1 , 2 , 3 , 4]

nums.insert(2,10)   #insert element at idx 
print(nums)         #at index 2 stored 10 : output - [1 , 2 , 10 , 3 , 4]

nums.sort()      #sorted on assending order
print(nums)      # output : [ 1 , 2 , 3 , 4 , 10]


nums.sort(reverse = True)      #sorted on desending order
print(nums)      #               output : [10, 4, 3, 2, 1]

nums.reverse()   # reversed that value
print(nums)       #output : [ 10, 4, 3, 2, 1]




# Loops in List
    # for going to serach every idx
    
    
#Ex :  using for loop search the 10 ( on which index that are available)

x = 10 
idx = 0
for val in nums:
    if(val == x):
        print(f"No {x} found on index {idx} ")
        break
    idx+=1
    
    


# "******************************************************"
"""
Tupes in Python 
    inmutables sequence in values ( not chnages )

"""
tup = ( 1,2,3,4)  #--for tuple we use (round brackets)
tup2 = (1,  2 ,3 , 4 , "abc" , 56.36 ) # we can stored multiple values on tuple 
                                        #list list but list can change but tuple not 

print(len(tup))   #length - 4       :output - 4
print(type(tup))  # type is tuple   :output - <class 'tuple'>
print(tup)        # values in tuple :output - (1 , 2 ,3 ,4)


# also we can access the number using index
print(tup[2])     # accessing the idx value  : ouput - 3

# But does not assign value to tuple
# if we try to do :
# tup[2] = 10
# --ERROR   :    File "D:\AIML\01_PYTHON\09_List_&_Tuple.py", line 105, in <module>
                #     tup[2] = 10
                #     ~~~^^^
                # TypeError: 'tuple' object does not support item assignment
                
                
                
# for tuple if we do as a single value in tuple
# it give the that value type not give the type tuple
#------EX :
tup3 = (1) # it consider as a int value not a tuple 
        # output : <class 'int'>
tup4 = ("Abc") #it consider a string value not a tuple
          # output : <class 'str'> 
# or if we write 
# After elment add comma it tell the tuple there are multple value in that tuple 
# so it can consider as a tuple ( comma is important in tuple)
tup3 = (1 , ) # it consider as a tuple not int 
      # output : <class 'tuple'>
tup4 = ("Abc" ,) #it consider a tuple not a string 
      # output : <class 'tuple'>

"""
we can also perform slicing and loop on tuple like list
"""
"""
Method in tuples:
    1. t.index(val)   --returns 1st occurence idx
    2. t.count(val)   --counts total occurrences



    1. t.index(val) 
        - if in that tuple same values is in mutiples times then it return their first apperance
            Ex: tup = ( 1,2,3,2,3,4,2,5,6,8)    #in that tuple no. 2 is 3times
            but the t.index(val) --return the 1st apperance of 2 at index 1
            
            
    2. t.count(val) 
        - if in that tuple same values is in mutiples times then it return count of the apperrance
            Ex: tup = ( 1,2,3,2,3,4,2,5,6,8)    #in that tuple no. 2 is 3times
            but the t.count(val) --return the 3 as a no.2 count
"""
tup = ( 1,2,3,2,3,4,2,5,6,8)
print(tup.index(2)) 
    #output: 1
    
print(tup.count(2))
    #output : 3