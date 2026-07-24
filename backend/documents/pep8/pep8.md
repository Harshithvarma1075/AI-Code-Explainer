# Python PEP 8 Style Guide

## Introduction

PEP 8 is the official style guide for Python code. It provides a set of conventions that improve code readability, consistency, and maintainability. Following PEP 8 helps developers write clean, professional code that is easier for others to understand and maintain.

Although Python code will execute regardless of whether it follows PEP 8, adhering to these guidelines is considered a best practice in both industry and open-source projects.

---

## Why Follow PEP 8?

Following PEP 8 offers several benefits:

- Improves readability
- Makes collaboration easier
- Produces consistent code
- Simplifies debugging
- Reduces maintenance effort
- Encourages good programming habits

---

## Indentation

Use **4 spaces** for each indentation level.

### Correct

```python
if age >= 18:
    print("Eligible")
```

### Incorrect

```python
if age >= 18:
  print("Eligible")
```

Avoid mixing tabs and spaces.

---

## Maximum Line Length

Limit lines to **79 characters**.

For comments and docstrings, keep lines within **72 characters** whenever practical.

### Poor

```python
result = calculate_total_price_after_discount(price, tax, shipping, membership_discount, coupon_discount)
```

### Better

```python
result = calculate_total_price_after_discount(
    price,
    tax,
    shipping,
    membership_discount,
    coupon_discount
)
```

---

## Blank Lines

Use blank lines to separate logical sections of code.

- Two blank lines between top-level functions and classes.
- One blank line between methods inside a class when appropriate.

### Example

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
```

---

## Imports

Imports should usually appear at the beginning of the file.

Group imports in the following order:

1. Standard library imports
2. Third-party library imports
3. Local application imports

### Example

```python
import os
import math

import numpy as np

from app.utils import helper
```

Avoid wildcard imports.

### Avoid

```python
from math import *
```

---

## Naming Conventions

### Variables

Use **snake_case**.

```python
student_name = "Alice"
total_marks = 95
```

Avoid

```python
StudentName
studentName
```

---

### Functions

Function names should use **snake_case**.

```python
def calculate_total():
    pass
```

---

### Classes

Class names should use **PascalCase**.

```python
class StudentManager:
    pass
```

---

### Constants

Constants should be written in **UPPER_CASE**.

```python
MAX_USERS = 100
PI = 3.14159
```

---

## Whitespace

Use spaces around operators.

### Good

```python
total = price + tax
```

### Avoid

```python
total=price+tax
```

---

## Comparisons

Use Python's readable comparison syntax.

### Good

```python
if value is None:
    pass
```

### Avoid

```python
if value == None:
    pass
```

Similarly,

```python
if value is not None:
```

is preferred over

```python
if value != None:
```

---

## Boolean Expressions

Avoid unnecessary comparisons.

### Good

```python
if is_valid:
    print("Accepted")
```

### Avoid

```python
if is_valid == True:
    print("Accepted")
```

---

## Comments

Write comments that explain **why**, not **what**.

### Good

```python
# Skip invalid records to prevent processing errors.
```

Avoid obvious comments.

```python
# Increment i
i += 1
```

---

## Docstrings

Public modules, classes, and functions should include docstrings.

### Example

```python
def square(number):
    """
    Return the square of a number.
    """
    return number * number
```

---

## Error Handling

Catch specific exceptions instead of using a generic exception.

### Good

```python
try:
    value = int(text)
except ValueError:
    print("Invalid number")
```

### Avoid

```python
try:
    value = int(text)
except:
    print("Error")
```

---

## Writing Readable Code

Readable code is more valuable than clever code.

Prefer

```python
if age >= 18:
    eligible = True
```

instead of overly complex one-line expressions that reduce clarity.

Always prioritize readability over brevity.

---

## PEP 8 Tools

Several tools help enforce PEP 8 automatically.

- Black
- Ruff
- Flake8
- autopep8
- isort

These tools can automatically format code and identify style violations.

---

## Best Practices

- Use meaningful variable names.
- Keep functions short and focused.
- Remove unused imports.
- Avoid deeply nested code.
- Write consistent formatting throughout the project.
- Prefer readability over clever tricks.
- Keep modules organized.
- Follow one consistent coding style.

---

## Interview Tips

Many technical interviews evaluate not only whether code works but also how readable and maintainable it is.

Interviewers often look for:

- Proper naming conventions
- Consistent indentation
- Clean function design
- Meaningful variable names
- Appropriate comments
- Readable control flow
- Good code organization

Following PEP 8 demonstrates professionalism and attention to detail.

---

## Summary

PEP 8 provides a standard set of guidelines for writing clean, readable, and maintainable Python code. By following these conventions, developers create code that is easier to understand, debug, and collaborate on, making it the preferred coding style across the Python community.