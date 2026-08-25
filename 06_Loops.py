"""
Loops in Python 

    Loops is used for performing the same task again and again 
    
    Types of Loops :
    1. While Loop 
    2. For Loop


    
""" 

#While Loop 
count = 1   #iterator  --- who strats the loop 
while( count <= 5 ):
    print ( count )
    count +=1  # main condition for increasing the count and sending to the while loop 
    # if this condition not write the loop will print for inifinte times

# output : 1
#          2
#          3
#          4
#          5



# Print multiplication table using while loop 


n = int(input("Enter the number for multiplication: ")) #Enter number that number multplication table you want 

i = 1  # loop starts form 1 
while (i <=10 ):  # check i is greater than equal to 10 -- true
    print ( n , "X" , n * i ) # then print ( n means that number user enter ( example : 2 ))
    i+=1  
                            
                            
                             # n X 2*i ( i means 1 then ) output will be 2 X 2 
            # ( i+=1 ) increase the i value it become 2 
                            
            #chek conditions entering the loop in print statment now i value is 2 
                    # n X 2*i ( now i is 2 ) output wil be 2 X 2*2 = 4 .......
                    #loops continues while i <=10 if i value is 11 loop will be terminated
                    
                    
                    
"""
Keywords in Loop 

    1 . Break 
    2 . continue
    
    
    1. Break    :  Terminated the loop
    2. continue : Skip the conditon on that loop 
"""

# Break Example 

i = 1 
while ( i <= 10 ):
    print(i)
    if i == 6 :
        break  # terminated the loop ( when i == 6 then loop will be terminated...)
    i+=1   # no next step follow 


# Skip Example

i = 1 
while ( i <= 10 ):
    if i == 3 :
        i+=1  # after condtion true the we have to increase the value of i 
        continue  # skip the condition  ( when i == 3 then loop will be skip 3 and print other values )
    print(i)
    i+=1    



"""
for loop : 


"""
name = "Hello "
#in = membership  opetator ( tracking the sequence )

for var in name :   #Getting the word of Hello and stored in memory of one word using in operator 
    print(var)




# For numbers 

for i in range(5):   #in starts from 0 
    print(i + 1)        
    
    
    
    
    
    
    
# range function : generted Seqences 

# range ( start, stop , step )  
        # Start and step is optional but stop is compulasory
        # if you write  i in range(5) then 5 is stop value - the loop terminated on 5
        
        # if we dont pass start and step
        #  then their by default value will be 
        # Start --- 0 
        # Step --- +1
        
        
                        # stop 
# Ex  :  for i in range (5 ) 
            # output : 0 , 1 , 2 , 3 , 4 

                        # start , stop 
# Ex  :  for i in range ( 1 , 6 ) 
            # output :  1 , 2 , 3 , 4 , 5 now starts from 1 and stop on 5

                        #start , stop ,step
# Ex  :  for i in range ( 1 , 10 , +2  ) 
            #  output :  1 , 3 , 5 , 7 ,  + now starts from 1 and stop on 5
