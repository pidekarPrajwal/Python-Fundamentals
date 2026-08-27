"""
Dictinary 
    ----- Key : value (pairs)  
        # like json data 
    
# key : always been unique 
# for creating a dictary we use { curely bracess }
# ******* is muttable  ( can change )
#Dict is unorder - not using any index in dic

    EX: 
        dict = {
            
            "name"     : "prajwal"     #name is key -  prajwal is assign value of that key
            "subject"  : "python"       #subject is a key
            "age"      : 24
            "salary    : 00.00 
        } 
        #in dictinary we can stored mutiple data types values 
            #using comma we seperated the key ( , )

                # aslo we can stored list & tuple in that dict
                
                EX: 
                    dict ={           
                    "name"     : "prajwal"     #String
                    "subject"  : "python"      #String
                    "age"      : 24            #int
                    "salary    : 00.00          #float
                    "marks"    : [32 , 65 , 98 , 87 , 22]  #list
                    "other_info" : (21 , "player" ,65.65)  # tuple
                } 
            
            # using the keys we access their values
            
"""

    # EX: 
dict ={           
    "name"     : "prajwal"   ,  #String
    "subject"  : "python"    ,  #String
    "age"      : 24          ,  #int
    "salary"    : 00.00        ,  #float
    "marks"    : [32 , 65 , 98 , 87 , 22],  #list
    "other_info" : (21 , "player" ,65.65) , # tuple
} 
            
print(dict["name"])
    #output : Prajwal
    
print(dict["age"])
    #output : 24
    
print(dict["marks"])
    #output : [32 , 65 , 98 , 87 , 22]
    
# Can also access their specific values on tuple or list
print(dict["marks"][1])
    #output : 65 
    
print(dict["other_info"])
    #output : (21, 'player', 65.65)
    
    
    
    
    
    
"""
Methods in Dictinary
    
        1. d.keys()                   --returns all keys
        2. d.values()                 --return all values 
        3. d.items()                  --returns ( key , value )pairs
        4. d.get(val)                 --return val access to key
        5. d.update(new_item)         --Adds new item to dict
        


"""

# We we have to print all keys from dict
    # d.keys()
print(dict.keys())
    # output : dict_keys(['name', 'subject', 'age', 'salary', 'marks', 'other_info'])

# We we have to print all values from dict
    # d.values()
print(dict.values())
    # output : dict_values(['prajwal', 'python', 24, 0.0, [32, 65, 98, 87, 22], (21, 'player', 65.65)])

# We we have to print all keys and values pairs from dict
    # d.items()
print(dict.items())
    # output : dict_items([('name', 'prajwal'), 
                        # ('subject', 'python'), 
                        # ('age', 24), ('salary', 0.0), 
                        # ('marks', [32, 65, 98, 87, 22]), 
                        # ('other_info', (21, 'player', 65.65))
                        # ])
                        
                        
#  if we have to not stop excution of code after 
    # if any value not in the dict
        # then we use get()method
        
# For example    
    # d.get()
print(dict.get("name"))         # if key is present then it show values also 
print("Succesfully got")        # also excute next stament 
    #output : Prajwal
    #           Successfully got
    
    
#  if we dont use get() method
# print(dict["name2"])         # if key is not present then it show Error 
print("Succesfully got")        # also not excute next stament 
    #output :  File "D:\AIML\01_PYTHON\10_Dict_&_Set.py", line 115, in <module>
            #     print(dict["name2"])         # if key is present then it show values also
            #         ~~~~^^^^^^^^^
            # KeyError: 'name2'
            

# But if we use get method 
print(dict.get("name2"))         # if key is not present then it show none  
print("Succesfully got")        # also excute next stament 
        #output : None
        #Successfully got
# ******* it not stop to excuted next stament it returns null not a erorr



# We we have to add  any keys and values pairs from dict
    # d.update({key_value})

dict.update({
    "city" : "Pune"
})
    #adding new key value pair in dict 

print(dict)
    #output :{'name': 'prajwal', 
            # 'subject': 'python', 
            # 'age': 24, 
            # 'salary': 0.0, 
            # 'marks': [32, 65, 98, 87, 22], 
            # 'other_info': (21, 'player', 65.65),
            # 'city': 'Pune'            # new key_value pair in list
            # }
            
            
            
            
"""
---------------- SETS ----------------------
    Collection of unique elements 
        - The set is mutalbe but the values in that set are immutable  
        #it stors only immutable  (eg. Strings, numbers, floating_values , tuples ) 
            # list and dict is not stores ( because it muttable ( it can change ))

    - In SETS no duplicated value will be stored 
        If in the SETS = { 1 , 2 , 3 , 2 , 2 , 4 , 5}
            #output : {1, 2, 3, 4, 5}
            
    - In set no order followed ( sets are unordered )

"""
SETS = { 1 , 2 , 3 , 2 , 2 , 4 , 5}

print(SETS)         # output :{1, 2, 3, 4, 5} # duplicate not allowed 
print(len(SETS))    #output  : 5   # in set 7 elements are there but 2 are duplicate that why cont is 5



# if we can creted an empty set 
# then we have to write

empty_set = set()  # its can empty set
print(type(empty_set))
    #output : <class 'set'>
    
# if we try to do like
empty_set1 = {} # it is not an empty set it is an empty dictinary
print(type(empty_set1))
    #output : <class 'dict'>
    
    
    





"""
Methods in Dictinary
    
        1. s.add(val)                    --adding a value in sets
        2. s.remove(val)                 --removed the value from sets all values 
        3. s.clear()                     --empties the set
        4. s.pop()                       --removed the random vlaue 
        5. s.union(set2)                 --returns a new union
        6. s.intersection(set2)          --returns a new intersection
        


"""


# We have to add values in set
    # s.add()
SETS.add(6)     # adding 6  in sets 
print(SETS)
    # output : {1, 2, 3, 4, 5, 6}


# We  have to removed  values in set
    # s.remove()
SETS.remove(2)     # removed 2 in sets 
print(SETS)
    # output : {1, 3, 4, 5, 6}
    
    
# We have empty the set ( clear all the set )
    # s.clear ()
# SETS.clear()          # removed all values form  sets 
print(SETS)
    # output : set()
    
    
    
# We have removed an any randome value from set 
    # s.pop()
SETS.pop()          # removed randome value from set
print(SETS)
    # output : {3, 4, 5, 6}
    
    
    
    
# -------- instersection & union

# if the two sets avabile like
SETS1 = { 1 , 2 , 3 , 4 , 5 , 6}
SETS2 = { 5 , 6  , 7 , 8 , 9 , 10}

# In that sets Intersections means (those value that value present in both sets)
    # EX
print(SETS1.intersection(SETS2))
    #output : {5, 6} present in both
    
# In that get all elemtents from both sets to use union()
    # EX
print(SETS1.union(SETS2))
    #output : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} # no duplicate 