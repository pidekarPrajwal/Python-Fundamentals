# ----- Python Programming Fundamentals 🐍 ------

A structured, topic-wise reference guide to Python programming concepts, featuring descriptions, key concepts, and code examples for each module.

---

## 📌 Table of Contents
1. [Module 1: First Program, Data Types & PEP 8 Style Guide](#1-first-program-data-types--pep-8-style-guide)
2. [Module 2: Operators & Operator Precedence](#2-operators--operator-precedence)
3. [Module 3: Type Conversion](#3-type-conversion)
4. [Module 4: Taking User Input](#4-taking-user-input)
5. [Module 5: Conditional Statements](#5-conditional-statements)
6. [Module 6: Loops & Iteration](#6-loops--iteration)
7. [Module 7: Functions](#7-functions)
8. [Module 8: Strings & String Formatting](#8-strings--string-formatting)
9. [Module 9: Lists & Tuples](#9-lists--tuples)
10. [Module 10: Dictionaries & Sets](#10-dictionaries--sets)
11. [Module 11: Object-Oriented Programming (OOP) - Part 1](#11-object-oriented-programming-oop---part-1)
12. [Module 12: Object-Oriented Programming (OOP) - Part 2](#12-object-oriented-programming-oop---part-2)
13. [Module 13: File Input/Output (File I/O)](#13-file-inputoutput-file-io)
14. [Module 14: Exception Handling, List Comprehension & JSON](#14-exception-handling-list-comprehension--json)
15. [Requirements & Execution](#-requirements--execution)

---

## 📑 Module Overview & Code Reference

### 1. First Program, Data Types & PEP 8 Style Guide
**File:** [`01_First_program.py`]

#### 📝 Description
Covers Python syntax basics including outputting text using `print()`, escape sequences, fundamental built-in data types, Python keywords, comment styles, and Python's official PEP 8 style guide for naming conventions.

#### 💡 Key Concepts
- **`print()` Function & Escape Sequences:** `\n` (newline), `\t` (tab space).
- **Data Types:** `int` (integers), `float` (decimals), `str` (text), `bool` (`True`/`False`), `None` (absence of value).
- **Python Keywords:** Reserved words (e.g., `if`, `for`, `def`, `class`, `import`, `return`, `True`, `False`, `None`) that cannot be used as variable identifiers.
- **Comments:** Single-line (`#`) and Multi-line comments / docstrings (`""" ... """`).
- **PEP 8 Naming Conventions:** 
  - `snake_case` for variables and functions (`total_marks = 100`)
  - `PascalCase` for classes (`TotalMarks`)
  - `UPPER_CASE` for constants (`TOTAL_MARKS = 100`)

#### 💻 Code Example
```python
# Printing with escape sequences
print("Hello World")
print("Hello \n World")  # \n: Newline
print("Hello \t World")  # \t: Tab space

# Data Types
name = "prajwal"       # str
age = 20               # int
is_student = True      # bool
salary = 50000.0       # float

print(type(name))       # Output: <class 'str'>
print(name)             # Output: prajwal

# PEP 8 Naming Conventions
total_price = 100       # snake_case (standard variable naming)
TOTAL_PRICE = 100       # UPPER_CASE (constant definition)
```

---

### 2. Operators & Operator Precedence
**File:** [`02_operators.py`]

#### 📝 Description
Explores the four major categories of Python operators (Arithmetic, Relational, Assignment, Logical) along with operator precedence rules (similar to BODMAS) for expression evaluation.

#### 💡 Operator Summary
| Operator Category | Operators | Description & Examples |
| :--- | :--- | :--- |
| **Arithmetic** | `+`, `-`, `*`, `/`, `%`, `**`, `//` | `a % b` (modulus/remainder), `a ** b` (power), `a // b` (floor division) |
| **Relational** | `==`, `!=`, `>`, `<`, `>=`, `<=` | Compares values and returns a boolean (`True`/`False`) |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=` | Assigns or updates variable values (e.g., `a += b` $\rightarrow$ `a = a + b`) |
| **Logical** | `and`, `or`, `not` | Evaluates boolean logic (`and` requires both true, `or` requires at least one true, `not` negates) |

#### 💡 Operator Precedence (Highest to Lowest)
1. **Parentheses `()`**
2. **Exponentiation `**`**
3. **Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`**
4. **Addition `+`, Subtraction `-`**
5. **Relational Operators `==`, `!=`, `<`, `<=`, `>`, `>=`**
6. **Logical NOT `not`, Logical AND `and`, Logical OR `or`**

#### 💻 Code Example
```python
a = 10
b = 3

# Arithmetic Operators
print("Addition:", a + b)           # Output: 13
print("Exponentiation:", a ** b)    # Output: 1000
print("Floor Division:", a // b)    # Output: 3

# Relational Operators
print("Greater than:", a > b)       # Output: True
print("Not equal to:", a != b)      # Output: True

# Assignment Operators
a += b                              # Equivalent to: a = 10 + 3 -> 13
print("Add and assign:", a)         # Output: 13

# Logical Operators
print("Logical AND:", a > 5 and b < 5)  # Output: True
print("Logical NOT:", not(a > 5))       # Output: False
```

---

### 3. Type Conversion
**File:** [`03_Type_conversion.py`](file:///d:/AIML/01_PYTHON/03_Type_conversion.py)

#### 📝 Description
Demonstrates how Python handles data type conversions, detailing both automatic implicit conversions by the interpreter and manual explicit type casting by the developer.

#### 💡 Key Concepts
- **Implicit Type Conversion:** Automatic type promotion performed by Python during operations (e.g., adding an `int` and a `float` results in a `float`).
- **Explicit Type Conversion (Type Casting):** Manual conversion enforced by the programmer using constructor functions like `int()`, `float()`, `str()`, etc.

#### 💻 Code Example
```python
# Implicit Type Conversion (Automatic)
a = 10         # int
b = 3.5        # float
c = a + b      
print(c)       # Output: 13.5 (type: float)

# Explicit Type Conversion (Manual Casting)
x = 10
y = 3.5
z = x + int(y) # int(3.5) converts 3.5 to 3
print(z)       # Output: 13 (type: int)
```

---

### 4. Taking User Input
**File:** [`04_Taking_Input.py`](file:///d:/AIML/01_PYTHON/04_Taking_Input.py)

#### 📝 Description
Explains how to take interactive input from users via the terminal using the `input()` function, highlighting that `input()` always returns a string and requires type casting for numeric calculations.

#### 💡 Key Concepts
- **`input()` Function:** Prompts the user and reads terminal input as a `str`.
- **String Concatenation vs. Addition:**
  - Without casting: `"10" + "20"` results in `"1020"` (string concatenation).
  - With casting: `int("10") + int("20")` results in `30` (numerical addition).

#### 💻 Code Example
```python
# Standard String Input
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Numeric Input with Type Conversion
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2
print("The sum is:", result)
```

---

### 5. Conditional Statements
**File:** [`05_conditional_statment.py`](file:///d:/AIML/01_PYTHON/05_conditional_statment.py)

#### 📝 Description
Demonstrates conditional branching logic in Python using `if`, `elif`, `else` structures, nested conditional statements for complex validation, and modern `match-case` statements (Python 3.10+).

#### 💡 Key Concepts
- **`if-elif-else` Logic:** Evaluates conditions sequentially until a `True` condition is met.
- **Nested Conditions:** Placing conditional blocks inside another condition (e.g., verifying username first, then password).
- **`match-case` Statement (Python 3.10+):** Structural pattern matching equivalent to switch-case statements in other languages. Supports wildcard default case `case _`.

#### 💻 Code Example
```python
# Basic Conditional Branching
age = int(input("Enter your age: "))
if age > 18:
    print("You are eligible to vote.")
elif age == 18:
    print("You are eligible to vote, but you need to register first.")
else:
    print("You are not eligible to vote yet.")

# Nested Conditionals (Authentication System)
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "admin123":
        print("Login successful!")
    else:
        print("Invalid password!")
else:
    print("Invalid username!")

# Match-Case Statement (Python 3.10+)
light_color = input("Enter traffic light color (red/yellow/green): ")

match light_color:
    case "red":
        print("Stop!")
    case "yellow":
        print("Get ready to go!")
    case "green":
        print("Go!")
    case _:             # Default case when no patterns match
        print("Invalid color!")
```

---

### 6. Loops & Iteration
**File:** [`06_Loops.py`](file:///d:/AIML/01_PYTHON/06_Loops.py)

#### 📝 Description
Covers repetitive execution concepts using `while` loops, multiplication table generation, loop control statements (`break` and `continue`), `for` loops, and sequence generation with `range()`.

#### 💡 Key Concepts
- **`while` Loop:** Repeats execution as long as the test condition remains `True`. Requires updating an iterator variable to prevent infinite loops.
- **Loop Control Keywords:**
  - `break`: Immediately exits the loop.
  - `continue`: Skips the remaining code in the current iteration and jumps to the next iteration.
- **`for` Loop:** Iterates over iterable objects (strings, lists) or numerical ranges.
- **`range(start, stop, step)` Function:** Generates integer sequences:
  - `start` (optional, default = 0)
  - `stop` (compulsory, non-inclusive upper bound)
  - `step` (optional, default = +1)

#### 💻 Code Example
```python
# While Loop
count = 1
while count <= 5:
    print(count)
    count += 1

# Loop Control (break & continue)
i = 1
while i <= 10:
    if i == 3:
        i += 1
        continue  # Skips printing 3
    if i == 6:
        break     # Terminates loop when i reaches 6
    print(i)
    i += 1

# For Loop with range(start, stop, step)
for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9
```

---

### 7. Functions
**File:** [`07_Functions.py`](file:///d:/AIML/01_PYTHON/07_Functions.py)

#### 📝 Description
Introduces modular programming using functions to package reusable code blocks that execute specific tasks.

#### 💡 Key Concepts
- **`def` Keyword:** Used to define a new function.
- **Function Body:** Indented block containing statements to execute.
- **Function Call:** Invoking the function by name to execute its code.

#### 💻 Code Example
```python
# Function Definition
def hello():
    print("Hello world")  # Function body

# Function Call
hello()  # Executes the function -> Output: Hello world
```

---

### 8. Strings & String Formatting
**File:** [`08_Strings.py`](file:///d:/AIML/01_PYTHON/08_Strings.py)

#### 📝 Description
Covers string fundamentals in Python, string immutability, operations such as length calculation, concatenation, indexing, slicing, iteration, and formatting methods (`.format()` and f-strings).

#### 💡 Key Concepts
- **String Immutability:** Once defined, string characters cannot be modified in place.
- **Length & Concatenation:** `len()` returns character count (including whitespace); `+` operator joins multiple strings.
- **Indexing & Slicing:** 
  - 0-indexed positioning accessed via `str[index]`.
  - Slicing via `str[start_idx : end_idx]` extracts substrings where `end_idx` is non-inclusive.
- **String Formatting:** Dynamic string interpolation using `.format()` and modern `f-strings` (`f"{variable}"`).

#### 💻 Code Example
```python
word = "Python"
word2 = "is good "

# String Length & Concatenation
print(len(word))                 # Output: 6
print(word + " " + word2)        # Output: Python is good 

# Indexing & Slicing
print(word[2])                   # Output: t
print(word[2:4])                 # Output: th (end index is non-inclusive)
print(word[2:])                  # Output: thon

# String Formatting (.format() and f-strings)
a, b, c = 5, 9, 14
print("Sum of {} and {} is {}".format(a, b, c))  # str.format() method
print(f"Sum of {a} and {b} is {c}")              # Modern f-string interpolation
```

---

### 9. Lists & Tuples
**File:** [`09_List_&_Tuple.py`](file:///d:/AIML/01_PYTHON/09_List_&_Tuple.py)

#### 📝 Description
Explores Python's built-in ordered sequence data structures: mutable `list` and immutable `tuple`. Details indexing, slicing, utility methods, search loops, and key differences.

#### 💡 Key Concepts
- **List (`[]`):** Ordered, mutable collection that can store multiple data types (integers, strings, floats, nested lists).
- **List Methods:**
  - `append(val)`: Adds a single element to the end of the list.
  - `insert(idx, val)`: Inserts an element at the specified index.
  - `sort()` / `sort(reverse=True)`: Sorts elements in ascending or descending order.
  - `reverse()`: Reverses the elements of the list in place.
- **Tuple (`()`):** Ordered, immutable sequence. Values cannot be altered after creation.
  - **Single Element Tuple:** Must include a trailing comma `(val,)` to be recognized as a tuple rather than a scalar type.
- **Tuple Methods:**
  - `index(val)`: Returns the index of the first occurrence of `val`.
  - `count(val)`: Returns the total count of occurrences of `val`.

#### 💻 Code Example
```python
# Lists (Mutable)
nums = [1, 2, 3]
nums.append(4)                   # Output: [1, 2, 3, 4]
nums.insert(2, 10)               # Output: [1, 2, 10, 3, 4]
nums.sort()                      # Output: [1, 2, 3, 4, 10]
nums.sort(reverse=True)          # Output: [10, 4, 3, 2, 1]

# Tuples (Immutable)
tup = (1, 2, 3, 2, 5)
single_tup = (1,)                # Trailing comma creates a tuple (<class 'tuple'>)
print(tup[2])                    # Output: 3
print(tup.index(2))              # Output: 1 (first appearance index)
print(tup.count(2))              # Output: 2 (total occurrences)
```

---

### 10. Dictionaries & Sets
**File:** [`10_Dict_&_Set.py`](file:///d:/AIML/01_PYTHON/10_Dict_&_Set.py)

#### 📝 Description
Covers key-value mapping structures (`dict`) and unique element collections (`set`), highlighting key uniqueness, safe value lookup methods, set immutability rules, and mathematical set operations.

#### 💡 Key Concepts
- **Dictionary (`{key: value}`):** Mutable, unordered collection of unique key-value pairs.
- **Dictionary Methods:**
  - `d.keys()`: Returns all dictionary keys.
  - `d.values()`: Returns all dictionary values.
  - `d.items()`: Returns key-value pairs as tuples `(key, value)`.
  - `d.get(key)`: Safely retrieves value without raising `KeyError` if key is missing (returns `None`).
  - `d.update({key: val})`: Updates existing key or adds a new key-value pair.
- **Set (`{val1, val2}`):** Unordered collection of unique, immutable elements (duplicates are automatically eliminated).
  - Empty set creation requires `set()` syntax (`{}` creates an empty dictionary).
- **Set Methods:**
  - `s.add(val)`: Adds an element.
  - `s.remove(val)`: Removes a specific element.
  - `s.pop()`: Removes and returns an arbitrary element.
  - `s.union(set2)`: Returns a new set containing all elements from both sets.
  - `s.intersection(set2)`: Returns a new set containing only common elements.

#### 💻 Code Example
```python
# Dictionary Usage & Safe Retrieval
student = {
    "name": "Prajwal",
    "age": 24,
    "marks": [85, 90, 95]
}
print(student.get("name"))       # Output: Prajwal
print(student.get("grade"))      # Output: None (prevents KeyError crash)
student.update({"city": "Pune"})

# Set Operations (Union & Intersection)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a.intersection(set_b)) # Output: {3, 4} (elements present in both)
print(set_a.union(set_b))        # Output: {1, 2, 3, 4, 5, 6} (all unique elements)
```

---

### 11. Object-Oriented Programming (OOP) - Part 1
**File:** [`11_OOPs_Part-01.py`](file:///d:/AIML/01_PYTHON/11_OOPs_Part-01.py)

#### 📝 Description
Introduces the core concepts of Object-Oriented Programming (OOP) in Python, focusing on Class definitions, Object creation, Class vs. Instance attributes, and Constructor initialization with `__init__`.

#### 💡 Key Concepts
- **Class:** A user-defined blueprint or template for creating objects. Defined using the `class` keyword with `PascalCase` naming convention.
- **Object (Instance):** A concrete instance of a class that encapsulates real data and operations defined by its class blueprint.
- **`__init__()` Constructor Method:** A special method automatically called whenever a new instance of a class is instantiated. Used for setting up initial state.
- **`self` Parameter:** A reference to the current instance of the class. It binds attributes to the specific object instance created.
- **Types of Constructors:**
  - **Default Constructor:** Accepts only `self` without additional parameters.
  - **Parameterized Constructor:** Accepts `self` along with custom arguments to initialize unique attributes per instance.

#### 💻 Code Example
```python
# Defining a Class with Class Attributes (Blueprint)
class Student:
    subject = "Python"           # Class attribute (shared by all instances)
    college = "ABCED"

# Instantiating Objects
stu1 = Student()
stu2 = Student()
print(stu1.subject)              # Output: Python
print(stu2.college)              # Output: ABCED

# Class with Parameterized Constructor (__init__)
class Students:
    def __init__(self, name):
        self.name = name         # Instance variable unique to each instance

# Initializing distinct objects with unique data
stu11 = Students("Rahul")
stu22 = Students("Raj")

print(stu11.name)                # Output: Rahul
print(stu22.name)                # Output: Raj
```

---

### 12. Object-Oriented Programming (OOP) - Part 2
**File:** [`12_OOPs_Part-02.py`](file:///d:/AIML/01_PYTHON/12_OOPs_Part-02.py)

#### 📝 Description
Explores the Four Pillars of Object-Oriented Programming (Encapsulation, Abstraction, Inheritance, and Polymorphism) and their implementation details in Python.

#### 💡 The 4 Pillars of OOP
| Pillar | Core Concept | Python Implementation & Usage |
| :--- | :--- | :--- |
| **1. Encapsulation** | Wrapping attributes and methods into a single unit (class) while restricting direct access to internal state. | Controlled via access specifiers: Public (`attr`), Protected (`_attr`), Private (`__attr`). Private data is accessed using Getter & Setter methods. |
| **2. Abstraction** | Hiding internal implementation details and exposing only essential interfaces to the user. | Simplifies complex system interaction by providing high-level methods while hiding complex execution logic. |
| **3. Inheritance** | Deriving attributes and methods from a parent (base) class into child (derived) classes to promote code reuse. | Supports Single-level, Multi-level, and Multiple inheritance. Uses `super()` to invoke parent class constructors/methods. |
| **4. Polymorphism** | Allowing the same method or operator to behave differently depending on the calling object or data context. | Achieved via Method Overriding (child class redefines parent method) and Duck Typing. |

#### 💡 Access Control & Inheritance Rules
- **Public Attributes:** Accessible from inside and outside the class.
- **Protected Attributes (`_name`):** Intended for access within the class and its subclasses (convention).
- **Private Attributes (`__name`):** Accessible only inside the class where defined. Python uses name mangling to prevent direct external access.
- **`super()` Function:** Allows a child class to call methods or constructor of its parent class.

#### 💻 Code Example
```python
# 1. Encapsulation (Private attributes & Getter/Setter)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public attribute
        self.__balance = balance    # Private attribute (__ prefix)

    def get_balance(self):          # Getter method
        return self.__balance

    def deposit(self, amount):      # Setter method
        if amount > 0:
            self.__balance += amount

# 2. Inheritance & super()
class Parent:
    def greet(self):
        print("Hello from Parent Class")

class Child(Parent):               # Single-Level Inheritance
    def greet(self):
        super().greet()             # Call parent method using super()
        print("Hello from Child Class")

# 3. Polymorphism (Method Overriding)
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):                # Overriding parent class method
        print("Woof! Woof!")

# Execution Demonstration
acc = BankAccount("Prajwal", 5000)
acc.deposit(1500)
print("Balance:", acc.get_balance()) # Output: Balance: 6500

child = Child()
child.greet()                        # Output: Parent greeting then Child greeting

dog = Dog()
dog.speak()                          # Output: Woof! Woof!
```

---

### 13. File Input/Output (File I/O)
**File:** [`13_File_IO.py`](file:///d:/AIML/01_PYTHON/13_File_IO.py)

#### 📝 Description
Provides a comprehensive guide to File I/O mechanisms in Python for software engineering and AIML applications. Explains memory persistence (RAM vs Hard Disk), file lifecycle (`open()` and `close()`), context managers (`with open()`), file access modes (`r`, `w`, `a`, `x`, `b`, `t`, `+`), reading techniques (`read()`, `readline()`, `readlines()`, line-by-line streaming), text vs binary files (`rb`/`wb`), cross-platform path management (`os.path`, `pathlib`), I/O exception handling, a real-world AIML metrics logger, and learner practice exercises.

#### 💡 File Modes & Core Concepts
| Mode / Concept | Behavior & Description |
| :--- | :--- |
| `'r'` | **Read Mode (Default):** Opens file for reading; raises `FileNotFoundError` if file is missing. |
| `'w'` | **Write Mode:** Opens file for writing; overwrites existing file contents or creates a new file. |
| `'a'` | **Append Mode:** Opens file for writing; appends data to the end without overwriting existing content. |
| `'x'` | **Exclusive Creation:** Creates a new file for writing; fails (`FileExistsError`) if file exists. |
| `'b'` / `'t'` | **Binary / Text Mode:** Text mode (`'t'`, default) for UTF-8 text vs Binary mode (`'b'`) for raw bytes (`.bin`, `.pkl`, `.pth`). |
| `'+'` | **Updating Mode:** Opens disk file for simultaneous reading and writing (e.g., `'r+'`, `'w+'`, `'a+'`). |
| **`with open()`** | **Context Manager (Preferred):** Automatically closes file resources even if runtime exceptions occur. |
| **Path Handling** | Cross-platform handling using forward slashes `/`, raw strings (`r"..."`), `os.path.join()`, or `pathlib.Path`. |

#### 💻 Code Example
```python
import os
import pathlib

# 1. Recommended Practice: Context Manager ('with open')
with open("training_log.txt", "w") as f:
    f.write("Epoch 1: Loss = 0.45, Accuracy = 82.5%\n")

# 2. Appending Data ('a' mode)
with open("training_log.txt", "a") as f:
    f.write("Epoch 2: Loss = 0.21, Accuracy = 93.8%\n")

# 3. Line-by-Line File Iteration (Memory-Efficient for large AIML datasets)
with open("training_log.txt", "r") as f:
    for line in f:
        print("Log entry:", line.strip())

# 4. Checking File Existence & Path Operations
path_obj = pathlib.Path("training_log.txt")
if path_obj.is_file():
    print(f"File size: {path_obj.stat().st_size} bytes")

# 5. Handling Common File Errors
try:
    with open("missing_dataset.csv", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"File missing error handled gracefully: {e}")
```

---

### 14. Exception Handling, List Comprehension & JSON
**File:** [`14_Exception_handling.py`](file:///d:/AIML/01_PYTHON/14_Exception_handling.py)

#### 📝 Description
Covers robust error handling using `try-except-else-finally` blocks, built-in exception types, manually raising exceptions, custom domain-specific exceptions, retained sequence transformations via list comprehensions, and error-safe JSON data processing for resilient AIML pipelines.

#### 💡 Key Concepts & Exception Summary
- **Exception Control Blocks:**
  - `try`: Encloses code that might raise a runtime exception.
  - `except`: Catches and handles specific exception types gracefully without crashing.
  - `else`: Executes ONLY if NO exception was raised in the `try` block.
  - `finally`: ALWAYS executes guaranteed cleanup code (closing files, releasing locks).
  - `raise`: Manually triggers built-in or custom exceptions.
- **Common Built-In Exceptions Covered:**
  - `ValueError`: Inappropriate value (e.g., `int("abc")`).
  - `TypeError`: Incompatible operand types (e.g., `"age: " + 25`).
  - `ZeroDivisionError`: Division or modulo by zero.
  - `FileNotFoundError`: Missing file during I/O operations.
  - `IndexError`: Sequence index out of range.
  - `KeyError`: Dictionary key lookup failure.
  - `NameError`: Accessing an undefined variable.
  - `AttributeError`: Accessing non-existent attribute/method on an object.
- **Custom Exceptions:** Domain-specific exceptions inheriting from `Exception` (e.g., `class ConfigValidationError(Exception): pass`).
- **List Comprehensions:** Concise list creation syntax: `[output_expr for item in iterable if condition]`.
- **JSON Processing (`json` module):** `json.loads()`, `json.dumps()`, `json.load()`, `json.dump()`, and catching `json.JSONDecodeError`.

#### 💻 Code Example
```python
import json

# 1. Full Exception Control Flow (try - except - else - finally)
try:
    value = float("12.5")
    result = 100 / value
except ValueError:
    print("Invalid numeric string!")
except ZeroDivisionError:
    print("Division by zero!")
else:
    print(f"Computation successful! Result: {result:.2f}")
finally:
    print("Cleanup step complete.")

# 2. Custom Exception & Raising Errors
class EmptyDatasetError(Exception):
    """Raised when an loaded dataset contains 0 records."""
    pass

def check_dataset(samples):
    if len(samples) == 0:
        raise EmptyDatasetError("Dataset is empty!")
    return len(samples)

try:
    check_dataset([])
except EmptyDatasetError as e:
    print(f"Caught custom exception: {e}")

# 3. Retained List Comprehension & JSON Handling
odd_squares = [i * i for i in range(1, 6) if i % 2 != 0] # Output: [1, 9, 25]

# Safe JSON Decode Handling
try:
    config = json.loads('{"model": "ResNet50", "epochs": 50}')
    print("Model:", config["model"])
except json.JSONDecodeError as e:
    print("Invalid JSON structure!", e)
```

---

## 🚀 Requirements & Execution

### Prerequisites
- Python 3.10 or higher (required for `match-case` statements in `05_conditional_statment.py`).

### Running the Code
Run any module directly from the terminal using:
```bash
python 01_First_program.py
python 02_operators.py
python 03_Type_conversion.py
python 04_Taking_Input.py
python 05_conditional_statment.py
python 06_Loops.py
python 07_Functions.py
python 08_Strings.py
python 09_List_&_Tuple.py
python 10_Dict_&_Set.py
python 11_OOPs_Part-01.py
python 12_OOPs_Part-02.py
python 13_File_IO.py
python 14_Exception_handling.py
```
