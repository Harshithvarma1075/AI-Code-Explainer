# Functions in Python

## Introduction

A function is a reusable block of code designed to perform a specific task. Functions help organize code into smaller, manageable pieces, making programs easier to read, test, and maintain.

Python provides two types of functions:

- Built-in Functions
- User-defined Functions

---

## Why Functions Matter

Functions provide several advantages:

- Reduce code duplication
- Improve readability
- Promote code reusability
- Simplify debugging
- Make testing easier
- Support modular programming

Without functions, the same code would need to be written repeatedly, increasing the chances of errors.

---

## Function Syntax

Functions are defined using the `def` keyword.

```python
def greet():
    print("Hello, World!")
```

Calling the function:

```python
greet()
```

Output:

```
Hello, World!
```

---

## Function with Parameters

Parameters allow functions to receive input values.

```python
def greet(name):
    print(f"Hello, {name}")
```

Calling:

```python
greet("Alice")
```

Output:

```
Hello, Alice
```

---

## Function with Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```
30
```

---

## Return Statement

The `return` statement sends a value back to the caller.

```python
def add(a, b):
    return a + b

result = add(5, 7)
print(result)
```

Output:

```
12
```

Unlike `print()`, `return` allows the result to be reused later in the program.

---

## Default Parameters

Python allows parameters to have default values.

```python
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("John")
```

Output:

```
Hello, Guest
Hello, John
```

---

## Keyword Arguments

Arguments can be passed using parameter names.

```python
def student(name, age):
    print(name, age)

student(age=20, name="Alice")
```

Output:

```
Alice 20
```

---

## Variable-Length Arguments

### *args

Accepts multiple positional arguments.

```python
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30)
```

Output:

```
60
```

---

### **kwargs

Accepts multiple keyword arguments.

```python
def profile(**details):
    print(details)

profile(name="Alice", age=21)
```

Output:

```
{'name': 'Alice', 'age': 21}
```

---

## Lambda Functions

Lambda functions are anonymous one-line functions.

```python
square = lambda x: x * x

print(square(5))
```

Output:

```
25
```

---

## Recursive Functions

A recursive function calls itself until a stopping condition is reached.

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```
120
```

---

## Scope of Variables

### Local Variable

```python
def demo():
    x = 10
    print(x)

demo()
```

---

### Global Variable

```python
x = 100

def demo():
    print(x)

demo()
```

---

## Docstrings

Functions should include documentation.

```python
def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b
```

---

## Common Mistakes

- Forgetting to call the function.
- Missing the `return` statement.
- Incorrect indentation.
- Passing the wrong number of arguments.
- Confusing `print()` with `return`.

---

## Best Practices

- Give functions meaningful names.
- Keep functions focused on one task.
- Use docstrings.
- Avoid global variables.
- Prefer returning values over printing them.
- Keep functions short and readable.

---

## Interview Questions

1. What is a function?
2. Difference between parameters and arguments.
3. Difference between `return` and `print`.
4. Explain `*args` and `**kwargs`.
5. What is recursion?
6. What is a lambda function?
7. Explain variable scope.
8. What are default arguments?

---

## Summary

Functions are one of the most important building blocks in Python. They improve modularity, readability, maintainability, and reusability. Mastering functions is essential before learning object-oriented programming, decorators, generators, and frameworks like Flask or FastAPI.