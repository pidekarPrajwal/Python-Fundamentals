# Python Programming Fundamentals 🐍

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
8. [Requirements & Execution](#-requirements--execution)

---

## 📑 Module Overview & Code Reference

### 1. First Program, Data Types & PEP 8 Style Guide
**File:** [`01_First_program.py`](file:///d:/AIML/01_PYTHON/01_First_program.py)

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
**File:** [`02_operators.py`](file:///d:/AIML/01_PYTHON/02_operators.py)

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
```
