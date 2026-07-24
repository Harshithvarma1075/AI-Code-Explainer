# Collections in Python

## Introduction

Collections are built-in data structures used to store and organize multiple values efficiently. Python provides four primary collection types:

- List
- Tuple
- Set
- Dictionary

Each collection serves a different purpose depending on whether the data should be ordered, mutable, unique, or associated with keys.

---

## Why Collections Matter

Collections allow programmers to:

- Store multiple values together.
- Organize data efficiently.
- Perform searching and sorting.
- Remove duplicate values.
- Represent real-world data structures.
- Improve code readability and performance.

Choosing the right collection improves both efficiency and maintainability.

---

# Lists

## Introduction

A list is an ordered, mutable collection that allows duplicate values.

### Creating a List

```python
fruits = ["Apple", "Banana", "Mango"]
print(fruits)
```

Output

```
['Apple', 'Banana', 'Mango']
```

---

### Accessing Elements

```python
print(fruits[0])
print(fruits[-1])
```

Output

```
Apple
Mango
```

---

### Modifying a List

```python
fruits[1] = "Orange"
print(fruits)
```

Output

```
['Apple', 'Orange', 'Mango']
```

---

### Common List Methods

```python
numbers = [3, 1, 5]

numbers.append(10)
numbers.insert(1, 20)
numbers.remove(5)
numbers.sort()

print(numbers)
```

Output

```
[1, 3, 10, 20]
```

Common methods include:

- append()
- insert()
- remove()
- pop()
- sort()
- reverse()
- clear()

---

# Tuples

## Introduction

A tuple is an ordered, immutable collection.

```python
coordinates = (10, 20)

print(coordinates)
```

Output

```
(10, 20)
```

Since tuples cannot be modified after creation, they are useful for storing constant values.

---

# Sets

## Introduction

A set is an unordered collection of unique elements.

```python
numbers = {1, 2, 3, 2, 1}

print(numbers)
```

Output

```
{1, 2, 3}
```

Notice that duplicate values are removed automatically.

---

### Set Operations

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
```

Output

```
{1, 2, 3, 4, 5}
{3}
{1, 2}
```

---

# Dictionaries

## Introduction

A dictionary stores data as key-value pairs.

```python
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python"
}

print(student)
```

Output

```
{'name': 'Alice', 'age': 21, 'course': 'Python'}
```

---

### Accessing Dictionary Values

```python
print(student["name"])
print(student.get("age"))
```

Output

```
Alice
21
```

---

### Updating Dictionaries

```python
student["age"] = 22
student["city"] = "Hyderabad"

print(student)
```

---

### Dictionary Methods

Useful methods include:

- keys()
- values()
- items()
- get()
- update()
- pop()

---

# Nested Collections

Collections can contain other collections.

```python
students = [
    {
        "name": "Alice",
        "marks": [90, 85, 88]
    },
    {
        "name": "Bob",
        "marks": [75, 80, 82]
    }
]

print(students[0]["marks"][1])
```

Output

```
85
```

---

# List Comprehension

List comprehension provides a concise way to create lists.

```python
squares = [x * x for x in range(6)]

print(squares)
```

Output

```
[0, 1, 4, 9, 16, 25]
```

---

# Choosing the Right Collection

| Collection | Ordered | Mutable | Duplicates | Key Feature |
|------------|----------|----------|------------|-------------|
| List | Yes | Yes | Yes | General-purpose sequence |
| Tuple | Yes | No | Yes | Immutable data |
| Set | No | Yes | No | Unique elements |
| Dictionary | Yes* | Yes | Keys must be unique | Key-value mapping |

(*Python 3.7+ preserves insertion order.)

---

# Common Mistakes

- Using a list when a set is more appropriate.
- Forgetting that tuples are immutable.
- Accessing dictionary keys that do not exist.
- Modifying a collection while iterating over it.
- Assuming sets preserve order.

---

# Best Practices

- Use lists for ordered data.
- Use tuples for fixed data.
- Use sets to remove duplicates.
- Use dictionaries for fast lookups.
- Prefer list comprehensions when they improve readability.
- Choose descriptive dictionary keys.

---

# Interview Questions

1. Difference between list and tuple.
2. Difference between list and set.
3. Difference between set and dictionary.
4. Why are dictionary lookups fast?
5. What is list comprehension?
6. Can dictionary keys be mutable?
7. How are duplicates handled in sets?
8. When should tuples be preferred over lists?

---

# Summary

Python collections provide powerful ways to organize and manipulate data. Lists, tuples, sets, and dictionaries each solve different problems, and selecting the appropriate collection leads to cleaner, more efficient, and more maintainable programs.