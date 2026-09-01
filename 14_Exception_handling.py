r"""
===================================================================
                  PYTHON EXCEPTION HANDLING
===================================================================

This module covers Exception Handling in Python in detail:
  1. What an Exception is & Why Exception Handling is vital
  2. Difference between Syntax Errors and Runtime Exceptions
  3. The Core Blocks: `try`, `except`, `else`, and `finally`
  4. Handling Specific Exceptions & Multiple `except` Blocks
  5. Detailed Breakdown of Common Built-in Exceptions:
     - ValueError, TypeError, ZeroDivisionError, FileNotFoundError
     - IndexError, KeyError, NameError, AttributeError
  6. Manually Raising Exceptions (`raise`)
  7. Creating Custom Exceptions (User-defined exception classes)
  8. Exception Handling with File I/O
  9. Retained Core Concepts: List Comprehensions & `json` Module Handling
  10. Best Practices for Clean Exception-Handling Code
  11. Real-World AIML Practical Example: Dataset & Config Loader
  12. Practice Exercises for Learners
"""

import os
import json

# =================================================================
# 1. WHAT IS AN EXCEPTION & WHY IS IT IMPORTANT?
# =================================================================
"""
1. WHAT IS AN EXCEPTION?
------------------------
An exception is an error that occurs during the execution of a program (at runtime).
When Python encounters an error condition that it cannot handle, it creates (raises) 
an exception object. If left unhandled, the program immediately terminates (crashes)
and prints a traceback.

WHY IS EXCEPTION HANDLING IMPORTANT?
------------------------------------
1. Prevents Crashes: Ensures your application or AIML pipeline does not abruptly stop
   when encountering bad data, missing files, or network timeouts.
2. Graceful Error Recovery: Allows the program to recover, use fallback default values,
   or report user-friendly error messages.
3. Resource Cleanup: Guarantees that open file handles, database connections, and GPU memory
   buffers are safely released even if an error occurs.
"""

print("=========================================================")
print("  1. INTRODUCTION TO EXCEPTION HANDLING")
print("=========================================================")
print("Exception handling keeps programs running smoothly despite unexpected runtime errors.\n")


# =================================================================
# 2. SYNTAX ERRORS VS RUNTIME EXCEPTIONS
# =================================================================
"""
2. SYNTAX ERRORS VS RUNTIME EXCEPTIONS
--------------------------------------
A. Syntax Errors (Compile-time Errors):
   - Caused by invalid Python code structure, typos, or illegal syntax.
   - Detected by Python BEFORE the script starts executing (during code parsing).
   - CANNOT be caught using `try-except` blocks.
   - Examples: Missing colon `:`, unbalanced parentheses, invalid keyword usage.
     (e.g., `if x == 5` without colon `:`)

B. Runtime Exceptions:
   - Code syntax is completely valid, but an illegal operation occurs while running.
   - Detected DURING program execution.
   - CAN be caught and handled using `try-except` blocks!
   - Examples: Division by zero, accessing an out-of-bounds list index, missing file.
"""

print("=========================================================")
print("  2. SYNTAX ERRORS VS RUNTIME EXCEPTIONS")
print("=========================================================")
print("Syntax Errors: Failed code parsing (cannot be caught with try-except).")
print("Runtime Exceptions: Occur during execution (can be caught with try-except).\n")


# =================================================================
# 3. CORE EXCEPTION BLOCKS: try, except, else, AND finally
# =================================================================
"""
3. THE FOUR CORE BLOCKS
-----------------------
- `try`: Contains code that might potentially raise an exception.
- `except`: Executes ONLY if an exception occurs inside the `try` block.
- `else`: Executes ONLY if NO exception occurred in the `try` block.
- `finally`: ALWAYS executes regardless of whether an exception occurred or not.
  (Perfect for cleanup operations like closing files or database connections).

SYNTAX:
  try:
      # Code that may raise an error
  except SpecificError:
      # Code to handle the error
  else:
      # Code to run if NO error occurred
  finally:
      # Code that ALWAYS runs
"""

print("=========================================================")
print("  3. THE try, except, else, AND finally BLOCKS")
print("=========================================================")

def divide_numbers(a, b):
    print(f"\nAttempting division: {a} / {b}")
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"  [EXCEPT] Caught Error: {e} - Division by zero is impossible!")
    else:
        print(f"  [ELSE] Success! Result = {result}")
    finally:
        print("  [FINALLY] Cleanup completed for division task.")

# Case 1: Valid division (triggers try -> else -> finally)
divide_numbers(10, 2)

# Case 2: Division by zero (triggers try -> except -> finally)
divide_numbers(10, 0)


# =================================================================
# 4. COMMON BUILT-IN EXCEPTIONS IN PYTHON
# =================================================================
"""
4. COMMON BUILT-IN EXCEPTIONS
-----------------------------
Here are 8 of the most common built-in Python exceptions every developer must know:

1. `ValueError`: Correct data type, but an inappropriate value.
2. `TypeError`: Operation applied to an incompatible data type.
3. `ZeroDivisionError`: Division or modulo operation with zero denominator.
4. `FileNotFoundError`: Requested file does not exist on disk.
5. `IndexError`: Sequence (list/tuple) subscript out of valid range.
6. `KeyError`: Dictionary key not found in dictionary.
7. `NameError`: Local or global variable name is not defined.
8. `AttributeError`: Object doesn't possess the referenced attribute/method.
"""

print("\n=========================================================")
print("  4. COMMON BUILT-IN EXCEPTIONS DEMONSTRATION")
print("=========================================================")

# 1. ValueError
try:
    num = int("abc")  # "abc" is string type, but cannot be parsed to integer
except ValueError as e:
    print(f"1. ValueError: {e}")

# 2. TypeError
try:
    total = "Epoch " + 5  # Cannot concatenate string and int directly
except TypeError as e:
    print(f"2. TypeError: {e}")

# 3. ZeroDivisionError
try:
    avg = 100 / 0
except ZeroDivisionError as e:
    print(f"3. ZeroDivisionError: {e}")

# 4. FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"4. FileNotFoundError: {e}")

# 5. IndexError
try:
    dataset_batch = [0.1, 0.4, 0.9]
    sample = dataset_batch[10]  # Index 10 out of bounds
except IndexError as e:
    print(f"5. IndexError: {e}")

# 6. KeyError
try:
    hyperparams = {"learning_rate": 0.001, "batch_size": 32}
    opt = hyperparams["optimizer"]  # Missing key
except KeyError as e:
    print(f"6. KeyError: Missing key {e}")

# 7. NameError
try:
    print(uninitialized_variable)  # Variable not defined
except NameError as e:
    print(f"7. NameError: {e}")

# 8. AttributeError
try:
    number = 42
    number.append(5)  # Integers do not have an 'append' method
except AttributeError as e:
    print(f"8. AttributeError: {e}")


# =================================================================
# 5. MULTIPLE EXCEPT BLOCKS & CATCHING MULTIPLE EXCEPTIONS
# =================================================================
"""
5. MULTIPLE EXCEPT BLOCKS
-------------------------
You can chain multiple `except` blocks to handle different types of errors specifically.
Python evaluates `except` blocks top-to-bottom and executes the FIRST match.

CATCHING MULTIPLE EXCEPTIONS IN ONE BLOCK:
  except (ValueError, TypeError) as e:
      # Handle both ValueError and TypeError here
"""

print("\n=========================================================")
print("  5. MULTIPLE EXCEPT BLOCKS & GROUPING EXCEPTIONS")
print("=========================================================")

def process_input(val):
    try:
        # Step A: Convert input to float (May raise ValueError)
        num = float(val)
        # Step B: Perform division (May raise ZeroDivisionError)
        result = 100 / num
        print(f"Input '{val}' processed successfully. Result = {result:.2f}")
    except ValueError:
        print(f"  Error: '{val}' is not a valid numeric string!")
    except ZeroDivisionError:
        print(f"  Error: Input cannot be zero!")
    except Exception as e:
        # Generic fallback for any other unexpected exception
        print(f"  Unexpected Error: {e}")

process_input("25")   # Valid -> 4.00
process_input("text") # Triggers ValueError
process_input("0")    # Triggers ZeroDivisionError


# =================================================================
# 6. RAISING EXCEPTIONS (`raise` KEYWORD)
# =================================================================
"""
6. RAISING EXCEPTIONS
---------------------
You can manually trigger exceptions using the `raise` keyword when custom conditions or
business rules are violated (e.g., negative learning rate, empty dataset).

SYNTAX:
  raise ExceptionType("Custom error message")
"""

print("\n=========================================================")
print("  6. MANUALLY RAISING EXCEPTIONS")
print("=========================================================")

def set_learning_rate(lr):
    if lr <= 0:
        raise ValueError(f"Learning rate must be greater than 0! Got: {lr}")
    if lr > 1.0:
        raise ValueError(f"Learning rate is dangerously high (> 1.0)! Got: {lr}")
    print(f"Learning rate successfully set to: {lr}")

# Testing valid and invalid values with raise
try:
    set_learning_rate(0.01)
    set_learning_rate(-0.05)  # Should trigger exception
except ValueError as e:
    print(f" Caught Raised Exception: {e}")


# =================================================================
# 7. CREATING AND USING CUSTOM EXCEPTIONS
# =================================================================
"""
7. CUSTOM EXCEPTIONS
--------------------
You can define domain-specific exceptions by creating a new class that inherits
from Python's built-in `Exception` class.

WHY CREATE CUSTOM EXCEPTIONS?
- Makes error messages domain-specific (e.g. `InvalidDatasetError`, `ModelNotTrainedError`).
- Helps distinguish application-level logic errors from general Python built-in errors.
"""

print("\n=========================================================")
print("  7. CREATING AND USING CUSTOM EXCEPTIONS")
print("=========================================================")

# Custom Exception Class
class InvalidDatasetConfigError(Exception):
    """Raised when AIML dataset configuration parameters are invalid."""
    pass

class EmptyDatasetError(Exception):
    """Raised when an loaded dataset file contains 0 samples."""
    pass

def load_dataset(samples_count):
    if samples_count == 0:
        raise EmptyDatasetError("Dataset loaded contains 0 records!")
    elif samples_count < 0:
        raise InvalidDatasetConfigError("Sample count cannot be negative!")
    print(f"Dataset loaded successfully with {samples_count} samples.")

# Test Custom Exception
try:
    load_dataset(0)
except EmptyDatasetError as e:
    print(f" Caught Custom Exception: {e}")
except InvalidDatasetConfigError as e:
    print(f" Caught Custom Exception: {e}")


# =================================================================
# 8. EXCEPTION HANDLING WITH FILE I/O
# =================================================================
"""
8. SAFE FILE I/O WITH EXCEPTION HANDLING
----------------------------------------
Combining File I/O operations with `try-except-finally` or `with open()` ensures
resilience against missing files, permissions issues, or corrupted data.
"""

print("\n=========================================================")
print("  8. EXCEPTION HANDLING WITH FILE I/O")
print("=========================================================")

def safe_read_file(filename):
    print(f"Attempting to read file: '{filename}'...")
    try:
        with open(filename, "r") as f:
            data = f.read()
            print("  Content read successfully!")
            return data
    except FileNotFoundError:
        print(f"  [ERROR] File '{filename}' does not exist on disk!")
    except PermissionError:
        print(f"  [ERROR] Insufficient OS permissions to read '{filename}'.")
    except Exception as e:
        print(f"  [ERROR] An unexpected I/O error occurred: {e}")
    return None

safe_read_file("non_existent_config.json")


# =================================================================
# 9. RETAINED CORE TOPICS: LIST COMPREHENSIONS & JSON MODULE
# =================================================================
"""
9. RETAINED TOPICS: LIST COMPREHENSIONS & JSON HANDLING
-------------------------------------------------------
(Preserved and integrated from original notes with added exception handling)

A. LIST COMPREHENSIONS:
   Syntax: [ output for item in iterable if condition ]
   
B. JSON MODULE:
   1. string to dict  : json.loads()
   2. dict to string  : json.dumps()
   3. file to dict    : json.load()
   4. dict to file    : json.dump()
"""

print("\n=========================================================")
print("  9. LIST COMPREHENSIONS & JSON MODULE WITH ERROR HANDLING")
print("=========================================================")

# --- A. List Comprehension Examples ---
print("--- List Comprehensions ---")
# Example 1: Squares 1 to 5
sq = [i * i for i in range(1, 6)]
print(f"Squares (1 to 5): {sq}")

# Example 2: Squares of odd numbers only
sq_odd = [i * i for i in range(1, 6) if i % 2 != 0]
print(f"Odd Squares (1 to 5): {sq_odd}\n")


# --- B. JSON Module Operations with Exception Handling ---
print("--- JSON Operations ---")
config_data = {
    "model_name": "ResNet50",
    "epochs": 50,
    "use_gpu": True
}

# 1. json.dumps() - Convert Python dict to JSON String
json_string = json.dumps(config_data, indent=2)
print(f"JSON String:\n{json_string}\n")

# 2. json.loads() - Parse JSON String back to Python Dict (with handling)
invalid_json = '{"model_name": "ResNet50", "epochs": 50, }'  # Trailing comma (Invalid JSON)

try:
    parsed_dict = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f" Caught json.JSONDecodeError: Invalid JSON format!\n Details: {e}")


# =================================================================
# 10. BEST PRACTICES FOR CLEAN EXCEPTION HANDLING
# =================================================================
"""
10. BEST PRACTICES CHEAT SHEET
------------------------------
1. NEVER USE BARE `except:` WITHOUT SPECIFYING AN EXCEPTION CLASS:
   - Bad: `except:` (Catches system signals like Ctrl+C and SystemExit!).
   - Good: `except Exception as e:` or specific error classes.

2. KEEP `try` BLOCKS SMALL AND GRANULAR:
   - Put only the exact line(s) that might fail inside the `try` block.

3. DO NOT SWALLOW EXCEPTIONS SILENTLY:
   - Bad: `except KeyError: pass` (Hides bugs and makes debugging impossible!).
   - Good: Log or print an informative error message.

4. CLEAN UP RESOURCES:
   - Use `finally` or context managers (`with open()`) for files/locks.
"""

print("\n=========================================================")
print("  10. BEST PRACTICES FOR EXCEPTION HANDLING")
print("=========================================================")
print("1. Avoid bare `except:`. Always catch specific exceptions.")
print("2. Keep `try` blocks as small as possible.")
print("3. Never silently swallow errors (`pass`) without logging.")
print("4. Always clean up file handles and resources using context managers or `finally`.\n")


# =================================================================
# 11. REAL-WORLD AIML EXAMPLE: ROBUST CONFIG & DATASET LOADER
# =================================================================
"""
11. REAL-WORLD AIML APPLICATION
-------------------------------
Below is a complete, production-ready utility that safely loads an AIML experiment
JSON configuration file, validates hyperparameter ranges, and handles missing or bad data gracefully.
"""

print("=========================================================")
print("  11. REAL-WORLD EXAMPLE: AIML CONFIG LOADER & VALIDATOR")
print("=========================================================")

class ConfigValidationError(Exception):
    """Raised when configuration values fail validation."""
    pass

def load_and_validate_config(config_filepath):
    """Safely loads and validates JSON model hyperparameter configuration."""
    print(f"Loading configuration from '{config_filepath}'...")
    
    # 1. Attempt File Read
    try:
        with open(config_filepath, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"  [Error] Config file '{config_filepath}' not found! Using fallback defaults.")
        return {"batch_size": 32, "learning_rate": 0.001, "status": "default"}
    except json.JSONDecodeError as e:
        print(f"  [Error] Corrupted JSON in config file: {e}")
        return None

    # 2. Validate Keys & Values
    try:
        batch_size = config["batch_size"]
        lr = config["learning_rate"]

        if not isinstance(batch_size, int) or batch_size <= 0:
            raise ConfigValidationError(f"Invalid batch_size: {batch_size}. Must be positive int.")
        if not isinstance(lr, float) or lr <= 0:
            raise ConfigValidationError(f"Invalid learning_rate: {lr}. Must be positive float.")

        print(f"  Config Loaded & Validated Successfully! Batch Size: {batch_size}, LR: {lr}")
        return config

    except KeyError as e:
        print(f"  [Validation Error] Missing required hyperparameter key: {e}")
    except ConfigValidationError as e:
        print(f"  [Validation Error] {e}")
    
    return None

# Test Scenario A: Non-existent file (triggers default fallback)
cfg1 = load_and_validate_config("missing_experiment_config.json")

# Test Scenario B: Create valid config file and test
demo_cfg_path = "demo_config.json"
valid_config_data = {"batch_size": 64, "learning_rate": 0.0005, "model": "Transformer"}

with open(demo_cfg_path, "w") as f:
    json.dump(valid_config_data, f)

cfg2 = load_and_validate_config(demo_cfg_path)

# Cleanup demo file
if os.path.exists(demo_cfg_path):
    os.remove(demo_cfg_path)


# =================================================================
# 12. PRACTICE EXERCISES FOR LEARNERS
# =================================================================
"""
===================================================================
                     PRACTICE EXERCISES
===================================================================

Exercise 1: Robust Integer Input Prompt
---------------------------------------
Write a function `get_valid_integer(prompt)` that repeatedly prompts the user
to enter an integer using `input()`.
- Use a `try-except` block to catch `ValueError` if the user enters non-numeric text.
- Print "Invalid input! Please enter a valid number." and loop until a valid integer is entered.

Exercise 2: Safe List Element Access
------------------------------------
Write a function `safe_get_element(lst, index, default_value=None)` that takes a list,
an integer index, and an optional default value.
- Use `try-except` to catch `IndexError` or `TypeError`.
- If valid, return `lst[index]`. If index is out of bounds or type is invalid, return `default_value`.

Exercise 3: Custom Age Validator Exception
-------------------------------------------
Create a custom exception `InvalidAgeError(Exception)`.
Write a function `check_voting_eligibility(age)`:
- If `age < 0`, raise `InvalidAgeError("Age cannot be negative!")`.
- If `age < 18`, return "Not eligible to vote."
- If `age >= 18`, return "Eligible to vote."
Handle the custom exception cleanly using `try-except`.

Exercise 4: Safe Dictionary Value Retrieval & Type Cast
-------------------------------------------------------
Write a function `get_numeric_metric(metrics_dict, key)` that retrieves a key from a dict 
and converts its value to `float`.
- Handle `KeyError` if key is missing (return `0.0`).
- Handle `ValueError` or `TypeError` if conversion fails (return `0.0`).
- Test with dictionary: `{"accuracy": "94.5", "loss": "invalid", "epoch": 10}`.
"""
