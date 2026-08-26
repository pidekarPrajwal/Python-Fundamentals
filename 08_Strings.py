"""

--- Strings In Python------ 
    -String is the sequence of character 
        Ex : "Python "  : P , y , t, h, o , n is character also in that dubble quotes spaces is also a charcter
    
    ** Strings Are Immutable ** (once you defined you cannot changes)
    
    = we can do multiple opeartion on string
        * len          - calculated length of word 
        * concatenate  -  joing the both string 
        * indexing     -  showing their places / position { it starts from 0}
""" 

# Strings
word = "Python" 
word2 = "is good "

# length
print(len(word))        #print the length of wrod : output - 6
print(len(word2))      # space also consider as a char:  output - 8 ( alphabet = 6 + 2 spaces )

# concate - joing the string
print(word + " " + word2) # word and word2 both are different string 
                            # for concate we have to use + sign 
                            # output: Python is good


# Indexing - to perform operation on that specific character
    # it starts form 0
    # like word = p y t h o n 
             #    0 1 2 3 4 5    = length : 6
             
             
    # For indexing we have to use [ sqaure brackets ] 

print(word[2])  #Output : t 
# print word of index 2 = is t  


# print whole python charcter using for loop 

for i in word:
    print(i)
    
    
    
"""
Slicing in String
        - it used cut the string in parts 
        
    Ex : like in python word we have to use only to words then we use slicing.

    
    --- 
        str[strt_idx : end_idx  ]  -- end_idx not included [ if you pass 5 then it get the word is 4 ]
    Example :
        like word = p y t h o n 
            #       0 1 2 3 4 5    =  in idx 2 - t , idx 3 -h idx 4 - o but ( 4 is not included it will print on 3)
    
        str[ 2 : 4]             : output - th      
"""

print(word[2:4]) # output - th
print(word[2:])  # if we not pass ending idx it consider string last idx ( by default)


 
 
"""
string formating
        - dynamic string ( variable & values)
        
        
        1 . format()
        2 . f-strings ---most mordern use
EX:
"""


a=5
b=9
c=a+b

# normal formatting
print("sum is " , c) #old method ( using comma (,) to seprate the words)

# using format() 
print("sum is {}".format(c))

# for variable 
print("{} is to easy..".format("python"))


# For multiple placeholders 
print("sum {} and {} is {}".format(a,b,c))





#------------f-strings
    # Literal string interpolation
    
    
# EX 
print(f"sum of {a} and {b} is {c} ")
    # - only we have to use f before string and directly add varible into the brackets 
        # it automatically replace by this variables 