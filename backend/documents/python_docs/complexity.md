# Time and Space Complexity in Python

## Introduction

Time and Space Complexity are measures used to evaluate the efficiency of an algorithm.

- **Time Complexity** measures how the execution time of an algorithm grows as the input size increases.
- **Space Complexity** measures how much additional memory an algorithm requires as the input size grows.

Rather than measuring exact execution time, complexity focuses on how an algorithm scales for large inputs.

---

## Why Complexity Matters

Understanding complexity helps developers:

- Write efficient programs.
- Compare different algorithms.
- Optimize code performance.
- Handle large datasets effectively.
- Prepare for coding interviews.

A solution that works for 10 elements may become impractical for 10 million elements if its complexity is poor.

---

# Big-O Notation

Big-O notation describes the **worst-case growth rate** of an algorithm.

It ignores constant factors and focuses on how performance changes as the input size (`n`) increases.

Example:

```python
for i in range(n):
    print(i)
```

This loop runs `n` times.

Time Complexity:

```
O(n)
```

---

# Common Time Complexities

| Complexity | Name         | Example                     |
| ---------- | ------------ | --------------------------- |
| O(1)       | Constant     | Accessing a list element    |
| O(log n)   | Logarithmic  | Binary Search               |
| O(n)       | Linear       | Traversing a list           |
| O(n log n) | Linearithmic | Merge Sort                  |
| O(n²)      | Quadratic    | Nested loops                |
| O(2ⁿ)      | Exponential  | Recursive subset generation |
| O(n!)      | Factorial    | Generating all permutations |

---

# O(1) - Constant Time

The operation always takes the same amount of time.

```python
numbers = [10, 20, 30]

print(numbers[1])
```

Time Complexity

```
O(1)
```

---

# O(log n) - Logarithmic Time

The input size is repeatedly divided.

Example: Binary Search.

```python
low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2
```

Time Complexity

```
O(log n)
```

---

# O(n) - Linear Time

The algorithm processes every element once.

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```

Time Complexity

```
O(n)
```

---

# O(n log n)

Efficient sorting algorithms such as Merge Sort and Heap Sort have this complexity.

Example:

```python
numbers.sort()
```

Python's built-in sorting (`sort()` and `sorted()`) uses **Timsort**, which has an average and worst-case complexity of **O(n log n)**.

---

# O(n²) - Quadratic Time

Usually caused by nested loops.

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Time Complexity

```
O(n²)
```

Quadratic algorithms become slow for large datasets.

---

# O(2ⁿ) - Exponential Time

Every additional input approximately doubles the work.

Example:

Naive recursive Fibonacci.

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
```

Time Complexity

```
O(2ⁿ)
```

---

# O(n!) - Factorial Time

Occurs when generating every possible arrangement.

Example:

Generating all permutations.

```
ABC

ACB

BAC

BCA

CAB

CBA
```

Time Complexity

```
O(n!)
```

This becomes impractical even for moderate values of `n`.

---

# Space Complexity

Space complexity measures the amount of additional memory required.

Example:

```python
numbers = []

for i in range(n):
    numbers.append(i)
```

Additional memory grows with the input size.

Space Complexity

```
O(n)
```

---

# Constant Space

```python
total = 0

for number in numbers:
    total += number
```

Only a few variables are used regardless of input size.

Space Complexity

```
O(1)
```

---

# Comparing Algorithms

Suppose we want to find a value in a sorted list.

| Algorithm     | Time Complexity |
| ------------- | --------------- |
| Linear Search | O(n)            |
| Binary Search | O(log n)        |

Binary Search performs significantly better on large sorted datasets.

---

# How to Optimize Algorithms

Common optimization techniques include:

- Using hash tables (dictionaries and sets).
- Avoiding unnecessary nested loops.
- Using efficient data structures.
- Choosing better algorithms.
- Avoiding repeated calculations.
- Using built-in Python functions when appropriate.

---

# Common Mistakes

- Confusing time complexity with execution time.
- Ignoring space complexity.
- Assuming nested loops always mean O(n²) (it depends on the loops).
- Optimizing prematurely before identifying bottlenecks.

---

# Best Practices

- Analyze algorithm efficiency before optimization.
- Prioritize readability unless performance is critical.
- Use Python's built-in data structures effectively.
- Consider both time and memory usage.
- Benchmark performance when necessary.

---

# Interview Questions

1. What is Big-O notation?
2. Difference between time and space complexity.
3. Explain O(1), O(log n), O(n), and O(n²).
4. Why is Binary Search O(log n)?
5. Why is Merge Sort O(n log n)?
6. What is the complexity of Python's `sort()`?
7. When should space complexity be considered?
8. How can hash tables improve performance?
9. Does nested looping always mean O(n²)?
10. How do you optimize an inefficient algorithm?

---

# Summary

Time and Space Complexity help developers evaluate the efficiency of algorithms and choose appropriate solutions for different problem sizes. Understanding Big-O notation, common complexity classes, and optimization techniques is essential for writing scalable applications and succeeding in technical interviews.
