


# BASICS

## STRINGS

`first = "frances"
last = "belleza"
full = f"{first} {last}"`

# len() is a function
# .find(), .title(), .upper(), etc. are string methods'

`print(first[0:2])      # "fr" -> index 0 up to (but not including) 2
print(first[-1])       # "s" -> last character
print(first[:3])       # "fra" -> start to index 3
print(last[2:])        # "lleza" -> index 2 to end

print(full.title())    # "Frances Belleza" -> capitalize each word
print(full.upper())    # uppercase all letters
print(full.lower())    # lowercase all letters
print(full.replace("a", "v"))   # replace all "a" with "v"
print(full.find("e"))  # index of first "e"
print("fran" in first)         # True -> checks if substring exists
print("fran" not in full)      # False -> checks if substring does not exist`


## NUMBERS

`print(round(2.7))      # 3 -> rounds to nearest integer
print(abs(-2))         # 2 -> absolute value
print(math.ceil(9.7))  # 10 -> rounds up
print(math.floor(9.7)) # 9 -> rounds down
`
## Type conversions
`print(int("5"))        # convert to int
print(float("5.5"))    # convert to float
print(bool(1))         # convert to bool
print(str(25))         # convert to string`

# INPUT

`# input() always returns a string
num = input("Enter a number: ")
num = int(num)   # convert input to integer`

# FALSY VALUES

- These are considered False in Python:
 ""      -> empty string
 0       -> zero
 None    -> no value
 False   -> boolean False

- Most other values are considered True


# IF STATEMENTS

`x = 5

if num > x:
    print("x is greater than 5")
elif num == x:
    print("x is 5")
else:
    print("x is less than 5")

# Ternary operator (one-line if statement)'
message = "greater than 5" if num > x else "equal to 5" if num == x else "less than 5"
print(message)

add_three = num + 3
print(f"Your number plus 3 is {add_three}")`


# LOGICAL AND COMPARISON OPERATORS

- Logical operators:
     and, or, not

- Comparison operators:
 ==   equal to
 !=   not equal to
 >    greater than
 <    less than
 >=   greater than or equal to
 <=   less than or equal to


# FOR LOOPS

`for number in range(5):
    print("attempt", number, (number + 1) * ".")

# range(5) -> 0, 1, 2, 3, 4`


# TYPES

- Basic types:
int, float, bool, str

- More complex types:
 list, tuple, set, dict

- Iterable types can be looped through with a for loop:
 str, list, tuple, set, dict


# FUNCTIONS

`# Function syntax:
def greet(name):
    print(f"Hello, {name}")

greet("Frances")

# Function that returns a value:
def add(a, b):
    return a + b

print(add(2, 3))

# Default parameters:
def increment(number, by=1):
    return number + by

print(increment(2))      # 3
print(increment(2, 5))   # 7`

*Notes: *
- Parameters = variables inside the function definition
- Arguments = values passed into the function when calling it'