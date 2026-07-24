# Exception Handling in Python

## Introduction

Exception handling is a mechanism used to detect and handle runtime errors without abruptly terminating the program. Instead of crashing, a program can respond gracefully to unexpected situations.

Examples of runtime errors include:

- Dividing by zero
- Accessing a non-existent file
- Invalid user input
- Index out of range
- Key not found in a dictionary

Python provides the `try`, `except`, `else`, `finally`, and `raise` statements to handle exceptions effectively.

---

## Why Exception Handling Matters

Exception handling helps developers:

- Prevent program crashes.
- Improve user experience.
- Handle unexpected situations gracefully.
- Make applications more reliable.
- Simplify debugging.
- Separate normal program logic from error-handling logic.

---

# What is an Exception?

An exception is an event that interrupts the normal flow of program execution.

Example:

```python
print(10 / 0)
```

Output

```
ZeroDivisionError: division by zero
```

---

# try and except

The `try` block contains code that may raise an exception.

The `except` block handles the exception.

```python
try:
    number = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output

```
Cannot divide by zero.
```

---

# Handling Multiple Exceptions

A program may encounter different kinds of errors.

```python
try:

    number = int(input("Enter a number:"))

    result = 100 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

---

# Catching Multiple Exceptions Together

```python
try:

    value = int(input())

except (ValueError, TypeError):
    print("Invalid input.")
```

---

# Generic Exception

The generic `Exception` class catches most runtime errors.

```python
try:

    print(10 / 0)

except Exception as error:

    print(error)
```

Output

```
division by zero
```

Use this carefully because it may hide unexpected errors.

---

# else Block

The `else` block executes only if no exception occurs.

```python
try:

    number = 10 / 2

except ZeroDivisionError:

    print("Error")

else:

    print("Division Successful")
```

Output

```
Division Successful
```

---

# finally Block

The `finally` block always executes whether an exception occurs or not.

```python
try:

    file = open("sample.txt")

except FileNotFoundError:

    print("File not found.")

finally:

    print("Execution completed.")
```

Typical uses:

- Closing files
- Closing database connections
- Releasing resources
- Cleaning temporary data

---

# Raising Exceptions

Developers can create exceptions manually.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Output

```
ValueError: Age cannot be negative.
```

---

# Custom Exceptions

Custom exceptions improve code readability.

```python
class InvalidAgeError(Exception):
    pass

age = -2

if age < 0:
    raise InvalidAgeError("Invalid age entered.")
```

---

# Common Built-in Exceptions

| Exception | Description |
|-----------|-------------|
| ZeroDivisionError | Division by zero |
| ValueError | Invalid value |
| TypeError | Wrong data type |
| IndexError | Invalid list index |
| KeyError | Missing dictionary key |
| FileNotFoundError | File does not exist |
| NameError | Variable not defined |
| AttributeError | Invalid object attribute |
| ImportError | Module import failed |

---

# Exception Hierarchy

```
BaseException
│
├── SystemExit
├── KeyboardInterrupt
└── Exception
      │
      ├── ValueError
      ├── TypeError
      ├── IndexError
      ├── KeyError
      ├── FileNotFoundError
      └── ZeroDivisionError
```

Understanding the hierarchy helps when deciding which exceptions to catch.

---

# Best Practices

- Catch only the exceptions you expect.
- Avoid using bare `except`.
- Use `finally` for cleanup operations.
- Keep `try` blocks as small as possible.
- Raise meaningful exceptions.
- Write descriptive error messages.
- Log exceptions in production applications.

---

# Common Mistakes

- Using bare `except`.
- Ignoring exceptions silently.
- Catching every exception unnecessarily.
- Writing very large `try` blocks.
- Forgetting to close files or database connections.

---

# Real-World Example

```python
try:

    with open("students.txt", "r") as file:

        print(file.read())

except FileNotFoundError:

    print("The requested file does not exist.")

finally:

    print("Program finished.")
```

Output (if file does not exist)

```
The requested file does not exist.
Program finished.
```

---

# Interview Questions

1. What is an exception?
2. Difference between syntax errors and exceptions.
3. Explain try-except.
4. Difference between else and finally.
5. Why should we avoid bare `except`?
6. What is the purpose of `raise`?
7. How do custom exceptions work?
8. Explain the Exception hierarchy.
9. Difference between errors and exceptions.
10. When should you use `finally`?

---

# Summary

Exception handling is an essential feature of Python that enables developers to build reliable and fault-tolerant applications. Proper use of `try`, `except`, `else`, `finally`, and custom exceptions allows programs to recover gracefully from runtime errors while improving maintainability and user experience.