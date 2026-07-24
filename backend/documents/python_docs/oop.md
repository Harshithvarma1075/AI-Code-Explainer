# Object-Oriented Programming (OOP) in Python

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm that organizes software around objects rather than functions. An object combines data (attributes) and behavior (methods) into a single unit.

Python fully supports OOP and uses it extensively in frameworks like Flask, Django, FastAPI, TensorFlow, and many others.

---

## Why OOP Matters

OOP helps developers:

- Organize large applications.
- Reuse code.
- Reduce duplication.
- Improve maintainability.
- Model real-world entities.
- Build scalable software.

---

# Classes and Objects

A class is a blueprint for creating objects.

An object is an instance of a class.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Alice", 20)

print(student.name)
print(student.age)
```

Output

```
Alice
20
```

---

# The __init__() Constructor

The constructor initializes object attributes when an object is created.

```python
class Car:

    def __init__(self, brand):
        self.brand = brand

car = Car("Toyota")

print(car.brand)
```

---

# Instance Attributes

Instance attributes belong to individual objects.

```python
class Employee:

    def __init__(self, name):
        self.name = name
```

Each object has its own value of `name`.

---

# Instance Methods

Methods define an object's behavior.

```python
class Dog:

    def bark(self):
        print("Woof!")

dog = Dog()

dog.bark()
```

---

# The self Keyword

`self` refers to the current object.

```python
class Person:

    def greet(self):
        print("Hello")
```

Python automatically passes the current object as the first argument.

---

# Four Pillars of OOP

## 1. Encapsulation

Encapsulation means combining data and methods inside a class while restricting direct access when appropriate.

```python
class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance
```

---

## 2. Inheritance

Inheritance allows one class to acquire properties and methods of another.

```python
class Animal:

    def speak(self):
        print("Animal speaks")

class Dog(Animal):

    pass

dog = Dog()

dog.speak()
```

Output

```
Animal speaks
```

---

## 3. Polymorphism

Different classes can define the same method differently.

```python
class Cat:

    def sound(self):
        print("Meow")

class Dog:

    def sound(self):
        print("Woof")

animals = [Cat(), Dog()]

for animal in animals:
    animal.sound()
```

Output

```
Meow
Woof
```

---

## 4. Abstraction

Abstraction hides implementation details and exposes only essential functionality.

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

---

# Method Overriding

A child class can redefine a parent class method.

```python
class Animal:

    def sound(self):
        print("Animal Sound")

class Dog(Animal):

    def sound(self):
        print("Bark")
```

---

# Class Variables

Shared across all objects.

```python
class Student:

    school = "ABC School"
```

---

# Static Methods

```python
class Math:

    @staticmethod
    def square(x):
        return x * x

print(Math.square(5))
```

Output

```
25
```

---

# Class Methods

```python
class Student:

    school = "ABC"

    @classmethod
    def get_school(cls):
        return cls.school
```

---

# Composition vs Inheritance

Inheritance represents an "is-a" relationship.

Example:

```
Dog is an Animal
```

Composition represents a "has-a" relationship.

Example:

```
Car has an Engine
```

Composition is often preferred because it creates looser coupling.

---

# Common Mistakes

- Forgetting `self`.
- Confusing classes with objects.
- Overusing inheritance.
- Accessing private variables directly.
- Creating classes for very simple tasks.

---

# Best Practices

- Keep classes focused on one responsibility.
- Prefer composition over deep inheritance.
- Use meaningful class names.
- Encapsulate internal state.
- Write reusable methods.
- Follow the Single Responsibility Principle.

---

# Interview Questions

1. What is OOP?
2. Difference between class and object.
3. Explain encapsulation.
4. Explain inheritance.
5. Explain polymorphism.
6. Explain abstraction.
7. Difference between class method and static method.
8. Difference between composition and inheritance.
9. What is method overriding?
10. Why do we use `self`?

---

# Summary

Object-Oriented Programming provides a structured way to build scalable and maintainable software. Understanding classes, objects, encapsulation, inheritance, polymorphism, and abstraction is essential for professional Python development and modern frameworks.