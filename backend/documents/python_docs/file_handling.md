# File Handling in Python

## Introduction

File handling allows Python programs to create, read, update, and delete files stored on a computer. It is an essential concept for working with persistent data such as configuration files, reports, logs, datasets, and user-generated content.

Python provides built-in functions that make file operations simple and efficient.

---

## Why File Handling Matters

File handling enables applications to:

- Store data permanently.
- Read configuration files.
- Process datasets.
- Generate reports.
- Maintain application logs.
- Exchange information with other programs.

Without file handling, data would be lost every time a program stops running.

---

# Opening a File

Python uses the `open()` function.

Syntax:

```python
file = open("example.txt", "mode")
```

Example:

```python
file = open("sample.txt", "r")
print(file.read())
file.close()
```

---

# File Modes

| Mode | Description |
|------|-------------|
| `r` | Read (default) |
| `w` | Write (creates or overwrites) |
| `a` | Append |
| `x` | Create a new file |
| `rb` | Read binary |
| `wb` | Write binary |

---

# Reading a File

## Read Entire File

```python
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
```

---

## Read One Line

```python
file = open("sample.txt", "r")

print(file.readline())

file.close()
```

---

## Read All Lines

```python
file = open("sample.txt", "r")

print(file.readlines())

file.close()
```

---

# Writing to a File

```python
file = open("sample.txt", "w")

file.write("Hello Python")

file.close()
```

If the file already exists, its previous content is overwritten.

---

# Appending to a File

```python
file = open("sample.txt", "a")

file.write("\nLearning File Handling")

file.close()
```

Appending adds new content without removing existing data.

---

# Using the `with` Statement

The recommended way to work with files is by using the `with` statement.

```python
with open("sample.txt", "r") as file:
    content = file.read()

print(content)
```

The file is automatically closed after the block finishes, even if an exception occurs.

---

# Checking if a File Exists

```python
import os

if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File not found")
```

---

# Deleting a File

```python
import os

os.remove("sample.txt")
```

Always check whether the file exists before deleting it.

---

# Working with File Paths

```python
from pathlib import Path

file_path = Path("sample.txt")

print(file_path.exists())
```

The `pathlib` module provides a modern and cross-platform way to work with file paths.

---

# Exception Handling with Files

Files may not always exist or may not have the required permissions.

```python
try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")
```

Using exception handling makes programs more reliable.

---

# Reading Large Files Efficiently

Instead of loading the entire file into memory:

```python
with open("large_file.txt", "r") as file:

    for line in file:
        print(line.strip())
```

This approach is more memory-efficient for large files.

---

# Binary Files

Binary files are used for images, videos, PDFs, and other non-text data.

```python
with open("image.jpg", "rb") as file:
    data = file.read()
```

---

# Common Mistakes

- Forgetting to close a file.
- Using the wrong file mode.
- Overwriting important files with `"w"` mode.
- Assuming a file always exists.
- Ignoring exceptions during file operations.

---

# Best Practices

- Prefer the `with` statement over manually calling `close()`.
- Handle exceptions when reading files.
- Use descriptive file names.
- Avoid hardcoding absolute paths.
- Use `pathlib` for better portability.
- Read large files line by line instead of loading everything into memory.

---

# Interview Questions

1. What is file handling?
2. Explain different file modes.
3. Difference between `read()`, `readline()`, and `readlines()`.
4. Why is the `with` statement preferred?
5. Difference between write and append modes.
6. How do you check whether a file exists?
7. How do you handle `FileNotFoundError`?
8. What is the purpose of the `pathlib` module?

---

# Summary

File handling is a fundamental Python skill that enables programs to store and retrieve persistent data. By understanding file modes, reading and writing operations, exception handling, and modern tools like `pathlib`, developers can build reliable and maintainable applications.