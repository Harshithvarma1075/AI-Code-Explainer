# Python Runtime Errors

## Introduction

A runtime error occurs after a Python program has successfully passed the syntax check and begins execution. These errors happen while the program is running and usually occur because of invalid operations, unexpected input, or incorrect assumptions made by the programmer.

Unlike syntax errors, runtime errors do not prevent the program from starting. Instead, they cause the program to terminate when the problematic line of code is executed unless the exception is handled appropriately.

---

## Common Runtime Errors

Some of the most common runtime errors in Python include:

- ZeroDivisionError
- NameError
- TypeError
- ValueError
- IndexError
- KeyError
- AttributeError
- FileNotFoundError

---

## ZeroDivisionError

Occurs when attempting to divide a number by zero.

### Incorrect

```python
a = 10
b = 0

print(a / b)
```

### Error

```text
ZeroDivisionError: division by zero
```

### Correct

```python
a = 10
b = 0

if b != 0:
    print(a / b)
else:
    print("Cannot divide by zero.")
```

---

## NameError

Occurs when a variable or function is used before it has been defined.

### Incorrect

```python
print(score)
```

### Error

```text
NameError: name 'score' is not defined
```

### Correct

```python
score = 95
print(score)
```

---

## TypeError

Occurs when an operation is performed on incompatible data types.

### Incorrect

```python
age = "25"

print(age + 5)
```

### Error

```text
TypeError: can only concatenate str (not "int") to str
```

### Correct

```python
age = "25"

print(int(age) + 5)
```

---

## ValueError

Occurs when a function receives the correct data type but an inappropriate value.

### Incorrect

```python
number = int("hello")
```

### Error

```text
ValueError: invalid literal for int() with base 10
```

### Correct

```python
number = int("25")
```

---

## IndexError

Occurs when attempting to access an index that does not exist.

### Incorrect

```python
numbers = [10, 20, 30]

print(numbers[5])
```

### Error

```text
IndexError: list index out of range
```

### Correct

```python
numbers = [10, 20, 30]

print(numbers[2])
```

---

## KeyError

Occurs when trying to access a dictionary key that does not exist.

### Incorrect

```python
student = {
    "name": "Alice"
}

print(student["age"])
```

### Error

```text
KeyError: 'age'
```

### Correct

```python
student = {
    "name": "Alice"
}

print(student.get("age", "Age not available"))
```

---

## AttributeError

Occurs when an object does not have the requested attribute or method.

### Incorrect

```python
number = 10

number.append(5)
```

### Error

```text
AttributeError: 'int' object has no attribute 'append'
```

### Correct

```python
numbers = [10]

numbers.append(5)
```

---

## FileNotFoundError

Occurs when attempting to open a file that does not exist.

### Incorrect

```python
with open("data.txt", "r") as file:
    print(file.read())
```

### Error

```text
FileNotFoundError: [Errno 2] No such file or directory
```

### Correct

```python
try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
```

---

## Using Exception Handling

Python provides the `try-except` statement to handle runtime errors gracefully.

### Example

```python
try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter a valid integer.")
```

Handling exceptions prevents the program from crashing unexpectedly and provides a better user experience.

---

## How to Debug Runtime Errors

1. Read the complete traceback carefully.
2. Identify the exception type.
3. Locate the line where the exception occurred.
4. Verify variable values before the error.
5. Use print statements or a debugger to inspect program state.
6. Add appropriate exception handling where necessary.

---

## Best Practices

- Validate user input before processing it.
- Use exception handling for operations that may fail.
- Avoid catching every exception with a generic `except`.
- Catch specific exception types whenever possible.
- Write meaningful error messages for users.
- Test edge cases such as empty lists, invalid inputs, and missing files.

---

## Interview Tips

Interviewers frequently ask candidates to explain common Python exceptions and how to handle them.

Be familiar with:

- ZeroDivisionError
- NameError
- TypeError
- ValueError
- IndexError
- KeyError
- AttributeError
- FileNotFoundError

Also understand how `try`, `except`, `else`, and `finally` blocks work.

---

## Summary

Runtime errors occur while a program is executing. They are caused by invalid operations, incorrect data, or unexpected situations such as missing files or invalid input. Proper exception handling, input validation, and careful debugging help create robust and reliable Python programs.