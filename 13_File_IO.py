"""
===================================================================
                  PYTHON FILE I/O (INPUT / OUTPUT)
===================================================================

This module covers File Handling in Python in detail:
  1. What File I/O is and why it is used in AIML & software dev
  2. Opening and closing files (`open()`, `close()`)
  3. File modes (`r`, `w`, `a`, `x`, `b`, `t`, `+`)
  4. Reading files (`read()`, `readline()`, `readlines()`, file iteration)
  5. Writing and Appending files (`write()`, `writelines()`)
  6. Using the `with open()` statement (Context Managers)
  7. Checking file existence (`os.path`, `pathlib`)
  8. Working with Text vs Binary files
  9. File paths & cross-platform path issues
  10. Common File I/O errors & exception handling
  11. Real-world AIML training log recorder example
  12. Practice exercises for learners
"""

import os
import pathlib

# =================================================================
# 1. WHAT IS FILE I/O AND WHY IS IT USED?
# =================================================================
"""
1. WHAT IS FILE I/O?
-------------------
File I/O (Input/Output) refers to how a program reads data FROM files (Input)
and writes data TO files (Output) on a computer's permanent storage (hard drive/SSD).

WHY USE FILE I/O?
-----------------
1. Data Persistence: Variables in Python live in RAM (Random Access Memory). 
   When your Python program stops running, RAM is cleared and all variable 
   data is lost. Files allow data to survive after program execution.
2. AIML Applications:
   - Reading datasets (CSV, JSON, images, audio, text corpora).
   - Saving trained model weights and hyperparameter configurations.
   - Writing epoch-by-epoch training logs, loss metrics, and evaluation reports.
"""

print("=========================================================")
print("  1. INTRODUCTION TO FILE I/O")
print("=========================================================")
print("File I/O enables persistent storage. Data stored in variables is lost when")
print("the script finishes, but files keep data permanently on disk.\n")


# =================================================================
# 2. OPENING AND CLOSING FILES & FILE MODES
# =================================================================
"""
2. OPENING AND CLOSING FILES
----------------------------
- `open(filename, mode)`: Built-in function to open a file. Returns a file object.
- `file.close()`: Closes the open file freed memory resources.

CRITICAL MODES CHEAT SHEET:
---------------------------
  r  : Reading mode (Default). Opens file for reading. Error if file does not exist.
  w  : Writing mode. Opens file for writing. Overwrites existing content or creates a new file.
  a  : Append mode. Opens file for writing. Appends data at the end without overwriting.
  x  : Exclusive creation mode. Creates a new file. Fails/raises FileExistsError if file exists.
  b  : Binary mode. Used for binary files (images, audio, model checkpoints, compiled bytes).
  t  : Text mode (Default). Used for text files (.txt, .py, .csv, .json).
  +  : Updating mode (Read + Write). Combined with other modes e.g., 'r+', 'w+', 'a+'.

SYNTAX:
  file_object = open("filename.txt", "mode")
  # operations ...
  file_object.close()
"""

print("=========================================================")
print("  2. OPENING AND CLOSING FILES (MANUAL APPROACH)")
print("=========================================================")

# Demo: Manual open and close
sample_file_path = "demo_manual.txt"

# Step 1: Open file in write mode ('w')
file_obj = open(sample_file_path, "w")
file_obj.write("Hello! This file was opened and written using manual open().\n")

# Step 2: ALWAYS close the file manually!
file_obj.close()
print(f"Created and closed '{sample_file_path}' manually.")

# Step 3: Read back manually
file_obj = open(sample_file_path, "r")
content = file_obj.read()
file_obj.close()
print("Read content:")
print(content)


# =================================================================
# 3. READING FILES: read(), readline(), readlines() & ITERATION
# =================================================================
"""
3. READING METHODS
------------------
1. `read()` or `read(size)`: 
   - Without argument: Reads the ENTIRE file content as a single string.
   - With `size` argument: Reads up to `size` characters/bytes.
2. `readline()`:
   - Reads a SINGLE line from the file up to the newline character ('\\n').
   - Sequential calls read consecutive lines.
3. `readlines()`:
   - Reads ALL lines and returns them as a LIST of strings.
4. Line-by-line Loop Iteration (`for line in file`):
   - Memory-efficient! Best for huge files (e.g., multi-gigabyte AIML datasets).
"""

print("=========================================================")
print("  3. READING FILES DEMONSTRATION")
print("=========================================================")

# Create a multi-line sample file first
read_demo_path = "demo_reading.txt"
with open(read_demo_path, "w") as f:
    f.write("Line 1: Python for AIML\n")
    f.write("Line 2: Data Preprocessing\n")
    f.write("Line 3: Model Training\n")
    f.write("Line 4: Model Evaluation\n")

# Method A: read() - Entire content
with open(read_demo_path, "r") as f:
    full_text = f.read()
print("--- Method A: read() [Entire File] ---")
print(full_text)

# Method B: read(size) - Specific character limit
with open(read_demo_path, "r") as f:
    chunk = f.read(15)
print("--- Method B: read(15) [First 15 chars] ---")
print(f"'{chunk}'\n")

# Method C: readline() - Line by line manually
with open(read_demo_path, "r") as f:
    line1 = f.readline()
    line2 = f.readline()
print("--- Method C: readline() [First two lines] ---")
print(f"Line 1: {line1.strip()}")
print(f"Line 2: {line2.strip()}\n")

# Method D: readlines() - Returns list of lines
with open(read_demo_path, "r") as f:
    lines_list = f.readlines()
print("--- Method D: readlines() [List of lines] ---")
print(lines_list)
print(f"Total lines count: {len(lines_list)}\n")

# Method E: Iteration over file object (Best Practice for large files)
print("--- Method E: for line in file (Memory Efficient) ---")
with open(read_demo_path, "r") as f:
    for index, line in enumerate(f, start=1):
        print(f"  Line {index}: {line.strip()}")
print()


# =================================================================
# 4. WRITING AND APPENDING DATA TO FILES
# =================================================================
"""
4. WRITING VS APPENDING
-----------------------
- Write mode ('w'): Overwrites any existing file content. If file does not exist, creates it.
- Append mode ('a'): Adds new content to the END of the file without deleting existing text.
- `write(string)`: Writes a single string to the file.
- `writelines(list_of_strings)`: Writes a list/iterable of strings to the file.
  (Note: `writelines` does NOT automatically add newlines '\\n', you must include them yourself!).
"""

print("=========================================================")
print("  4. WRITING AND APPENDING DEMONSTRATION")
print("=========================================================")

write_demo_path = "demo_write_append.txt"

# Step 1: Writing using write() and writelines() ('w' mode)
with open(write_demo_path, "w") as f:
    f.write("--- LOG START ---\n")
    lines_to_add = [
        "Initial Status: Initializing Neural Network...\n",
        "Epoch 0: Loss = 0.85, Accuracy = 62.5%\n"
    ]
    f.writelines(lines_to_add)

print("Step 1: File created with initial logs in 'w' mode.")

# Step 2: Appending new logs ('a' mode)
with open(write_demo_path, "a") as f:
    f.write("Epoch 1: Loss = 0.42, Accuracy = 81.0%\n")
    f.write("Epoch 2: Loss = 0.18, Accuracy = 94.5%\n")
    f.write("--- LOG END ---\n")

print("Step 2: New epoch metrics appended in 'a' mode.")

# Step 3: Verify content
print("\nFinal File Contents after Writing & Appending:")
with open(write_demo_path, "r") as f:
    print(f.read())


# =================================================================
# 5. USING THE 'with open()' STATEMENT (CONTEXT MANAGERS)
# =================================================================
"""
5. WHY IS 'with open()' PREFERRED?
----------------------------------
In Python, using `with open(...) as file:` is the RECOMMENDED standard practice.

ADVANTAGES OF CONTEXT MANAGERS (`with` statement):
1. Automatic Cleanup: The file is automatically closed when the `with` block finishes,
   even if an exception or error occurs inside the block!
2. Resource Leak Prevention: Avoids keeping open file handles in memory.
3. Cleaner Syntax: No need to explicitly write `file.close()` every time.

SYNTAX:
  with open("filename.txt", "mode") as file_var:
      # Perform file operations
      data = file_var.read()
  # File is automatically closed here outside the block!
"""

print("=========================================================")
print("  5. THE 'with open()' STATEMENT (PREFERRED APPROACH)")
print("=========================================================")

with_demo_path = "demo_with.txt"

with open(with_demo_path, "w") as f:
    f.write("Using 'with open()' context manager for clean file handling.")

# Verify closed status
print(f"Inside 'with' block file is active.")
print(f"Is file closed outside 'with' block? -> {f.closed}")


# =================================================================
# 6. CHECKING IF A FILE EXISTS
# =================================================================
"""
6. CHECKING FILE EXISTENCE
--------------------------
Before reading or deleting files, always check if the file exists to prevent
runtime `FileNotFoundError` exceptions.

Two Common Approaches:
1. `os.path.exists(path)` / `os.path.isfile(path)`
2. `pathlib.Path(path).exists()` / `pathlib.Path(path).is_file()` (Modern OOP approach)
"""

print("\n=========================================================")
print("  6. CHECKING FILE EXISTENCE")
print("=========================================================")

test_file = "demo_with.txt"
fake_file = "non_existent_dataset.csv"

# Approach 1: Using os module
print(f"Using os.path.exists('{test_file}'): {os.path.exists(test_file)}")
print(f"Using os.path.exists('{fake_file}'): {os.path.exists(fake_file)}")

# Approach 2: Using pathlib module (Recommended in modern Python)
file_path_obj = pathlib.Path(test_file)
print(f"Using pathlib.Path('{test_file}').is_file(): {file_path_obj.is_file()}")


# =================================================================
# 7. WORKING WITH TEXT AND BASIC BINARY FILES
# =================================================================
"""
7. TEXT VS BINARY FILES
-----------------------
- Text Files ('t' mode): Store human-readable characters encoded in UTF-8 or ASCII.
  (Examples: .txt, .py, .csv, .json, .html)
- Binary Files ('b' mode): Store raw bytes (0s and 1s) representing non-text media
  or serialized binary structures.
  (Examples: .png, .jpg, .mp3, .pkl (Pickle models), .pth (PyTorch models), .exe)

Reading/Writing Bytes:
- Requires byte literals e.g., `b"Hello Bytes"` or `bytes([65, 66, 67])`.
"""

print("\n=========================================================")
print("  7. TEXT VS BINARY FILES DEMONSTRATION")
print("=========================================================")

binary_demo_path = "demo_model_weights.bin"

# Step 1: Write raw bytes to a binary file ('wb')
mock_binary_weights = bytes([0x41, 0x49, 0x4D, 0x4C, 0x00, 0xFF, 0x7F])
with open(binary_demo_path, "wb") as f:
    f.write(mock_binary_weights)
print(f"Wrote raw binary data ({len(mock_binary_weights)} bytes) to '{binary_demo_path}'.")

# Step 2: Read raw bytes back from binary file ('rb')
with open(binary_demo_path, "rb") as f:
    raw_data = f.read()

print(f"Read binary data type: {type(raw_data)}")
print(f"Raw Byte Representation: {raw_data}")
print(f"Hex Representation: {raw_data.hex()}")


# =================================================================
# 8. FILE PATHS & COMMON PATH-RELATED ISSUES
# =================================================================
r"""
8. FILE PATHS & OS COMPATIBILITY
--------------------------------
1. Relative Path: Path relative to the current working directory.
   Example: "data/dataset.csv" or "./data/dataset.csv"
2. Absolute Path: Complete system path starting from the root directory.
   Example (Windows): "C:/Users/Prajwal/Projects/data.csv"
   Example (Linux/Mac): "/home/prajwal/projects/data.csv"

PATH ISSUES & BEST PRACTICES:
- Windows Backslash Issue: Windows uses '\' in paths, but '\' in Python strings acts 
  as an escape character (e.g. \n, \t, \U).
  Solutions:
    a. Use forward slashes: "C:/Users/Prajwal/data.csv" (Supported on Windows by Python!).
    b. Use Raw Strings: r"C:\Users\Prajwal\data.csv"
    c. Use `os.path.join()` or `pathlib.Path`: Automatically handles OS path separators!
"""

print("\n=========================================================")
print("  8. FILE PATHS & CROSS-PLATFORM PATH HANDLING")
print("=========================================================")

# Get Current Working Directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# Joining paths safely using os.path.join
folder_name = "data_folder"
file_name = "sample_dataset.csv"
safe_path_os = os.path.join(cwd, folder_name, file_name)
print(f"OS-Safe Path (os.path.join): {safe_path_os}")

# Joining paths using pathlib.Path (Overloaded '/' operator)
safe_path_lib = pathlib.Path(cwd) / folder_name / file_name
print(f"Pathlib Safe Path: {safe_path_lib}")


# =================================================================
# 9. COMMON FILE I/O ERRORS & HOW TO HANDLE THEM
# =================================================================
"""
9. COMMON FILE ERRORS
---------------------
- `FileNotFoundError`: Occurs when trying to read or open a file in 'r' mode that doesn't exist.
- `PermissionError`: Occurs when accessing a file without proper OS permissions or trying 
  to open a directory as a file.
- `IsADirectoryError`: Occurs when expecting a file but specifying a directory path.
- `FileExistsError`: Occurs when opening a file in 'x' mode if the file already exists.
"""

print("\n=========================================================")
print("  9. HANDLING COMMON FILE I/O ERRORS")
print("=========================================================")

missing_filename = "missing_data_2026.csv"

try:
    print(f"Attempting to open '{missing_filename}'...")
    with open(missing_filename, "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print(f" caught FileNotFoundError: {e}")
    print("  -> Fix: Verify path or create default file if missing.")
except PermissionError as e:
    print(f" caught PermissionError: {e}")
except Exception as e:
    print(f" caught Unexpected Error: {e}")


# =================================================================
# 10. REAL-WORLD PRACTICAL EXAMPLE: AIML TRAINING METRICS LOGGER
# =================================================================
"""
10. REAL-WORLD AIML APPLICATION
-------------------------------
Below is a complete, realistic utility that logs machine learning training progress
(Epoch, Loss, Accuracy) to a CSV log file and later reads it back to display summary statistics.
"""

print("\n=========================================================")
print("  10. REAL-WORLD EXAMPLE: AIML TRAINING LOG RECORDER")
print("=========================================================")

class MetricsLogger:
    def __init__(self, log_filepath):
        self.filepath = log_filepath
        # Initialize log file with CSV header if it does not exist
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w") as f:
                f.write("Epoch,Loss,Accuracy\n")

    def log_epoch(self, epoch, loss, accuracy):
        """Appends metric for a single epoch to the log file."""
        with open(self.filepath, "a") as f:
            f.write(f"{epoch},{loss:.4f},{accuracy:.2f}\n")

    def read_summary(self):
        """Reads logs and displays epoch stats."""
        print(f"\n--- Metrics Summary from '{self.filepath}' ---")
        if not os.path.exists(self.filepath):
            print("No log file found.")
            return

        with open(self.filepath, "r") as f:
            header = f.readline()  # Skip CSV header
            lines = f.readlines()
            
        print(f"Total Epochs Recorded: {len(lines)}")
        for line in lines:
            ep, loss, acc = line.strip().split(",")
            print(f"  [Epoch {ep}] Loss: {loss} | Accuracy: {acc}%")

# Simulation of training loop
logger = MetricsLogger("aiml_training_log.csv")

# Simulate 3 training epochs
simulated_epochs = [
    (1, 0.6931, 52.0),
    (2, 0.4120, 78.5),
    (3, 0.1542, 95.2)
]

for epoch, loss, acc in simulated_epochs:
    logger.log_epoch(epoch, loss, acc)

# Display summary report
logger.read_summary()


# =================================================================
# CLEANUP TEMPORARY DEMO FILES
# =================================================================
# Clean up temporary files created during demonstration
temp_files = [
    sample_file_path, read_demo_path, write_demo_path,
    with_demo_path, binary_demo_path, "aiml_training_log.csv"
]
for file_name in temp_files:
    if os.path.exists(file_name):
        os.remove(file_name)


# =================================================================
# 11. PRACTICE EXERCISES FOR LEARNERS
# =================================================================
"""
===================================================================
                     PRACTICE EXERCISES
===================================================================

Exercise 1: Word & Line Counter
------------------------------
Write a Python function `count_file_stats(filename)` that takes a text 
filename as input, reads the file, and prints:
- Total number of lines
- Total number of words
- Total number of characters
(Hint: Use `with open(filename, 'r')` and split lines into words using `.split()`).

Exercise 2: User Profile Saver
-----------------------------
Create a program that prompts for user input (Name, Age, Favorite Programming Language)
and appends this information as a new line in a file named `users.txt` using append mode ('a').
Ensure the user data is formatted cleanly e.g., "Name: Prajwal | Age: 22 | Lang: Python".

Exercise 3: Safe File Reader with Exception Handling
----------------------------------------------------
Write a function `safe_read_dataset(filepath)` that attempts to open and read a file.
- If the file exists, return its content.
- If the file is missing (`FileNotFoundError`), catch the error, print a friendly warning 
  "Dataset file missing! Creating empty placeholder...", and create an empty file at that path.

Exercise 4: Binary File Copy Tool
---------------------------------
Write a function `copy_binary_file(source_path, destination_path)` that copies a 
binary file (e.g. an image or raw data file) from source to destination using 
chunked reading (`read(4096)`) in binary mode ('rb' and 'wb').
"""