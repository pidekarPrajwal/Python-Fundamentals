"""
Taking Input From user in Python

    Use to take input from user in python we use input() function. The input() function takes input from the user and returns it as a string. We can also specify a prompt message to display to the user before taking input.
    Example :
        name = input("Enter your name: ")
        print("Hello, " + name + "!")  # output: Hello, <name>!
        
    Terminal : After running the code
    Terminal Ask first : 
        Enter your name: Prajwal
            Hello, Prajwal! 
    
"""


print("Enter your name: ")
name = input()  # taking input from user
print("Hello, " + name + "!")  # output: Hello, <name> 


# Addition 
print("Addition of Two Numbers")
num1 = int(input("Enter first number: "))  #int use to convert the input string to integer
num2 = int(input("Enter second number: "))
# if we dont use int() then the input will be taken as string and the output will be concatenated string instead of sum of two numbers.
# Ex : output: Enter first number: 10
#       Enter second number: 20
#      The sum is:  1020  -- output will be concatenated string instead of sum of two numbers.
        # -- This output will be not valid because 10 + 20 = 30 not 1020. So we need to convert the input string to integer using int() function.

result = num1 + num2
print("The sum is: ", result)