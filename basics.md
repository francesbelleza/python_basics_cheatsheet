# Python Basics Cheatsheet

## High level thoughts
- print statements show infor
- variables store values
- if statements control flow of program
- for & while loops allow for repetitive actions
- functions are for when you want to reuse code
- recursion calls itself back

## Strings

```python
first = "frances"
last = "belleza"
full = f"{first} {last}"
```

- `len()` is a function
- `.find()`, `.title()`, `.upper()`, `.replace()` are string methods

### Common string examples

```python
print(first[0:2])   # "fr" -> index 0 up to (but not including) 2
print(first[-1])    # "s" -> last character
print(first[:3])    # "fra" -> start to index 3
print(last[2:])     # "lleza" -> index 2 to end

print(full.title())            # capitalize each word
print(full.upper())            # uppercase all letters
print(full.lower())            # lowercase all letters
print(full.replace("a", "v"))  # replace "a" with "v"
print(full.find("e"))          # index of first "e"
print("fran" in first)         # True if substring exists
print("fran" not in full)      # True if substring does not exist
```

---

## Numbers

```python
import math

print(round(2.7))      # 3
print(abs(-2))         # 2
print(math.ceil(9.7))  # 10
print(math.floor(9.7)) # 9
```

### Type conversions

```python
int("5")
float("5.5")
bool(1)
str(25)
```

---

## Input

- `input()` always returns a string

```python
num = input("Enter a number: ")
num = int(num)
```

---

## Falsy Values

These are considered false in Python:

- `""` → empty string
- `0` → zero
- `None` → no value
- `False` → boolean false

Most other values are considered true.

---

## If Statements

```python
x = 5

if num > x:
    print("x is greater than 5")
elif num == x:
    print("x is 5")
else:
    print("x is less than 5")
```

### Ternary Operator

A ternary operator is a one-line `if` statement.

```python
message = "greater than 5" if num > x else "equal to 5" if num == x else "less than 5"
print(message)
```

### Example

```python
add_three = num + 3
print(f"Your number plus 3 is {add_three}")
```

---

## Logical and Comparison Operators

### Logical operators

- `and`
- `or`
- `not`

### Comparison operators

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

---

## For Loops

```python
for number in range(5):
    print("attempt", number, (number + 1) * ".")
```

- `range(5)` gives: `0, 1, 2, 3, 4`

---

## Types

### Basic types

- `int`
- `float`
- `bool`
- `str`

### More complex types

- `list`
- `tuple`
- `set`
- `dict`

### Iterable types

These can be looped through with a `for` loop:

- `str`
- `list`
- `tuple`
- `set`
- `dict`

---

## Functions

### Basic syntax

```python
def greet(name):
    print(f"Hello, {name}")
```

### Calling a function

```python
greet("Frances")
```

### Function that returns a value

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

### Default parameters

```python
def increment(number, by=1):
    return number + by

print(increment(2))    # 3
print(increment(2, 5)) # 7
```

### Parameters vs Arguments

- **Parameters** are the variables in the function definition
- **Arguments** are the values passed into the function when calling it