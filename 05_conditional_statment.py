"""
conditional Statement in Python

    Conditional statements are used to perform different actions based on different conditions. 
        In Python, we use if, elif, and else statements to implement conditional logic.
    Example: if age > 18:
                print("You are eligible to vote.")
             elif age == 18:
                print("You are eligible to vote, but you need to register first.")
             else:
                print("You are not eligible to vote yet.")
                

"""

# Example of conditional statement in Python
age = int(input("Enter your age: "))  # taking input from user and converting it to integer
if age > 18:
    print("You are eligible to vote.")
elif age == 18:
    print("You are eligible to vote, but you need to register first.")
else:
    print("You are not eligible to vote yet.")
    
    # output: Enter your age: 20
    #         You are eligible to vote.
    


# Simple authentication system using conditional statements

Username = input("Enter your username: ")
Password = input("Enter your password: ")

if Username == "admin" and Password == "admin123":
    print("Login successful!")
elif Username != "admin" :
    print("Invalid username!")
elif Password != "admin123":
    print("Invalid password!")
    
    # output: Enter your username: admin
    #         Enter your password: admin123
    
    
    
""""
Nesting of conditional statements in Python

    Nexting of conditional statements means using one conditional statement inside another conditional statement. 
    This allows us to create more complex decision-making logic.
    Example: if username == "admin":
                if password == "admin123":
                    print("Login successful!")
                else:
                    print("Invalid password!")
            else:
                print("Invalid username!")
                
"""

#authentication system using nested conditional statements
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "admin123":
        print("Login successful!")
    else:
        print("Invalid password!")
else:
    print("Invalid username!")
    
    # output: Enter your username: admin
    #         Enter your password: admin123
    #         Login successful!
    
    
    
"""
Match case statement in Python

    Match case statement is a new feature introduced in Python 3.10. 
    It allows us to match a value against a set of patterns and execute the corresponding block of code.
    like switch case statement in other programming languages.
    Example: light_color = "red"
                match light_color:
                        case "red":
                            print("Stop!")
                        case "yellow":
                            print("Get ready to go!")
                        case "green":
                            print("Go!")
                        case _:
                            print("Invalid color!")
                            
            output: Enter the traffic light color (red/yellow/green): red
                    Stop!
                    
            also we can write default case using underscore (_) which will be executed 
            if none of the cases match.
            
            
"""
# Example of match case statement in Python
light_color = input("Enter the traffic light color (red/yellow/green): ")

match light_color:
    case "red":
        print("Stop!")
    case "yellow":
        print("Get ready to go!")
    case "green":
        print("Go!")
    case _:             # default case ( print when no case matches)
        print("Invalid color!")
    
        # output: Enter the traffic light color (red/yellow/green): red
        #         Stop!

