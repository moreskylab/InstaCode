
## Solutions: Category 1 - Python Fundamentals (Q1-Q100)

### Basic Concepts Solutions (Q1-Q25)

#### Q1: What is Python? List its advantages and disadvantages.

**Complete Answer:**

```python
"""
PYTHON OVERVIEW - Complete Interview Answer
============================================
"""

# DEFINITION
"""
Python is a high-level, interpreted, general-purpose programming language
created by Guido van Rossum in 1991.

Named after: Monty Python's Flying Circus (not the snake!)
Current Version: Python 3.12 (as of 2024)
Philosophy: "There should be one-- and preferably only one --obvious way to do it"
"""

# ADVANTAGES
advantages = {
    "1. Easy to Learn": {
        "description": "Simple, readable syntax similar to English",
        "example": """
# Python
if user_age >= 18:
    print("Adult")

# vs Java
if (userAge >= 18) {
    System.out.println("Adult");
}
        """
    },

    "2. Interpreted Language": {
        "description": "No compilation needed, execute line by line",
        "benefit": "Faster development cycle, easier debugging"
    },

    "3. Dynamically Typed": {
        "description": "No need to declare variable types",
        "example": """
# Python
x = 5        # int
x = "hello"  # now str - no problem!

# vs C++
int x = 5;
x = "hello";  // Error!
        """
    },

    "4. Extensive Libraries": {
        "description": "200,000+ packages on PyPI",
        "examples": [
            "Data Science: NumPy, Pandas, Matplotlib",
            "ML/AI: TensorFlow, PyTorch, Scikit-learn",
            "Web: Django, Flask, FastAPI",
            "Automation: Selenium, BeautifulSoup"
        ]
    },

    "5. Cross-Platform": {
        "description": "Write once, run anywhere",
        "platforms": ["Windows", "Linux", "macOS", "Unix"]
    },

    "6. Object-Oriented": {
        "description": "Supports OOP principles",
        "features": ["Classes", "Inheritance", "Polymorphism", "Encapsulation"]
    },

    "7. Open Source": {
        "description": "Free to use and distribute",
        "benefit": "Large community support, continuous improvement"
    },

    "8. Integration": {
        "description": "Easy integration with C/C++, Java, .NET",
        "use_case": "Can use Python as scripting language for existing apps"
    },

    "9. Rapid Prototyping": {
        "description": "Quick development and testing",
        "use_case": "Perfect for startups and MVPs"
    },

    "10. Versatile": {
        "applications": [
            "Web Development",
            "Data Science & Analytics",
            "Machine Learning & AI",
            "Automation & Scripting",
            "Scientific Computing",
            "Game Development",
            "Desktop Applications",
            "Network Programming"
        ]
    }
}

# DISADVANTAGES
disadvantages = {
    "1. Slow Execution Speed": {
        "reason": "Interpreted, not compiled",
        "comparison": "10-100x slower than C/C++",
        "mitigation": [
            "Use PyPy (JIT compiler)",
            "Write critical sections in C (Cython)",
            "Use NumPy for numerical operations"
        ],
        "example": """
# Example: Matrix multiplication
# Pure Python: ~2 seconds
# NumPy (C backend): ~0.02 seconds (100x faster!)
        """
    },

    "2. High Memory Consumption": {
        "reason": "Everything is an object, dynamic typing",
        "comparison": "Python int uses 28 bytes vs C int 4 bytes",
        "impact": "Not ideal for memory-constrained devices"
    },

    "3. Global Interpreter Lock (GIL)": {
        "description": "Prevents true multi-threading",
        "impact": "CPU-bound programs can't utilize multiple cores",
        "workaround": "Use multiprocessing instead of threading",
        "example": """
# Threading (limited by GIL for CPU work)
import threading

# Multiprocessing (bypasses GIL)
import multiprocessing
        """
    },

    "4. Not Native Mobile Development": {
        "issue": "Not first-class for iOS/Android",
        "alternatives": "Kivy, BeeWare exist but not mainstream",
        "recommendation": "Use Swift/Kotlin for native mobile"
    },

    "5. Runtime Errors": {
        "reason": "Dynamic typing catches errors at runtime",
        "example": """
# This error only shows when code executes
def divide(a, b):
    return a / b

divide(10, 0)  # ZeroDivisionError (runtime!)
        """,
        "solution": "Type hints + mypy for static checking"
    },

    "6. Design Restrictions": {
        "description": "Significant whitespace (indentation)",
        "issue": "Can cause errors if not consistent",
        "example": """
# Error due to indentation
if True:
    print("Hello")
  print("World")  # IndentationError!
        """
    },

    "7. Database Access": {
        "issue": "DB layers less developed than Java/PHP",
        "note": "Improving with SQLAlchemy, Django ORM"
    },

    "8. Two Major Versions": {
        "issue": "Python 2 vs Python 3 incompatibility",
        "status": "Python 2 EOL since 2020, but legacy code exists",
        "migration": "Can be challenging for large codebases"
    }
}

# WHEN TO USE PYTHON
use_python_when = [
    "Building web applications (Django, Flask)",
    "Data analysis and visualization",
    "Machine learning and AI projects",
    "Automation and scripting tasks",
    "Rapid prototyping",
    "Scientific computing",
    "Web scraping",
    "API development",
    "DevOps and system administration"
]

# WHEN NOT TO USE PYTHON
avoid_python_when = [
    "Building native mobile apps",
    "Need maximum performance (game engines, HFT)",
    "Memory-critical applications",
    "Real-time systems with strict timing",
    "Low-level system programming",
    "Applications requiring true multi-threading"
]

# COMPARISON WITH OTHER LANGUAGES
comparison = """
Python vs Java:
  + Easier to learn, faster development
  + Better for data science, scripting
  - Slower execution
  - Less suitable for Android development

Python vs JavaScript:
  + Better for backend, data science, ML
  + Cleaner syntax for complex logic
  - Not for frontend (browser)
  - Smaller web ecosystem than Node.js

Python vs C++:
  + Much easier to learn and use
  + Faster development time
  - Significantly slower execution
  - Higher memory usage

Python vs R:
  + General-purpose, not just statistics
  + Better software engineering practices
  - R better for some statistical analyses
"""

# PRINT COMPREHENSIVE SUMMARY
print("=" * 80)
print("PYTHON LANGUAGE OVERVIEW")
print("=" * 80)

print("\n✅ ADVANTAGES:")
for i, (adv, details) in enumerate(advantages.items(), 1):
    print(f"\n{i}. {adv}")
    if isinstance(details, dict):
        for key, value in details.items():
            if isinstance(value, list):
                print(f"   {key}:")
                for item in value:
                    print(f"     - {item}")
            else:
                print(f"   {key}: {value}")

print("\n\n❌ DISADVANTAGES:")
for i, (disadv, details) in enumerate(disadvantages.items(), 1):
    print(f"\n{i}. {disadv}")
    if isinstance(details, dict):
        for key, value in details.items():
            if isinstance(value, list):
                print(f"   {key}:")
                for item in value:
                    print(f"     - {item}")
            elif not isinstance(value, str) or len(value) < 100:
                print(f"   {key}: {value}")

print("\n\n🎯 USE PYTHON FOR:")
for use_case in use_python_when:
    print(f"  ✓ {use_case}")

print("\n\n⚠️ AVOID PYTHON FOR:")
for avoid_case in avoid_python_when:
    print(f"  ✗ {avoid_case}")

print("\n" + comparison)

# SAMPLE PYTHON CODE SHOWCASING FEATURES
print("\n" + "=" * 80)
print("PYTHON CODE EXAMPLE - Showcasing Key Features")
print("=" * 80)

# Simple yet powerful example
def fibonacci_generator(n):
    """Generate Fibonacci sequence - showcases generators, clean syntax"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# List comprehension - Pythonic feature
squares = [x**2 for x in range(10)]

# Dictionary comprehension
char_count = {char: text.count(char) for char in set("hello world")}

# Lambda function
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[0])

# Context manager - automatic resource management
with open('file.txt', 'w') as f:
    f.write("Python is awesome!")

# Decorator - metaprogramming
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def example_function():
    return sum(range(1000000))

print("\nKey Takeaway for Interviews:")
print("""
When asked about Python:
1. Start with definition (high-level, interpreted, OOP)
2. Mention 3-4 key advantages (easy to learn, extensive libraries, versatile)
3. Acknowledge 2-3 disadvantages (speed, GIL, mobile)
4. Give real-world use case example from your experience
5. Compare briefly with one other language if relevant to job

Example: "I used Python for a data pipeline project because its Pandas library
         made data manipulation 10x faster than our previous Java solution,
         despite Python being slower in raw execution speed."
""")
```

---

#### Q2: What is PEP 8 and why is it important?

**Complete Solution:**

```python
"""
PEP 8 - PYTHON STYLE GUIDE
===========================
PEP = Python Enhancement Proposal
PEP 8 = Style Guide for Python Code
Author: Guido van Rossum, Barry Warsaw, Nick Coghlan
"""

# WHY PEP 8 IS IMPORTANT
importance = """
1. Readability: Code is read more often than written
2. Consistency: Team members can understand each other's code
3. Maintainability: Easier to maintain consistent codebase
4. Professionalism: Shows you write production-quality code
5. Collaboration: Essential for open-source contributions
"""

# KEY PEP 8 GUIDELINES
print("=" * 80)
print("PEP 8 STYLE GUIDE - KEY RULES")
print("=" * 80)

# 1. INDENTATION
print("\n1. INDENTATION - Use 4 spaces per level")

# ✅ Correct
def calculate_total(items):
    total = 0
    for item in items:
        if item.is_valid():
            total += item.price
    return total

# ❌ Wrong - mixing tabs and spaces, or using 2 spaces
# def calculate_total(items):
#   total = 0    # 2 spaces - inconsistent!
#     for item in items:    # tab? - error!

# 2. LINE LENGTH
print("\n2. LINE LENGTH - Max 79 characters for code, 72 for comments")

# ✅ Correct - break long lines
def send_email(recipient_email, subject, body, 
               cc_list=None, bcc_list=None,
               attachments=None):
    pass

# ✅ Correct - use parentheses for implicit line continuation
total = (first_variable + second_variable
         + third_variable + fourth_variable)

# ❌ Wrong - line too long
# def send_email(recipient_email, subject, body, cc_list=None, bcc_list=None, attachments=None, priority="normal"):

# 3. BLANK LINES
print("\n3. BLANK LINES - 2 before top-level, 1 before methods")

# ✅ Correct

class MyClass:
    """Class docstring"""

    def __init__(self):
        self.value = 0

    def method_one(self):
        pass

    def method_two(self):
        pass


class AnotherClass:
    """Two blank lines before this class"""
    pass


def top_level_function():
    """Two blank lines before this function"""
    pass

# 4. IMPORTS
print("\n4. IMPORTS - One per line, grouped and ordered")

# ✅ Correct
import os
import sys
from typing import List, Dict

import numpy as np
import pandas as pd

from myapp.models import User
from myapp.utils import helper_function

# ❌ Wrong
# import os, sys    # Multiple on one line
# from typing import *    # Wildcard import
# import myapp.models    # After third-party

# Import order:
# 1. Standard library
# 2. Third-party
# 3. Local application

# 5. NAMING CONVENTIONS
print("\n5. NAMING CONVENTIONS")

# ✅ Correct naming
class UserAccount:  # PascalCase for classes
    pass

def calculate_total_price():  # snake_case for functions
    pass

user_name = "Alice"  # snake_case for variables
MAX_CONNECTIONS = 100  # UPPER_CASE for constants

_private_variable = "secret"  # Leading underscore for internal use
__name_mangled = "very_private"  # Double underscore for name mangling

# ❌ Wrong naming
# class userAccount:  # Wrong case
# def CalculateTotalPrice():  # Wrong case
# UserName = "Alice"  # Wrong case for variable
# maxConnections = 100  # Wrong case for constant

# 6. WHITESPACE
print("\n6. WHITESPACE IN EXPRESSIONS")

# ✅ Correct
spam(ham[1], {eggs: 2})
x = 1
y = 2
long_variable = 3

if x == 4:
    print(x, y)

dict_value = {'key': 'value'}
list_slice = my_list[1:4]

# ❌ Wrong
# spam( ham[ 1 ], { eggs: 2 } )  # Extra spaces
# x=1  # No space around =
# y  =  2  # Too many spaces
# if x==4:  # No space around ==
# dict_value = {'key' : 'value'}  # Space before colon
# list_slice = my_list[1: 4]  # Space after colon

# 7. COMMENTS
print("\n7. COMMENTS - Complete sentences, update when code changes")

# ✅ Correct - Inline comment (use sparingly)
x = x + 1  # Compensate for border

# ✅ Correct - Block comment
# This is a longer explanation that spans multiple lines.
# It explains the complex logic below in detail.
# Always keep comments up to date with code changes.

def complex_function():
    """
    Docstring explains what function does.

    Args:
        param1: Description

    Returns:
        Description of return value
    """
    pass

# ❌ Wrong
#incorrect comment spacing
# x=x+1 Compensate for border  # Comment should be 2 spaces after code

# 8. DOCSTRINGS
print("\n8. DOCSTRINGS - Use for all public modules, functions, classes, methods")

# ✅ Correct
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns:
        float: The area of the rectangle

    Raises:
        ValueError: If length or width is negative

    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    if length < 0 or width < 0:
        raise ValueError("Dimensions must be positive")
    return length * width

# 9. STRING QUOTES
print("\n9. STRING QUOTES - Be consistent")

# ✅ Correct - pick one style and stick to it
single_quote = 'Hello'
double_quote = "World"
triple_quote = """Multi-line
string"""

# Use the other quote to avoid escaping
phrase = "Don't worry"  # Better than 'Don\'t worry'

# 10. PROGRAMMING RECOMMENDATIONS
print("\n10. PROGRAMMING RECOMMENDATIONS")

# ✅ Correct - Comparisons
if value is None:  # Use 'is' for None
    pass

if isinstance(obj, str):  # Use isinstance for type checks
    pass

if my_list:  # Implicit false check
    pass

# ❌ Wrong
# if value == None:  # Use 'is', not '=='
# if type(obj) == str:  # Use isinstance
# if len(my_list) > 0:  # Implicit check is more Pythonic

# ✅ Correct - Use 'in' for containment
if key in dictionary:
    pass

# ❌ Wrong
# if dictionary.has_key(key):  # Deprecated

# ✅ Correct - Use startswith/endswith
if filename.endswith('.py'):
    pass

# ❌ Wrong
# if filename[-3:] == '.py':  # Less readable

# COMPLETE PEP 8 EXAMPLE
print("\n" + "=" * 80)
print("COMPLETE PEP 8 COMPLIANT CODE EXAMPLE")
print("=" * 80)

"""
Module docstring explaining what this module does.

This module demonstrates PEP 8 compliant Python code.
"""

import sys
from typing import List, Optional

# Constants
MAX_RETRY_COUNT = 3
DEFAULT_TIMEOUT = 30


class DataProcessor:
    """
    Process data according to specified rules.

    This class demonstrates PEP 8 naming and structure conventions.
    """

    def __init__(self, name: str, max_items: int = 100):
        """
        Initialize the DataProcessor.

        Args:
            name: The name of the processor
            max_items: Maximum number of items to process
        """
        self.name = name
        self.max_items = max_items
        self._processed_count = 0  # Private attribute

    def process_items(self, items: List[str]) -> List[str]:
        """
        Process a list of items.

        Args:
            items: List of items to process

        Returns:
            List of processed items

        Raises:
            ValueError: If items list is empty
        """
        if not items:
            raise ValueError("Items list cannot be empty")

        processed = []
        for item in items:
            if self._is_valid_item(item):
                processed.append(self._transform_item(item))
                self._processed_count += 1

        return processed

    def _is_valid_item(self, item: str) -> bool:
        """Check if item is valid (private method)."""
        return len(item) > 0

    def _transform_item(self, item: str) -> str:
        """Transform item (private method)."""
        return item.upper()


def main():
    """Main entry point of the program."""
    processor = DataProcessor("MyProcessor")
    items = ["apple", "banana", "cherry"]

    try:
        result = processor.process_items(items)
        print(f"Processed {len(result)} items")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

# TOOLS TO CHECK PEP 8 COMPLIANCE
print("\n" + "=" * 80)
print("TOOLS TO ENFORCE PEP 8")
print("=" * 80)

pep8_tools = """
1. pylint
   - Comprehensive code quality checker
   - Command: pylint myfile.py
   - Configurable with .pylintrc

2. flake8
   - Wrapper around pycodestyle, pyflakes, mccabe
   - Command: flake8 myfile.py
   - Faster than pylint

3. black
   - Opinionated code formatter
   - Command: black myfile.py
   - Auto-formats to PEP 8

4. autopep8
   - Automatically fixes PEP 8 violations
   - Command: autopep8 --in-place myfile.py

5. pycodestyle (formerly pep8)
   - Official PEP 8 checker
   - Command: pycodestyle myfile.py

6. IDEs with built-in checking
   - PyCharm (auto PEP 8 checking)
   - VS Code (with Python extension)
   - Sublime Text (with plugins)

Usage example:
$ pip install flake8 black
$ flake8 myfile.py  # Check for violations
$ black myfile.py   # Auto-format
"""

print(pep8_tools)

# PEP 8 EXCEPTIONS
print("\n" + "=" * 80)
print("WHEN TO IGNORE PEP 8")
print("=" * 80)

exceptions = """
It's okay to break PEP 8 when:

1. Following the guideline would make code less readable
2. To be consistent with surrounding code (that breaks PEP 8)
3. Code predates the guideline
4. Backward compatibility requires it
5. IDE-generated code doesn't follow it

Example:
# Okay to exceed 79 characters for URLs
VERY_LONG_URL = "https://example.com/very/long/path/that/should/not/be/broken"

Remember: "A Foolish Consistency is the Hobgoblin of Little Minds" - PEP 8
"""

print(exceptions)

# INTERVIEW TIP
print("\n" + "=" * 80)
print("INTERVIEW TIP")
print("=" * 80)

tip = """
When asked about PEP 8:

1. Define it: "PEP 8 is the official style guide for Python code"

2. Mention key points:
   - 4 spaces for indentation
   - 79 character line limit
   - Naming conventions (snake_case, PascalCase, UPPER_CASE)
   - Import organization

3. Explain why it matters:
   - Readability and maintainability
   - Team collaboration
   - Professional code quality

4. Show you use it:
   - "I use flake8/black in my projects"
   - "My IDE checks PEP 8 automatically"
   - "We enforce it in CI/CD pipeline"

5. Know when to break it:
   - "Readability over rigid rules"
   - "Consistency with existing code"
"""

print(tip)
```

---

#### Q3: Explain Python's execution model (interpreted vs compiled).

**Complete Solution:**

```python
"""
PYTHON EXECUTION MODEL
======================
How Python code gets executed
"""

print("=" * 80)
print("PYTHON EXECUTION MODEL - INTERPRETED VS COMPILED")
print("=" * 80)

# TRADITIONAL COMPILATION (C/C++)
print("\n📌 TRADITIONAL COMPILED LANGUAGE (C/C++):")
compilation_model = """
Source Code (.c) 
    ↓ 
Compiler (gcc)
    ↓
Machine Code (.exe, binary)
    ↓
CPU Execution

Characteristics:
✓ Compiled once to machine code
✓ Direct CPU execution
✓ Very fast execution
✓ Platform-specific binary
✗ Need to recompile for changes
✗ Different binary for each OS
"""
print(compilation_model)

# PYTHON EXECUTION MODEL
print("\n📌 PYTHON EXECUTION MODEL (Hybrid):")
python_model = """
Source Code (.py)
    ↓
Python Interpreter
    ↓
Bytecode (.pyc) - Platform Independent
    ↓
Python Virtual Machine (PVM)
    ↓
Machine Code Execution

Characteristics:
✓ No explicit compilation step
✓ Platform independent (.pyc works on any OS with Python)
✓ Faster development (no compile wait time)
✓ Dynamic features possible
✗ Slower than compiled languages
✗ Needs Python installed to run
"""
print(python_model)

# DETAILED EXECUTION FLOW
print("\n" + "=" * 80)
print("DETAILED PYTHON EXECUTION FLOW")
print("=" * 80)

execution_steps = """
STEP 1: Source Code
-------------------
# example.py
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))


STEP 2: Lexical Analysis (Tokenization)
----------------------------------------
Interpreter breaks code into tokens:
- Keywords: def, return, print
- Identifiers: greet, name
- Operators: =
- Literals: "Hello", "World"
- Delimiters: (), :


STEP 3: Parsing
---------------
Tokens → Abstract Syntax Tree (AST)
Check syntax errors at this stage


STEP 4: Compilation to Bytecode
--------------------------------
AST → Bytecode (low-level, platform-independent instructions)

Bytecode is stored in .pyc files in __pycache__ directory:
__pycache__/
    example.cpython-311.pyc  # Python 3.11 bytecode


STEP 5: Execution by PVM
-------------------------
Python Virtual Machine interprets bytecode:
- Loads bytecode instructions
- Executes them one by one
- Manages memory
- Calls system resources


STEP 6: Output
--------------
Hello, World!
"""
print(execution_steps)

# DEMONSTRATE BYTECODE
print("\n" + "=" * 80)
print("VIEWING PYTHON BYTECODE")
print("=" * 80)

import dis

def simple_function(a, b):
    """Simple function to demonstrate bytecode"""
    c = a + b
    return c

print("\nPython Source Code:")
print("""
def simple_function(a, b):
    c = a + b
    return c
""")

print("\nGenerated Bytecode:")
dis.dis(simple_function)

# INTERPRETED VS COMPILED COMPARISON
print("\n" + "=" * 80)
print("INTERPRETED VS COMPILED - DETAILED COMPARISON")
print("=" * 80)

comparison_table = """
┌────────────────────┬──────────────────────┬──────────────────────┐
│ Feature            │ Compiled (C/C++)     │ Interpreted (Python) │
├────────────────────┼──────────────────────┼──────────────────────┤
│ Execution Speed    │ Very Fast (1x)       │ Slower (10-100x)     │
│ Compilation Time   │ Slow                 │ None (instant run)   │
│ Development Speed  │ Slower               │ Faster               │
│ Error Detection    │ Compile-time         │ Runtime              │
│ Portability        │ Recompile per OS     │ Same code all OS     │
│ Distribution       │ Binary file          │ Source + Interpreter │
│ Debugging          │ Harder               │ Easier               │
│ Memory Usage       │ Lower                │ Higher               │
│ Dynamic Features   │ Limited              │ Extensive            │
│ Code Protection    │ Better (binary)      │ Weaker (source)      │
└────────────────────┴──────────────────────┴──────────────────────┘
"""
print(comparison_table)

# PYTHON IS BOTH!
print("\n" + "=" * 80)
print("PYTHON IS BOTH COMPILED AND INTERPRETED!")
print("=" * 80)

hybrid_explanation = """
Common Misconception: "Python is purely interpreted" ❌

Reality: Python is a HYBRID ✅

1. COMPILATION PHASE:
   .py → .pyc (bytecode compilation)
   - Happens automatically
   - Cached in __pycache__
   - Skipped if .pyc is up-to-date

2. INTERPRETATION PHASE:
   .pyc → Execution by PVM
   - Line-by-line execution
   - Runtime type checking
   - Dynamic features

So Python is:
• Compiled: Source → Bytecode
• Interpreted: Bytecode → Machine code (by PVM)

This is why Python is often called:
"Compiled to bytecode, interpreted by VM"
"""
print(hybrid_explanation)

# PRACTICAL DEMONSTRATION
print("\n" + "=" * 80)
print("PRACTICAL DEMONSTRATION")
print("=" * 80)

# Create a simple Python file
with open('demo_execution.py', 'w') as f:
    f.write("""
# demo_execution.py
def add(a, b):
    return a + b

result = add(5, 3)
print(f"Result: {result}")
""")

print("\n1. Created demo_execution.py")
print("2. First run: Python compiles to bytecode")
print("3. Check __pycache__/ for .pyc file")
print("4. Second run: Uses cached bytecode (faster)")

import demo_execution  # This will create .pyc

print("\n✓ Bytecode created in __pycache__/")

# Clean up
import os
os.remove('demo_execution.py')

# CPYTHON VS OTHER IMPLEMENTATIONS
print("\n" + "=" * 80)
print("PYTHON IMPLEMENTATIONS")
print("=" * 80)

implementations = """
1. CPython (Standard Python)
   - Reference implementation
   - Written in C
   - Compiles to bytecode → Interpreted by PVM
   - Has GIL (Global Interpreter Lock)
   - Most widely used

2. PyPy
   - Just-In-Time (JIT) compiler
   - Compiles bytecode to machine code at runtime
   - 4-7x faster than CPython for long-running programs
   - Good for: CPU-intensive tasks
   - Same Python language, different execution

3. Jython
   - Python implemented in Java
   - Compiles to Java bytecode
   - Runs on JVM (Java Virtual Machine)
   - Good for: Java integration

4. IronPython
   - Python for .NET framework
   - Compiles to .NET bytecode
   - Runs on CLR (Common Language Runtime)
   - Good for: .NET integration

5. Cython
   - Python with C data types
   - Compiles to C code
   - Can be compiled to native machine code
   - Good for: Performance-critical code
"""
print(implementations)

# EXECUTION SPEED COMPARISON
print("\n" + "=" * 80)
print("EXECUTION SPEED COMPARISON")
print("=" * 80)

import time

def fibonacci_python(n):
    if n <= 1:
        return n
    return fibonacci_python(n-1) + fibonacci_python(n-2)

# Time Python execution
start = time.time()
result = fibonacci_python(30)
python_time = time.time() - start

print(f"\nPython Fibonacci(30): {python_time:.4f} seconds")
print(f"Result: {result}")

print("""
Comparison with other languages (Fibonacci 30):
- C/C++:     ~0.001 seconds (1x - baseline)
- Python:    ~0.5 seconds (500x slower)
- JavaScript: ~0.01 seconds (10x slower)

Why is Python slower?
1. Interpreted execution (no direct machine code)
2. Dynamic typing (runtime type checks)
3. Everything is an object (overhead)
4. GIL prevents true parallelism
""")

# OPTIMIZATION TECHNIQUES
print("\n" + "=" * 80)
print("HOW TO MAKE PYTHON FASTER")
print("=" * 80)

optimizations = """
1. Use PyPy
   - JIT compilation
   - Drop-in replacement for CPython
   - 4-7x faster for long-running programs

2. Use Cython
   - Add type declarations
   - Compile to C
   - Can be 100x faster for numerical code

3. Use NumPy/Pandas
   - C/Fortran backend
   - Vectorized operations
   - 10-100x faster than pure Python

4. Use built-in functions
   - Implemented in C
   - Faster than Python equivalents
   Example: sum() vs manual loop

5. Use multiprocessing
   - Bypass GIL
   - True parallelism
   - Good for CPU-bound tasks

6. Profile and optimize
   - Use cProfile to find bottlenecks
   - Optimize only what matters
"""
print(optimizations)

# INTERVIEW ANSWER TEMPLATE
print("\n" + "=" * 80)
print("INTERVIEW ANSWER TEMPLATE")
print("=" * 80)

interview_answer = """
Q: Is Python interpreted or compiled?

A: "Python is a hybrid between compiled and interpreted:

1. COMPILATION: Python source code (.py) is first compiled to 
   bytecode (.pyc files in __pycache__). This happens automatically.

2. INTERPRETATION: The Python Virtual Machine (PVM) then interprets 
   this bytecode line by line.

So technically, Python is 'compiled to bytecode, then interpreted'.

This differs from:
• Purely compiled languages (C/C++): Source → Machine code directly
• Purely interpreted languages (old JavaScript): Source → Execution directly

The hybrid model gives Python:
✓ Platform independence (bytecode runs on any OS)
✓ Fast development (no explicit compilation step)
✗ Slower execution than fully compiled languages

For production, we can use PyPy (JIT compiler) or Cython (compile to C) 
to improve performance while keeping Python's ease of use."

This shows you understand:
- The execution model
- Trade-offs
- Real-world solutions
"""
print(interview_answer)
```

---

#### Q4: What are Python's built-in data types?

**Complete Solution:**

```python
"""
PYTHON BUILT-IN DATA TYPES
===========================
Complete guide with examples and use cases
"""

print("=" * 80)
print("PYTHON BUILT-IN DATA TYPES - COMPREHENSIVE GUIDE")
print("=" * 80)

# OVERVIEW OF ALL DATA TYPES
data_types_overview = """
Python Data Types Categories:

1. NUMERIC TYPES
   - int (integer)
   - float (floating point)
   - complex (complex numbers)

2. SEQUENCE TYPES
   - list (mutable sequence)
   - tuple (immutable sequence)
   - range (immutable sequence of numbers)

3. TEXT TYPE
   - str (string)

4. MAPPING TYPE
   - dict (dictionary)

5. SET TYPES
   - set (mutable unordered collection)
   - frozenset (immutable unordered collection)

6. BOOLEAN TYPE
   - bool (True/False)

7. BINARY TYPES
   - bytes (immutable)
   - bytearray (mutable)
   - memoryview (memory view object)

8. NONE TYPE
   - NoneType (represents absence of value)
"""
print(data_types_overview)

# 1. NUMERIC TYPES
print("\n" + "=" * 80)
print("1. NUMERIC TYPES")
print("=" * 80)

# Integer
print("\n📌 INT - Integer Numbers")
int_examples = """
Arbitrary precision (no overflow)
"""
print(int_examples)

x = 42
y = -17
z = 0
huge_number = 123456789012345678901234567890  # No limit!

print(f"Positive: {x}, type: {type(x)}")
print(f"Negative: {y}")
print(f"Zero: {z}")
print(f"Huge number: {huge_number}")

# Different number systems
binary = 0b1010  # Binary (base 2)
octal = 0o12     # Octal (base 8)
hexadecimal = 0xA  # Hexadecimal (base 16)

print(f"\nBinary 0b1010 = {binary}")
print(f"Octal 0o12 = {octal}")
print(f"Hexadecimal 0xA = {hexadecimal}")

# Integer operations
print(f"\nDivision: 10 / 3 = {10 / 3}")  # Float result
print(f"Floor division: 10 // 3 = {10 // 3}")  # Integer result
print(f"Modulo: 10 % 3 = {10 % 3}")
print(f"Power: 2 ** 10 = {2 ** 10}")

# Float
print("\n📌 FLOAT - Floating Point Numbers")
float_examples = """
Double precision (64-bit)
Limited precision (~15-17 decimal places)
"""
print(float_examples)

pi = 3.14159
negative_float = -2.5
scientific = 1.5e3  # 1.5 × 10³ = 1500.0
small = 2.5e-4      # 2.5 × 10⁻⁴ = 0.00025

print(f"Pi: {pi}, type: {type(pi)}")
print(f"Scientific notation 1.5e3 = {scientific}")
print(f"Small number 2.5e-4 = {small}")

# Float precision issues
print(f"\nPrecision issue: 0.1 + 0.2 = {0.1 + 0.2}")  # Not exactly 0.3!
print(f"Reason: Binary floating point limitation")

# Solution: Use decimal for precision
from decimal import Decimal
precise = Decimal('0.1') + Decimal('0.2')
print(f"Using Decimal: {precise}")  # Exactly 0.3

# Complex
print("\n📌 COMPLEX - Complex Numbers")
complex_examples = """
Form: a + bj (where j = √-1)
Used in scientific computing
"""
print(complex_examples)

c1 = 3 + 4j
c2 = complex(2, -5)  # 2 - 5j

print(f"Complex number: {c1}, type: {type(c1)}")
print(f"Real part: {c1.real}")
print(f"Imaginary part: {c1.imag}")
print(f"Addition: {c1} + {c2} = {c1 + c2}")
print(f"Multiplication: {c1} * {c2} = {c1 * c2}")

# 2. SEQUENCE TYPES
print("\n" + "=" * 80)
print("2. SEQUENCE TYPES")
print("=" * 80)

# List
print("\n📌 LIST - Mutable Ordered Sequence")
list_features = """
✓ Ordered (maintains insertion order)
✓ Mutable (can change after creation)
✓ Allows duplicates
✓ Can contain mixed types
✓ Dynamic size
"""
print(list_features)

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"Empty list: {empty_list}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"Nested: {nested}")

# List operations
fruits = ['apple', 'banana', 'cherry']
print(f"\nOriginal: {fruits}")

fruits.append('date')  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, 'blueberry')  # Insert at position
print(f"After insert: {fruits}")

fruits.remove('banana')  # Remove by value
print(f"After remove: {fruits}")

popped = fruits.pop()  # Remove and return last
print(f"Popped: {popped}, List: {fruits}")

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Tuple
print("\n📌 TUPLE - Immutable Ordered Sequence")
tuple_features = """
✓ Ordered
✗ Immutable (cannot change after creation)
✓ Allows duplicates
✓ Faster than lists
✓ Can be used as dict keys
"""
print(tuple_features)

# Creating tuples
empty_tuple = ()
single_item = (42,)  # Comma required for single item!
coordinates = (10, 20)
mixed_tuple = (1, "two", 3.0, True)

print(f"Empty: {empty_tuple}")
print(f"Single item: {single_item}")
print(f"Coordinates: {coordinates}")
print(f"Mixed: {mixed_tuple}")

# Tuple unpacking
x, y = coordinates
print(f"\nUnpacked: x={x}, y={y}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Swapping
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Tuple immutability
try:
    coordinates[0] = 100  # This will fail!
except TypeError as e:
    print(f"\nCannot modify tuple: {e}")

# Range
print("\n📌 RANGE - Immutable Sequence of Numbers")
range_features = """
✓ Memory efficient (generates on demand)
✓ Commonly used in loops
✓ Immutable
"""
print(range_features)

r1 = range(5)           # 0, 1, 2, 3, 4
r2 = range(1, 6)        # 1, 2, 3, 4, 5
r3 = range(0, 10, 2)    # 0, 2, 4, 6, 8
r4 = range(10, 0, -2)   # 10, 8, 6, 4, 2

print(f"range(5): {list(r1)}")
print(f"range(1, 6): {list(r2)}")
print(f"range(0, 10, 2): {list(r3)}")
print(f"range(10, 0, -2): {list(r4)}")

# 3. TEXT TYPE
print("\n" + "=" * 80)
print("3. TEXT TYPE (STRING)")
print("=" * 80)

print("\n📌 STR - String (Immutable Sequence of Characters)")
string_features = """
✓ Immutable
✓ Unicode support
✓ Rich set of methods
"""
print(string_features)

# Creating strings
single_quote = 'Hello'
double_quote = "World"
triple_quote = """Multi-line
string"""
raw_string = r"C:\Users\name"  # Raw string (no escaping)

print(f"Single quote: {single_quote}")
print(f"Double quote: {double_quote}")
print(f"Triple quote: {triple_quote}")
print(f"Raw string: {raw_string}")

# String operations
text = "Python Programming"
print(f"\nOriginal: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Split: {text.split()}")
print(f"Starts with 'Python': {text.startswith('Python')}")
print(f"Length: {len(text)}")

# String indexing and slicing
print(f"\nFirst char: {text[0]}")
print(f"Last char: {text[-1]}")
print(f"First 6 chars: {text[:6]}")
print(f"Last 11 chars: {text[-11:]}")
print(f"Every 2nd char: {text[::2]}")
print(f"Reversed: {text[::-1]}")

# String formatting
name = "Alice"
age = 30
print(f"\nf-string: My name is {name} and I'm {age}")
print("format(): My name is {} and I'm {}".format(name, age))
print("%-formatting: My name is %s and I'm %d" % (name, age))

# 4. MAPPING TYPE
print("\n" + "=" * 80)
print("4. MAPPING TYPE (DICTIONARY)")
print("=" * 80)

print("\n📌 DICT - Key-Value Pairs")
dict_features = """
✓ Unordered (Python 3.7+ maintains insertion order)
✓ Mutable
✓ Keys must be immutable (str, int, tuple)
✓ No duplicate keys
✓ Fast lookup O(1)
"""
print(dict_features)

# Creating dictionaries
empty_dict = {}
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}
dict_constructor = dict(name='Bob', age=25)

print(f"Empty: {empty_dict}")
print(f"Person: {person}")
print(f"Constructor: {dict_constructor}")

# Dictionary operations
print(f"\nAccess: person['name'] = {person['name']}")
person['email'] = 'alice@example.com'  # Add new key
print(f"After adding email: {person}")

person['age'] = 31  # Update value
print(f"After updating age: {person}")

del person['city']  # Delete key
print(f"After deleting city: {person}")

# Dictionary methods
print(f"\nKeys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")
print(f"Get (safe): {person.get('phone', 'Not found')}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dict: {squares_dict}")

# 5. SET TYPES
print("\n" + "=" * 80)
print("5. SET TYPES")
print("=" * 80)

print("\n📌 SET - Unordered Collection of Unique Items")
set_features = """
✓ Unordered
✓ Mutable
✗ No duplicates (automatically removed)
✓ Fast membership testing O(1)
✓ Mathematical set operations
"""
print(set_features)

# Creating sets
empty_set = set()  # {} creates dict, not set!
numbers_set = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])  # Duplicates removed

print(f"Empty: {empty_set}")
print(f"Numbers: {numbers_set}")
print(f"From list [1,2,2,3,3,3]: {from_list}")

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"\nset1: {set1}")
print(f"set2: {set2}")
print(f"Union (|): {set1 | set2}")
print(f"Intersection (&): {set1 & set2}")
print(f"Difference (-): {set1 - set2}")
print(f"Symmetric difference (^): {set1 ^ set2}")

# Set methods
colors = {'red', 'green', 'blue'}
colors.add('yellow')
print(f"\nAfter add: {colors}")

colors.remove('green')  # Raises error if not found
print(f"After remove: {colors}")

colors.discard('purple')  # No error if not found
print(f"After discard (not found): {colors}")

# Frozenset
print("\n📌 FROZENSET - Immutable Set")
frozen = frozenset([1, 2, 3, 4])
print(f"Frozenset: {frozen}")
print(f"Can be used as dict key: {True}")

# 6. BOOLEAN TYPE
print("\n" + "=" * 80)
print("6. BOOLEAN TYPE")
print("=" * 80)

print("\n📌 BOOL - True or False")
bool_info = """
✓ Subclass of int (True=1, False=0)
✓ Result of comparisons
✓ Used in conditions
"""
print(bool_info)

is_active = True
is_deleted = False

print(f"True: {is_active}, type: {type(is_active)}")
print(f"False: {is_deleted}")
print(f"True as int: {int(True)}")
print(f"False as int: {int(False)}")
print(f"True + True = {True + True}")

# Truthy and Falsy values
print("\nFalsy values (evaluate to False):")
falsy = [None, False, 0, 0.0, 0j, '', [], {}, set(), range(0)]
for value in falsy:
    print(f"  bool({repr(value)}) = {bool(value)}")

print("\nTruthy values (evaluate to True):")
truthy = [True, 1, -1, 3.14, 'text', [1], {1: 2}, {1}]
for value in truthy:
    print(f"  bool({repr(value)}) = {bool(value)}")

# 7. BINARY TYPES
print("\n" + "=" * 80)
print("7. BINARY TYPES")
print("=" * 80)

print("\n📌 BYTES - Immutable Binary Data")
b1 = b'Hello'
b2 = bytes([65, 66, 67])  # ASCII values
b3 = 'Hello'.encode('utf-8')

print(f"Bytes literal: {b1}")
print(f"From list: {b2}")
print(f"Encoded: {b3}")
print(f"Decode: {b3.decode('utf-8')}")

print("\n📌 BYTEARRAY - Mutable Binary Data")
ba = bytearray(b'Hello')
print(f"Original: {ba}")
ba[0] = 74  # ASCII 'J'
print(f"Modified: {ba}")

print("\n📌 MEMORYVIEW - Memory View")
mv = memoryview(b'Hello')
print(f"Memoryview: {mv}")
print(f"First byte: {mv[0]}")

# 8. NONE TYPE
print("\n" + "=" * 80)
print("8. NONE TYPE")
print("=" * 80)

print("\n📌 NONETYPE - Absence of Value")
result = None
print(f"None: {result}, type: {type(result)}")

def no_return():
    pass

print(f"Function with no return: {no_return()}")

# Checking for None
if result is None:
    print("Use 'is None', not '== None'")

# TYPE CHECKING AND CONVERSION
print("\n" + "=" * 80)
print("TYPE CHECKING AND CONVERSION")
print("=" * 80)

x = 42
print(f"\nVariable: {x}")
print(f"type(): {type(x)}")
print(f"isinstance(x, int): {isinstance(x, int)}")
print(f"isinstance(x, (int, float)): {isinstance(x, (int, float))}")

# Type conversion
print("\nType Conversion:")
print(f"int('42') = {int('42')}")
print(f"float('3.14') = {float('3.14')}")
print(f"str(42) = {str(42)}")
print(f"list('hello') = {list('hello')}")
print(f"tuple([1,2,3]) = {tuple([1, 2, 3])}")
print(f"set([1,2,2,3]) = {set([1, 2, 2, 3])}")

# COMPARISON TABLE
print("\n" + "=" * 80)
print("DATA TYPES COMPARISON TABLE")
print("=" * 80)

comparison = """
┌─────────────┬──────────┬─────────┬────────────┬───────────┬─────────────┐
│ Type        │ Ordered  │ Mutable │ Duplicates │ Indexable │ Use Case    │
├─────────────┼──────────┼─────────┼────────────┼───────────┼─────────────┤
│ list        │ Yes      │ Yes     │ Yes        │ Yes       │ General     │
│ tuple       │ Yes      │ No      │ Yes        │ Yes       │ Fixed data  │
│ dict        │ Yes(3.7+)│ Yes     │ No (keys)  │ By key    │ Mapping     │
│ set         │ No       │ Yes     │ No         │ No        │ Unique      │
│ frozenset   │ No       │ No      │ No         │ No        │ Immut. set  │
│ str         │ Yes      │ No      │ Yes        │ Yes       │ Text        │
└─────────────┴──────────┴─────────┴────────────┴───────────┴─────────────┘
"""
print(comparison)

# MEMORY USAGE
print("\n" + "=" * 80)
print("MEMORY USAGE COMPARISON")
print("=" * 80)

import sys

data = list(range(1000))
print(f"\nList of 1000 items: {sys.getsizeof(data)} bytes")

data_tuple = tuple(range(1000))
print(f"Tuple of 1000 items: {sys.getsizeof(data_tuple)} bytes")

data_set = set(range(1000))
print(f"Set of 1000 items: {sys.getsizeof(data_set)} bytes")

print("\nTuples use less memory than lists!")

# INTERVIEW ANSWER TEMPLATE
print("\n" + "=" * 80)
print("INTERVIEW ANSWER TEMPLATE")
print("=" * 80)

interview_template = """
Q: What are Python's built-in data types?

A: "Python has several categories of built-in data types:

1. NUMERIC: int, float, complex
   - int: arbitrary precision integers
   - float: 64-bit floating point
   - complex: complex numbers (a+bj)

2. SEQUENCE: list, tuple, range
   - list: mutable ordered collection
   - tuple: immutable ordered collection
   - range: immutable sequence of numbers

3. TEXT: str
   - Immutable Unicode strings

4. MAPPING: dict
   - Key-value pairs, O(1) lookup

5. SET: set, frozenset
   - Unordered unique elements
   - frozenset is immutable

6. BOOLEAN: bool
   - True/False (subclass of int)

7. BINARY: bytes, bytearray, memoryview
   - For binary data manipulation

8. NONE: NoneType
   - Represents absence of value

Key differences:
- Mutable: list, dict, set, bytearray
- Immutable: int, float, str, tuple, frozenset, bytes
- Ordered: list, tuple, str, dict (3.7+)
- Unordered: set, frozenset

I typically use:
- Lists for collections that change
- Tuples for fixed data (coordinates, return multiple values)
- Dicts for key-value mapping
- Sets for unique elements and membership testing"
"""
print(interview_template)
```

---

#### Q5: Explain mutable vs immutable objects with examples.

**Complete Solution:**

```python
"""
MUTABLE VS IMMUTABLE OBJECTS IN PYTHON
======================================
Understanding object mutability and its implications
"""

print("=" * 80)
print("MUTABLE VS IMMUTABLE OBJECTS - COMPLETE GUIDE")
print("=" * 80)

# DEFINITIONS
print("\n📌 DEFINITIONS")
definitions = """
IMMUTABLE OBJECTS:
- Cannot be changed after creation
- Any modification creates a NEW object
- Original object remains unchanged
- Examples: int, float, str, tuple, frozenset, bytes

MUTABLE OBJECTS:
- Can be changed after creation
- Modifications happen IN-PLACE
- Same object, different content
- Examples: list, dict, set, bytearray
"""
print(definitions)

# IMMUTABLE EXAMPLES
print("\n" + "=" * 80)
print("IMMUTABLE OBJECTS - DETAILED EXAMPLES")
print("=" * 80)

# String (Immutable)
print("\n📌 STRING - Immutable")
s1 = "Hello"
print(f"Original string: {s1}, id: {id(s1)}")

s2 = s1  # s2 references same object
print(f"After s2 = s1: s2={s2}, id: {id(s2)}")
print(f"s1 is s2: {s1 is s2}")  # True - same object

s1 = s1 + " World"  # Creates NEW string!
print(f"\nAfter s1 += ' World':")
print(f"s1: {s1}, id: {id(s1)}")  # New id!
print(f"s2: {s2}, id: {id(s2)}")  # Old id!
print(f"s1 is s2: {s1 is s2}")  # False - different objects

# Integer (Immutable)
print("\n📌 INTEGER - Immutable")
x = 10
print(f"Original: x={x}, id: {id(x)}")

y = x
print(f"After y = x: y={y}, id: {id(y)}")
print(f"x is y: {x is y}")  # True

x = x + 5  # Creates NEW integer!
print(f"\nAfter x += 5:")
print(f"x: {x}, id: {id(x)}")  # New id!
print(f"y: {y}, id: {id(y)}")  # Old id!
print(f"x is y: {x is y}")  # False

# Tuple (Immutable)
print("\n📌 TUPLE - Immutable")
t1 = (1, 2, 3)
print(f"Original tuple: {t1}, id: {id(t1)}")

try:
    t1[0] = 100  # This will fail!
except TypeError as e:
    print(f"Cannot modify: {e}")

# But you can create a new tuple
t2 = t1 + (4, 5)  # Creates NEW tuple
print(f"New tuple t2: {t2}, id: {id(t2)}")
print(f"Original t1: {t1}, id: {id(t1)}")  # Unchanged

# MUTABLE EXAMPLES
print("\n" + "=" * 80)
print("MUTABLE OBJECTS - DETAILED EXAMPLES")
print("=" * 80)

# List (Mutable)
print("\n📌 LIST - Mutable")
list1 = [1, 2, 3]
print(f"Original list: {list1}, id: {id(list1)}")

list2 = list1  # list2 references SAME object
print(f"After list2 = list1: {list2}, id: {id(list2)}")
print(f"list1 is list2: {list1 is list2}")  # True

list1.append(4)  # Modifies IN-PLACE
print(f"\nAfter list1.append(4):")
print(f"list1: {list1}, id: {id(list1)}")  # Same id!
print(f"list2: {list2}, id: {id(list2)}")  # Same id!
print(f"list2 also changed! list1 is list2: {list1 is list2}")  # True

# How to create independent copy
list3 = list1.copy()  # or list1[:]
print(f"\nlist3 (copy): {list3}, id: {id(list3)}")  # Different id
list1.append(5)
print(f"After list1.append(5):")
print(f"list1: {list1}")
print(f"list3: {list3}")  # Unchanged!

# Dictionary (Mutable)
print("\n📌 DICTIONARY - Mutable")
dict1 = {'a': 1, 'b': 2}
print(f"Original dict: {dict1}, id: {id(dict1)}")

dict2 = dict1  # Same object
print(f"After dict2 = dict1, id: {id(dict2)}")

dict1['c'] = 3  # Modifies in-place
print(f"\nAfter dict1['c'] = 3:")
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")  # Also changed!

# Set (Mutable)
print("\n📌 SET - Mutable")
set1 = {1, 2, 3}
print(f"Original set: {set1}, id: {id(set1)}")

set2 = set1  # Same object
set1.add(4)  # Modifies in-place

print(f"After set1.add(4):")
print(f"set1: {set1}")
print(f"set2: {set2}")  # Also changed!

# THE DANGER: MUTABLE DEFAULT ARGUMENTS
print("\n" + "=" * 80)
print("⚠️  COMMON PITFALL: MUTABLE DEFAULT ARGUMENTS")
print("=" * 80)

# WRONG WAY ❌
def wrong_add_item(item, items=[]):  # Dangerous!
    items.append(item)
    return items

print("\n❌ WRONG: Mutable default argument")
print(f"Call 1: {wrong_add_item('apple')}")
print(f"Call 2: {wrong_add_item('banana')}")  # Reuses same list!
print(f"Call 3: {wrong_add_item('cherry')}")  # Problem!

# RIGHT WAY ✅
def correct_add_item(item, items=None):
    if items is None:
        items = []  # Create new list each time
    items.append(item)
    return items

print("\n✅ CORRECT: Use None as default")
print(f"Call 1: {correct_add_item('apple')}")
print(f"Call 2: {correct_add_item('banana')}")  # New list
print(f"Call 3: {correct_add_item('cherry')}")  # New list

# FUNCTION PARAMETERS
print("\n" + "=" * 80)
print("FUNCTION PARAMETERS: PASS BY REFERENCE")
print("=" * 80)

# Immutable parameter
def modify_immutable(x):
    print(f"  Inside function before: {x}, id: {id(x)}")
    x = x + 10  # Creates new object
    print(f"  Inside function after: {x}, id: {id(x)}")
    return x

print("\n📌 Passing Immutable (int):")
num = 5
print(f"Before call: {num}, id: {id(num)}")
result = modify_immutable(num)
print(f"After call: {num}, id: {id(num)}")  # Unchanged!
print(f"Return value: {result}")

# Mutable parameter
def modify_mutable(lst):
    print(f"  Inside function before: {lst}, id: {id(lst)}")
    lst.append(4)  # Modifies original!
    print(f"  Inside function after: {lst}, id: {id(lst)}")

print("\n📌 Passing Mutable (list):")
my_list = [1, 2, 3]
print(f"Before call: {my_list}, id: {id(my_list)}")
modify_mutable(my_list)
print(f"After call: {my_list}, id: {id(my_list)}")  # Changed!

# TUPLE WITH MUTABLE ELEMENTS
print("\n" + "=" * 80)
print("⚠️  GOTCHA: TUPLE WITH MUTABLE ELEMENTS")
print("=" * 80)

t = ([1, 2], [3, 4])  # Tuple containing lists
print(f"Tuple: {t}, id: {id(t)}")

# Cannot reassign tuple elements
try:
    t[0] = [5, 6]
except TypeError as e:
    print(f"Cannot reassign: {e}")

# But CAN modify the mutable elements!
t[0].append(3)  # This works!
print(f"After t[0].append(3): {t}")  # Tuple unchanged, but list inside changed!

# SHALLOW VS DEEP COPY
print("\n" + "=" * 80)
print("SHALLOW VS DEEP COPY")
print("=" * 80)

import copy

# Original nested list
original = [[1, 2], [3, 4]]
print(f"Original: {original}")

# Shallow copy
shallow = original.copy()  # or list(original) or original[:]
print(f"\nShallow copy: {shallow}")
print(f"Different objects: {original is shallow}")  # False

# Modify nested list
original[0].append(999)
print(f"\nAfter original[0].append(999):")
print(f"Original: {original}")
print(f"Shallow: {shallow}")  # Also changed! (nested list is same object)

# Deep copy
original2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(original2)

original2[0].append(999)
print(f"\nAfter original2[0].append(999):")
print(f"Original2: {original2}")
print(f"Deep: {deep}")  # Unchanged! (completely independent)

# PERFORMANCE IMPLICATIONS
print("\n" + "=" * 80)
print("PERFORMANCE IMPLICATIONS")
print("=" * 80)

import timeit

# String concatenation (immutable - creates many objects)
def string_concat():
    s = ""
    for i in range(1000):
        s = s + str(i)  # Creates new string each time!
    return s

# List concatenation (mutable - modifies in-place)
def list_concat():
    lst = []
    for i in range(1000):
        lst.append(str(i))  # In-place modification
    return ''.join(lst)

time_string = timeit.timeit(string_concat, number=100)
time_list = timeit.timeit(list_concat, number=100)

print(f"\nString concatenation: {time_string:.4f} seconds")
print(f"List concatenation: {time_list:.4f} seconds")
print(f"List is {time_string/time_list:.2f}x faster!")

# IMMUTABILITY FOR THREAD SAFETY
print("\n" + "=" * 80)
print("IMMUTABILITY FOR THREAD SAFETY")
print("=" * 80)

thread_safety = """
Immutable objects are inherently thread-safe:

✅ Immutable (thread-safe):
- Multiple threads can read simultaneously
- No race conditions
- No need for locks

❌ Mutable (needs protection):
- Concurrent modifications can corrupt data
- Need locks/synchronization
- Performance overhead

Example: Using tuple instead of list in multi-threaded code
ensures data integrity without locks.
"""
print(thread_safety)

# HASHABILITY
print("\n" + "=" * 80)
print("HASHABILITY (Dict Keys and Set Elements)")
print("=" * 80)

print("\n📌 Only IMMUTABLE objects can be hashed:")

# Valid dict keys (immutable)
valid_keys = {
    42: "int key",
    3.14: "float key",
    "name": "string key",
    (1, 2): "tuple key",
    frozenset([1, 2]): "frozenset key"
}
print(f"\nValid dict with immutable keys: {valid_keys}")

# Invalid dict keys (mutable)
try:
    invalid = {[1, 2]: "list key"}  # Error!
except TypeError as e:
    print(f"\n❌ Cannot use list as key: {e}")

try:
    invalid = {{1, 2}: "set key"}  # Error!
except TypeError as e:
    print(f"❌ Cannot use set as key: {e}")

# COMPARISON TABLE
print("\n" + "=" * 80)
print("MUTABLE VS IMMUTABLE - COMPARISON TABLE")
print("=" * 80)

comparison = """
┌──────────────┬────────────┬──────────────────────────────────────┐
│ Data Type    │ Mutability │ Key Characteristics                  │
├──────────────┼────────────┼──────────────────────────────────────┤
│ int          │ Immutable  │ Arbitrary precision                  │
│ float        │ Immutable  │ 64-bit floating point                │
│ complex      │ Immutable  │ Complex numbers                      │
│ str          │ Immutable  │ Unicode text, hashable               │
│ tuple        │ Immutable  │ Ordered, hashable, can be dict key   │
│ frozenset    │ Immutable  │ Unordered, hashable, set operations  │
│ bytes        │ Immutable  │ Binary data, hashable                │
├──────────────┼────────────┼──────────────────────────────────────┤
│ list         │ Mutable    │ Ordered, dynamic, in-place mods      │
│ dict         │ Mutable    │ Key-value, O(1) lookup               │
│ set          │ Mutable    │ Unordered, unique elements           │
│ bytearray    │ Mutable    │ Mutable binary data                  │
└──────────────┴────────────┴──────────────────────────────────────┘

MEMORY IMPACT:
- Immutable: More memory (creates new objects)
- Mutable: Less memory (in-place modification)

THREAD SAFETY:
- Immutable: Thread-safe by default
- Mutable: Needs synchronization

HASHABILITY:
- Immutable: Can be dict keys/set elements
- Mutable: Cannot be hashed
"""
print(comparison)

# PRACTICAL EXAMPLES
print("\n" + "=" * 80)
print("PRACTICAL EXAMPLES")
print("=" * 80)

# Example 1: Avoiding unintended modifications
print("\n📌 Example 1: Protecting data")

def process_data(data):
    """Process data without modifying original"""
    data_copy = data.copy()  # Create copy for mutable objects
    data_copy.append(999)
    return data_copy

original_data = [1, 2, 3]
processed = process_data(original_data)
print(f"Original: {original_data}")  # Unchanged
print(f"Processed: {processed}")

# Example 2: Using tuples for fixed data
print("\n📌 Example 2: Tuples for coordinates")

def calculate_distance(point1, point2):
    """Tuples ensure coordinates don't change accidentally"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

p1 = (0, 0)
p2 = (3, 4)
print(f"Distance from {p1} to {p2}: {calculate_distance(p1, p2)}")

# Example 3: Immutable configuration
print("\n📌 Example 3: Immutable configuration")

from collections import namedtuple

Config = namedtuple('Config', ['host', 'port', 'debug'])
config = Config('localhost', 8080, True)

print(f"Config: {config}")
print(f"Access: config.host = {config.host}")

# Cannot modify
try:
    config.port = 9000
except AttributeError as e:
    print(f"Cannot modify: {e}")

# INTERVIEW ANSWER TEMPLATE
print("\n" + "=" * 80)
print("INTERVIEW ANSWER TEMPLATE")
print("=" * 80)

interview_answer = """
Q: Explain mutable vs immutable objects with examples.

A: "In Python, objects are either mutable or immutable based on whether
they can be changed after creation.

IMMUTABLE OBJECTS:
- Cannot be modified after creation
- Any 'modification' creates a NEW object
- Examples: int, float, str, tuple, frozenset
- Benefits: Thread-safe, hashable (can be dict keys)
- Drawback: More memory for modifications

Example:
s = 'hello'
s = s + ' world'  # Creates NEW string, doesn't modify original

MUTABLE OBJECTS:
- Can be modified in-place after creation
- Same object, different content
- Examples: list, dict, set, bytearray
- Benefits: Memory efficient for modifications
- Drawback: Not thread-safe, cannot be dict keys

Example:
lst = [1, 2, 3]
lst.append(4)  # Modifies IN-PLACE, same object

KEY IMPLICATIONS:

1. Function parameters:
   - Mutable objects passed by reference
   - Modifications inside function affect original

2. Default arguments:
   - Never use mutable objects as defaults
   - Use None and create inside function

3. Hashability:
   - Only immutable objects can be dict keys
   - Only immutable objects in sets

In practice, I use:
- Tuples for fixed data (coordinates, config)
- Lists for collections that change
- Immutable objects when thread safety matters
- .copy() or deepcopy() to avoid unintended modifications"
"""
print(interview_answer)
```

---

#### Q6: What are Python operators? Explain with examples.

**Complete Solution:**

```python
"""
PYTHON OPERATORS - COMPREHENSIVE GUIDE
=======================================
All operator types with examples and use cases
"""

print("=" * 80)
print("PYTHON OPERATORS - COMPLETE GUIDE")
print("=" * 80)

# OPERATOR CATEGORIES
categories = """
Python has 7 types of operators:

1. ARITHMETIC OPERATORS
2. COMPARISON (RELATIONAL) OPERATORS
3. LOGICAL OPERATORS
4. BITWISE OPERATORS
5. ASSIGNMENT OPERATORS
6. IDENTITY OPERATORS
7. MEMBERSHIP OPERATORS
"""
print(categories)

# 1. ARITHMETIC OPERATORS
print("\n" + "=" * 80)
print("1. ARITHMETIC OPERATORS")
print("=" * 80)

a, b = 17, 5

print(f"\na = {a}, b = {b}\n")
print(f"Addition (+):        {a} + {b} = {a + b}")
print(f"Subtraction (-):     {a} - {b} = {a - b}")
print(f"Multiplication (*):  {a} * {b} = {a * b}")
print(f"Division (/):        {a} / {b} = {a / b}")  # Float result
print(f"Floor Division (//): {a} // {b} = {a // b}")  # Integer result
print(f"Modulo (%):          {a} % {b} = {a % b}")  # Remainder
print(f"Exponentiation (**): {a} ** {b} = {a ** b}")  # Power

# Special cases
print(f"\n📌 Division Edge Cases:")
print(f"10 / 3 = {10 / 3}")  # 3.333...
print(f"10 // 3 = {10 // 3}")  # 3 (floor)
print(f"10 % 3 = {10 % 3}")  # 1 (remainder)
print(f"-10 // 3 = {-10 // 3}")  # -4 (floor toward negative infinity)
print(f"-10 % 3 = {-10 % 3}")  # 2

# 2. COMPARISON OPERATORS
print("\n" + "=" * 80)
print("2. COMPARISON (RELATIONAL) OPERATORS")
print("=" * 80)

x, y = 10, 20

print(f"\nx = {x}, y = {y}\n")
print(f"Equal (==):              {x} == {y} → {x == y}")
print(f"Not Equal (!=):          {x} != {y} → {x != y}")
print(f"Greater Than (>):        {x} > {y} → {x > y}")
print(f"Less Than (<):           {x} < {y} → {x < y}")
print(f"Greater or Equal (>=):   {x} >= {y} → {x >= y}")
print(f"Less or Equal (<=):      {x} <= {y} → {x <= y}")

# Chained comparisons (Python special feature!)
print(f"\n📌 Chained Comparisons:")
n = 15
print(f"10 < n < 20: {10 < n < 20}")  # True
print(f"10 < n < 15: {10 < n < 15}")  # False
print(f"1 < 2 < 3 < 4: {1 < 2 < 3 < 4}")  # True

# 3. LOGICAL OPERATORS
print("\n" + "=" * 80)
print("3. LOGICAL OPERATORS")
print("=" * 80)

p, q = True, False

print(f"\np = {p}, q = {q}\n")
print(f"AND:  p and q → {p and q}")
print(f"OR:   p or q  → {p or q}")
print(f"NOT:  not p   → {not p}")

# Truth table
print("\n📌 Complete Truth Table:")
print("┌───────┬───────┬─────────┬────────┬───────┐")
print("│   p   │   q   │ p and q │ p or q │ not p │")
print("├───────┼───────┼─────────┼────────┼───────┤")
for p in [True, False]:
    for q in [True, False]:
        print(f"│ {str(p):5} │ {str(q):5} │ {str(p and q):7} │ {str(p or q):6} │ {str(not p):5} │")
print("└───────┴───────┴─────────┴────────┴───────┘")

# Short-circuit evaluation
print("\n📌 Short-Circuit Evaluation:")
print("and: Returns first falsy value or last value")
print(f"5 and 10 = {5 and 10}")  # 10
print(f"0 and 10 = {0 and 10}")  # 0 (stops at first falsy)
print(f"None and 10 = {None and 10}")  # None

print("\nor: Returns first truthy value or last value")
print(f"5 or 10 = {5 or 10}")  # 5 (stops at first truthy)
print(f"0 or 10 = {0 or 10}")  # 10
print(f"0 or None = {0 or None}")  # None

# Practical use
def get_name(user):
    return user.get('name') or 'Anonymous'  # Default if no name

print(f"\nDefault value: {get_name({})}")  # Anonymous
print(f"With value: {get_name({'name': 'Alice'})}")  # Alice

# 4. BITWISE OPERATORS
print("\n" + "=" * 80)
print("4. BITWISE OPERATORS")
print("=" * 80)

a, b = 60, 13  # Binary: 60 = 0011 1100, 13 = 0000 1101

print(f"\na = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})\n")

print(f"AND (&):  {a} & {b} = {a & b} (binary: {bin(a & b)})")
print(f"OR (|):   {a} | {b} = {a | b} (binary: {bin(a | b)})")
print(f"XOR (^):  {a} ^ {b} = {a ^ b} (binary: {bin(a ^ b)})")
print(f"NOT (~):  ~{a} = {~a} (binary: {bin(~a & 0xFF)})")  # 2's complement
print(f"Left Shift (<<):  {a} << 2 = {a << 2} (binary: {bin(a << 2)})")
print(f"Right Shift (>>): {a} >> 2 = {a >> 2} (binary: {bin(a >> 2)})")

# Practical uses
print("\n📌 Practical Bitwise Applications:")

# Check if number is even/odd
num = 17
print(f"\n{num} is {'odd' if num & 1 else 'even'}")

# Swap without temp variable
x, y = 5, 10
print(f"\nBefore swap: x={x}, y={y}")
x = x ^ y
y = x ^ y
x = x ^ y
print(f"After XOR swap: x={x}, y={y}")

# Check if power of 2
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

print(f"\n16 is power of 2: {is_power_of_2(16)}")
print(f"17 is power of 2: {is_power_of_2(17)}")

# Set, clear, toggle bits
print("\n📌 Bit Manipulation:")
flags = 0b0000

# Set bit at position 2
flags |= (1 << 2)
print(f"After setting bit 2: {bin(flags)}")

# Clear bit at position 2
flags &= ~(1 << 2)
print(f"After clearing bit 2: {bin(flags)}")

# Toggle bit at position 3
flags ^= (1 << 3)
print(f"After toggling bit 3: {bin(flags)}")

# 5. ASSIGNMENT OPERATORS
print("\n" + "=" * 80)
print("5. ASSIGNMENT OPERATORS")
print("=" * 80)

print("\n📌 Basic Assignment:")
x = 10
print(f"x = 10 → {x}")

print("\n📌 Compound Assignment Operators:")
x = 10
print(f"Start: x = {x}")

x += 5  # x = x + 5
print(f"x += 5 → x = {x}")

x -= 3  # x = x - 3
print(f"x -= 3 → x = {x}")

x *= 2  # x = x * 2
print(f"x *= 2 → x = {x}")

x /= 4  # x = x / 4
print(f"x /= 4 → x = {x}")

x = 10
x //= 3  # x = x // 3
print(f"x //= 3 → x = {x}")

x %= 2  # x = x % 2
print(f"x %= 2 → x = {x}")

x = 2
x **= 3  # x = x ** 3
print(f"x **= 3 → x = {x}")

# Bitwise assignment
x = 60
x &= 13  # x = x & 13
print(f"x &= 13 → x = {x}")

x = 60
x |= 13  # x = x | 13
print(f"x |= 13 → x = {x}")

x = 60
x ^= 13  # x = x ^ 13
print(f"x ^= 13 → x = {x}")

x = 60
x >>= 2  # x = x >> 2
print(f"x >>= 2 → x = {x}")

x = 60
x <<= 2  # x = x << 2
print(f"x <<= 2 → x = {x}")

# Walrus operator (Python 3.8+)
print("\n📌 Walrus Operator (:=) - Assignment Expression:")

# Without walrus
data = [1, 2, 3, 4, 5]
length = len(data)
if length > 3:
    print(f"List has {length} items")

# With walrus
if (length := len(data)) > 3:
    print(f"Using walrus: List has {length} items")

# Useful in while loops
numbers = [1, 2, 3, 4, 5]
index = 0
while (num := numbers[index] if index < len(numbers) else None) is not None:
    print(f"Processing: {num}")
    index += 1
    if index >= 3:  # Limit for demo
        break

# 6. IDENTITY OPERATORS
print("\n" + "=" * 80)
print("6. IDENTITY OPERATORS")
print("=" * 80)

print("\n📌 'is' and 'is not' - Check object identity (memory address)")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"\na = {a}, id: {id(a)}")
print(f"b = {b}, id: {id(b)}")
print(f"c = a, id: {id(c)}")

print(f"\na is b: {a is b}")  # False (different objects)
print(f"a == b: {a == b}")  # True (same values)
print(f"a is c: {a is c}")  # True (same object)

print("\n📌 Important: Use 'is' for None, True, False")
x = None
if x is None:  # ✅ Correct
    print("x is None (correct way)")

if x == None:  # ❌ Works but not recommended
    print("x == None (works but use 'is')")

# Integer caching (-5 to 256)
a = 256
b = 256
print(f"\na = 256, b = 256")
print(f"a is b: {a is b}")  # True (cached)

a = 257
b = 257
print(f"\na = 257, b = 257")
print(f"a is b: {a is b}")  # False (not cached, different objects)

# 7. MEMBERSHIP OPERATORS
print("\n" + "=" * 80)
print("7. MEMBERSHIP OPERATORS")
print("=" * 80)

print("\n📌 'in' and 'not in' - Check membership in sequence")

# List
fruits = ['apple', 'banana', 'cherry']
print(f"\nList: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# String
text = "Hello, World!"
print(f"\nString: '{text}'")
print(f"'World' in text: {'World' in text}")
print(f"'Python' in text: {'Python' in text}")

# Dictionary (checks keys)
person = {'name': 'Alice', 'age': 30}
print(f"\nDictionary: {person}")
print(f"'name' in person: {'name' in person}")
print(f"'email' in person: {'email' in person}")
print(f"'Alice' in person: {'Alice' in person}")  # False (checks keys, not values)
print(f"'Alice' in person.values(): {'Alice' in person.values()}")  # True

# Set (fastest membership test)
numbers_set = {1, 2, 3, 4, 5}
print(f"\nSet: {numbers_set}")
print(f"3 in numbers_set: {3 in numbers_set}")

# OPERATOR PRECEDENCE
print("\n" + "=" * 80)
print("OPERATOR PRECEDENCE (Highest to Lowest)")
print("=" * 80)

precedence = """
1.  ()                          Parentheses
2.  **                          Exponentiation
3.  +x, -x, ~x                  Unary plus, minus, bitwise NOT
4.  *, /, //, %                 Multiplication, Division, Floor div, Modulo
5.  +, -                        Addition, Subtraction
6.  <<, >>                      Bitwise shifts
7.  &                           Bitwise AND
8.  ^                           Bitwise XOR
9.  |                           Bitwise OR
10. ==, !=, >, <, >=, <=        Comparisons
    is, is not                  Identity
    in, not in                  Membership
11. not                         Logical NOT
12. and                         Logical AND
13. or                          Logical OR
"""
print(precedence)

# Examples
print("📌 Precedence Examples:")
result = 2 + 3 * 4
print(f"2 + 3 * 4 = {result} (not 20)")

result = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result}")

result = 2 ** 3 ** 2
print(f"2 ** 3 ** 2 = {result} (right associative: 2^(3^2) = 2^9)")

result = 10 > 5 and 20 < 30 or False
print(f"10 > 5 and 20 < 30 or False = {result}")

# PRACTICAL EXAMPLES
print("\n" + "=" * 80)
print("PRACTICAL OPERATOR APPLICATIONS")
print("=" * 80)

# Example 1: Validation
print("\n📌 Example 1: Input Validation")
age = 25
if 0 < age < 120 and isinstance(age, int):
    print(f"Valid age: {age}")

# Example 2: Default values
print("\n📌 Example 2: Default Values with 'or'")
username = ""
display_name = username or "Guest"
print(f"Display name: {display_name}")

# Example 3: Swap variables
print("\n📌 Example 3: Swapping Variables")
a, b = 5, 10
print(f"Before: a={a}, b={b}")
a, b = b, a  # Pythonic way!
print(f"After: a={a}, b={b}")

# Example 4: Ternary operator
print("\n📌 Example 4: Conditional Expression (Ternary)")
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")

# Example 5: Membership for validation
print("\n📌 Example 5: Validation with 'in'")
allowed_roles = {'admin', 'editor', 'viewer'}
user_role = 'editor'

if user_role in allowed_roles:
    print(f"Access granted for {user_role}")
else:
    print("Access denied")

# Example 6: Bitwise flags
print("\n📌 Example 6: Bitwise Flags for Permissions")

# Define permissions
READ = 1    # 0001
WRITE = 2   # 0010
EXECUTE = 4 # 0100
DELETE = 8  # 1000

# Set user permissions
user_perms = READ | WRITE | EXECUTE  # 0111 = 7

# Check permissions
has_read = bool(user_perms & READ)
has_write = bool(user_perms & WRITE)
has_delete = bool(user_perms & DELETE)

print(f"Permissions: {bin(user_perms)}")
print(f"Has READ: {has_read}")
print(f"Has WRITE: {has_write}")
print(f"Has DELETE: {has_delete}")

# OPERATOR OVERLOADING
print("\n" + "=" * 80)
print("OPERATOR OVERLOADING IN CLASSES")
print("=" * 80)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Overload * operator"""
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(f"\nv1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"v1 == v2: {v1 == v2}")

# COMMON PITFALLS
print("\n" + "=" * 80)
print("⚠️  COMMON PITFALLS")
print("=" * 80)

pitfalls = """
1. Using '==' instead of 'is' for None:
   ❌ if x == None:
   ✅ if x is None:

2. Confusing '=' (assignment) with '==' (comparison):
   ❌ if x = 5:  # SyntaxError
   ✅ if x == 5:

3. Division operator changed in Python 3:
   Python 2: 5 / 2 = 2 (integer division)
   Python 3: 5 / 2 = 2.5 (true division)
   Use // for integer division in Python 3

4. Bitwise vs Logical operators:
   ❌ if 1 & 2:  # Bitwise, not recommended for booleans
   ✅ if True and False:

5. Operator precedence confusion:
   2 + 3 * 4 = 14 (not 20)
   Use parentheses: (2 + 3) * 4 = 20

6. Chained assignment references:
   a = b = []  # Both reference SAME list!
   a.append(1)  # b is also [1]
"""
print(pitfalls)

# INTERVIEW ANSWER TEMPLATE
print("\n" + "=" * 80)
print("INTERVIEW ANSWER TEMPLATE")
print("=" * 80)

interview_answer = """
Q: What are Python operators? Explain with examples.

A: "Python operators are special symbols that perform operations on operands.
Python has 7 main categories:

1. ARITHMETIC: +, -, *, /, //, %, **
   Example: 17 // 5 = 3 (floor division)

2. COMPARISON: ==, !=, >, <, >=, <=
   Example: 10 < 20 < 30 (chained comparison)

3. LOGICAL: and, or, not
   Example: True and False → False
   Uses short-circuit evaluation

4. BITWISE: &, |, ^, ~, <<, >>
   Example: 60 & 13 = 12 (binary AND)
   Used for: flags, permissions, optimization

5. ASSIGNMENT: =, +=, -=, *=, etc.
   Example: x += 5 (equivalent to x = x + 5)
   Python 3.8+: := (walrus operator)

6. IDENTITY: is, is not
   Example: Use 'x is None' (not 'x == None')
   Checks if same object in memory

7. MEMBERSHIP: in, not in
   Example: 'apple' in fruits
   O(1) for sets, O(n) for lists

KEY POINTS:
- Operator precedence: () > ** > *, / > +, - > comparisons > logical
- Use 'is' for None, True, False
- Use '==' for value comparison
- Bitwise operators work on binary representation
- Can overload operators in custom classes using __add__, __eq__, etc.

In real projects, I commonly use:
- 'or' for default values: name or 'Guest'
- 'in' for validation: if role in allowed_roles
- Bitwise flags for permissions
- Walrus operator to avoid repeated function calls"
"""
print(interview_answer)
```

---

- Complete code examples
- Visual diagrams
- Comparisons
- Practical demonstrations
- Interview answer templates
- Common pitfalls
- Best practices

**Would you like me to:**

1. **Continue adding detailed solutions** for all 600 questions (this will create a very large file - estimated 100,000+ lines)
2. **Create a separate comprehensive solutions file** to keep the main guide manageable
3. **Add concise solutions** (shorter, code-focused) for faster coverage
4. **Focus on specific categories** you need most (e.g., algorithms, OOP, etc.)

Please let me know your preference, and I'll continue accordingly!

### 51. What is `__name__ == "__main__"`?

**Answer:**

```python
# script.py
def main():
    print("Running main function")

if __name__ == "__main__":
    # This runs only when script is executed directly
    # Not when imported as a module
    main()
```

### 52. What are Python's naming conventions?

**Answer:**

- **Variables/Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_CASE`
- **Private**: `_single_leading_underscore`
- **Name mangling**: `__double_leading_underscore`
- **Special methods**: `__dunder__`

### 53. What is the difference between `range()` and `xrange()`?

**Answer:**

- Python 2: `range()` returns list, `xrange()` returns iterator
- Python 3: `range()` returns iterator (like old `xrange()`), `xrange()` doesn't exist

### 54. How do you handle command-line arguments?

**Answer:**

```python
# Using sys
import sys
print(sys.argv)  # List of command-line arguments

# Using argparse
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```

### 55. What is virtual environment and why use it?

**Answer:**
Virtual environments isolate project dependencies.

```bash
# Create virtual environment
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Activate (Unix/Mac)
source myenv/bin/activate

# Install packages
pip install requests

# Freeze dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

---

## Good Luck with Your Interview! 🚀

Remember: The key to success is **practice, practice, practice**. Don't just read the answers—write the code yourself, experiment, and understand the concepts deeply.

#### Q7: What are control flow statements in Python?

**Complete Solution:**

Control flow statements determine execution order: if/elif/else (conditions), for/while (loops), break/continue/pass (control).

```python
# IF-ELIF-ELSE
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'

# Ternary
status = "Adult" if age >= 18 else "Minor"

# FOR loops
for i, item in enumerate(['a', 'b']):
    print(f"{i}: {item}")

# WHILE
count = 0
while count < 5:
    count += 1

# BREAK/CONTINUE
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)
```

**Interview Answer:** "Python has conditional (if/elif/else), looping (for/while), and control statements (break/continue/pass). Key features: uses indentation, for-else runs if no break, chained comparisons (10 < x < 20). Prefer list comprehensions for simple loops, early returns for validation, for-else for searches."

---

#### Q8: Explain list, tuple, dict, and set differences

**Complete Solution:**

```python
# LIST - Mutable, ordered, duplicates allowed
lst = [1, 2, 3, 2]
lst.append(4)  # Modify
lst[0] = 10

# TUPLE - Immutable, ordered
tpl = (1, 2, 3)
x, y, z = tpl  # Unpacking

# DICT - Mutable, key-value
dct = {'name': 'Alice', 'age': 30}
dct['city'] = 'NYC'

# SET - Mutable, unique
st = {1, 2, 3, 2}  # {1, 2, 3}
st.add(4)
```

**Answer:** "List: mutable ordered. Tuple: immutable ordered, use for fixed data. Dict: mutable key-value with O(1) lookup. Set: mutable unordered unique elements."

---

#### Q9: What is the difference between == and is?

**Complete Solution:**

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (values)
print(a is b)  # False (different objects)
print(a is c)  # True (same object)

# Use 'is' for None
if x is None:  # Correct
    pass
```

**Answer:** "'==' compares values, 'is' compares identity. Use 'is' for None/True/False. Python caches small integers (-5 to 256) and interns strings."

---

#### Q10: What are Python's built-in functions?

**Complete Solution:**

```python
# Type conversion: int(), float(), str(), list()
# I/O: print(), input()
# Math: abs(), max(), min(), sum(), pow(), round()
# Sequences: len(), sorted(), reversed(), range()
# Iteration: enumerate(), zip()
# Type checking: type(), isinstance()
# Functional: all(), any(), filter(), map()
# Object: dir(), help(), id()
```

**Answer:** "69 built-ins covering type conversion, I/O, math, sequences, iteration, type checking, functional programming. Most used: len(), range(), enumerate(), zip(), isinstance()."

---

#### Q11: What is list comprehension?

**Complete Solution:**

```python
# Syntax: [expression for item in iterable if condition]

squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
pairs = [(x,y) for x in [1,2] for y in ['a','b']]

# Dict comprehension
{x: x**2 for x in range(5)}

# Generator (memory efficient)
sum(x**2 for x in range(1000000))
```

**Answer:** "Concise way to create lists: [expr for item in iterable if cond]. 20-30% faster than loops. Works for dicts/sets. Use generators for large data."

---

#### Q12: Explain *args and **kwargs

**Complete Solution:**

```python
# *args - tuple of positional arguments
def sum_all(*args):
    return sum(args)

# **kwargs - dict of keyword arguments
def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

# Combined
def full(pos, *args, kw="default", **kwargs):
    pass

# Unpacking
numbers = [1, 2, 3]
print(*numbers)  # 1 2 3

# Merge dicts
{**dict1, **dict2}
```

**Answer:** "*args collects positional args into tuple. **kwargs collects keyword args into dict. Order: positional, *args, keyword-only, **kwargs. Use for flexible APIs, wrappers."

---

#### Q13: What is a lambda function?

**Complete Solution:**

```python
# Syntax: lambda args: expression

square = lambda x: x**2
multiply = lambda x, y: x * y

# With map/filter/sorted
list(map(lambda x: x**2, [1,2,3]))
list(filter(lambda x: x%2==0, [1,2,3,4]))
sorted(students, key=lambda s: s['grade'])

# Limitations: single expression only, no statements
```

**Answer:** "Anonymous function: lambda args: expression. Used for short, simple functions with map/filter/sorted. Limitations: single expression, no statements. Use 'def' for complex logic."

---

#### Q14: Explain map(), filter(), and reduce()

**Complete Solution:**

```python
# map() - transform each
list(map(lambda x: x**2, [1,2,3]))  # [1,4,9]

# filter() - select elements
list(filter(lambda x: x%2==0, [1,2,3,4]))  # [2,4]

# reduce() - aggregate to single value
from functools import reduce
reduce(lambda x,y: x+y, [1,2,3,4,5])  # 15

# Modern Python prefers comprehensions
[x**2 for x in [1,2,3]]  # Instead of map
[x for x in [1,2,3,4] if x%2==0]  # Instead of filter
```

**Answer:** "map transforms each element, filter selects, reduce aggregates. Modern Python prefers comprehensions (more readable). Use sum()/max()/min() instead of reduce when possible."

---

#### Q15: Shallow vs deep copy?

**Complete Solution:**

```python
import copy

# Shallow copy - copies outer only
shallow = original.copy()
shallow[2].append(99)  # Affects original nested objects!

# Deep copy - copies everything
deep = copy.deepcopy(original)
deep[2].append(99)  # Independent

# Methods
.copy(), [:], list()  # Shallow
copy.deepcopy()  # Deep
```

**Answer:** "Shallow copies outer object, shares nested. Deep copies everything recursively. Shallow: faster, simple structures. Deep: slower, nested structures need independence."

---

#### Q16: What are Python decorators?

**Complete Solution:**

```python
# Decorator wraps a function to extend behavior

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Equivalent to: say_hello = my_decorator(say_hello)

# With arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")

# Built-in decorators
@staticmethod
@classmethod
@property
```

**Answer:** "Decorator modifies function behavior without changing code. Syntax: @decorator above function. Used for logging, timing, access control, caching. Common built-ins: @property, @staticmethod, @classmethod, @functools.wraps."

---

#### Q17: Explain generators and yield

**Complete Solution:**

```python
# Generator function uses yield instead of return

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Returns generator object (lazy evaluation)
gen = count_up_to(5)
print(next(gen))  # 1
print(next(gen))  # 2

# Use in for loop
for num in count_up_to(5):
    print(num)

# Generator expression (like list comprehension)
gen_exp = (x**2 for x in range(1000000))  # Memory efficient!

# vs List comprehension
list_comp = [x**2 for x in range(1000000)]  # Creates entire list

# Benefits:
# - Memory efficient (generates on-demand)
# - Lazy evaluation
# - Can represent infinite sequences
# - Faster for large datasets

# Infinite generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

**Answer:** "Generator uses yield to produce values lazily. Benefits: memory efficient, lazy evaluation, can be infinite. Generator expression: (x for x in items). Use for large datasets, streams, infinite sequences. Returns iterator, consumed once."

---

#### Q18: What are iterators and iterables?

**Complete Solution:**

```python
# ITERABLE - object that can return an iterator
# Has __iter__() method
# Examples: list, tuple, dict, set, string

my_list = [1, 2, 3]  # Iterable
iterator = iter(my_list)  # Get iterator

# ITERATOR - object that produces next value
# Has __next__() method
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# next(iterator)  # StopIteration exception

# Custom iterator
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

counter = Counter(3)
for num in counter:
    print(num)  # 1, 2, 3

# Difference:
# - Iterable: Can be looped over (has __iter__)
# - Iterator: Produces values one at a time (has __next__)
# - All iterators are iterables
# - Not all iterables are iterators

# for loop uses iterators internally
for item in my_list:  # Calls iter(my_list) then next() repeatedly
    print(item)
```

**Answer:** "Iterable has __iter__() (list, dict, set). Iterator has __next__() (produces values). iter() creates iterator from iterable. next() gets next value. for loops use iterators internally. Generators are iterators. All iterators are iterables."

---

#### Q19: What is scope (LEGB rule)?

**Complete Solution:**

```python
# LEGB: Local, Enclosing, Global, Built-in

x = "global"  # Global scope

def outer():
    x = "enclosing"  # Enclosing scope

    def inner():
        x = "local"  # Local scope
        print(x)  # "local" (L)

    inner()
    print(x)  # "enclosing" (E)

outer()
print(x)  # "global" (G)

# Built-in scope (B)
print(len([1, 2, 3]))  # len is built-in

# Global keyword
def modify_global():
    global x
    x = "modified"

# Nonlocal keyword (access enclosing scope)
def outer():
    count = 0

    def inner():
        nonlocal count  # Access enclosing scope
        count += 1
        return count

    return inner

# Without nonlocal/global, assignment creates new local variable
def func():
    x = 10  # Local, doesn't affect global x
```

**Answer:** "LEGB rule: Local (function) → Enclosing (outer function) → Global (module) → Built-in. 'global' keyword accesses global scope. 'nonlocal' accesses enclosing scope. Assignment creates local unless specified. Python searches scopes in LEGB order."

---

#### Q20: What are closures?

**Complete Solution:**

```python
# Closure: inner function that captures enclosing scope

def outer(x):
    def inner(y):
        return x + y  # Captures x from outer
    return inner

add_5 = outer(5)
print(add_5(3))  # 8 (5+3)
print(add_5(10))  # 15 (5+10)

# x is "closed over" by inner function

# Practical use: Function factories
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_3 = make_multiplier(3)
print(times_3(10))  # 30

# Check closure variables
print(add_5.__closure__)  # Shows captured variables

# Use cases:
# - Function factories
# - Callbacks with state
# - Decorators
# - Data hiding/encapsulation

# Example: Counter with closure
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

**Answer:** "Closure: inner function that captures variables from enclosing scope. Created when nested function references outer variables. Use for function factories, callbacks with state, data hiding. Check with __closure__ attribute. Requires nonlocal for modification."

---

#### Q21: Explain try-except-else-finally

**Complete Solution:**

```python
# TRY-EXCEPT: Handle exceptions

try:
    result = 10 / 0  # May raise exception
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError as e:
    print(f"Value error: {e}")
except Exception as e:  # Catch-all
    print(f"Error: {e}")

# ELSE: Runs if no exception
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print(f"Success: {result}")  # This runs

# FINALLY: Always runs (cleanup)
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()  # Always executes

# Better: Use context manager
with open("data.txt") as file:
    data = file.read()  # Automatically closes

# Raise exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# Custom exceptions
class CustomError(Exception):
    pass

# Multiple exceptions
try:
    # code
except (ValueError, TypeError) as e:
    print(e)
```

**Answer:** "try: code that may raise exception. except: handle specific exceptions. else: runs if no exception. finally: always runs (cleanup). Use for error handling, resource cleanup. Prefer context managers (with) for files. Can raise custom exceptions."

---

#### Q22: What is the difference between append() and extend()?

**Complete Solution:**

```python
# APPEND: Add single element (anything)
lst = [1, 2, 3]
lst.append(4)
print(lst)  # [1, 2, 3, 4]

lst.append([5, 6])
print(lst)  # [1, 2, 3, 4, [5, 6]] - List added as single element

# EXTEND: Add elements from iterable
lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)  # [1, 2, 3, 4, 5]

lst.extend("ab")
print(lst)  # [1, 2, 3, 4, 5, 'a', 'b']

# Comparison
lst1 = [1, 2]
lst1.append([3, 4])  # [1, 2, [3, 4]]

lst2 = [1, 2]
lst2.extend([3, 4])  # [1, 2, 3, 4]

# Also can use:
lst = [1, 2, 3]
lst += [4, 5]  # Same as extend
lst = lst + [6, 7]  # Creates new list
```

**Answer:** "append() adds single element (even if list). extend() adds each element from iterable. append([1,2]) → [x, y, [1,2]]. extend([1,2]) → [x, y, 1, 2]. += is same as extend(). + creates new list."

---

#### Q23: What is __init__ and __new__?

**Complete Solution:**

```python
# __new__: Creates instance (rarely used)
# __init__: Initializes instance (constructor)

class MyClass:
    def __new__(cls, *args, **kwargs):
        print("__new__ called (creates instance)")
        instance = super().__new__(cls)
        return instance

    def __init__(self, value):
        print("__init__ called (initializes instance)")
        self.value = value

obj = MyClass(10)
# Output:
# __new__ called (creates instance)
# __init__ called (initializes instance)

# __new__ is static method that returns instance
# __init__ is instance method that returns None

# When to override __new__:
# - Immutable types (int, str, tuple subclasses)
# - Singleton pattern
# - Factory pattern
# - Metaclasses

# Singleton example
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True (same instance)

# __init__ is most common (constructor)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

**Answer:** "__new__ creates instance (called first), __init__ initializes instance (constructor). __new__ returns instance, __init__ returns None. Override __new__ for singletons, immutable types, metaclasses. __init__ is most common for initialization."

---

#### Q24: Explain self in Python classes

**Complete Solution:**

```python
# self refers to instance of the class

class Dog:
    def __init__(self, name):
        self.name = name  # Instance variable

    def bark(self):
        print(f"{self.name} says woof!")  # Access via self

dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.bark()  # Buddy says woof!
dog2.bark()  # Max says woof!

# self is convention (can use any name, but don't!)
class Cat:
    def __init__(this, name):  # 'this' works but not Pythonic
        this.name = name

# self is automatically passed
dog1.bark()  # Python calls: Dog.bark(dog1)

# Instance vs Class variables
class Counter:
    count = 0  # Class variable (shared)

    def __init__(self):
        self.instance_count = 0  # Instance variable (unique)
        Counter.count += 1  # Access class variable

c1 = Counter()
c2 = Counter()
print(Counter.count)  # 2 (shared)
print(c1.instance_count)  # 0 (unique to c1)

# self is required for instance methods
# Not required for @staticmethod or @classmethod
class MyClass:
    @staticmethod
    def static_method():
        pass  # No self

    @classmethod
    def class_method(cls):
        pass  # cls instead of self

    def instance_method(self):
        pass  # self required
```

**Answer:** "self refers to current instance. Required first parameter for instance methods. Convention (not keyword). Python passes automatically: obj.method() → Class.method(obj). Use for accessing instance variables/methods. Not needed for @staticmethod, use cls for @classmethod."

---

#### Q25: What are class methods vs static methods?

**Complete Solution:**

```python
class MyClass:
    class_var = "shared"

    # INSTANCE METHOD (default)
    def instance_method(self):
        return f"Instance: {self.class_var}"

    # CLASS METHOD - operates on class
    @classmethod
    def class_method(cls):
        return f"Class: {cls.class_var}"

    # STATIC METHOD - utility function
    @staticmethod
    def static_method(x, y):
        return x + y

# Usage
obj = MyClass()

obj.instance_method()  # Needs instance
MyClass.class_method()  # Can call on class
MyClass.static_method(1, 2)  # No instance or class needed

# INSTANCE METHOD:
# - Takes self (instance)
# - Access instance and class variables
# - Most common

# CLASS METHOD:
# - Takes cls (class)
# - Access class variables
# - Alternative constructors
# - Factory methods

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)  # Create instance

date1 = Date(2024, 1, 15)
date2 = Date.from_string("2024-01-15")  # Alternative constructor

# STATIC METHOD:
# - No self or cls
# - Pure function related to class
# - Utility function
# - Cannot access instance or class state

class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

print(Math.add(5, 3))  # 8
print(Math.is_prime(17))  # True
```

**Answer:** "Instance method: takes self, accesses instance. Class method: takes cls, operates on class, used for alternative constructors. Static method: no self/cls, utility function, pure function. Use @classmethod for factory methods, @staticmethod for utilities."

---

#### Q26: Explain inheritance in Python

**Complete Solution:**

```python
# SINGLE INHERITANCE

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

dog = Dog("Buddy")
print(dog.speak())  # Buddy says woof!

# super() calls parent method
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent __init__
        self.breed = breed

# MULTIPLE INHERITANCE

class Flying:
    def fly(self):
        return "Flying!"

class Swimming:
    def swim(self):
        return "Swimming!"

class Duck(Animal, Flying, Swimming):  # Multiple parents
    def speak(self):
        return f"{self.name} says quack!"

duck = Duck("Donald")
print(duck.speak())  # quack!
print(duck.fly())  # Flying!
print(duck.swim())  # Swimming!

# MRO (Method Resolution Order)
print(Duck.__mro__)  # Shows inheritance chain
# (<class 'Duck'>, <class 'Animal'>, <class 'Flying'>, 
#  <class 'Swimming'>, <class 'object'>)

# isinstance() and issubclass()
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True

# Override parent methods
class GermanShepherd(Dog):
    def speak(self):
        return f"{self.name} barks loudly!"
```

**Answer:** "Inheritance: class inherits from parent class(es). Use super() to call parent methods. Multiple inheritance supported. MRO determines method lookup order. isinstance() checks if object is instance of class. issubclass() checks inheritance. Override methods in child class."

---

#### Q27: What is polymorphism?

**Complete Solution:**

```python
# POLYMORPHISM: Same interface, different implementation

# Method overriding (runtime polymorphism)
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Same method name, different behavior
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())  # Calls appropriate method

# Duck typing: "If it walks like a duck..."
def draw_shape(shape):
    shape.draw()  # Works for any object with draw() method

# Operator overloading
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overload +
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):  # Overload str()
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Uses __add__
print(v3)  # Uses __str__

# Function overloading (not built-in, use default args)
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Hello, Alice!
print(greet("Bob", "Hi"))  # Hi, Bob!
```

**Answer:** "Polymorphism: same interface, different implementations. Method overriding: subclass redefines parent method. Duck typing: object's suitability determined by methods/properties. Operator overloading: __add__, __mul__, etc. Python uses duck typing heavily."

---

#### Q28: What is encapsulation?

**Complete Solution:**

```python
# ENCAPSULATION: Bundling data with methods, restricting access

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private (name mangling)
        self._account_id = "12345"  # Protected (convention)

    # Public method to access private variable
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

account = BankAccount(1000)
print(account.get_balance())  # 1000
# print(account.__balance)  # AttributeError
print(account._BankAccount__balance)  # 1000 (name mangling)

# Access levels (convention-based):
# public: no underscore (name)
# protected: single underscore (_name) - internal use
# private: double underscore (__name) - name mangling

class MyClass:
    def __init__(self):
        self.public = "everyone can access"
        self._protected = "internal use"
        self.__private = "name mangled"

# Property decorator (getter/setter)
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):  # Getter
        return self._age

    @age.setter
    def age(self, value):  # Setter
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age cannot be negative")

person = Person(25)
print(person.age)  # Uses getter
person.age = 30  # Uses setter
# person.age = -5  # ValueError

# Benefits:
# - Data hiding
# - Controlled access
# - Validation
# - Easier to change internal implementation
```

**Answer:** "Encapsulation: bundle data with methods, control access. Python naming: public (name), protected (_name convention), private (__name name mangling). Use @property for getters/setters. Benefits: data hiding, validation, controlled access. Python relies on conventions more than strict access control."

---

#### Q29: What are abstract classes and interfaces?

**Complete Solution:**

```python
from abc import ABC, abstractmethod

# ABSTRACT BASE CLASS
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Must be implemented by subclass

    @abstractmethod
    def perimeter(self):
        pass

    def description(self):  # Concrete method
        return "This is a shape"

# Cannot instantiate abstract class
# shape = Shape()  # TypeError

# Must implement all abstract methods
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

circle = Circle(5)
print(circle.area())  # Works

# Python doesn't have interfaces (use ABC)
# Interface: all methods abstract

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Clickable(ABC):
    @abstractmethod
    def click(self):
        pass

class Button(Drawable, Clickable):  # Implement multiple "interfaces"
    def draw(self):
        print("Drawing button")

    def click(self):
        print("Button clicked")

# Abstract properties
class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    @property
    def sound(self):
        return "woof"

# Use cases:
# - Define contracts
# - Ensure consistent API
# - Template method pattern
# - Plugin systems
```

**Answer:** "Abstract class: cannot instantiate, has @abstractmethod(s) using ABC. Subclasses must implement abstract methods. Python has no interfaces, use ABC with all abstract methods. Multiple ABCs simulate interfaces. Use for contracts, consistent API, template patterns."

---

#### Q30: Explain @property decorator

**Complete Solution:**

```python
# @property: Make method accessible as attribute

class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):  # Getter
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, name):  # Setter
        first, last = name.split(' ')
        self._first_name = first
        self._last_name = last

    @full_name.deleter
    def full_name(self):  # Deleter
        self._first_name = None
        self._last_name = None

person = Person("John", "Doe")
print(person.full_name)  # John Doe (calls getter)
person.full_name = "Jane Smith"  # Calls setter
del person.full_name  # Calls deleter

# Computed property
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

circle = Circle(5)
print(circle.area)  # 78.5 (computed)
circle.diameter = 20  # Sets radius to 10
print(circle.area)  # 314.0

# Validation with setter
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.fahrenheit)  # 77.0
# temp.celsius = -300  # ValueError

# Benefits:
# - Clean syntax (obj.attr instead of obj.get_attr())
# - Computed values
# - Validation
# - Backward compatibility
# - Encapsulation
```

**Answer:** "@property makes method accessible as attribute. Use @property for getter, @name.setter for setter, @name.deleter for deleter. Benefits: clean syntax, computed properties, validation, encapsulation. Access like attribute: obj.name not obj.name(). Common for getters/setters, computed values, validation."

---

#### Q31: What is recursion?

**Complete Solution:**

```python
# Recursion: Function calls itself

def factorial(n):
    # Base case (stopping condition)
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(factorial(5))  # 5 * 4 * 3 * 2 * 1 = 120

# Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Sum of list
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))  # 10

# Recursion vs Iteration
# Recursive
def countdown_recursive(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown_recursive(n - 1)

# Iterative
def countdown_iterative(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")

# Recursion depth limit
import sys
print(sys.getrecursionlimit())  # Default: 1000
sys.setrecursionlimit(2000)  # Increase if needed

# Tail recursion (not optimized in Python)
def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

# Memoization to optimize recursion
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Tree traversal (classic recursion use case)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value)
        inorder_traversal(node.right)
```

**Answer:** "Recursion: function calls itself. Requires base case (stop) and recursive case. Stack space grows with depth. Python limit: 1000 (sys.getrecursionlimit). Use for trees, divide-and-conquer, backtracking. Optimize with memoization. Often slower than iteration but cleaner for some problems."

---

#### Q32: How does context manager (with statement) work?

**Complete Solution:**

```python
# Context manager: Setup and cleanup automatically

# File handling (most common use)
with open('file.txt', 'r') as f:
    data = f.read()
# File automatically closed

# Equivalent to:
f = open('file.txt', 'r')
try:
    data = f.read()
finally:
    f.close()

# Multiple context managers
with open('input.txt') as infile, open('output.txt', 'w') as outfile:
    outfile.write(infile.read())

# Custom context manager using class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")
        if self.file:
            self.file.close()
        # Return True to suppress exception
        # Return False/None to propagate exception
        return False

with FileManager('test.txt', 'w') as f:
    f.write('Hello!')

# Using contextlib decorator
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        f = open(filename, mode)
        yield f  # Return value to 'as' variable
    finally:
        f.close()

with file_manager('test.txt', 'r') as f:
    print(f.read())

# Database connection example
class DatabaseConnection:
    def __enter__(self):
        self.conn = connect_to_db()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

with DatabaseConnection() as conn:
    conn.execute("SELECT * FROM users")

# Lock example (threading)
from threading import Lock

lock = Lock()
with lock:
    # Critical section
    # Lock automatically released

# Suppress exceptions
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove('nonexistent.txt')  # Won't raise error

# Timer context manager
import time

@contextmanager
def timer(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{label}: {end - start:.2f}s")

with timer("Processing"):
    # Code to time
    time.sleep(1)
```

**Answer:** "Context manager: __enter__ (setup) and __exit__ (cleanup). Used with 'with' statement. Ensures cleanup even if exception occurs. Common for files, locks, database connections. Create with class (__enter__/__exit__) or @contextmanager decorator. Benefits: automatic cleanup, exception safety, cleaner code."

---

#### Q33: What are modules and packages?

**Complete Solution:**

```python
# MODULE: Single Python file (.py)

# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159

# Import module
import math_utils
print(math_utils.add(2, 3))
print(math_utils.PI)

# Import specific items
from math_utils import add, PI
print(add(2, 3))

# Import with alias
import math_utils as mu
print(mu.multiply(4, 5))

# Import all (not recommended)
from math_utils import *

# PACKAGE: Directory with __init__.py

# mypackage/
#   __init__.py
#   module1.py
#   module2.py
#   subpackage/
#     __init__.py
#     module3.py

# Import from package
from mypackage import module1
from mypackage.subpackage import module3

# __init__.py can initialize package
# mypackage/__init__.py
from .module1 import func1
from .module2 import func2

__all__ = ['func1', 'func2']  # Define what * imports

# Relative imports (within package)
# From module1.py in mypackage
from . import module2  # Same directory
from .. import parent_module  # Parent directory
from .subpackage import module3  # Subdirectory

# Absolute imports (preferred)
from mypackage import module1
from mypackage.subpackage import module3

# Module attributes
import math
print(math.__name__)  # 'math'
print(math.__file__)  # Location
print(dir(math))  # List all attributes

# if __name__ == "__main__":
# module.py
def main():
    print("Running as script")

if __name__ == "__main__":
    main()  # Only runs if executed directly, not imported

# sys.path: where Python looks for modules
import sys
print(sys.path)
sys.path.append('/custom/path')  # Add custom path

# Reload module (for development)
import importlib
importlib.reload(math_utils)
```

**Answer:** "Module: single .py file. Package: directory with __init__.py. Import with 'import module' or 'from module import item'. __init__.py initializes package. Relative imports: from . import. Absolute imports preferred. if __name__ == '__main__': runs only when executed directly. sys.path defines module search locations."

---

#### Q34: Explain *args and **kwargs

**Complete Solution:**

```python
# *args: Variable number of positional arguments (tuple)

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs: Variable number of keyword arguments (dict)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# name: Alice
# age: 30
# city: NYC

# Combined: positional, *args, keyword, **kwargs
def full_example(pos1, pos2, *args, key1="default", **kwargs):
    print(f"Positional: {pos1}, {pos2}")
    print(f"Args: {args}")
    print(f"Key1: {key1}")
    print(f"Kwargs: {kwargs}")

full_example(1, 2, 3, 4, key1="custom", extra="value")
# Positional: 1, 2
# Args: (3, 4)
# Key1: custom
# Kwargs: {'extra': 'value'}

# Order matters!
# def func(pos, *args, key="default", **kwargs):  # Correct
# def func(*args, pos, **kwargs):  # Error!

# Unpacking with * and **
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # Unpacks list to arguments

def greet(name, age):
    print(f"{name} is {age}")

info = {"name": "Bob", "age": 25}
greet(**info)  # Unpacks dict to keyword arguments

# Function forwarding
def wrapper(*args, **kwargs):
    print("Before")
    result = some_function(*args, **kwargs)  # Forward all arguments
    print("After")
    return result

# Merging dictionaries (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Python 3.8+ positional-only and keyword-only
def func(pos_only, /, standard, *, kw_only):
    pass

# func(1, 2, 3)  # Error: kw_only must be keyword
func(1, 2, kw_only=3)  # Correct
```

**Answer:** "*args collects positional arguments as tuple. **kwargs collects keyword arguments as dict. Use for variable arguments. Order: positional, *args, keyword, **kwargs. Unpack with *list and **dict. Use / for positional-only, * for keyword-only parameters. Common in decorators, wrappers, API functions."

---

#### Q35: What is the difference between import and from...import?

**Complete Solution:**

```python
# IMPORT: Import entire module

import math
print(math.sqrt(16))  # Need module prefix
print(math.pi)

# Namespace pollution: None (everything under 'math')

# FROM...IMPORT: Import specific items

from math import sqrt, pi
print(sqrt(16))  # No prefix needed
print(pi)

# Namespace pollution: sqrt and pi in current namespace

# Import with alias
import numpy as np
import pandas as pd

from math import sqrt as square_root
print(square_root(25))

# Import all (NOT RECOMMENDED)
from math import *
print(sqrt(16))  # Works but unclear where sqrt comes from

# Why avoid import *:
# - Namespace pollution
# - Name conflicts
# - Hard to track source
# - IDE/linter issues

# Example of conflict
from module1 import *  # Has 'calculate'
from module2 import *  # Also has 'calculate' - overwrites!

# Better: Explicit imports
from module1 import calculate as calc1
from module2 import calculate as calc2

# Submodule import
import os.path  # Need: os.path.join()
from os.path import join  # Can use: join()
from os import path  # Can use: path.join()

# Performance consideration
# import math
# for i in range(1000000):
#     math.sqrt(i)  # Lookup 'math' then 'sqrt' each time

# from math import sqrt
# for i in range(1000000):
#     sqrt(i)  # Direct access (slightly faster)

# Best practices:
# 1. Use 'import module' for standard libraries
# 2. Use 'from module import item' for specific items
# 3. Avoid 'from module import *'
# 4. Group imports: stdlib, third-party, local
# 5. Use aliases for long names (np, pd)

# Import organization (PEP 8)
# Standard library
import os
import sys

# Third-party
import numpy as np
import pandas as pd

# Local
from myapp import module1
from myapp import module2
```

**Answer:** "import module: imports entire module, use module.item. from module import item: imports specific items, use directly. import * imports everything (avoid). Use import for standard libraries, from import for specific items. Aliases: import module as alias. Group imports: stdlib, third-party, local. from import is slightly faster for repeated use."

---

#### Q36: What is __name__ and __main__?

**Complete Solution:**

```python
# __name__: Built-in variable for module name

# module.py
print(f"Module name: {__name__}")

# When imported: __name__ = "module"
# When run directly: __name__ = "__main__"

# Common pattern: Execute only when run directly
def main():
    print("Running main function")
    # Your code here

if __name__ == "__main__":
    main()  # Only runs when script executed directly

# Example: math_utils.py
def add(a, b):
    return a + b

def test():
    print("Testing add function")
    assert add(2, 3) == 5
    print("All tests passed!")

if __name__ == "__main__":
    test()  # Run tests when executed directly

# When imported
# import math_utils  # test() doesn't run
# math_utils.add(2, 3)  # Use functions

# When executed
# python math_utils.py  # test() runs

# Real-world example: CLI tool
import sys

def process_file(filename):
    with open(filename) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    result = process_file(filename)
    print(result)

if __name__ == "__main__":
    main()

# Can still import and use as library
# from script import process_file
# data = process_file("myfile.txt")

# Other uses
# Check if being run as script
if __name__ == "__main__":
    # Development/testing code
    # Command-line interface
    # Example usage
    pass

# Module introspection
import math
print(math.__name__)  # 'math'
print(__name__)  # '__main__' or module name

# Package main
# mypackage/__main__.py
# Runs when: python -m mypackage
def main():
    print("Package main")

if __name__ == "__main__":
    main()
```

**Answer:** "__name__ is module name. When run directly: '__main__'. When imported: module name. Pattern: if __name__ == '__main__': runs only when executed directly, not when imported. Use for tests, CLI, examples. Allows module to be both library and script. __main__.py makes package executable with python -m."

---

#### Q37: What are lambda functions?

**Complete Solution:**

```python
# Lambda: Anonymous one-line function

# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(add_lambda(2, 3))  # 5

# Syntax: lambda arguments: expression

# Single argument
square = lambda x: x ** 2
print(square(5))  # 25

# Multiple arguments
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # 24

# No arguments
greet = lambda: "Hello!"
print(greet())  # Hello!

# With map/filter/reduce
numbers = [1, 2, 3, 4, 5]

# map
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# sorted with key
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
# [(2, 'a'), (1, 'b'), (3, 'c')]

# Limitations:
# - Single expression only (no statements)
# - No multiple lines
# - Less readable for complex logic
# - No docstring
# - Hard to debug

# What you CAN'T do with lambda:
# lambda x: if x > 0: return x  # Syntax error
# lambda x: print(x)  # Can't use statements (but this works)
# lambda x: x = x + 1  # Can't assign

# What you CAN do:
# Ternary operator
abs_value = lambda x: x if x >= 0 else -x

# Calling functions
apply_func = lambda f, x: f(x)

# Nested lambdas (not recommended)
add = lambda x: lambda y: x + y
print(add(2)(3))  # 5

# When to use lambda:
# - Short, simple operations
# - One-time use (callbacks)
# - map/filter/sorted key
# - List/dict sorting

# When NOT to use:
# - Complex logic (use def)
# - Reusable functions (use def)
# - Need docstring
# - Multiple statements

# Better alternatives
# Instead of:
result = list(map(lambda x: x**2, numbers))

# Use comprehension:
result = [x**2 for x in numbers]  # More Pythonic!

# Instead of:
result = list(filter(lambda x: x % 2 == 0, numbers))

# Use comprehension:
result = [x for x in numbers if x % 2 == 0]
```

**Answer:** "Lambda: anonymous one-line function. Syntax: lambda args: expression. Use for simple operations, callbacks, map/filter/sorted key. Limitations: single expression, no statements, less readable. Prefer list comprehensions for map/filter. Use def for complex logic, reusable functions, or when need docstring."

---

#### Q38: Explain map, filter, and reduce

**Complete Solution:**

```python
from functools import reduce

# MAP: Apply function to each element

numbers = [1, 2, 3, 4, 5]

# Using map
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Equivalent list comprehension (preferred)
squared = [x**2 for x in numbers]

# map with multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)  # [11, 22, 33]

# FILTER: Keep elements that match condition

# Using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Equivalent list comprehension (preferred)
evens = [x for x in numbers if x % 2 == 0]

# Filter with custom function
def is_positive(n):
    return n > 0

values = [-2, -1, 0, 1, 2]
positives = list(filter(is_positive, values))
print(positives)  # [1, 2]

# REDUCE: Reduce sequence to single value

# Sum of all elements
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# Equivalent (prefer built-in sum)
total = sum(numbers)

# Product of all elements
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
# Or use: max(numbers)

# With initial value
result = reduce(lambda x, y: x + y, [1, 2, 3], 10)
print(result)  # 16 (10 + 1 + 2 + 3)

# Combining map, filter, reduce
# Sum of squares of even numbers
result = reduce(
    lambda x, y: x + y,
    map(lambda x: x**2, 
        filter(lambda x: x % 2 == 0, numbers))
)

# Better: Use comprehension
result = sum(x**2 for x in numbers if x % 2 == 0)

# Performance comparison
import timeit

numbers = range(10000)

# map/filter
def using_map_filter():
    return sum(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

# comprehension
def using_comprehension():
    return sum(x**2 for x in numbers if x % 2 == 0)

# Comprehension is usually faster and more readable!

# When to use:
# map: Transform all elements (but prefer comprehension)
# filter: Select elements (but prefer comprehension)
# reduce: Accumulate/combine (use only for complex operations)

# Modern Python: Prefer comprehensions
# Old style:
result = list(map(lambda x: x.upper(), filter(lambda x: len(x) > 3, words)))

# Modern style:
result = [word.upper() for word in words if len(word) > 3]
```

**Answer:** "map(func, iterable): apply function to each element. filter(func, iterable): keep elements where func returns True. reduce(func, iterable): accumulate to single value. All return iterators (need list()). Modern Python: prefer comprehensions (faster, more readable). Use reduce from functools for complex accumulation. Built-ins better: sum(), max(), min()."

---

#### Q39: What is the GIL (Global Interpreter Lock)?

**Complete Solution:**

```python
# GIL: Mutex that allows only one thread to execute Python bytecode at a time

# Problem: CPU-bound tasks can't use multiple cores effectively

import threading
import time

# CPU-bound task (affected by GIL)
def cpu_bound():
    count = 0
    for i in range(100000000):
        count += i
    return count

# Single thread
start = time.time()
cpu_bound()
print(f"Single: {time.time() - start:.2f}s")  # ~5s

# Multiple threads (no speedup due to GIL!)
start = time.time()
threads = [threading.Thread(target=cpu_bound) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Threaded: {time.time() - start:.2f}s")  # ~5s (same!)

# Solution for CPU-bound: multiprocessing (separate processes)
from multiprocessing import Process

start = time.time()
processes = [Process(target=cpu_bound) for _ in range(2)]
for p in processes: p.start()
for p in processes: p.join()
print(f"Multiprocess: {time.time() - start:.2f}s")  # ~2.5s (faster!)

# I/O-bound tasks NOT affected (threads work fine)
import requests

def io_bound():
    requests.get('https://example.com')

# Threads good for I/O (network, disk, sleep)
start = time.time()
threads = [threading.Thread(target=io_bound) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print(f"I/O threads: {time.time() - start:.2f}s")  # Fast!

# Why GIL exists:
# - Memory management (reference counting)
# - C extension compatibility
# - Simplifies implementation

# When GIL is released:
# - I/O operations
# - time.sleep()
# - Some C extensions (NumPy)

# Workarounds:
# 1. multiprocessing for CPU-bound
from multiprocessing import Pool

def square(n):
    return n * n

with Pool(4) as pool:
    results = pool.map(square, range(100))

# 2. Use C extensions (NumPy, Pandas - release GIL)
import numpy as np
array = np.arange(1000000)
result = array ** 2  # Releases GIL internally

# 3. concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Threads for I/O
with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(io_bound, range(10))

# Processes for CPU
with ProcessPoolExecutor(max_workers=4) as executor:
    results = executor.map(cpu_bound, range(4))

# 4. async/await for I/O concurrency
import asyncio

async def async_io():
    await asyncio.sleep(1)

async def main():
    tasks = [async_io() for _ in range(10)]
    await asyncio.gather(*tasks)

# asyncio.run(main())

# Guidelines:
# - I/O-bound: Use threading or asyncio
# - CPU-bound: Use multiprocessing
# - Mixed: Consider ProcessPoolExecutor
```

**Answer:** "GIL: Global Interpreter Lock allows only one thread to execute Python bytecode at a time. Affects CPU-bound tasks (no multi-core speedup). I/O-bound tasks unaffected (GIL released during I/O). Workarounds: multiprocessing for CPU-bound, threading/asyncio for I/O-bound, NumPy/C extensions (release GIL). Exists for memory management and C extension compatibility."

---

#### Q40: What is duck typing?

**Complete Solution:**

```python
# Duck typing: "If it walks like a duck and quacks like a duck, it's a duck"
# Type determined by methods/properties, not inheritance

# Example 1: File-like objects
class StringBuffer:
    def __init__(self):
        self.data = []

    def write(self, text):
        self.data.append(text)

    def read(self):
        return ''.join(self.data)

# Function accepts any object with write()
def log_message(file_obj, message):
    file_obj.write(message)

# Works with real file
with open('log.txt', 'w') as f:
    log_message(f, "Hello")

# Works with StringBuffer (duck typing!)
buffer = StringBuffer()
log_message(buffer, "Hello")

# Example 2: Iteration
class CustomRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        raise StopIteration

# Works like any iterable
for num in CustomRange(0, 5):
    print(num)  # 0, 1, 2, 3, 4

# Example 3: Numeric types
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Works like numbers!

# EAFP vs LBYL

# LBYL: Look Before You Leap
if hasattr(obj, 'quack'):
    obj.quack()

# EAFP: Easier to Ask Forgiveness than Permission (Pythonic)
try:
    obj.quack()
except AttributeError:
    print("Not a duck!")

# Why duck typing is powerful:
def process_items(items):
    # Works with list, tuple, set, generator, custom iterable
    for item in items:
        print(item)

process_items([1, 2, 3])
process_items((1, 2, 3))
process_items({1, 2, 3})
process_items(range(3))

# Protocol: Informal interface
# Iterable protocol: __iter__
# Iterator protocol: __next__
# Context manager protocol: __enter__, __exit__
# Sequence protocol: __len__, __getitem__

# Type hints with Protocol (Python 3.8+)
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(obj: Drawable):
    obj.draw()  # Works with any object with draw()

# vs Static typing
class Animal:
    def speak(self): pass

class Dog(Animal):  # Must inherit
    def speak(self): 
        return "Woof"

# Duck typing: No inheritance needed
class Cat:  # Doesn't inherit Animal
    def speak(self):
        return "Meow"

def make_sound(animal):
    return animal.speak()  # Works for both Dog and Cat!
```

**Answer:** "Duck typing: object's suitability determined by presence of methods/properties, not type. 'If it has quack(), it's a duck'. No need for inheritance. Python is dynamically typed. Use EAFP (try/except) over LBYL (if hasattr). Protocols: informal interfaces (__iter__, __enter__, etc.). Type hints with Protocol for duck typing validation."

---

#### Q41: What are magic/dunder methods?

**Complete Solution:**

```python
# Magic methods: __method__ (double underscore)
# Define object behavior for operators and built-in functions

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' ({self.pages} pages)"

    def __repr__(self):
        return f"Book(title='{self.title}', pages={self.pages})"

    def __eq__(self, other):
        return self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __add__(self, other):
        return Book(f"{self.title} & {other.title}", self.pages + other.pages)

    def __len__(self):
        return self.pages

    def __getitem__(self, index):
        return f"Page {index}"

    def __call__(self, page):
        return f"Reading page {page}"

book1 = Book("Python Basics", 200)
book2 = Book("Advanced Python", 300)

print(str(book1))
print(repr(book1))
print(book1 == book2)
print(book1 < book2)
print(len(book1))
print(book1[5])
print(book1(10))
```

**Answer:** "Magic methods: __method__ methods define object behavior. __init__ initializes, __str__ for string, __repr__ for representation, __eq__ for ==, __lt__ for <, __add__ for +, __len__ for len(), __getitem__ for [], __iter__ for iteration, __enter__/__exit__ for context managers. Enable operator overloading and protocol implementation."

---

#### Q42: What is the difference between __str__ and __repr__?

**Complete Solution:**

```python
# __str__: User-friendly string
# __repr__: Developer-friendly representation

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)
print(str(person))  # Alice, 30 years old
print(repr(person)) # Person(name='Alice', age=30)
```

**Answer:** "__str__: user-friendly string (print, str()). __repr__: developer-friendly (debugging, repr()). __repr__ should be unambiguous, ideally eval(repr(obj)) recreates object. Always implement __repr__, __str__ optional. print() uses __str__ if available, else __repr__."

---

#### Q43: What is method resolution order (MRO)?

**Complete Solution:**

```python
# MRO: Order Python searches for methods in inheritance

class A:
    def method(self): print("A")

class B(A):
    def method(self): print("B")

class C(A):
    def method(self): print("C")

class D(B, C):
    pass

print(D.__mro__)
# (<class D>, <class B>, <class C>, <class A>, <class object>)

d = D()
d.method()  # B (follows MRO)
```

**Answer:** "MRO: Method Resolution Order determines method lookup. Uses C3 linearization: children before parents, left to right. Check with __mro__ or .mro(). super() follows MRO. Diamond problem solved. Multiple inheritance: first parent preferred."

---

#### Q44: What are descriptors?

**Complete Solution:**

```python
# Descriptor: Object with __get__, __set__, __del__

class ValidatedAttribute:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Must be integer")
        obj.__dict__[self.name] = value

class Person:
    age = ValidatedAttribute("age")

p = Person()
p.age = 30  # OK
# p.age = "30"  # TypeError
```

**Answer:** "Descriptor: object with __get__, __set__, __del__. Controls attribute access. property, staticmethod, classmethod are descriptors. Methods are descriptors (bind to instance). Use for validation, lazy loading, type checking."

---

#### Q45: What is the difference between @staticmethod and @classmethod?

**Complete Solution:**

```python
class MyClass:
    class_var = "shared"

    def instance_method(self):
        return f"Instance: {self.class_var}"

    @classmethod
    def class_method(cls):
        return f"Class: {cls.class_var}"

    @staticmethod
    def static_method(x, y):
        return x + y

# Alternative constructor example
class Date:
    def __init__(self, year, month, day):
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        y, m, d = date_string.split("-")
        return cls(int(y), int(m), int(d))
```

**Answer:** "Instance method: takes self. Class method: takes cls, use for factory methods. Static method: no self/cls, pure utility. @classmethod inheritance-aware. Choose: instance (instance data), class (factory), static (utility)."

---

#### Q46: What is a metaclass?

**Complete Solution:**

```python
# Metaclass: Class of a class

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print(f"Creating class {name}")
        dct["added"] = 100
        return super().__new__(mcs, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.added)  # 100

# Singleton pattern
class Singleton(type):
    _instances = {}
    def __call__(cls, *args):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args)
        return cls._instances[cls]
```

**Answer:** "Metaclass: class factory. type is default metaclass. Override __new__ to modify class creation. Use for singletons, class registration, ORMs. Rarely needed. Alternative: __init_subclass__."

---

#### Q47: What is monkey patching?

**Complete Solution:**

```python
# Monkey patching: Modify class/module at runtime

class Dog:
    def bark(self): return "Woof!"

# Add method
def fetch(self): return "Fetching!"
Dog.fetch = fetch

dog = Dog()
print(dog.fetch())  # Fetching!

# Use unittest.mock for testing
from unittest.mock import patch

with patch.object(Dog, "bark", return_value="Mocked"):
    print(dog.bark())  # Mocked
```

**Answer:** "Monkey patching: modify classes at runtime. Use for testing (mock), fixing bugs. Dangers: hard to debug. Use unittest.mock. Better: inheritance, composition. Only in tests."

---

#### Q48: What are __slots__?

**Complete Solution:**

```python
# __slots__: Define allowed attributes, save memory

class Normal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ["x", "y"]
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Memory savings: ~40-50% for millions of instances
# Faster attribute access
# Prevents adding new attributes

s = WithSlots(1, 2)
# s.z = 3  # AttributeError
```

**Answer:** "__slots__: define allowed attributes. Benefits: 40-50% memory savings, faster access, prevents typos. No __dict__. Use for millions of instances. Python 3.10+: @dataclass(slots=True)."

---

#### Q49: What is the difference between deepcopy and shallow copy?

**Complete Solution:**

```python
import copy

# Shallow copy: new object, shared nested objects
original = [1, 2, [3, 4]]
shallow = original.copy()
shallow[2][0] = 999
print(original)  # [1, 2, [999, 4]] - Modified!

# Deep copy: complete independence
original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)
deep[2][0] = 999
print(original)  # [1, 2, [3, 4]] - Unchanged!
```

**Answer:** "Shallow copy: new object, nested objects shared. Methods: .copy(), [:], dict.copy(). Deep copy: recursively copies all (copy.deepcopy()). Shallow faster. Deep for independence. Handles circular references."

---

#### Q50: What is the difference between Python 2 and Python 3?

**Complete Solution:**

```python
# Major differences:

# 1. PRINT: statement vs function
print("Hello")  # Python 3 (function)

# 2. DIVISION: / is true division
print(5 / 2)   # 2.5 (Python 3)
print(5 // 2)  # 2 (floor division)

# 3. UNICODE: str is unicode by default
s = "unicode"  # Python 3
b = b"bytes"   # bytes type

# 4. RANGE: returns iterator
range(10)  # range object (Python 3)

# 5. DICT METHODS: return views
d = {"a": 1}
d.keys()    # dict_keys (view)
d.values()  # dict_values (view)

# 6. EXCEPTION SYNTAX:
try:
    raise ValueError("msg")
except ValueError as e:  # as, not comma
    pass

# 7. NEW FEATURES:
# - f-strings (3.6+)
# - Type hints (3.5+)
# - async/await (3.5+)
# - Dataclasses (3.7+)
# - Walrus operator := (3.8+)
```

**Answer:** "Major: print function, / true division, str=unicode, range=iterator, dict views, exception as e, no comparing incompatible types. Python 3: f-strings, type hints, async/await. Python 2 EOL 2020. Use 2to3 for migration."

---

#### Q51: What are list comprehensions and how do they compare to map/filter?

**Complete Solution:**

```python
# List comprehension: [expression for item in iterable if condition]

# Create squares
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# vs map/filter
squares_map = list(map(lambda x: x**2, range(10)))
even_squares_filter = list(filter(lambda x: x % 2 == 0, 
                           map(lambda x: x**2, range(10))))

# Nested comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dict comprehension
square_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
unique_lengths = {len(word) for word in ["a", "ab", "abc", "a"]}
# {1, 2, 3}

# Generator expression (lazy)
gen = (x**2 for x in range(1000000))  # Memory efficient!

# Performance comparison
import timeit
# Comprehension: 0.8s, map: 1.2s, for loop: 1.5s

# Walrus operator (Python 3.8+)
# Avoid repeated computation
results = [y for x in range(10) if (y := x**2) > 10]
```

**Answer:** "List comprehension: [expr for item in iterable if condition]. More Pythonic than map/filter. Dict: {k:v for...}, Set: {expr for...}, Generator: (expr for...). Nested: multiple for clauses. Walrus := avoids recomputation. Comprehensions faster and more readable."

---

#### Q52: Explain async/await and asyncio

**Complete Solution:**

```python
import asyncio

# async def: coroutine function
async def fetch_data(n):
    print(f"Fetching {n}...")
    await asyncio.sleep(1)  # Non-blocking sleep
    return f"Data {n}"

# await: wait for coroutine
async def main():
    result = await fetch_data(1)
    print(result)

# Run coroutine
asyncio.run(main())

# Concurrent execution with gather
async def main_concurrent():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print(results)  # ["Data 1", "Data 2", "Data 3"]

# Create tasks for concurrent execution
async def main_tasks():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    result2 = await task2

# Async context manager
class AsyncDatabase:
    async def __aenter__(self):
        print("Connecting...")
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, *args):
        print("Closing...")
        await asyncio.sleep(0.1)

async def use_db():
    async with AsyncDatabase() as db:
        print("Using database")

# Async iterator
class AsyncCounter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current < self.max:
            await asyncio.sleep(0.1)
            self.current += 1
            return self.current
        raise StopAsyncIteration

async def count():
    async for i in AsyncCounter(5):
        print(i)
```

**Answer:** "async def creates coroutine. await pauses until result ready. asyncio.run() runs coroutine. asyncio.gather() runs multiple concurrently. create_task() for background tasks. Use for I/O-bound operations (network, files). Not for CPU-bound (use multiprocessing). __aenter__/__aexit__ for async context managers."

---

#### Q53: What are itertools and common patterns?

**Complete Solution:**

```python
import itertools

# INFINITE ITERATORS

# count: infinite counter
for i in itertools.count(10, 2):  # Start 10, step 2
    if i > 20: break
    print(i)  # 10, 12, 14, 16, 18, 20

# cycle: repeat infinitely
counter = 0
for item in itertools.cycle(["A", "B", "C"]):
    if counter >= 7: break
    print(item)  # A, B, C, A, B, C, A
    counter += 1

# repeat: repeat n times or infinitely
list(itertools.repeat("X", 3))  # ["X", "X", "X"]

# COMBINATORIC ITERATORS

# product: cartesian product
list(itertools.product([1, 2], ["a", "b"]))
# [(1, "a"), (1, "b"), (2, "a"), (2, "b")]

# permutations: all orderings
list(itertools.permutations([1, 2, 3], 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# combinations: unique subsets
list(itertools.combinations([1, 2, 3], 2))
# [(1,2), (1,3), (2,3)]

# combinations_with_replacement
list(itertools.combinations_with_replacement([1, 2], 2))
# [(1,1), (1,2), (2,2)]

# TERMINATING ITERATORS

# chain: concatenate iterables
list(itertools.chain([1, 2], [3, 4], [5]))
# [1, 2, 3, 4, 5]

# compress: filter by boolean mask
list(itertools.compress([1,2,3,4], [1,0,1,0]))
# [1, 3]

# dropwhile: drop until condition false
list(itertools.dropwhile(lambda x: x < 5, [1,4,6,3,8]))
# [6, 3, 8]

# takewhile: take while condition true
list(itertools.takewhile(lambda x: x < 5, [1,4,6,3,8]))
# [1, 4]

# groupby: group consecutive elements
data = [("A", 1), ("A", 2), ("B", 1), ("B", 2)]
for key, group in itertools.groupby(data, lambda x: x[0]):
    print(key, list(group))
# A [(A,1), (A,2)]
# B [(B,1), (B,2)]

# islice: slice iterator
list(itertools.islice(range(10), 2, 8, 2))
# [2, 4, 6]

# zip_longest: zip with fillvalue
list(itertools.zip_longest([1,2], ["a","b","c"], fillvalue=0))
# [(1,"a"), (2,"b"), (0,"c")]

# Practical patterns

# Pairwise iteration
def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

list(pairwise([1,2,3,4]))  # [(1,2), (2,3), (3,4)]

# Flatten nested list
nested = [[1, 2], [3, 4], [5]]
list(itertools.chain.from_iterable(nested))
# [1, 2, 3, 4, 5]
```

**Answer:** "itertools provides efficient iterators. Infinite: count, cycle, repeat. Combinatoric: product, permutations, combinations. Terminating: chain, compress, dropwhile, takewhile, groupby, islice, zip_longest. Memory efficient (lazy evaluation). Use for complex iteration patterns without loops."

---

#### Q54: What are design patterns in Python (Singleton, Factory, etc.)?

**Complete Solution:**

```python
# SINGLETON PATTERN - Single instance

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True

# Or using metaclass
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    pass

# FACTORY PATTERN - Create objects

class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        raise ValueError("Unknown animal")

animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # Woof!

# OBSERVER PATTERN - Event notification

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received: {message}")

subject = Subject()
subject.attach(Observer("A"))
subject.attach(Observer("B"))
subject.notify("Event occurred")

# DECORATOR PATTERN - Add functionality

class Coffee:
    def cost(self): return 5

class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 2

coffee = MilkDecorator(Coffee())
print(coffee.cost())  # 7

# STRATEGY PATTERN - Interchangeable algorithms

class SortStrategy:
    def sort(self, data): pass

class QuickSort(SortStrategy):
    def sort(self, data):
        return sorted(data)  # Simplified

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)
```

**Answer:** "Common patterns: Singleton (__new__ or metaclass for single instance), Factory (create objects), Observer (event notification), Decorator (add functionality), Strategy (interchangeable algorithms). Python features often replace patterns: decorators, first-class functions, duck typing. Use patterns for structure and maintainability."

---

#### Q55: What is the difference between threading and multiprocessing?

**Complete Solution:**

```python
import threading
import multiprocessing
import time

# THREADING - Multiple threads, shared memory, GIL affects CPU-bound

def cpu_task():
    count = 0
    for i in range(10000000):
        count += i
    return count

# Threading (not faster for CPU-bound due to GIL)
start = time.time()
threads = [threading.Thread(target=cpu_task) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Threading: {time.time() - start:.2f}s")  # ~10s

# Multiprocessing (faster for CPU-bound, separate processes)
start = time.time()
processes = [multiprocessing.Process(target=cpu_task) for _ in range(4)]
for p in processes: p.start()
for p in processes: p.join()
print(f"Multiprocessing: {time.time() - start:.2f}s")  # ~2.5s

# I/O-bound task (threading works well)
import requests

def io_task(url):
    requests.get(url)

# Threading good for I/O
urls = ["https://example.com"] * 10
threads = [threading.Thread(target=io_task, args=(url,)) for url in urls]
for t in threads: t.start()
for t in threads: t.join()

# Thread-safe operations
from threading import Lock

counter = 0
lock = Lock()

def increment():
    global counter
    with lock:
        counter += 1

# Process communication
from multiprocessing import Queue

def worker(queue):
    queue.put("Result")

queue = Queue()
p = multiprocessing.Process(target=worker, args=(queue,))
p.start()
result = queue.get()
p.join()

# concurrent.futures - High-level interface
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Thread pool for I/O
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(io_task, urls)

# Process pool for CPU
with ProcessPoolExecutor(max_workers=4) as executor:
    results = executor.map(cpu_task, range(4))

# Comparison table:
# Threading: Shared memory, lighter, GIL limitation, I/O-bound
# Multiprocessing: Separate memory, heavier, no GIL, CPU-bound
```

**Answer:** "Threading: shared memory, lighter, GIL limits CPU-bound, good for I/O. Multiprocessing: separate memory, heavier, no GIL, good for CPU-bound. Use threading for I/O (network, files), multiprocessing for CPU (computation). concurrent.futures provides high-level interface. Lock for thread safety, Queue for process communication."

---

#### Q56: What are context managers and how do you create custom ones?

**Complete Solution:**

```python
# Context manager: Setup and teardown using with statement

# Method 1: Class with __enter__ and __exit__
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return True to suppress exception
        return False

with FileManager("test.txt", "w") as f:
    f.write("Hello")
# File automatically closed

# Method 2: contextlib.contextmanager decorator
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    try:
        yield f  # Provide resource
    finally:
        f.close()  # Cleanup

with file_manager("test.txt", "w") as f:
    f.write("Hello")

# Timer context manager
import time

@contextmanager
def timer(label):
    start = time.time()
    try:
        yield
    finally:
        print(f"{label}: {time.time() - start:.2f}s")

with timer("Operation"):
    time.sleep(1)
# Operation: 1.00s

# Database transaction
class DatabaseTransaction:
    def __enter__(self):
        self.conn = connect_to_db()
        self.conn.begin_transaction()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()

# Suppress exceptions
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("nonexistent.txt")  # No error

# Redirect stdout
from contextlib import redirect_stdout
import io

f = io.StringIO()
with redirect_stdout(f):
    print("Hello")
output = f.getvalue()  # "Hello\n"
```

**Answer:** "Context manager: __enter__ (setup) and __exit__ (cleanup). Create with class or @contextmanager decorator. Use for resource management (files, locks, transactions). with statement ensures cleanup. __exit__ parameters: exc_type, exc_val, exc_tb. Return True to suppress exceptions. contextlib provides utilities: suppress, redirect_stdout."

---

#### Q57: Explain functools (partial, lru_cache, wraps, etc.)

**Complete Solution:**

```python
from functools import partial, lru_cache, wraps, reduce, singledispatch

# PARTIAL - Fix some arguments
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(5))   # 125

# Practical use: callbacks
from functools import partial
import tkinter as tk

def button_click(button_id):
    print(f"Button {button_id} clicked")

# button1 = tk.Button(command=partial(button_click, 1))

# LRU_CACHE - Memoization (cache results)
@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # Fast! Cached results
print(fibonacci.cache_info())  # Cache statistics

# Clear cache
fibonacci.cache_clear()

# WRAPS - Preserve function metadata in decorators
def my_decorator(func):
    @wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Greet someone"""
    return f"Hello, {name}"

print(greet.__name__)  # "greet" (not "wrapper"!)
print(greet.__doc__)   # "Greet someone"

# REDUCE - Accumulate (already covered)
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15

# SINGLEDISPATCH - Function overloading
@singledispatch
def process(arg):
    print(f"Default: {arg}")

@process.register(int)
def _(arg):
    print(f"Integer: {arg * 2}")

@process.register(str)
def _(arg):
    print(f"String: {arg.upper()}")

@process.register(list)
def _(arg):
    print(f"List: {len(arg)} items")

process(5)         # Integer: 10
process("hello")   # String: HELLO
process([1, 2])    # List: 2 items

# TOTAL_ORDERING - Generate comparison methods
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade
    # __le__, __gt__, __ge__ automatically generated!

s1 = Student("Alice", 90)
s2 = Student("Bob", 85)
print(s1 > s2)  # True
```

**Answer:** "functools utilities: partial (fix arguments), lru_cache (memoization), wraps (preserve metadata), reduce (accumulate), singledispatch (function overloading), total_ordering (generate comparisons). Use lru_cache for expensive functions. Always use wraps in decorators. partial for callbacks. singledispatch for type-based dispatch."

---

#### Q58: What are collections (Counter, defaultdict, namedtuple, deque)?

**Complete Solution:**

```python
from collections import Counter, defaultdict, namedtuple, deque, OrderedDict

# COUNTER - Count elements
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print(counter)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
print(counter.most_common(2))  # [('apple', 3), ('banana', 2)]
print(counter['apple'])  # 3

# Counter operations
c1 = Counter(['a', 'b', 'c'])
c2 = Counter(['a', 'b', 'd'])
print(c1 + c2)  # Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1})
print(c1 - c2)  # Counter({'c': 1})

# DEFAULTDICT - Default value for missing keys
dd = defaultdict(int)  # Default: 0
dd['a'] += 1
print(dd['b'])  # 0 (not KeyError!)

# Group items
from collections import defaultdict
words = ["apple", "apricot", "banana", "avocado"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
print(dict(grouped))  # {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana']}

# NAMEDTUPLE - Lightweight class
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # 10 20
print(p[0], p[1])  # 10 20 (still a tuple!)

# vs regular tuple
regular = (10, 20)  # Less readable
named = Point(10, 20)  # More readable

# Convert dict to namedtuple
data = {'x': 10, 'y': 20}
p = Point(**data)

# DEQUE - Double-ended queue (fast append/pop both ends)
dq = deque([1, 2, 3])
dq.append(4)        # Add right: [1, 2, 3, 4]
dq.appendleft(0)    # Add left: [0, 1, 2, 3, 4]
dq.pop()            # Remove right: [0, 1, 2, 3]
dq.popleft()        # Remove left: [1, 2, 3]

# Rotating
dq.rotate(1)   # Rotate right: [3, 1, 2]
dq.rotate(-1)  # Rotate left: [1, 2, 3]

# Max length (circular buffer)
dq = deque(maxlen=3)
dq.extend([1, 2, 3, 4])  # [2, 3, 4] (1 dropped)

# ORDEREDDICT - Preserve insertion order (Python 3.7+: regular dict is ordered)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od.move_to_end('a')  # Move 'a' to end
print(list(od.keys()))  # ['b', 'c', 'a']

# CHAINMAP - Combine multiple dicts
from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print(chain['b'])  # 2 (from dict1, first match)
print(chain['c'])  # 4 (from dict2)
```

**Answer:** "collections module: Counter (count elements, most_common), defaultdict (default value for missing keys), namedtuple (lightweight immutable class), deque (fast append/pop both ends, rotate, maxlen), OrderedDict (preserve order, move_to_end), ChainMap (combine dicts). Use Counter for counting, defaultdict for grouping, namedtuple for data, deque for queues."

---

#### Q59: What are regular expressions (re module)?

**Complete Solution:**

```python
import re

# BASIC PATTERNS

# Match pattern
text = "My phone is 123-456-7890"
pattern = r'\d{3}-\d{3}-\d{4}'  # Raw string
match = re.search(pattern, text)
if match:
    print(match.group())  # 123-456-7890

# Find all matches
text = "Emails: user@example.com, admin@test.org"
pattern = r'\w+@\w+\.\w+'
emails = re.findall(pattern, text)
print(emails)  # ['user@example.com', 'admin@test.org']

# Replace
text = "Hello 123 World 456"
result = re.sub(r'\d+', 'X', text)
print(result)  # Hello X World X

# SPECIAL CHARACTERS
# .  - Any character except newline
# ^  - Start of string
# $  - End of string
# *  - 0 or more
# +  - 1 or more
# ?  - 0 or 1
# {n} - Exactly n times
# {n,m} - n to m times
# [] - Character set
# |  - OR
# () - Group
# \  - Escape

# CHARACTER CLASSES
# \d - Digit [0-9]
# \D - Non-digit
# \w - Word char [a-zA-Z0-9_]
# \W - Non-word char
# \s - Whitespace
# \S - Non-whitespace

# GROUPS AND CAPTURE
text = "John Doe, Jane Smith"
pattern = r'(\w+) (\w+)'
matches = re.findall(pattern, text)
print(matches)  # [('John', 'Doe'), ('Jane', 'Smith')]

# Named groups
pattern = r'(?P<first>\w+) (?P<last>\w+)'
match = re.search(pattern, "John Doe")
print(match.group('first'))  # John
print(match.group('last'))   # Doe

# COMPILE for reuse
pattern = re.compile(r'\d+')
print(pattern.findall("123 abc 456"))  # ['123', '456']

# FLAGS
# re.IGNORECASE (re.I) - Case insensitive
# re.MULTILINE (re.M)  - ^ and $ match line starts/ends
# re.DOTALL (re.S)     - . matches newline
# re.VERBOSE (re.X)    - Allow comments and whitespace

pattern = re.compile(r'hello', re.IGNORECASE)
print(pattern.search("HELLO"))  # Match!

# LOOKAHEAD/LOOKBEHIND
# (?=...) - Positive lookahead
# (?!...) - Negative lookahead
# (?<=...) - Positive lookbehind
# (?<!...) - Negative lookbehind

# Match number followed by 'px'
text = "width: 100px, height: 200"
matches = re.findall(r'\d+(?=px)', text)
print(matches)  # ['100']

# COMMON PATTERNS
email = r'^[\w.-]+@[\w.-]+\.\w+$'
url = r'https?://[\w.-]+\.\w+'
phone = r'\(\d{3}\) \d{3}-\d{4}'
ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

# SPLIT
text = "apple,banana;cherry:date"
parts = re.split(r'[,;:]', text)
print(parts)  # ['apple', 'banana', 'cherry', 'date']

# Validate email
def is_valid_email(email):
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return bool(re.match(pattern, email))
```

**Answer:** "re module for regex: search (find first), findall (find all), sub (replace), match (start of string), compile (reuse pattern). Special chars: . (any), ^ (start), $ (end), * (0+), + (1+), ? (0/1). Classes: \d (digit), \w (word), \s (space). Groups: () capture, (?P<name>) named. Flags: IGNORECASE, MULTILINE, DOTALL. Use for validation, extraction, replacement."

---

#### Q60: What are dataclasses (Python 3.7+)?

**Complete Solution:**

```python
from dataclasses import dataclass, field, asdict, astuple
from typing import List

# BASIC DATACLASS - Auto __init__, __repr__, __eq__
@dataclass
class Person:
    name: str
    age: int
    city: str = "Unknown"  # Default value

p = Person("Alice", 30)
print(p)  # Person(name='Alice', age=30, city='Unknown')
print(p.name)  # Alice

# Comparison (auto __eq__)
p2 = Person("Alice", 30)
print(p == p2)  # True

# WITH ORDER - Enable <, >, <=, >=
@dataclass(order=True)
class Student:
    name: str
    grade: int

s1 = Student("Alice", 90)
s2 = Student("Bob", 85)
print(s1 > s2)  # True (compares by grade)

# FROZEN - Immutable
@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(10, 20)
# p.x = 15  # FrozenInstanceError!

# FIELD with default_factory
@dataclass
class Team:
    name: str
    members: List[str] = field(default_factory=list)
    # Don't use: members: List[str] = []  # Shared across instances!

team1 = Team("Team A")
team2 = Team("Team B")
team1.members.append("Alice")
print(team2.members)  # [] (separate list)

# POST_INIT - Custom initialization
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)  # Not in __init__

    def __post_init__(self):
        self.area = self.width * self.height

r = Rectangle(10, 20)
print(r.area)  # 200

# EXCLUDE from repr
@dataclass
class User:
    name: str
    password: str = field(repr=False)  # Hidden in repr

u = User("alice", "secret")
print(u)  # User(name='alice')

# EXCLUDE from comparison
@dataclass
class Product:
    name: str
    price: float
    stock: int = field(compare=False)  # Not used in ==

# CONVERT to dict/tuple
@dataclass
class Book:
    title: str
    pages: int

book = Book("Python", 300)
print(asdict(book))   # {'title': 'Python', 'pages': 300}
print(astuple(book))  # ('Python', 300)

# REPLACE - Create copy with changes
from dataclasses import replace
book2 = replace(book, pages=400)
print(book2)  # Book(title='Python', pages=400)

# SLOTS for memory efficiency (Python 3.10+)
@dataclass(slots=True)
class Point3D:
    x: int
    y: int
    z: int

# Inheritance
@dataclass
class Animal:
    name: str
    age: int

@dataclass
class Dog(Animal):
    breed: str

dog = Dog("Buddy", 5, "Labrador")
print(dog)  # Dog(name='Buddy', age=5, breed='Labrador')

# vs Regular class
# Regular (verbose):
class PersonOld:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"PersonOld(name={self.name!r}, age={self.age!r})"

    def __eq__(self, other):
        return (self.name, self.age) == (other.name, other.age)

# Dataclass (concise):
@dataclass
class PersonNew:
    name: str
    age: int
```

**Answer:** "dataclass decorator: auto generates __init__, __repr__, __eq__. Use @dataclass for data-holding classes. Options: order=True (__lt__, __gt__), frozen=True (immutable), slots=True (memory efficient). field(): default_factory (list, dict), init=False, repr=False, compare=False. __post_init__ for custom logic. asdict/astuple for conversion. replace() for copying. Simpler than regular classes."

---

#### Q61: How do you handle file I/O in Python?

**Complete Solution:**

```python
# READING FILES

# Method 1: with statement (recommended)
with open('file.txt', 'r') as f:
    content = f.read()  # Read entire file
# File automatically closed

# Read line by line (memory efficient)
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())

# Read all lines into list
with open('file.txt', 'r') as f:
    lines = f.readlines()  # List of lines

# Read specific number of bytes
with open('file.txt', 'r') as f:
    chunk = f.read(100)  # First 100 characters

# WRITING FILES

# Write mode (overwrite)
with open('file.txt', 'w') as f:
    f.write("Hello\n")
    f.writelines(["Line 1\n", "Line 2\n"])

# Append mode
with open('file.txt', 'a') as f:
    f.write("Appended line\n")

# BINARY FILES
# Read binary
with open('image.png', 'rb') as f:
    data = f.read()

# Write binary
with open('image.png', 'wb') as f:
    f.write(data)

# FILE MODES
# 'r'  - Read (default)
# 'w'  - Write (overwrite)
# 'a'  - Append
# 'x'  - Exclusive create (fails if exists)
# 'r+' - Read and write
# 'w+' - Write and read (overwrite)
# 'a+' - Append and read
# 'b'  - Binary mode (rb, wb, etc.)
# 't'  - Text mode (default)

# CHECK if file exists
import os
if os.path.exists('file.txt'):
    with open('file.txt', 'r') as f:
        content = f.read()

# PATHLIB (modern approach)
from pathlib import Path

path = Path('file.txt')
if path.exists():
    content = path.read_text()  # Read
    path.write_text("Hello")    # Write
    lines = path.read_text().splitlines()

# Binary with pathlib
data = path.read_bytes()
path.write_bytes(data)

# TEMPORARY FILES
import tempfile

# Temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
    f.write("Temporary data")
    temp_name = f.name

# Temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Created {temp_dir}")
    # Do work
# Automatically deleted

# FILE OPERATIONS
import os
import shutil

os.rename('old.txt', 'new.txt')  # Rename
os.remove('file.txt')  # Delete
shutil.copy('src.txt', 'dst.txt')  # Copy
shutil.move('src.txt', 'dst.txt')  # Move

# Directory operations
os.mkdir('newdir')  # Create directory
os.makedirs('path/to/dir', exist_ok=True)  # Create nested
os.listdir('.')  # List files
os.rmdir('emptydir')  # Remove empty directory
shutil.rmtree('nonemptydir')  # Remove directory tree

# ENCODING
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# CSV files
import csv

# Read CSV
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Write CSV
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerows([['Alice', 30], ['Bob', 25]])

# CSV with DictReader/DictWriter
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], row['Age'])
```

**Answer:** "File I/O: use with statement for auto-close. Modes: r (read), w (write), a (append), x (exclusive), b (binary). Methods: read(), readline(), readlines(), write(), writelines(). pathlib.Path modern approach: read_text(), write_text(), exists(). CSV: csv.reader/writer, DictReader/DictWriter. Always specify encoding. os/shutil for file operations."

---

#### Q62: How do you work with JSON data?

**Complete Solution:**

```python
import json

# SERIALIZE (Python -> JSON)

# Dict to JSON string
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "JavaScript"],
    "active": True,
    "score": None
}

json_string = json.dumps(data)
print(json_string)
# {"name": "Alice", "age": 30, "skills": ["Python", "JavaScript"], "active": true, "score": null}

# Pretty print
json_string = json.dumps(data, indent=4, sort_keys=True)
print(json_string)

# Write to file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# DESERIALIZE (JSON -> Python)

# JSON string to dict
json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)
print(data['name'])  # Alice

# Read from file
with open('data.json', 'r') as f:
    data = json.load(f)

# TYPE MAPPING
# Python -> JSON
# dict -> object
# list, tuple -> array
# str -> string
# int, float -> number
# True -> true
# False -> false
# None -> null

# JSON -> Python
# object -> dict
# array -> list
# string -> str
# number (int) -> int
# number (real) -> float
# true -> True
# false -> False
# null -> None

# CUSTOM OBJECTS

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Custom encoder
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {'name': obj.name, 'age': obj.age}
        return super().default(obj)

person = Person("Alice", 30)
json_string = json.dumps(person, cls=PersonEncoder)

# Or use default parameter
def person_to_dict(obj):
    if isinstance(obj, Person):
        return {'name': obj.name, 'age': obj.age}
    raise TypeError("Not serializable")

json_string = json.dumps(person, default=person_to_dict)

# Custom decoder
def dict_to_person(dct):
    if 'name' in dct and 'age' in dct:
        return Person(dct['name'], dct['age'])
    return dct

person = json.loads(json_string, object_hook=dict_to_person)

# DATETIME handling
from datetime import datetime

def datetime_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Not serializable")

data = {'timestamp': datetime.now()}
json_string = json.dumps(data, default=datetime_handler)

# VALIDATION with pydantic
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int
    email: str

try:
    user = User(name="Alice", age=30, email="alice@example.com")
    print(user.json())  # Serialize
    user2 = User.parse_raw('{"name":"Bob","age":25,"email":"bob@example.com"}')
except ValidationError as e:
    print(e)

# JSONL (JSON Lines) - One JSON per line
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]

# Write JSONL
with open('data.jsonl', 'w') as f:
    for item in data:
        f.write(json.dumps(item) + '\n')

# Read JSONL
with open('data.jsonl', 'r') as f:
    for line in f:
        item = json.loads(line)
        print(item)

# API response handling
import requests

response = requests.get('https://api.example.com/data')
data = response.json()  # Parse JSON response
```

**Answer:** "JSON module: dumps() (object to string), dump() (object to file), loads() (string to object), load() (file to object). Type mapping: dict↔object, list↔array, None↔null, True/False↔true/false. Custom encoding: JSONEncoder subclass or default parameter. Custom decoding: object_hook. indent for pretty print. Handle datetime with isoformat(). JSONL for streaming. pydantic for validation."

---

#### Q63: What is pickle and how to use it?

**Complete Solution:**

```python
import pickle

# PICKLE - Serialize Python objects to bytes

# SERIALIZE (pickling)
data = {
    'name': 'Alice',
    'scores': [90, 85, 92],
    'metadata': {'course': 'Python'}
}

# To bytes
pickled = pickle.dumps(data)
print(type(pickled))  # <class 'bytes'>

# To file
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# DESERIALIZE (unpickling)
# From bytes
data = pickle.loads(pickled)

# From file
with open('data.pkl', 'rb') as f:
    data = pickle.load(f)

# PICKLE PROTOCOLS
# 0 - ASCII (compatible, verbose)
# 1 - Binary (old)
# 2 - Binary (Python 2.3+)
# 3 - Binary (Python 3, default 3.0-3.7)
# 4 - Binary (Python 3.4+, default 3.8+)
# 5 - Binary (Python 3.8+, out-of-band data)

# Use highest protocol
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

# CUSTOM OBJECTS
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
pickled = pickle.dumps(person)
person_restored = pickle.loads(pickled)
print(person_restored.name)  # Alice

# CUSTOM PICKLE BEHAVIOR
class CustomClass:
    def __init__(self, data):
        self.data = data
        self.cache = None  # Don't pickle

    def __getstate__(self):
        # Return state to pickle (exclude cache)
        state = self.__dict__.copy()
        state['cache'] = None
        return state

    def __setstate__(self, state):
        # Restore state
        self.__dict__.update(state)
        self.cache = None  # Initialize

obj = CustomClass("data")
obj.cache = "computed"
restored = pickle.loads(pickle.dumps(obj))
print(restored.cache)  # None

# SECURITY WARNING
# Never unpickle untrusted data!
# Pickle can execute arbitrary code

# Safe alternative: JSON (if possible)
# Or use restricted unpickler

# LIMITATIONS
# - Python-specific (not portable)
# - Can't pickle: file handles, sockets, database connections
# - Lambda functions (use dill)
# - Functions defined in __main__

# Alternative: dill (extended pickle)
import dill

# Can pickle lambdas
f = lambda x: x ** 2
pickled = dill.dumps(f)
f_restored = dill.loads(pickled)
print(f_restored(5))  # 25

# SHELVE - Persistent dictionary
import shelve

# Write
with shelve.open('mydata') as db:
    db['key1'] = {'name': 'Alice'}
    db['key2'] = [1, 2, 3]

# Read
with shelve.open('mydata') as db:
    print(db['key1'])  # {'name': 'Alice'}

# When to use:
# Pickle: Python objects, caching, temporary storage
# JSON: Data exchange, configuration, web APIs
# Shelve: Simple persistent storage
# Database: Large datasets, queries, concurrency
```

**Answer:** "pickle serializes Python objects to bytes. dumps() to bytes, dump() to file. loads() from bytes, load() from file. Binary format, Python-specific. Protocols 0-5 (use HIGHEST_PROTOCOL). __getstate__/__setstate__ for custom behavior. WARNING: Never unpickle untrusted data (security risk). Can't pickle: file handles, lambdas (use dill), __main__ functions. Use JSON for portability, pickle for Python-only caching."

---

#### Q64: How do you work with dates and times?

**Complete Solution:**

```python
from datetime import datetime, date, time, timedelta, timezone
import time as time_module

# DATETIME - Date and time combined
now = datetime.now()  # Current local time
print(now)  # 2024-01-15 10:30:45.123456

utc_now = datetime.now(timezone.utc)  # UTC time
print(utc_now)

# Create specific datetime
dt = datetime(2024, 1, 15, 10, 30, 45)
print(dt)  # 2024-01-15 10:30:45

# DATE - Just date
today = date.today()
print(today)  # 2024-01-15

specific_date = date(2024, 1, 15)

# TIME - Just time
t = time(10, 30, 45)  # 10:30:45
print(t)

# TIMEDELTA - Duration
delta = timedelta(days=7, hours=2, minutes=30)
future = datetime.now() + delta
past = datetime.now() - timedelta(days=30)

# Date arithmetic
date1 = date(2024, 1, 15)
date2 = date(2024, 1, 10)
diff = date1 - date2
print(diff.days)  # 5

# FORMATTING (strftime)
dt = datetime(2024, 1, 15, 10, 30, 45)
formatted = dt.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # 2024-01-15 10:30:45

# Common format codes:
# %Y - Year (4 digits)
# %m - Month (01-12)
# %d - Day (01-31)
# %H - Hour 24h (00-23)
# %I - Hour 12h (01-12)
# %M - Minute (00-59)
# %S - Second (00-59)
# %p - AM/PM
# %a - Weekday short (Mon)
# %A - Weekday full (Monday)
# %b - Month short (Jan)
# %B - Month full (January)

formatted = dt.strftime("%A, %B %d, %Y at %I:%M %p")
print(formatted)  # Monday, January 15, 2024 at 10:30 AM

# PARSING (strptime)
date_string = "2024-01-15 10:30:45"
dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

# ISO FORMAT
dt = datetime.now()
iso_string = dt.isoformat()  # 2024-01-15T10:30:45.123456
dt_parsed = datetime.fromisoformat(iso_string)

# UNIX TIMESTAMP
timestamp = datetime.now().timestamp()  # Seconds since epoch
dt = datetime.fromtimestamp(timestamp)

# TIME MODULE - Lower level
import time
current_time = time.time()  # Unix timestamp
time.sleep(1)  # Sleep 1 second

# Measure execution time
start = time.time()
# ... code ...
end = time.time()
print(f"Elapsed: {end - start:.2f}s")

# Or use perf_counter (more accurate)
start = time.perf_counter()
# ... code ...
end = time.perf_counter()
print(f"Elapsed: {end - start:.2f}s")

# TIMEZONES
from datetime import timezone, tzinfo
import pytz  # Third-party, but recommended

# UTC
utc_time = datetime.now(timezone.utc)

# Specific timezone (pytz)
eastern = pytz.timezone('US/Eastern')
eastern_time = datetime.now(eastern)

# Convert timezone
utc_time = datetime.now(timezone.utc)
eastern_time = utc_time.astimezone(pytz.timezone('US/Eastern'))

# DATEUTIL - Flexible parsing
from dateutil import parser

# Parse various formats
dt = parser.parse("Jan 15, 2024")
dt = parser.parse("2024-01-15T10:30:45")
dt = parser.parse("15/01/2024", dayfirst=True)

# Relative deltas
from dateutil.relativedelta import relativedelta

# Add 1 month (handles month boundaries)
future = datetime.now() + relativedelta(months=1)
# Add 1 year
future = datetime.now() + relativedelta(years=1)

# COMMON PATTERNS

# Get age
def calculate_age(birth_date):
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

# Format time ago
def time_ago(dt):
    now = datetime.now()
    diff = now - dt
    seconds = diff.total_seconds()

    if seconds < 60:
        return f"{int(seconds)} seconds ago"
    elif seconds < 3600:
        return f"{int(seconds / 60)} minutes ago"
    elif seconds < 86400:
        return f"{int(seconds / 3600)} hours ago"
    else:
        return f"{int(seconds / 86400)} days ago"

# Business days
from datetime import timedelta

def add_business_days(start_date, days):
    current = start_date
    while days > 0:
        current += timedelta(days=1)
        if current.weekday() < 5:  # Monday-Friday
            days -= 1
    return current
```

**Answer:** "datetime module: datetime (date+time), date (date only), time (time only), timedelta (duration). now() current time, strftime() format, strptime() parse. ISO format: isoformat(), fromisoformat(). Timestamp: timestamp(), fromtimestamp(). time.time() for Unix timestamp, time.perf_counter() for precise timing. pytz for timezones. dateutil.parser for flexible parsing. relativedelta for month/year arithmetic. weekday() for day of week (0=Monday)."

---

#### Q65: What are type hints and mypy?

**Complete Solution:**

```python
from typing import List, Dict, Tuple, Optional, Union, Any, Callable, TypeVar, Generic

# BASIC TYPE HINTS (Python 3.5+)

def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

# VARIABLE ANNOTATIONS (Python 3.6+)
age: int = 30
name: str = "Alice"
scores: List[int] = [90, 85, 92]

# COLLECTION TYPES
def process_names(names: List[str]) -> Dict[str, int]:
    return {name: len(name) for name in names}

def get_coordinates() -> Tuple[float, float]:
    return (10.5, 20.3)

# OPTIONAL - Value or None
def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None  # OK

# UNION - Multiple possible types
def process_data(data: Union[int, str]) -> str:
    return str(data)

# Python 3.10+ - Use | instead of Union
def process_data_new(data: int | str) -> str:
    return str(data)

# ANY - Any type (defeats purpose of type hints)
def process_anything(data: Any) -> Any:
    return data

# CALLABLE - Function type
def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def add(x: int, y: int) -> int:
    return x + y

result = apply_function(add, 5, 3)

# GENERIC TYPES
T = TypeVar('T')

def first_element(items: List[T]) -> T:
    return items[0]

# Works with any type
num = first_element([1, 2, 3])  # T = int
name = first_element(["a", "b"])  # T = str

# Generic class
class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

stack: Stack[int] = Stack()
stack.push(1)
stack.push(2)

# LITERAL - Specific values (Python 3.8+)
from typing import Literal

def set_color(color: Literal["red", "green", "blue"]) -> None:
    print(color)

set_color("red")  # OK
# set_color("yellow")  # Type error

# TYPE ALIASES
UserId = int
UserDict = Dict[str, Union[str, int]]

def get_user(user_id: UserId) -> UserDict:
    return {"name": "Alice", "age": 30}

# PROTOCOL - Structural subtyping (Python 3.8+)
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(obj: Drawable) -> None:
    obj.draw()

# Any object with draw() method works
class Circle:
    def draw(self) -> None:
        print("Drawing circle")

render(Circle())  # OK (duck typing with type checking)

# MYPY - Static type checker

# Run mypy on file
# $ mypy script.py

# Type checking example
def add_numbers(a: int, b: int) -> int:
    return a + b

# add_numbers("1", "2")  # mypy error: Expected int, got str

# Ignore specific line
result = add_numbers("1", "2")  # type: ignore

# CONFIGURATION - mypy.ini or pyproject.toml
# [mypy]
# python_version = 3.10
# warn_return_any = True
# warn_unused_configs = True
# disallow_untyped_defs = True

# GRADUAL TYPING - Add types incrementally
# Without types
def old_function(a, b):
    return a + b

# With types
def new_function(a: int, b: int) -> int:
    return a + b

# TYPE GUARDS (Python 3.10+)
from typing import TypeGuard

def is_str_list(val: List[object]) -> TypeGuard[List[str]]:
    return all(isinstance(x, str) for x in val)

def process(items: List[object]) -> None:
    if is_str_list(items):
        # items is now List[str]
        print(items[0].upper())

# BEST PRACTICES
# 1. Start with function signatures
# 2. Use Optional for nullable values
# 3. Use type aliases for complex types
# 4. Protocol for duck typing
# 5. Generic for reusable code
# 6. Run mypy in CI/CD
# 7. Gradual adoption (don't type everything at once)

# TYPE STUBS - .pyi files for untyped libraries
# Create stub: library.pyi
# def function(x: int) -> str: ...
```

**Answer:** "Type hints (PEP 484): function annotations for static type checking. Basic: int, str, float, bool. Collections: List[T], Dict[K,V], Tuple[T,...], Set[T]. Optional[T] = T | None. Union[A,B] = A | B (or A | B in 3.10+). Callable[[Args], Return] for functions. TypeVar for generics. Protocol for structural typing. mypy static type checker. Benefits: catch errors early, better IDE support, documentation. Gradual typing: add incrementally."

---

#### Q66: What are enumerate and zip?

**Complete Solution:**

**Answer:** "enumerate(iterable, start=0): index and item. zip(*iterables): combine multiple iterables, stops at shortest. zip_longest: pads with fillvalue. Unzip: zip(*pairs). Use enumerate instead of range(len()). zip for parallel iteration."

---

#### Q67: What is the difference between sort() and sorted()?

**Complete Solution:**

**Answer:** "sort(): in-place, modifies list, returns None. sorted(): returns new list, works on any iterable. Both have reverse and key parameters. Use key for custom sorting. lambda or operator.itemgetter for keys. sorted() more versatile. sort() faster for large lists."

---

#### Q68: How do you debug Python code?

**Complete Solution:**

**Answer:** "Debugging: print/print(f"{var=}"), pdb.set_trace() or breakpoint(), logging module (DEBUG/INFO/WARNING/ERROR/CRITICAL), traceback.print_exc(), assertions. Profiling: cProfile, line_profiler, memory_profiler. IDE debuggers: VS Code, PyCharm. PDB commands: n (next), s (step), c (continue), p (print). Use logging over print in production."

---

#### Q69: What are Python's best practices and PEP 8?

**Complete Solution:**

```python
# PEP 8 - Style Guide

# NAMING CONVENTIONS
class MyClass:  # CapWords for classes
    pass

def my_function():  # lowercase_with_underscores for functions
    pass

MY_CONSTANT = 42  # UPPERCASE for constants
my_variable = 10  # lowercase for variables

# INDENTATION - 4 spaces (not tabs)
def function():
    if True:
        print("Correct indentation")

# LINE LENGTH - Max 79 characters (72 for docstrings)
result = some_function(
    argument1,
    argument2,
    argument3
)

# IMPORTS
# Order: standard library, third-party, local
import os
import sys

import numpy as np
import pandas as pd

from mypackage import mymodule

# One import per line
import os
import sys
# Not: import os, sys

# Avoid wildcard imports
# from module import *  # BAD

# WHITESPACE
# Yes:
spam(ham[1], {eggs: 2})
x = 1
y = 2

# No:
spam( ham[ 1 ], { eggs : 2 } )
x=1
y=2

# COMMENTS
# Good: Explain WHY, not WHAT
# Calculate compound interest (why)
result = principal * (1 + rate) ** time

# Bad: Obvious
# Multiply x by 2 (what code does)
x = x * 2

# DOCSTRINGS
def function(arg1, arg2):
    Triple-quote docstring

    Args:
        arg1: Description
        arg2: Description

    Returns:
        Description

    return arg1 + arg2

# PYTHONIC PATTERNS

# List comprehension (good)
squares = [x**2 for x in range(10)]

# Not:
squares = []
for x in range(10):
    squares.append(x**2)

# Context managers (good)
with open('file.txt') as f:
    data = f.read()

# enumerate instead of range(len())
for i, item in enumerate(items):
    print(i, item)

# EAFP over LBYL
# Good:
try:
    value = dict[key]
except KeyError:
    value = default

# Not:
if key in dict:
    value = dict[key]
else:
    value = default

# Use is for None
if value is None:
    pass

# Boolean evaluation
# Good:
if items:  # Check if non-empty
    pass

# Not:
if len(items) > 0:
    pass

# Tools: black (formatter), flake8 (linter), pylint, mypy
```

**Answer:** "PEP 8: Style guide. Naming: snake_case (functions/variables), CapWords (classes), UPPERCASE (constants). 4 spaces indentation. Max 79 chars. Import order: stdlib, third-party, local. Avoid wildcard imports. Docstrings for functions/classes. Pythonic: comprehensions, context managers, enumerate, EAFP, is for None. Tools: black, flake8, pylint, mypy."

---

#### Q70: How do you write unit tests with pytest/unittest?

**Complete Solution:**

```python
# UNITTEST - Built-in testing framework
import unittest

class TestMathOperations(unittest.TestCase):
    def setUp(self):
        # Runs before each test
        self.value = 10

    def tearDown(self):
        # Runs after each test
        pass

    def test_addition(self):
        self.assertEqual(2 + 2, 4)
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertIs(a, b)
        self.assertIsNone(value)
        self.assertIn(item, container)
        self.assertRaises(ValueError, function, args)

    def test_subtraction(self):
        result = 10 - 5
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

# PYTEST - Third-party (more Pythonic)
# pip install pytest

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_add_strings():
    assert add("Hello", " World") == "Hello World"

# FIXTURES - Setup/teardown
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_with_fixture(sample_data):
    assert len(sample_data) == 5
    assert sum(sample_data) == 15

# PARAMETRIZE - Multiple inputs
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

# EXCEPTION TESTING
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# MOCKING
from unittest.mock import Mock, patch, MagicMock

def test_with_mock():
    mock_obj = Mock()
    mock_obj.method.return_value = 42
    assert mock_obj.method() == 42
    mock_obj.method.assert_called_once()

# Patch external dependency
@patch('module.external_api')
def test_api_call(mock_api):
    mock_api.return_value = {'status': 'ok'}
    result = my_function()
    assert result == expected

# COVERAGE
# pytest --cov=mymodule tests/

# TEST ORGANIZATION
# project/
#   src/
#     module.py
#   tests/
#     test_module.py
#     conftest.py  # Shared fixtures

# RUN TESTS
# unittest: python -m unittest
# pytest: pytest
# pytest -v  # Verbose
# pytest -k test_name  # Run specific test
# pytest --pdb  # Drop to debugger on failure

# ASSERTIONS
assert condition
assert condition, "Error message"
assert a == b
assert a is b
assert a in container
assert callable(function)
```

**Answer:** "Testing: unittest (built-in) or pytest (recommended). unittest: TestCase class, setUp/tearDown, assertEqual/assertTrue/assertRaises. pytest: simple assert statements, fixtures for setup, @pytest.mark.parametrize for multiple inputs, pytest.raises for exceptions, Mock/patch for mocking. Coverage: pytest --cov. Organization: tests/ directory. Run: python -m unittest or pytest. pytest more Pythonic and concise."

---

#### Q71: What are virtual environments and how to use them?

**Complete Solution:**

```python
# Virtual environment: Isolated Python environment

# VENV (built-in Python 3.3+)

# Create virtual environment
# Windows:
python -m venv myenv

# Linux/Mac:
python3 -m venv myenv

# Activate
# Windows:
myenv\Scripts\activate

# Linux/Mac:
source myenv/bin/activate

# Deactivate
deactivate

# VIRTUALENV (third-party, more features)
pip install virtualenv
virtualenv myenv
# Or specify Python version:
virtualenv -p python3.10 myenv

# CONDA (Anaconda/Miniconda)
conda create -n myenv python=3.10
conda activate myenv
conda deactivate
conda env list  # List environments
conda env remove -n myenv  # Delete

# PIPENV (dependency management + venv)
pip install pipenv
pipenv install requests  # Creates Pipfile
pipenv install --dev pytest  # Dev dependency
pipenv shell  # Activate
pipenv run python script.py  # Run in env

# POETRY (modern dependency management)
pip install poetry
poetry new myproject
poetry add requests
poetry install
poetry shell

# WHY USE VIRTUAL ENVIRONMENTS?
# 1. Isolate dependencies per project
# 2. Avoid version conflicts
# 3. Reproducible environments
# 4. Clean system Python

# REQUIREMENTS.TXT
# Generate:
pip freeze > requirements.txt

# Install from:
pip install -r requirements.txt

# Better: use pip-tools
pip install pip-tools
# requirements.in (high-level):
# requests
# pandas>=1.0

# Compile:
pip-compile requirements.in
# Creates requirements.txt with pinned versions

# BEST PRACTICES
# 1. One venv per project
# 2. Keep in .gitignore
# 3. Use requirements.txt or Pipfile
# 4. Activate before pip install
# 5. Use Python version managers (pyenv)

# PYENV - Manage multiple Python versions
# Install Python versions:
pyenv install 3.10.0
pyenv install 3.11.0

# Set global Python:
pyenv global 3.10.0

# Set local (per directory):
pyenv local 3.11.0

# DOCKER - Ultimate isolation
# Dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

# Directory structure
# project/
#   venv/  (in .gitignore)
#   src/
#   tests/
#   requirements.txt
#   README.md
```

**Answer:** "Virtual environments: isolated Python installations. venv (built-in): python -m venv myenv, activate with Scripts\activate (Windows) or source bin/activate (Linux/Mac). virtualenv: more features. conda: Anaconda, manages Python versions too. pipenv/poetry: modern dependency management. requirements.txt: freeze/install dependencies. Use one venv per project. pyenv: manage Python versions. Docker: ultimate isolation."

---

#### Q72: What are common Python idioms and patterns?

**Complete Solution:**

```python
# SWAPPING VARIABLES
a, b = b, a

# TERNARY OPERATOR
value = true_val if condition else false_val

# MULTIPLE COMPARISONS
if 0 < x < 10:
    pass

# FOR-ELSE (runs if no break)
for item in items:
    if condition:
        break
else:
    print("No break occurred")

# DICT.GET with default
value = my_dict.get('key', 'default')

# DICT.SETDEFAULT
my_dict.setdefault('key', []).append('value')

# ENUMERATE instead of range(len())
for i, item in enumerate(items):
    print(i, item)

# ZIP for parallel iteration
for name, age in zip(names, ages):
    print(name, age)

# UNPACKING
first, *rest, last = [1, 2, 3, 4, 5]
# first=1, rest=[2,3,4], last=5

# DICT MERGE (Python 3.9+)
merged = dict1 | dict2

# WALRUS OPERATOR (Python 3.8+)
if (n := len(items)) > 10:
    print(f"{n} items")

# LIST/DICT/SET COMPREHENSION
squares = [x**2 for x in range(10)]
evens_dict = {x: x**2 for x in range(10) if x % 2 == 0}
unique = {x for x in items}

# GENERATOR EXPRESSION (memory efficient)
total = sum(x**2 for x in range(1000000))

# ANY/ALL
if any(x > 10 for x in numbers):
    pass
if all(x > 0 for x in numbers):
    pass

# WITH STATEMENT for resource management
with open('file.txt') as f:
    data = f.read()

# DEFAULTDICT for grouping
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[item.category].append(item)

# COUNTER for counting
from collections import Counter
counts = Counter(words)

# CHAIN for flattening
from itertools import chain
flattened = list(chain(*nested_list))

# NAMEDTUPLE for data
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

# DATACLASS (Python 3.7+)
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int

# PROPERTY for getters/setters
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

# CONTEXT MANAGER
from contextlib import contextmanager
@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start}")

# DECORATOR for functionality
def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    pass
            raise Exception("Failed after retries")
        return wrapper
    return decorator

# GENERATOR for lazy evaluation
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# FUNCTOOLS
from functools import lru_cache, partial
@lru_cache(maxsize=128)
def expensive_function(n):
    pass

# PATHLIB instead of os.path
from pathlib import Path
path = Path('folder') / 'file.txt'
if path.exists():
    content = path.read_text()
```

**Answer:** "Python idioms: swap (a,b=b,a), ternary (x if cond else y), chained comparison (0<x<10), for-else, dict.get, enumerate, zip, unpacking (*rest), walrus (:=), comprehensions, any/all, with statement, defaultdict, Counter, chain, namedtuple, dataclass, property, context manager, decorator, generator, lru_cache, pathlib. Write Pythonic code: readable, concise, idiomatic."

---

#### Q73: What is __all__ and how is it used?

**Complete Solution:**

```python
# __all__ - Define public API of module

# mymodule.py
def public_function():
    pass

def _private_function():  # Leading underscore convention
    pass

def __really_private():  # Name mangling
    pass

__all__ = ['public_function']  # Only this exported with *

# When someone does:
# from mymodule import *
# Only public_function is imported

# Without __all__:
# from mymodule import *
# Imports public_function, _private_function (not __really_private)

# PACKAGE __init__.py
# mypackage/__init__.py
from .module1 import func1
from .module2 import func2

__all__ = ['func1', 'func2']

# Now can do:
# from mypackage import *
# Gets func1, func2

# CHECK what's imported
import mymodule
print(dir(mymodule))  # All attributes
print(mymodule.__all__)  # Defined public API

# BEST PRACTICES
# 1. Define __all__ for public modules
# 2. Use leading _ for internal functions
# 3. Avoid import * in code (use in interactive)
# 4. Explicit imports better: from module import specific_func
```

**Answer:** "__all__: list of strings defining public API for from module import *. Only names in __all__ are imported with *. Without __all__, all non-underscore names imported. Use in modules and __init__.py. Leading underscore (_) convention for private, double underscore (__) for name mangling. Best practice: avoid import *, use explicit imports."

---

#### Q74: What are context variables (contextvars)?

**Complete Solution:**

```python
import contextvars
import asyncio

# Context variable - Thread-safe, async-safe state

# Create context variable
request_id = contextvars.ContextVar('request_id', default='unknown')

# Set value
request_id.set('req-123')

# Get value
current_id = request_id.get()  # 'req-123'

# USE CASE: Request tracking in async web app
async def handle_request(req_id):
    request_id.set(req_id)
    await process_request()

async def process_request():
    # Access request_id from any nested call
    print(f"Processing {request_id.get()}")

# CONTEXT ISOLATION
async def task1():
    request_id.set('task-1')
    await asyncio.sleep(0.1)
    print(request_id.get())  # Still 'task-1'

async def task2():
    request_id.set('task-2')
    await asyncio.sleep(0.1)
    print(request_id.get())  # Still 'task-2'

# Both tasks have separate contexts!

# vs THREADING LOCAL
import threading

# Thread local (doesn't work with async)
local_data = threading.local()
local_data.value = 'thread-1'

# Context vars work with both threads and async!

# PRACTICAL: Logging with request ID
import logging

class RequestIDFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id.get()
        return True

logging.basicConfig(
    format='%(request_id)s - %(message)s'
)
logger = logging.getLogger()
logger.addFilter(RequestIDFilter())

# MANUAL CONTEXT MANAGEMENT
ctx = contextvars.copy_context()
# Run function in context
ctx.run(function, args)

# When to use:
# - Async applications (web frameworks)
# - Request/transaction tracking
# - User context in multi-tenant apps
# - Any state that should be context-isolated
```

**Answer:** "contextvars: context-local state for async and threading. ContextVar('name', default=value) creates variable. set()/get() for values. Isolated per async task or thread. Use for request tracking, logging context, user sessions. Better than threading.local for async. Common in web frameworks (FastAPI, etc). Context isolation prevents cross-contamination in concurrent execution."

---

#### Q75: How do you handle command-line arguments?

**Complete Solution:**

```python
import sys
import argparse

# SYS.ARGV - Raw arguments
# python script.py arg1 arg2
print(sys.argv)  # ['script.py', 'arg1', 'arg2']

# Simple usage
if len(sys.argv) > 1:
    filename = sys.argv[1]

# ARGPARSE - Recommended for complex CLI
parser = argparse.ArgumentParser(
    description='Process some files',
    epilog='Example: python script.py file.txt'
)

# Positional argument
parser.add_argument('filename', help='Input file')

# Optional argument
parser.add_argument('--output', '-o', help='Output file')

# Flag (boolean)
parser.add_argument('--verbose', '-v', action='store_true')

# Argument with default
parser.add_argument('--count', type=int, default=10)

# Multiple values
parser.add_argument('--files', nargs='+', help='Multiple files')

# Choices
parser.add_argument('--format', choices=['json', 'xml', 'csv'])

# Required optional argument
parser.add_argument('--config', required=True)

# Parse arguments
args = parser.parse_args()

# Use arguments
print(args.filename)
print(args.output)
if args.verbose:
    print("Verbose mode")

# SUBCOMMANDS (like git)
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

# git clone
clone_parser = subparsers.add_parser('clone')
clone_parser.add_argument('repo')

# git commit
commit_parser = subparsers.add_parser('commit')
commit_parser.add_argument('-m', '--message')

args = parser.parse_args()
if args.command == 'clone':
    print(f"Cloning {args.repo}")
elif args.command == 'commit':
    print(f"Committing: {args.message}")

# CLICK - Third-party (cleaner API)
import click

@click.command()
@click.argument('filename')
@click.option('--count', default=1, help='Number of times')
@click.option('--verbose', '-v', is_flag=True)
def process(filename, count, verbose):
    Triple-quote docstring
    if verbose:
        click.echo(f"Processing {filename} {count} times")

if __name__ == '__main__':
    process()

# ENVIRONMENT VARIABLES
import os
config_file = os.getenv('CONFIG_FILE', 'default.conf')

# TYPER - Click + type hints
from typer import Typer
app = Typer()

@app.command()
def main(name: str, age: int = 0):
    print(f"Hello {name}, age {age}")

if __name__ == '__main__':
    app()

# DOCOPT - CLI from docstring
Usage: script.py [options] <filename>

Options:
  -h --help     Show help
  -v --verbose  Verbose mode
  --output FILE Output file

from docopt import docopt
args = docopt(__doc__)

# FIRE - Auto-generate CLI from functions
import fire

def hello(name, greeting='Hello'):
    return f'{greeting}, {name}!'

if __name__ == '__main__':
    fire.Fire(hello)

# python script.py Alice
# python script.py Alice --greeting=Hi
```

**Answer:** "CLI arguments: sys.argv (raw list), argparse (recommended built-in), click (clean decorator API), typer (type hints), docopt (from docstring), fire (auto-generate). argparse: add_argument() for positional/optional, action='store_true' for flags, type=int for conversion, nargs='+' for multiple, choices for validation, subparsers for commands. Environment vars: os.getenv(). Choose: argparse (standard), click/typer (nicer API)."

---

#### Q76: What are some performance optimization techniques?

**Complete Solution:**

```python
# 1. PROFILING - Find bottlenecks first!
import cProfile
cProfile.run('slow_function()')

# 2. LIST COMPREHENSIONS vs loops (faster)
# Fast:
squares = [x**2 for x in range(1000)]
# Slow:
squares = []
for x in range(1000):
    squares.append(x**2)

# 3. GENERATOR for large datasets
# Memory efficient:
def numbers():
    for i in range(1000000):
        yield i**2
# vs list (uses all memory):
numbers = [i**2 for i in range(1000000)]

# 4. LOCAL VARIABLES (faster than global)
def func():
    local_var = some_global  # Cache global in local
    for i in range(1000):
        result = local_var + i  # Faster access

# 5. BUILT-IN FUNCTIONS (C-optimized)
# Fast:
result = sum(numbers)
# Slow:
result = 0
for n in numbers:
    result += n

# 6. SET for membership testing
# Fast (O(1)):
if item in my_set:
    pass
# Slow (O(n)):
if item in my_list:
    pass

# 7. DICT for lookups vs repeated if/elif
# Fast:
action = actions_dict.get(key, default)
# Slow:
if key == 'a':
    action = action_a
elif key == 'b':
    action = action_b

# 8. JOIN strings (don't concatenate in loop)
# Fast:
result = ''.join(string_list)
# Slow:
result = ''
for s in string_list:
    result += s  # Creates new string each time!

# 9. CACHING with lru_cache
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 10. SLOTS for classes (memory)
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 11. NUMPY for numerical computation
import numpy as np
# Fast (vectorized):
result = np.array(data) ** 2
# Slow (loop):
result = [x**2 for x in data]

# 12. MULTIPROCESSING for CPU-bound
from multiprocessing import Pool
with Pool(4) as pool:
    results = pool.map(cpu_intensive_func, data)

# 13. ASYNC for I/O-bound
import asyncio
async def fetch_all():
    tasks = [fetch_data(url) for url in urls]
    return await asyncio.gather(*tasks)

# 14. AVOID repeated attribute lookup
# Fast:
append = lst.append
for item in items:
    append(item)
# Slow:
for item in items:
    lst.append(item)

# 15. USE APPROPRIATE DATA STRUCTURES
# List: ordered, indexed access
# Set: unique, fast membership
# Dict: key-value, fast lookup
# Deque: fast append/pop both ends
# Heap: priority queue

# 16. LAZY EVALUATION
# Don't compute until needed
data = (expensive_func(x) for x in items)  # Generator
# vs
data = [expensive_func(x) for x in items]  # Computes all

# 17. RELEASE THE GIL (use C extensions)
# NumPy, Pandas release GIL internally

# 18. PYPY for long-running programs
# JIT compiler, can be 4x faster

# 19. CYTHON for critical code
# Compile Python to C

# 20. MEASURE, don't guess!
import timeit
time = timeit.timeit('sum(range(100))', number=10000)
```

**Answer:** "Performance: 1) Profile first (cProfile), 2) List comprehensions over loops, 3) Generators for large data, 4) Local variables faster, 5) Built-ins (sum, max, min), 6) Set for membership O(1), 7) Dict for lookups, 8) ''.join() not +=, 9) lru_cache memoization, 10) __slots__ for memory, 11) NumPy for numerics, 12) Multiprocessing for CPU, 13) Async for I/O, 14) Cache attribute lookups, 15) Appropriate data structures, 16) Lazy evaluation, 17) C extensions, 18) PyPy JIT, 19) Cython, 20) Measure!"

---

### Q77. How does Python manage memory?

```python
# Python Memory Management

# 1. Private Heap Space - All Python objects stored in private heap
import sys

x = [1, 2, 3]
print(f"Reference count: {sys.getrefcount(x)}")  # 2

y = x  # Increase reference count
print(f"Reference count: {sys.getrefcount(x)}")  # 3

# 2. Garbage Collection (for cyclic references)
import gc

class Node:
    def __init__(self):
        self.ref = None

a = Node()
b = Node()
a.ref = b
b.ref = a  # Circular reference

gc.collect()  # Manual garbage collection
print(f"GC stats: {gc.get_count()}")

# 3. Object Interning (optimization)
a = 256
b = 256
print(a is b)  # True (cached)

a = 257
b = 257
print(a is b)  # False (not cached)

# 4. Memory Profiling
from memory_profiler import profile

@profile
def memory_intensive():
    large_list = [i for i in range(1000000)]
    return sum(large_list)

# 5. Weak References
import weakref

class ExpensiveObject:
    def __del__(self):
        print("Deleted")

obj = ExpensiveObject()
weak_ref = weakref.ref(obj)
print(weak_ref())  # Access object
del obj
print(weak_ref())  # None

# 6. Best Practices
# - Use generators for large datasets
# - Delete large objects explicitly
# - Use __slots__ to reduce memory
# - Avoid circular references
# - Profile memory usage
```

**Answer:** Python uses reference counting for immediate deallocation, garbage collection for cyclic references, memory pools for small objects, and object interning for optimization.

---

### Q78. What is the Global Interpreter Lock (GIL)?

```python
# Global Interpreter Lock (GIL)

# 1. What is GIL?
# Mutex that prevents multiple threads from executing Python bytecode simultaneously
# Only one thread can execute Python code at a time

import threading
import time

# CPU-bound task (limited by GIL)
def cpu_bound(n):
    return sum(i ** 2 for i in range(n))

# Single-threaded
start = time.time()
cpu_bound(10000000)
cpu_bound(10000000)
single_time = time.time() - start
print(f"Single: {single_time:.2f}s")

# Multi-threaded (no benefit due to GIL)
start = time.time()
t1 = threading.Thread(target=cpu_bound, args=(10000000,))
t2 = threading.Thread(target=cpu_bound, args=(10000000,))
t1.start()
t2.start()
t1.join()
t2.join()
multi_time = time.time() - start
print(f"Multi: {multi_time:.2f}s")  # Similar or slower!

# 2. I/O-bound tasks (GIL released during I/O)
def io_bound(url):
    import requests
    return requests.get(url)

# Multi-threading benefits I/O tasks

# 3. Workarounds for CPU-bound Tasks
from multiprocessing import Pool

def parallel_cpu():
    with Pool(2) as pool:
        results = pool.map(cpu_bound, [10000000, 10000000])
    return results

# 4. Check GIL switch interval
import sys
print(f"Switch interval: {sys.getswitchinterval()}")

# 5. Best Practices
# - Use multiprocessing for CPU-bound tasks
# - Use threading for I/O-bound tasks
# - Use async/await for concurrent I/O
# - Leverage C extensions that release GIL
```

**Answer:** The GIL is a mutex in CPython that allows only one thread to execute Python bytecode at a time, making threading ineffective for CPU-bound tasks but acceptable for I/O-bound operations.

---

### Q79. How do you identify and prevent memory leaks in Python?

```python
# Memory Leaks in Python

# 1. Common Causes

# A. Unclosed Resources
# BAD
file = open('data.txt')
# file never closed

# GOOD
with open('data.txt') as file:
    data = file.read()

# B. Global Variables
cache = {}
def add_to_cache(key, large_data):
    cache[key] = large_data  # Grows indefinitely

# 2. Detection Tools

# A. tracemalloc (built-in)
import tracemalloc

tracemalloc.start()
large_list = [i for i in range(1000000)]
snapshot1 = tracemalloc.take_snapshot()

another_list = [i for i in range(2000000)]
snapshot2 = tracemalloc.take_snapshot()

top_stats = snapshot2.compare_to(snapshot1, 'lineno')
for stat in top_stats[:10]:
    print(stat)

tracemalloc.stop()

# B. memory_profiler
from memory_profiler import profile

@profile
def memory_hog():
    data = [0] * (10 ** 6)
    del data
    return True

# C. objgraph
import objgraph
objgraph.show_most_common_types()
objgraph.show_growth()

# 3. Prevention Strategies

# A. Use Context Managers
class DatabaseConnection:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

# B. Weak References
import weakref

class Cache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def add(self, key, obj):
        self._cache[key] = obj

# C. Limit Cache Size
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(n):
    return n ** 2

# D. Use Generators
def get_records():
    for record in database:
        yield record

# 4. Monitoring
import psutil
import os

def monitor_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    print(f"RSS: {mem_info.rss / 1024 / 1024:.2f} MB")
```

**Answer:** Use tracemalloc, memory_profiler, and objgraph to detect leaks; prevent them with context managers, weak references, explicit cleanup, and generators.

---

### Q80. Explain metaclasses and provide advanced examples

```python
# Metaclasses Deep Dive

# 1. What is a Metaclass?
# A class of a class - classes are instances of metaclasses

class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
print(isinstance(MyClass, type))  # True

# 2. Creating Classes Dynamically
DynamicClass = type('DynamicClass', (), {'x': 5})
obj = DynamicClass()
print(obj.x)  # 5

# 3. Custom Metaclass
class Meta(type):
    def __new__(mcs, name, bases, attrs):
        print(f"Creating class {name}")
        attrs['created_by'] = 'Meta'
        return super().__new__(mcs, name, bases, attrs)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(obj.created_by)  # Meta

# 4. Singleton Pattern
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        print("Connecting")

db1 = Database()
db2 = Database()
print(db1 is db2)  # True

# 5. Automatic Registration
class RegisterMeta(type):
    registry = {}

    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if name != 'Plugin':
            mcs.registry[name] = cls
        return cls

class Plugin(metaclass=RegisterMeta):
    pass

class AudioPlugin(Plugin):
    pass

print(RegisterMeta.registry)

# 6. Method Timing
import time

class TimedMeta(type):
    def __new__(mcs, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value) and not key.startswith('_'):
                attrs[key] = mcs.time_method(value)
        return super().__new__(mcs, name, bases, attrs)

    @staticmethod
    def time_method(method):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = method(*args, **kwargs)
            print(f"{method.__name__} took {time.time() - start:.4f}s")
            return result
        return wrapper

# 7. Alternative: __init_subclass__ (Python 3.6+)
class AutoRegister:
    registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.registry.append(cls)

class Plugin1(AutoRegister):
    pass

print(AutoRegister.registry)
```

**Answer:** Metaclasses are classes of classes that control class creation; use them for frameworks, auto-registration, validation, and patterns like Singleton, but prefer simpler alternatives when possible.

---

### Q81. What are descriptors and how do you implement them?

```python
# Descriptors in Python

# 1. What is a Descriptor?
# Object defining __get__, __set__, or __delete__

class Descriptor:
    def __get__(self, obj, objtype=None):
        return "Getting"

    def __set__(self, obj, value):
        print(f"Setting to {value}")

class MyClass:
    attr = Descriptor()

obj = MyClass()
print(obj.attr)  # Getting
obj.attr = 42    # Setting to 42

# 2. Typed Attribute
class TypedProperty:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be {self.expected_type}")
        obj.__dict__[self.name] = value

class Person:
    name = TypedProperty('name', str)
    age = TypedProperty('age', int)

p = Person()
p.name = "Alice"
p.age = 30

# 3. Validated Descriptor
class ValidatedDescriptor:
    def __init__(self, name, **validators):
        self.name = name
        self.validators = validators

    def __set__(self, obj, value):
        if 'min' in self.validators and value < self.validators['min']:
            raise ValueError(f"{self.name} must be >= {self.validators['min']}")
        obj.__dict__[self.name] = value

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

class Product:
    price = ValidatedDescriptor('price', min=0)

# 4. Lazy Property
class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.name, value)
        return value

class DataLoader:
    @LazyProperty
    def expensive_data(self):
        print("Loading...")
        return [i for i in range(1000000)]

# 5. __set_name__ (Python 3.6+)
class AutoNameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value
```

**Answer:** Descriptors are objects defining __get__, __set__, or __delete__ that manage attribute access; used for type checking, validation, lazy evaluation, and implementing property, staticmethod, and classmethod.

---

### Q82. Explain Python's import system in detail

```python
# Python Import System

# 1. Import Basics
import math
from math import sqrt
import math as m
from math import sqrt as sq

# 2. Import Search Path
import sys
print(sys.path)  # Directories Python searches
sys.path.append('/custom/path')

# 3. Module Import Process
# Step 1: Check sys.modules cache
print(sys.modules.get('math'))

# Step 2: Find module
# Step 3: Load module
# Step 4: Cache in sys.modules

# 4. Package Structure
# mypackage/
#     __init__.py
#     module1.py
#     subpackage/
#         __init__.py

# 5. Relative vs Absolute Imports
# Absolute
from mypackage.module1 import func

# Relative (inside package)
from . import module1
from .. import parent_module
from .subpackage import module3

# 6. importlib (Dynamic Imports)
import importlib

module = importlib.import_module('json')
importlib.reload(module)  # Reload

# Import from path
spec = importlib.util.spec_from_file_location("name", "/path/to/file.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# 7. Circular Imports Solution
# Import inside function
def func_a():
    import module_b
    module_b.func_b()

# 8. __all__ Export List
__all__ = ['public_func', 'PublicClass']

def public_func():
    pass

def _private_func():
    pass

# 9. Module Attributes
print(__name__)     # Module name
print(__file__)     # File path
print(__package__)  # Package name

# 10. Conditional Imports
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

# 11. Entry Point Pattern
if __name__ == '__main__':
    main()

# 12. Best Practices
# - Use absolute imports
# - Import at top
# - Group imports (stdlib, third-party, local)
# - Avoid wildcard imports
# - Use __all__ for public API
# - Handle ImportError
```

**Answer:** Python's import system searches sys.path, caches modules in sys.modules, executes module code once, and supports absolute/relative imports, packages with __init__.py, lazy imports with importlib, and import hooks for customization.

---

### Q83. What's the difference between coroutines and generators?

```python
# Coroutines vs Generators

# 1. Generators (Data Producers)
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))  # 1

# 2. Coroutines (Data Consumers)
def simple_coroutine():
    while True:
        value = yield
        print(f"Received: {value}")

coro = simple_coroutine()
next(coro)  # Prime
coro.send(10)

# 3. Generator-Based Coroutine
def averaging_coroutine():
    total = 0
    count = 0
    average = None
    while True:
        value = yield average
        total += value
        count += 1
        average = total / count

avg = averaging_coroutine()
next(avg)
print(avg.send(10))  # 10.0
print(avg.send(20))  # 15.0

# 4. Modern async/await
import asyncio

async def modern_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End")
    return 42

# 5. Key Differences
# Generators: yield values (iteration)
# Coroutines: receive values (processing)

# 6. Coroutine Decorator
def coroutine_decorator(func):
    def wrapper(*args, **kwargs):
        coro = func(*args, **kwargs)
        next(coro)  # Auto-prime
        return coro
    return wrapper

@coroutine_decorator
def auto_primed():
    while True:
        value = yield
        print(f"Got: {value}")

# 7. yield from
def delegator():
    yield from range(5)

# 8. async generators
async def async_generator():
    for i in range(5):
        await asyncio.sleep(0.1)
        yield i

# 9. Coroutine States
import inspect

def stateful():
    value = yield

coro = stateful()
print(inspect.getgeneratorstate(coro))  # GEN_CREATED

# 10. Use Cases
# Generators: lazy evaluation, iteration
# Coroutines: async I/O, event-driven programming
```

**Answer:** Generators yield values for iteration (pull-based), while coroutines receive values via send() and handle data processing (push-based); modern Python uses async/await for coroutines instead of generator-based coroutines.

---

### Q84. How do you create and distribute a Python package?

```python
# Creating and Distributing Python Packages

# 1. Basic pyproject.toml
# [build-system]
# requires = ["setuptools>=61.0"]
# build-backend = "setuptools.build_meta"
#
# [project]
# name = "mypackage"
# version = "1.0.0"
# dependencies = ["requests>=2.25.0"]

# 2. Package Structure
# mypackage/
#     mypackage/
#         __init__.py
#         module1.py
#     tests/
#     setup.py
#     pyproject.toml
#     README.md

# 3. __init__.py
__version__ = '1.0.0'
__all__ = ['func1', 'Class1']

from .module1 import func1

# 4. Building
# pip install build
# python -m build

# 5. Uploading to PyPI
# pip install twine
# twine upload dist/*

# 6. Version Management (Semantic)
# MAJOR.MINOR.PATCH
# 1.0.0 -> 1.1.0 (new features)
# 1.1.0 -> 1.1.1 (bug fixes)

# 7. Entry Points
# [project.scripts]
# mycommand = "mypackage.cli:main"

def main():
    print("CLI tool")

# 8. Dependencies
# install_requires = ["requests>=2.25.0"]
# extras_require = {"dev": ["pytest"]}

# 9. Testing
# pytest tests/

# 10. Best Practices
# - Use semantic versioning
# - Include README
# - Write tests
# - Document APIs
# - Use type hints
# - Follow PEP 8
```

**Answer:** Create a package with pyproject.toml, use 'python -m build' to create distributions, test with 'pip install -e .', upload to PyPI with twine, and follow best practices for versioning, dependencies, testing, and documentation.

---

### Q85. Compare different concurrency models in Python

```python
# Python Concurrency Models

# 1. Threading (I/O-bound)
import threading
import time

def io_task(name):
    print(f"{name} starting")
    time.sleep(1)
    print(f"{name} done")

threads = [threading.Thread(target=io_task, args=(f"T-{i}",)) for i in range(3)]
for t in threads:
    t.start()
for t in threads:
    t.join()

# 2. Multiprocessing (CPU-bound)
from multiprocessing import Pool

def cpu_task(n):
    return sum(i * i for i in range(n))

with Pool(4) as pool:
    results = pool.map(cpu_task, [1000000, 2000000])

# 3. Async/Await (Concurrent I/O)
import asyncio

async def async_task(name):
    await asyncio.sleep(1)
    return f"{name} done"

async def main():
    results = await asyncio.gather(
        async_task("Task1"),
        async_task("Task2")
    )
    return results

# 4. concurrent.futures (High-level)
from concurrent.futures import ThreadPoolExecutor

def download(url):
    time.sleep(1)
    return f"Downloaded {url}"

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(download, f"url{i}") for i in range(3)]
    results = [f.result() for f in futures]

# 5. Comparison
# Threading: I/O-bound, GIL limited
# Multiprocessing: CPU-bound, no GIL
# Async: High-concurrency I/O
# concurrent.futures: High-level abstraction

# 6. Thread Synchronization
lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        counter += 1

# 7. Process Communication
from multiprocessing import Queue

def producer(q):
    for i in range(5):
        q.put(i)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(item)

# 8. When to Use
# Threading: I/O operations, UI
# Multiprocessing: CPU-intensive
# Async: Web servers, many connections
# futures: Simple parallelism
```

**Answer:** Use threading for I/O-bound tasks (GIL limits CPU parallelism), multiprocessing for CPU-bound tasks (separate processes bypass GIL), async/await for high-concurrency I/O, and concurrent.futures for high-level abstraction over both.

---

### Q86. What is duck typing and how does Python implement it?

```python
# Duck Typing in Python

# "If it walks like a duck and quacks like a duck, it's a duck"

# 1. Basic Duck Typing
class Duck:
    def quack(self):
        return "Quack!"

    def fly(self):
        return "Flying..."

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

    def fly(self):
        return "I'm flapping my arms!"

def make_it_quack(duck):
    # Doesn't check type, just behavior
    print(duck.quack())
    print(duck.fly())

duck = Duck()
person = Person()

make_it_quack(duck)    # Works
make_it_quack(person)  # Also works!

# 2. File-like Objects
class StringBuffer:
    def __init__(self):
        self.buffer = []

    def write(self, text):
        self.buffer.append(text)

    def getvalue(self):
        return ''.join(self.buffer)

def write_to_file(file_like):
    file_like.write("Hello ")
    file_like.write("World")

import io
string_io = io.StringIO()
custom_buffer = StringBuffer()

write_to_file(string_io)      # Standard file-like
write_to_file(custom_buffer)  # Custom file-like

# 3. Iterable Protocol
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

for num in Countdown(5):
    print(num)  # 5, 4, 3, 2, 1

# 4. Context Manager Protocol
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"Elapsed: {elapsed:.2f}s")
        return False

with Timer():
    import time
    time.sleep(1)

# 5. Callable Objects
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
print(double(5))  # 10

# 6. Sequence Protocol
class CustomList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

custom = CustomList([1, 2, 3])
print(len(custom))      # 3
print(custom[0])        # 1
custom[0] = 10
print(list(custom))     # [10, 2, 3]

# 7. EAFP vs LBYL
# EAFP: Easier to Ask for Forgiveness than Permission
try:
    value = my_dict[key]
except KeyError:
    value = None

# LBYL: Look Before You Leap (Not Pythonic)
if key in my_dict:
    value = my_dict[key]
else:
    value = None

# 8. Protocol vs ABC
from collections.abc import Iterable

# Duck typing (no inheritance needed)
class MyIterable:
    def __iter__(self):
        return iter([1, 2, 3])

obj = MyIterable()
print(isinstance(obj, Iterable))  # True (virtual subclass)

# 9. Structural Subtyping (typing.Protocol)
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...

class Circle:
    def draw(self) -> str:
        return "Drawing circle"

def render(shape: Drawable):
    print(shape.draw())

circle = Circle()
render(circle)  # Type checker accepts this

# 10. Best Practices
# - Design for interfaces, not implementations
# - Use EAFP over LBYL
# - Document expected behavior
# - Use Protocol for type hints
# - Avoid explicit type checks
# - Embrace polymorphism
```

**Answer:** Duck typing means checking behavior (methods/attributes) rather than type; Python implements it through protocols (__iter__, __len__, etc.) and EAFP (try/except) rather than LBYL (if/else type checking).

---

### Q87. Explain monkey patching with advanced examples

```python
# Monkey Patching in Python

# 1. Basic Monkey Patching
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(2, 3))  # 5

# Patch the method
def new_add(self, a, b):
    print("Adding...")
    return a + b

Calculator.add = new_add
print(calc.add(2, 3))  # Adding... 5

# 2. Patching Built-in Functions
import builtins

original_print = print

def custom_print(*args, **kwargs):
    original_print("[LOG]", *args, **kwargs)

builtins.print = custom_print
print("Hello")  # [LOG] Hello

# Restore
builtins.print = original_print

# 3. Patching Modules
import json

original_dumps = json.dumps

def logged_dumps(obj, **kwargs):
    print(f"Dumping: {type(obj)}")
    return original_dumps(obj, **kwargs)

json.dumps = logged_dumps
result = json.dumps({'key': 'value'})  # Dumping: <class 'dict'>

# 4. Adding New Methods
class Dog:
    def bark(self):
        return "Woof!"

def fetch(self, item):
    return f"Fetching {item}"

Dog.fetch = fetch
dog = Dog()
print(dog.fetch("ball"))  # Fetching ball

# 5. Instance-level Patching
class Person:
    def greet(self):
        return "Hello"

person1 = Person()
person2 = Person()

# Patch only person1
def custom_greet(self):
    return "Hi there!"

import types
person1.greet = types.MethodType(custom_greet, person1)

print(person1.greet())  # Hi there!
print(person2.greet())  # Hello

# 6. Context Manager for Patching
from unittest.mock import patch

class EmailService:
    def send(self, to, message):
        # Actually send email
        return f"Sent to {to}"

def send_notification(email, msg):
    service = EmailService()
    return service.send(email, msg)

# Temporary patch
with patch.object(EmailService, 'send', return_value='Mocked'):
    result = send_notification('test@example.com', 'Hello')
    print(result)  # Mocked

# Original behavior restored
service = EmailService()
print(service.send('real@example.com', 'Hi'))  # Sent to real@example.com

# 7. Decorator-based Patching
@patch('builtins.open', create=True)
def test_file_reading(mock_open):
    mock_open.return_value.__enter__.return_value.read.return_value = 'mocked data'

    with open('file.txt') as f:
        data = f.read()

    print(data)  # mocked data

# 8. Patching for Testing
from unittest.mock import MagicMock

class Database:
    def query(self, sql):
        # Real database query
        pass

def get_users():
    db = Database()
    return db.query("SELECT * FROM users")

# Test with mocked database
original_query = Database.query
Database.query = MagicMock(return_value=[{'id': 1, 'name': 'Alice'}])

users = get_users()
print(users)  # [{'id': 1, 'name': 'Alice'}]

Database.query = original_query

# 9. Patching Class Attributes
class Config:
    DEBUG = False
    DATABASE = 'production'

print(Config.DEBUG)  # False

Config.DEBUG = True
Config.DATABASE = 'test'

print(Config.DEBUG)  # True

# 10. Dangers and Best Practices
# Dangers:
# - Hard to debug
# - Breaks encapsulation
# - Version-dependent
# - Can cause unexpected behavior

# When to Use:
# - Testing (mocking dependencies)
# - Hotfixes (temporary)
# - Adding functionality to third-party code
# - Debugging

# Best Practices:
# - Prefer subclassing/composition
# - Use for testing primarily
# - Document patches clearly
# - Keep patches localized
# - Use context managers
# - Restore original behavior
# - Consider using dependency injection instead
```

**Answer:** Monkey patching is runtime modification of classes/modules by replacing methods/attributes; use unittest.mock for testing, context managers for safety, and prefer composition/dependency injection for production code.

---

### Q88. What are Python optimization techniques?

```python
# Python Optimization Techniques

# 1. Use Built-in Functions
# Slower
def sum_squares_slow(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

# Faster
def sum_squares_fast(n):
    return sum(i * i for i in range(n))

# 2. List Comprehensions vs Loops
import time

# Slower (loop)
start = time.time()
squares = []
for i in range(1000000):
    squares.append(i * i)
loop_time = time.time() - start

# Faster (comprehension)
start = time.time()
squares = [i * i for i in range(1000000)]
comp_time = time.time() - start

print(f"Loop: {loop_time:.4f}s, Comprehension: {comp_time:.4f}s")

# 3. Local Variables are Faster
# Slower (global lookup)
import math

def compute_slow(x):
    return math.sqrt(x) + math.pi

# Faster (local reference)
def compute_fast(x):
    sqrt = math.sqrt
    pi = math.pi
    return sqrt(x) + pi

# 4. String Concatenation
# Slower (repeated concatenation)
def concat_slow(items):
    result = ""
    for item in items:
        result += str(item)
    return result

# Faster (join)
def concat_fast(items):
    return ''.join(str(item) for item in items)

# 5. Use __slots__
# Without slots (more memory)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# With slots (less memory, faster)
class PointSlots:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

# 6. Generators for Memory
# Memory-heavy
def get_all_numbers():
    return [i for i in range(1000000)]

# Memory-efficient
def get_numbers():
    for i in range(1000000):
        yield i

# 7. Use Sets for Membership Testing
# Slower (list)
items_list = list(range(10000))
1000 in items_list  # O(n)

# Faster (set)
items_set = set(range(10000))
1000 in items_set  # O(1)

# 8. Cache Expensive Computations
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 9. Use Appropriate Data Structures
from collections import deque, defaultdict, Counter

# Deque for queue operations
queue = deque([1, 2, 3])
queue.append(4)      # O(1)
queue.popleft()      # O(1)

# defaultdict to avoid key checks
counts = defaultdict(int)
for item in items:
    counts[item] += 1  # No KeyError

# Counter for counting
from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])

# 10. Lazy Evaluation
# Eager (computes all)
data = [expensive_function(x) for x in range(1000)]

# Lazy (computes on demand)
data = (expensive_function(x) for x in range(1000))

# 11. Use NumPy for Numerical Operations
import numpy as np

# Slower (pure Python)
def python_sum(n):
    return sum(range(n))

# Faster (NumPy)
def numpy_sum(n):
    return np.arange(n).sum()

# 12. Avoid Global Variables
global_var = 10

def use_global():
    return global_var * 2  # Slower

def use_local(val):
    return val * 2  # Faster

# 13. Use map/filter for Simple Operations
# Slower
result = []
for i in range(1000):
    result.append(i * 2)

# Faster
result = list(map(lambda x: x * 2, range(1000)))

# 14. Profiling
import cProfile
import pstats

def profile_function():
    # Your code
    pass

cProfile.run('profile_function()', 'stats')
stats = pstats.Stats('stats')
stats.sort_stats('cumulative')
stats.print_stats(10)

# 15. timeit for Micro-benchmarks
import timeit

# Compare approaches
time1 = timeit.timeit('[i*2 for i in range(1000)]', number=10000)
time2 = timeit.timeit('list(map(lambda x: x*2, range(1000)))', number=10000)

# 16. Use C Extensions
# ctypes, Cython, or write extension modules

# 17. Multiprocessing for CPU-bound
from multiprocessing import Pool

def cpu_intensive(x):
    return sum(i*i for i in range(x))

with Pool(4) as pool:
    results = pool.map(cpu_intensive, [1000000] * 4)

# 18. Memory Profiling
from memory_profiler import profile

@profile
def memory_intensive():
    data = [i for i in range(1000000)]
    return sum(data)

# 19. Best Practices
# - Profile before optimizing
# - Optimize hotspots only
# - Use built-in functions
# - Choose right data structures
# - Avoid premature optimization
# - Measure improvements
# - Consider readability vs performance
```

**Answer:** Use built-in functions, list comprehensions, local variables, generators, __slots__, sets for membership, lru_cache, appropriate data structures, NumPy for numerics, and profile before optimizing.

---

### Q89. What are context variables and when should you use them?

```python
# Context Variables (contextvars)

# 1. Basic Usage
import contextvars

# Create context variable
request_id = contextvars.ContextVar('request_id', default='N/A')

def process_request():
    # Get current value
    current_id = request_id.get()
    print(f"Processing request: {current_id}")

# Set value
request_id.set('REQ-123')
process_request()  # Processing request: REQ-123

# 2. Context-local State
user_context = contextvars.ContextVar('user')

def get_current_user():
    return user_context.get(None)

def set_current_user(user):
    user_context.set(user)

# In different contexts
set_current_user({'name': 'Alice', 'id': 1})
print(get_current_user())  # {'name': 'Alice', 'id': 1}

# 3. Async Isolation
import asyncio

async def handle_request(request_id_value, user_name):
    # Each coroutine has isolated context
    request_id.set(request_id_value)
    user_context.set({'name': user_name})

    await asyncio.sleep(0.1)

    # Context preserved across await
    print(f"Request {request_id.get()} by {user_context.get()['name']}")

async def main():
    await asyncio.gather(
        handle_request('REQ-1', 'Alice'),
        handle_request('REQ-2', 'Bob'),
        handle_request('REQ-3', 'Charlie'),
    )

# asyncio.run(main())

# 4. Manual Context Management
ctx = contextvars.copy_context()

def in_context():
    print(f"Request: {request_id.get()}")

# Run in copied context
request_id.set('MAIN-REQ')
ctx.run(in_context)  # Uses context from copy time

# 5. Context Variable Token
request_id.set('REQ-ORIGINAL')

# Set returns token
token = request_id.set('REQ-NEW')
print(request_id.get())  # REQ-NEW

# Reset to previous value
request_id.reset(token)
print(request_id.get())  # REQ-ORIGINAL

# 6. Web Framework Pattern
class RequestContext:
    def __init__(self):
        self.request_id = contextvars.ContextVar('request_id')
        self.user = contextvars.ContextVar('user')
        self.session = contextvars.ContextVar('session')

    def setup(self, request_id, user, session):
        self.request_id.set(request_id)
        self.user.set(user)
        self.session.set(session)

    def get_request_id(self):
        return self.request_id.get()

    def get_user(self):
        return self.user.get()

# 7. Logging with Context
import logging

class ContextFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id.get('N/A')
        return True

logger = logging.getLogger(__name__)
logger.addFilter(ContextFilter())

def log_with_context(message):
    logger.info(message)  # Includes request_id

# 8. Thread vs Context Variables
import threading

# Thread-local (doesn't work with async)
thread_local = threading.local()

# Context variable (works with async)
context_var = contextvars.ContextVar('data')

# 9. Database Connection Per Request
db_connection = contextvars.ContextVar('db_connection')

async def get_db():
    conn = db_connection.get(None)
    if conn is None:
        # Create new connection
        conn = await create_connection()
        db_connection.set(conn)
    return conn

async def query_database():
    db = await get_db()
    # Use connection
    pass

# 10. Middleware Pattern
async def middleware(request):
    # Set context for this request
    request_id.set(request.headers.get('X-Request-ID'))
    user_context.set(request.user)

    try:
        response = await process(request)
        return response
    finally:
        # Cleanup if needed
        pass

# 11. Testing with Contexts
def test_with_context():
    # Save current context
    token = request_id.set('TEST-REQ')

    try:
        # Test code
        assert request_id.get() == 'TEST-REQ'
    finally:
        # Restore
        request_id.reset(token)

# 12. Best Practices
# - Use for request-scoped data in web apps
# - Prefer over thread-local in async code
# - One ContextVar per logical value
# - Always provide defaults
# - Document context requirements
# - Clean up in finally blocks
# - Use for logging context
# - Avoid overuse (not for all globals)
```

**Answer:** Context variables (contextvars) provide isolated state for async tasks and threads; use them for request-scoped data in web frameworks, logging context, and database connections in async code where thread-local storage fails.

---

### Q90. Explain advanced type hints in Python

```python
# Advanced Type Hints

# 1. Basic Types
def greet(name: str) -> str:
    return f"Hello, {name}"

age: int = 30
height: float = 5.9
is_active: bool = True

# 2. Collections
from typing import List, Dict, Set, Tuple

names: List[str] = ['Alice', 'Bob']
scores: Dict[str, int] = {'Alice': 95, 'Bob': 87}
unique_ids: Set[int] = {1, 2, 3}
coordinates: Tuple[float, float] = (10.5, 20.3)

# 3. Optional and Union
from typing import Optional, Union

def find_user(user_id: int) -> Optional[str]:
    # Returns str or None
    return "Alice" if user_id == 1 else None

def process(value: Union[int, str]) -> str:
    # Accepts int or str
    return str(value)

# 4. Callable
from typing import Callable

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

def add(x: int, y: int) -> int:
    return x + y

result = apply(add, 2, 3)

# 5. Generic Types
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

int_stack: Stack[int] = Stack()
int_stack.push(1)

# 6. Protocol (Structural Subtyping)
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...

class Circle:
    def draw(self) -> str:
        return "Circle"

def render(shape: Drawable) -> None:
    print(shape.draw())

# 7. Literal Types
from typing import Literal

def set_mode(mode: Literal['read', 'write', 'append']) -> None:
    print(f"Mode: {mode}")

set_mode('read')  # OK
# set_mode('delete')  # Type error

# 8. TypedDict
from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int
    email: str

user: UserDict = {
    'name': 'Alice',
    'age': 30,
    'email': 'alice@example.com'
}

# 9. NewType
from typing import NewType

UserId = NewType('UserId', int)

def get_user(user_id: UserId) -> str:
    return f"User {user_id}"

user_id = UserId(123)
get_user(user_id)  # OK
# get_user(123)  # Type error (static checker)

# 10. Type Aliases
from typing import List, Dict

Vector = List[float]
Matrix = List[Vector]
JsonDict = Dict[str, any]

def process_matrix(m: Matrix) -> Vector:
    return m[0]

# 11. Overload
from typing import overload

@overload
def process(x: int) -> int: ...

@overload
def process(x: str) -> str: ...

def process(x: Union[int, str]) -> Union[int, str]:
    if isinstance(x, int):
        return x * 2
    return x.upper()

# 12. ParamSpec and Concatenate (Python 3.10+)
from typing import ParamSpec, Concatenate

P = ParamSpec('P')

def add_logging(f: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"Calling {f.__name__}")
        return f(*args, **kwargs)
    return wrapper

# 13. Self Type (Python 3.11+)
from typing import Self

class Builder:
    def set_name(self, name: str) -> Self:
        self.name = name
        return self

    def set_age(self, age: int) -> Self:
        self.age = age
        return self

# 14. Type Guards
from typing import TypeGuard

def is_str_list(val: List[object]) -> TypeGuard[List[str]]:
    return all(isinstance(x, str) for x in val)

def process_strings(items: List[object]) -> None:
    if is_str_list(items):
        # Type narrowed to List[str]
        print([s.upper() for s in items])

# 15. Final
from typing import Final

MAX_SIZE: Final = 100
# MAX_SIZE = 200  # Error (static)

class Base:
    def method(self) -> None:
        pass

from typing import final

class Child(Base):
    @final
    def method(self) -> None:
        pass

# 16. ClassVar
from typing import ClassVar

class Config:
    instances: ClassVar[int] = 0

    def __init__(self) -> None:
        Config.instances += 1

# 17. Type Checking
# Run: mypy script.py

# 18. Runtime Type Checking
from typing import get_type_hints

def validate(obj: any, cls: type) -> bool:
    hints = get_type_hints(cls.__init__)
    for field, field_type in hints.items():
        if field == 'return':
            continue
        if not isinstance(getattr(obj, field), field_type):
            return False
    return True

# 19. Best Practices
# - Use type hints for function signatures
# - Prefer specific types over generic
# - Use Optional for nullable values
# - Document with type hints
# - Run mypy in CI/CD
# - Use Protocol for duck typing
# - Keep types simple and readable
```

**Answer:** Python type hints include generics (TypeVar), protocols (structural subtyping), Literal types, TypedDict, overload, ParamSpec, Self, type guards, and Final; use mypy for static type checking.

---

### Q91. What are advanced async patterns in Python?

```python
# Advanced Async Patterns

# 1. Basic Async/Await
import asyncio

async def fetch_data(url):
    await asyncio.sleep(1)  # Simulate I/O
    return f"Data from {url}"

async def main():
    result = await fetch_data("https://api.example.com")
    print(result)

# 2. Concurrent Execution
async def fetch_all():
    # Run concurrently
    results = await asyncio.gather(
        fetch_data("url1"),
        fetch_data("url2"),
        fetch_data("url3"),
    )
    return results

# 3. Create Task
async def background_task():
    task1 = asyncio.create_task(fetch_data("url1"))
    task2 = asyncio.create_task(fetch_data("url2"))

    # Do other work
    await asyncio.sleep(0.5)

    # Wait for results
    result1 = await task1
    result2 = await task2
    return result1, result2

# 4. Timeout
async def with_timeout():
    try:
        result = await asyncio.wait_for(
            fetch_data("slow_url"),
            timeout=5.0
        )
    except asyncio.TimeoutError:
        print("Request timed out")

# 5. Semaphore (Limit Concurrency)
async def limited_concurrency():
    semaphore = asyncio.Semaphore(3)  # Max 3 concurrent

    async def fetch_with_limit(url):
        async with semaphore:
            return await fetch_data(url)

    urls = [f"url{i}" for i in range(10)]
    results = await asyncio.gather(*[fetch_with_limit(url) for url in urls])
    return results

# 6. Queue Pattern
async def producer_consumer():
    queue = asyncio.Queue()

    async def producer():
        for i in range(5):
            await queue.put(i)
            await asyncio.sleep(0.1)
        await queue.put(None)  # Sentinel

    async def consumer():
        while True:
            item = await queue.get()
            if item is None:
                break
            print(f"Consumed: {item}")
            queue.task_done()

    await asyncio.gather(producer(), consumer())

# 7. Async Context Manager
class AsyncResource:
    async def __aenter__(self):
        print("Acquiring resource")
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")
        await asyncio.sleep(0.1)
        return False

async def use_resource():
    async with AsyncResource() as resource:
        print("Using resource")

# 8. Async Iterator
class AsyncRange:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.current += 1
        return self.current - 1

async def iterate():
    async for i in AsyncRange(5):
        print(i)

# 9. Async Generator
async def async_generator():
    for i in range(5):
        await asyncio.sleep(0.1)
        yield i

async def consume_generator():
    async for value in async_generator():
        print(value)

# 10. Event Loop Management
async def run_in_executor():
    import concurrent.futures

    def cpu_bound(n):
        return sum(i*i for i in range(n))

    loop = asyncio.get_event_loop()

    # Run in thread pool
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound, 1000000)

    return result

# 11. Error Handling
async def handle_errors():
    tasks = [
        fetch_data("url1"),
        fetch_data("url2"),
        fetch_data("url3"),
    ]

    # return_exceptions=True prevents exception propagation
    results = await asyncio.gather(*tasks, return_exceptions=True)

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {i} failed: {result}")
        else:
            print(f"Task {i} succeeded: {result}")

# 12. Cancellation
async def cancellable_task():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("Task was cancelled")
        raise

async def cancel_example():
    task = asyncio.create_task(cancellable_task())
    await asyncio.sleep(1)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Caught cancellation")

# 13. Shield from Cancellation
async def critical_task():
    await asyncio.sleep(5)
    return "Important result"

async def shield_example():
    task = asyncio.create_task(critical_task())
    shielded = asyncio.shield(task)

    try:
        result = await asyncio.wait_for(shielded, timeout=1)
    except asyncio.TimeoutError:
        print("Timeout, but task continues")
        result = await task  # Task still running

    return result

# 14. Best Practices
# - Use gather for concurrent execution
# - Set timeouts for all I/O operations
# - Use semaphores to limit concurrency
# - Handle CancelledError properly
# - Use create_task for fire-and-forget
# - Prefer async libraries (aiohttp vs requests)
# - Avoid blocking calls in async code
# - Use run_in_executor for CPU-bound work
```

**Answer:** Advanced async patterns include gather/create_task for concurrency, semaphores for limiting, queues for producer-consumer, async context managers/iterators, error handling with return_exceptions, cancellation, and shielding critical tasks.

---

### Q92. What are effective Python debugging techniques?

```python
# Debugging Techniques

import pdb
import logging

# 1. Debugger
def buggy_function(x):
    pdb.set_trace()  # Breakpoint
    result = x * 2
    return result

# 2. Logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")

# 3. Assertions
def divide(a, b):
    assert b != 0, "Divisor cannot be zero"
    return a / b

# 4. Print debugging
def process(data):
    print(f"DEBUG: data = {data}")
    result = data * 2
    print(f"DEBUG: result = {result}")
    return result
```

**Answer:** Use pdb for interactive debugging, logging for production, assertions for invariants, print statements for quick checks, and IDE debuggers for complex scenarios.

---

### Q93. What are Python testing best practices?

```python
# Testing Best Practices

import pytest
from unittest.mock import Mock, patch

# 1. Unit Tests
def test_addition():
    assert 1 + 1 == 2

# 2. Fixtures
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_with_fixture(sample_data):
    assert len(sample_data) == 5

# 3. Parametrize
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert input * 2 == expected

# 4. Mocking
def test_with_mock():
    mock_db = Mock()
    mock_db.query.return_value = [{'id': 1}]

    result = mock_db.query("SELECT *")
    assert len(result) == 1

# 5. Coverage
# pytest --cov=mymodule tests/
```

**Answer:** Use pytest for testing, fixtures for setup, parametrize for multiple cases, mocking for dependencies, and coverage tools to ensure comprehensive test coverage.

---

### Q94. What Python code quality tools should you use?

```python
# Code Quality Tools

# 1. Black (formatting)
# black script.py

# 2. Flake8 (linting)
# flake8 script.py

# 3. Pylint (analysis)
# pylint script.py

# 4. Mypy (type checking)
# mypy script.py

# 5. isort (import sorting)
# isort script.py

# 6. pre-commit hooks
# .pre-commit-config.yaml
# - repo: https://github.com/psf/black
#   hooks:
#     - id: black
```

**Answer:** Use Black for formatting, Flake8/Pylint for linting, Mypy for type checking, isort for imports, and pre-commit hooks to enforce quality standards automatically.

---

### Q95. What are Python security best practices?

```python
# Security Best Practices

# 1. Never hardcode secrets
# BAD
API_KEY = "secret-key-123"

# GOOD
import os
API_KEY = os.environ.get('API_KEY')

# 2. SQL Injection Prevention
import sqlite3

# BAD
query = f"SELECT * FROM users WHERE id = {user_id}"

# GOOD
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# 3. Path Traversal Prevention
from pathlib import Path

def safe_join(directory, filename):
    base = Path(directory).resolve()
    target = (base / filename).resolve()

    if not str(target).startswith(str(base)):
        raise ValueError("Path traversal detected")

    return target

# 4. Input Validation
def validate_email(email):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
```

**Answer:** Never hardcode secrets, use parameterized queries to prevent SQL injection, validate inputs, prevent path traversal, use environment variables for sensitive data, and keep dependencies updated.

---

### Q96. How do you build REST APIs in Python?

```python
# REST API Development

from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. GET endpoint
@app.route('/api/users', methods=['GET'])
def get_users():
    users = [{'id': 1, 'name': 'Alice'}]
    return jsonify(users)

# 2. POST endpoint
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    # Validate and save
    return jsonify({'id': 1, 'name': data['name']}), 201

# 3. Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# 4. FastAPI (modern alternative)
from fastapi import FastAPI

api = FastAPI()

@api.get("/users")
async def get_users():
    return [{'id': 1, 'name': 'Alice'}]
```

**Answer:** Use Flask or FastAPI for building REST APIs, implement proper HTTP methods (GET, POST, PUT, DELETE), validate inputs, handle errors, use JSON for data exchange, and document with OpenAPI/Swagger.

---

### Q97. How do you work with databases in Python?

```python
# Database Operations

# 1. SQLite (built-in)
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT)''')

cursor.execute("INSERT INTO users (name) VALUES (?)", ('Alice',))
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# 2. SQLAlchemy (ORM)
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create
user = User(name='Bob')
session.add(user)
session.commit()

# Query
users = session.query(User).all()
```

**Answer:** Use sqlite3 for simple databases, SQLAlchemy ORM for complex applications, always use parameterized queries, implement connection pooling, handle transactions properly, and use context managers for connections.

---

### Q98. What are file operations best practices?

```python
# File Operations Best Practices

# 1. Context Managers
with open('file.txt', 'r') as f:
    content = f.read()

# 2. Pathlib (modern)
from pathlib import Path

path = Path('data/file.txt')
content = path.read_text()
path.write_text('New content')

# 3. JSON Files
import json

with open('data.json', 'r') as f:
    data = json.load(f)

with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)

# 4. CSV Files
import csv

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# 5. Binary Files
with open('image.png', 'rb') as f:
    data = f.read()
```

**Answer:** Always use context managers (with statement), prefer pathlib over os.path, use appropriate modes (r/w/a/b), handle encoding explicitly, use json/csv modules for structured data, and handle exceptions properly.

---

### Q99. How do you use regular expressions in Python?

```python
# Regular Expressions

import re

# 1. Basic Matching
pattern = r'\d+'
text = "Order 123 costs $45"
matches = re.findall(pattern, text)  # ['123', '45']

# 2. Groups
pattern = r'(\w+)@(\w+)\.(\w+)'
email = 'user@example.com'
match = re.match(pattern, email)
if match:
    print(match.groups())  # ('user', 'example', 'com')

# 3. Named Groups
pattern = r'(?P<user>\w+)@(?P<domain>\w+\.com)'
match = re.match(pattern, email)
print(match.group('user'))  # 'user'

# 4. Substitution
text = "Hello 123 World 456"
result = re.sub(r'\d+', 'X', text)  # "Hello X World X"

# 5. Compile for Reuse
pattern = re.compile(r'\d+')
matches = pattern.findall(text)

# 6. Common Patterns
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
url_pattern = r'https?://[\w.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'\d{3}-\d{3}-\d{4}'
```

**Answer:** Use re module with findall/search/match/sub methods, compile patterns for reuse, use groups for extraction, raw strings (r'') for patterns, and named groups for clarity.

---

### Q100. What are the top Python best practices?

```python
# Python Best Practices Summary

# 1. Code Style
# - Follow PEP 8
# - Use meaningful names
# - Keep functions small
# - Document with docstrings

def calculate_total(items: list) -> float:
    '''Calculate total price of items.

    Args:
        items: List of item dictionaries

    Returns:
        Total price as float
    '''
    return sum(item['price'] for item in items)

# 2. Error Handling
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Operation failed: {e}")
    raise
finally:
    cleanup()

# 3. Resource Management
with open('file.txt') as f:
    data = f.read()

# 4. Use Built-ins
# Good
squares = [x**2 for x in range(10)]

# 5. Type Hints
def process(data: list[int]) -> int:
    return sum(data)

# 6. Testing
def test_process():
    assert process([1, 2, 3]) == 6

# 7. Documentation
# Write README, docstrings, comments
# Keep docs updated

# 8. Version Control
# Use git, meaningful commits
# Branch strategy

# 9. Virtual Environments
# python -m venv venv
# source venv/bin/activate

# 10. Continuous Learning
# Read PEPs, follow updates
# Practice, review code
```

**Answer:** Follow PEP 8, use type hints, write tests, document code, use virtual environments, handle errors properly, leverage built-ins, use context managers, practice DRY principle, and continuously learn.

---