# Python Syntax Errors

## Introduction

A syntax error occurs when Python encounters code that violates the language grammar. These errors are detected before the program begins execution, preventing the interpreter from running the code.

Syntax errors are among the most common mistakes for beginners and usually involve missing punctuation, incorrect indentation, or malformed statements.

---

## Common Causes

- Missing colon (`:`)
- Missing parentheses
- Incorrect indentation
- Unmatched brackets
- Invalid assignment
- Misspelled keywords

---

## Missing Colon

Control statements and function definitions require a colon at the end.

### Incorrect

```python
for i in range(5)
    print(i)
```

### Error

```text
SyntaxError: expected ':'
```

### Correct

```python
for i in range(5):
    print(i)
```

---

## Incorrect Indentation

Python uses indentation to define blocks of code.

### Incorrect

```python
def greet():
print("Hello")
```

### Error

```text
IndentationError: expected an indented block
```

### Correct

```python
def greet():
    print("Hello")
```

---

## Missing Parentheses

Function calls require parentheses.

### Incorrect

```python
print "Hello"
```

### Error

```text
SyntaxError: Missing parentheses in call to 'print'
```

### Correct

```python
print("Hello")
```

---

## Unmatched Brackets

Opening and closing brackets must always match.

### Incorrect

```python
numbers = [1, 2, 3
```

### Error

```text
SyntaxError: '[' was never closed
```

### Correct

```python
numbers = [1, 2, 3]
```

---

## Invalid Assignment

Values cannot be assigned to literals or expressions.

### Incorrect

```python
5 = x
```

### Error

```text
SyntaxError: cannot assign to literal
```

### Correct

```python
x = 5
```

---

## Misspelled Keywords

Python keywords must be spelled correctly.

### Incorrect

```python
iff x > 0:
    print(x)
```

### Error

```text
SyntaxError: invalid syntax
```

### Correct

```python
if x > 0:
    print(x)
```

---

## How to Debug Syntax Errors

1. Read the error message carefully.
2. Check the line number reported by Python.
3. Inspect the line before the reported error, since the actual mistake is often there.
4. Verify brackets, quotes, and parentheses are balanced.
5. Ensure correct indentation.
6. Check for missing colons after control statements and function definitions.

---

## Best Practices

- Use an IDE with syntax highlighting.
- Enable automatic formatting tools like Black.
- Keep code properly indented.
- Write small sections of code and test frequently.
- Read traceback messages carefully before making changes.

---

## Interview Tips

Interviewers often ask candidates to identify syntax errors in code snippets. Focus on:

- Missing colons
- Incorrect indentation
- Bracket mismatches
- Invalid assignments
- Misspelled keywords

Being able to quickly recognize these mistakes demonstrates a solid understanding of Python syntax.

---

## Summary

Syntax errors prevent Python programs from running. They are detected before execution and are usually caused by incorrect grammar, indentation, or punctuation. Careful reading of error messages and following Python's syntax rules can help identify and fix these issues efficiently.