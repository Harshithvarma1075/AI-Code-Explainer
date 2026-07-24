# Variables in Python

## Introduction

A variable is a named reference to a value stored in memory. Python variables are dynamically typed, meaning you do not need to declare their data type explicitly.

---

## Variable Declaration

```python
name = "John"
age = 25
height = 5.9
```

---

## Naming Rules

Valid:

```python
student_name
_marks
age1
```

Invalid:

```python
1age
student-name
class
```

---

## Multiple Assignment

```python
a, b, c = 1, 2, 3
```

```python
x = y = z = 100
```

---

## Dynamic Typing

```python
x = 10
x = "Python"
```

---

## Type Checking

```python
x = 10
print(type(x))
```

---

## Type Conversion

```python
age = "25"

age = int(age)
```

---

## Common Errors

- Using keywords as variable names
- Misspelled variable names
- Accessing variables before assignment

---

## Best Practices

- Use snake_case
- Choose descriptive names
- Avoid single-letter names except loop variables

---

## Interview Tips

- Explain dynamic typing
- Difference between mutable and immutable objects
- Variable scope