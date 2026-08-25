""" 
python First program 
.py is the python extension for python files that knows this file is a python file 

Print is by defautl function of python to print the word in the console.s
""" 
print("Hello World")
# output: Hello World

print("Hello \n World")  #\n is used to print the next word in the next line
# output: Hello 
#         World

print("Hello \t World")  #\t is used to print the next word in the next tab space  
# output: Hello 	 World


"""
# Data Types in Python
1. int - Integer data type is used to store whole numbers without any decimal point.
2. float - Float data type is used to store numbers with decimal points.
3. str - String data type is used to store a sequence of characters.
4. bool - Boolean data type is used to store True or False values.
5. None - None data type is used to represent the absence of a value or a null value.

"""

name = "prajwal"  # str
age = 20  # int
is_student = True  # bool
salary = 50000.0  # float

# str - String 
print(type(name))  # output: <class 'str'>
print(name)  # output: prajwal

# int - Integer
print(type(age))  # output: <class 'int'>
print(age)  # output: 20

# Bool - Boolean
print(type(is_student))  # output: <class 'bool'>
print(is_student)  # output: True

# float - Floating point
print(type(salary))  # output: <class 'float'>
print(salary)  # output: 50000.0


"""
-----Keywords in Python-------
EX : False , Bool , None , True , and , as , assert , break , class , continue , def , del , elif , else , except , finally , for , from , global , if , import , in , is , lambda , nonlocal , not , or , pass , raise , return , try, while, with, yield 

That are reserved words in python and cannot be used as variable names or identifiers.
"""


"""
Comments in Python

comments are used to explain the code and make it more readable.
There are two types of comments in python:
1. Single line comments - Single line comments are used to explain a single line of code. They are created using the # symbol.
Ex : # This is a single line comment
2. Multi-line comments - Multi-line comments are used to explain multiple lines of code. They
EX : This is a multi-line comment use three double quotes ("" ") or three single quotes (''') to create multi-line comments.

"""


"""
Style Guide In Python

It is used for writing the words correctly and in a proper way. It is used to make the code more readable and understandable. It is also used to make the code more consistent and maintainable. The style guide for python is PEP 8 (Python Enhancement Proposal 8). It is a set of guidelines for writing python code. It is used to make the code more readable and understandable. It is also used to make the code more consistent and maintainable.
like if the variable name is a single word then it should be in lowercase letters. If the variable name is a multiple words then it should be in lowercase letters and separated by underscores. If the variable name is a class name then it should be in CamelCase. If the variable name is a constant then it should be in uppercase letters.

Ex : toal_marks = 100 , TotalMarks = 100 , TOTAL_MARKS = 100 --This is the correct way to write the variable names in python.
    total marks = 100 , totalMarks = 100 , Total_marks = 100 --This is the incorrect way to write the variable names in python.

total_price : is a snake_case variable name because it is in lowercase letters and separated by underscores.
totalPrice : is a camelCase variable name because it is in lowercase letters and the first letter of the second word is in uppercase letters.
TotalPrice : is a PascalCase variable name because the first letter of each word is in uppercase letters.
"""


