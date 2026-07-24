# Loops in Python

## Introduction

Loops execute a block of code repeatedly.

Python supports:

- for loop
- while loop

---

## for Loop

```python
for i in range(5):
    print(i)
```

---

## while Loop

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## range()

```python
range(5)

range(2,10)

range(1,10,2)
```

---

## break

```python
for i in range(10):
    if i == 5:
        break
```

---

## continue

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

---

## pass

```python
for i in range(5):
    pass
```

---

## Nested Loops

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

---

## Infinite Loop

```python
while True:
    print("Running")
```

---

## Common Errors

- Infinite loops
- Incorrect indentation
- Forgetting to update loop variables

---

## Best Practices

- Prefer for loops when iterations are known.
- Avoid deeply nested loops.
- Keep loop bodies concise.

---

## Interview Tips

- Difference between for and while.
- Time complexity of nested loops.
- Use cases for break and continue.