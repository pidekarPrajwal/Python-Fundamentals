"""
===================================================================
  OBJECT-ORIENTED PROGRAMMING (OOP) - PART 01: FUNDAMENTALS
===================================================================

1. WHAT IS OBJECT-ORIENTED PROGRAMMING (OOP)?
   OOP is a programming paradigm based on the concept of "objects", which 
   can contain data (attributes/properties) and code (methods/functions).
   It structures software design around data or objects, rather than functions and logic.

2. PROCEDURAL PROGRAMMING VS OBJECT-ORIENTED PROGRAMMING:
   -----------------------------------------------------------------
   Feature            | Procedural Programming    | OOP
   -----------------------------------------------------------------
   Focus              | Functions & Procedures    | Objects & Data
   Data Security      | Less secure (global data) | High (Encapsulation)
   Code Reusability   | Low (function duplication)| High (Inheritance)
   Structure          | Top-down approach         | Bottom-up approach
   -----------------------------------------------------------------

3. CORE CONCEPTS COVERED IN PART 01:
   - Classes and Objects (Blueprints & Instances)
   - Instance Attributes vs Class Attributes
   - Constructors (__init__) - Default vs Parameterized
   - Types of Methods: Instance Methods, Class Methods (@classmethod), Static Methods (@staticmethod)
   - Destructors (__del__) and Object Lifecycle
   - Special / Dunder Methods (__str__, __repr__)
"""

# =================================================================
# 1. CLASS & OBJECT DEFINITION
# =================================================================
# A Class is a blueprint/template for creating objects.
# An Object is an instance of a class that holds actual data.

class Student:
    # Class Attributes (shared across all instances of this class)
    subject = "Python"
    college = "ABC Institute"
    year = "2nd Year"

# Creating instances (objects) of Student class
stu1 = Student()
stu2 = Student()
stu3 = Student()

print("--- 1. Basic Class & Objects ---")
print(f"stu1 subject: {stu1.subject}")  # Output: Python
print(f"stu2 college: {stu2.college}")  # Output: ABC Institute
print(f"stu3 year: {stu3.year}")        # Output: 2nd Year
print(f"Object memory reference: {stu1}")


# =================================================================
# 2. INSTANCE ATTRIBUTES VS CLASS ATTRIBUTES
# =================================================================
# Class attributes belong to the class itself and are shared by all objects.
# Instance attributes are unique to each individual object (defined via self).

class Employee:
    # Class Attribute (Shared)
    company_name = "Tech Corp"
    total_employees = 0

    # Constructor (__init__) to initialize Instance Attributes
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id       # Instance Attribute
        self.name = name           # Instance Attribute
        self.salary = salary       # Instance Attribute
        Employee.total_employees += 1

print("\n--- 2. Instance vs Class Attributes ---")
emp1 = Employee(101, "Alice", 75000)
emp2 = Employee(102, "Bob", 85000)

print(f"{emp1.name} works at {emp1.company_name} with salary ${emp1.salary}")
print(f"{emp2.name} works at {emp2.company_name} with salary ${emp2.salary}")
print(f"Total Employees created: {Employee.total_employees}")


# =================================================================
# 3. TYPES OF CONSTRUCTORS: DEFAULT VS PARAMETERIZED
# =================================================================
# Constructor is a special method (__init__) automatically called when an object is created.
# Default Constructor: Takes only 'self' parameter.
# Parameterized Constructor: Takes 'self' along with custom arguments.

class DefaultConstructorExample:
    # Default Constructor
    def __init__(self):
        self.status = "Active"
        print("Default Constructor Called: New object initialized with status 'Active'")

class ParameterizedConstructorExample:
    # Parameterized Constructor
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        print(f"Parameterized Constructor Called: Course '{self.title}' ({self.duration} hours)")

print("\n--- 3. Constructors ---")
obj_default = DefaultConstructorExample()
obj_param = ParameterizedConstructorExample("Python Fundamentals", 40)


# =================================================================
# 4. TYPES OF METHODS: INSTANCE, CLASS (@classmethod), STATIC (@staticmethod)
# =================================================================
class MathOperations:
    pi = 3.14159  # Class attribute

    def __init__(self, value):
        self.value = value  # Instance attribute

    # 1. Instance Method: Operates on instance attributes (takes 'self')
    def double_value(self):
        return self.value * 2

    # 2. Class Method: Operates on class attributes (takes 'cls', decorated with @classmethod)
    @classmethod
    def get_pi(cls):
        return f"Value of PI is {cls.pi}"

    # 3. Static Method: Utility method independent of class/instance state (decorated with @staticmethod)
    @staticmethod
    def add_numbers(x, y):
        return x + y

print("\n--- 4. Types of Methods ---")
math_obj = MathOperations(10)
print(f"Instance Method (Double Value of 10): {math_obj.double_value()}")
print(f"Class Method (Get PI): {MathOperations.get_pi()}")
print(f"Static Method (Add 15 + 25): {MathOperations.add_numbers(15, 25)}")


# =================================================================
# 5. DESTRUCTOR (__del__) AND OBJECT DELETION
# =================================================================
# __del__() is called when an object is garbage collected or explicitly deleted using 'del'.

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        print(f"FileHandler: Opened connection to '{self.filename}'")

    def __del__(self):
        print(f"FileHandler: Closed connection to '{self.filename}' (Destructor executed)")

print("\n--- 5. Destructors (__del__) ---")
file_obj = FileHandler("data.txt")
del file_obj  # Explicitly deleting the object triggers __del__


# =================================================================
# 6. DUNDER / MAGIC METHODS (__str__ and __repr__)
# =================================================================
# __str__: User-friendly string representation (used by print() and str()).
# __repr__: Formal string representation (useful for debugging).

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"'{self.title}' by {self.author} (${self.price})"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"

print("\n--- 6. Special / Dunder Methods ---")
b1 = Book("Clean Code", "Robert C. Martin", 45.0)
print(f"str(b1) -> {str(b1)}")    # Calls __str__
print(f"repr(b1) -> {repr(b1)}")  # Calls __repr__


# =================================================================
# SUMMARY OF BEST PRACTICES & COMMON MISTAKES:
# =================================================================
# 1. Use PascalCase for Class names (e.g., StudentRecord).
# 2. Always include 'self' as the first parameter in instance methods.
# 3. Do NOT pass multiple constructors in Python (Python doesn't support method overloading natively;
#    the last defined __init__ will overwrite previous ones).
# 4. Use @classmethod when creating alternative constructors or modifying class state.
# 5. Use @staticmethod for utility functions that don't need access to self or cls.
