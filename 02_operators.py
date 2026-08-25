"""
Operators in Python 

    It is used to show the relationship between two values. It is used to perform operations on variables and values. It is used to perform arithmetic operations, comparison operations, logical operations, and bitwise operations.
    Ex: Sum = a + b
            = is an a assignment operator
            + is an operator 
            a, b is a operands
            
            
    Types of Operators in Python
    1. Arithmetic Operators : 
        + : Addition
        - : Subtraction
        * : Multiplication
        / : Division
        % : Modulus
        ** : Exponentiation
        // : Floor Division
        
        
    2. Relational Operators :
        == : Equal to
        != : Not equal to
        > : Greater than
        < : Less than
        >= : Greater than or equal to
        <= : Less than or equal to
    
    3. Assignment Operators :
        = : Assign
        += : Add and assign
        -= : Subtract and assign
        *= : Multiply and assign
        /= : Divide and assign
        %= : Modulus and assign
        **= : Exponentiation and assign
        //= : Floor division and assign
        
    4. Logical Operators :
        and : Logical AND
        or : Logical OR
        not : Logical NOT
"""

# Arthimetic Operators
a = 10
b = 3

print("Addition: ", a + b)          # 10 + 3 : output: 13
print("Subtraction: ", a - b)       # 10 - 3 : output: 7
print("Multiplication: ", a * b)    # 10 * 3 :  output: 30
print("Division: ", a / b)          # 10 / 3 output: 3.333333333
print("Modulus: ", a % b)           # 10 % 3 : output: 1  -- For Remainder
print("Exponentiation: ", a ** b)   # 10 ** 3 : output: 1000 -- For Power
print("Floor Division: ", a // b)   # 10 // 3 : output: 3 -- For Quotient 


# Relational Operators - comparing the values of a and b
print("Equal to: ", a == b)                      # 10 == 3 : output: False -- 10 is not equal to 3
print("Not equal to: ", a != b)                  # 10 != 3 : output: True  -- 10 is not equal to 3 ( for not equal to use != operator)
print("Greater than: ", a > b)                   # 10 > 3 : output : True  -- 10 is greater than 3
print("Less than: ", a < b)                      # 10 < 3 : output : False -- 10 is not less than 3
print("Greater than or equal to: ", a >= b)      # 10 >= 3 : output : True -- 10 is greater than or equal to 3
print("Less than or equal to: ", a <= b)         # 10 <= 3 : output : False -- 10 is not less than or equal to 3



# Assignment Operators -- To assign values to variables

print("Assign: ", a)           # output: 10  -- means a is assigned with 10
a += b                         # a = a + b ( a = 10+ 3 now a = 13 )
print("Add and assign: ", a)   # output: 13  -- means a is assigned with the sum of a and b 


# Logical Operators -- To perform logical operations on boolean values

print("Logical AND: ", a > 5 and b < 5)   # output: True -- both conditions are true
print("Logical OR: ", a > 5 or b < 5)     # output: True -- one of the conditions is true
print("Logical NOT: ", not(a > 5))        # output: False -- negation of the condition is false




"""
Operator Precedence in Python
    Operator precedence is the order in which operators are evaluated in an expression. 
    The operator with the highest precedence is evaluated first, followed by the operator with the next highest precedence, and so on. 
    If two operators have the same precedence, they are evaluated from left to right.

    Precedence of Operators in Python:
    1. Parentheses ()
    2. Exponentiation **
    3. Multiplication *, Division /, Floor Division //, Modulus %
    4. Addition + and Subtraction -
    5. Relational Operators ==, <, <=, >, >=
    6. Equality Operators ==, !=
    7. Logical NOT not
    8. Logical AND and
    9. Logical OR or
    
    
    Simliar like BODMAS - 
        B - Brackets
        O - Order (Exponents)
        D - Division
        M - Multiplication
        A - Addition
        S - Subtraction
        
        
    If Same Precedence then it will be evaluated from left to right.
    
"""