# ---- LISTS -----
## What is a List? 
### A list is a collection of similar of different data types 

Main features:
- A list can have multiple types
`numbers = [1, 'c', "d", 0.9]`
- lists can have duplicates
- list can be empty
`numbers = []` 
- lists are mutuable *aka* changeable

## Accessing lists
- Access a specific index in a 1D list
`# given numbers = [1, 2, 3, 4, 5]`
`numbers[0] = 1`

- Negative indexing
```python
numbers[-1] = 5
numbers[-2] = 4
numbers[-3] = 3
```

- Accessing a multi-dimensional list, meaning multiple list in list
```python
numbers_three_dee = [[1, 2, 3], 'hi', [5, 6, 7]]

numbers_three_dee[0][1] = 2
numbers_three_dee[2] = [5, 6, 7]
```

## Adding elements to a list 
`append()` this adds one item at the end of the list
syntax `list_name.append(value)`

can add multiple items as one `list_name.append([argument_1, argument_2])`
for `append()` you can use other types too

`insert()` adds item at a specific location
syntax `list_name.insert(position, value)`

`extend()` adds all items of one list into another list as different items
syntax `list_name.extend(list_two_name)`

```python
letters = ['a', 'b', 'c']
more_letters = ['d', 'e', 'f']

letters.extend(more_letters) # it gets added to the end and 
# letters will now look like 
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
```

*What's the difference between append and extend?*
```python
nums = [1, 2, 3]
nums.append([4, 5])
print(nums)   # [1, 2, 3, [4, 5]]

#### VERSUS ####
nums = [1, 2, 3]
nums.extend([4, 5])
print(nums)   # [1, 2, 3, 4, 5]

```
## input() 
Input takes an input from the user.

### syntax
syntax `number = input()`
input with a message `number = input('enter a number: ')`
inputs are usually taken in as a string
typecasting `number = int(input('enter a number: '))` or `number = onput('enter a number: ')` then `int(number)`

### input using loops
```python
    list = [1, 'b', 2, 'd', 'c']

    print(f"your list is currently: {list}")

    for x in range(3):
        number = input('enter a number: ')
        list.insert(x, int(number))

    print(f"your new  list is: {list}")
    # there's many ways to do this, this is just one example
```

## split() method
### What is the split method?
It splits a string into a list of substrings
syntax `string.split(seperator, maxsplit)`
- seperator tells the method where to split, by default it is any white space character ' '
- maxsplit tells the maximum number of split, by default is -1, meaning that if no argument, then the maximum occurrance is everywhere the separator exists


### input a list using split() method
```python
    numbers = input('please input 3 numbers followed by a space, then click enter when complete: ')
    list = numbers.split(' ', 3)
    print("your new list of numbers is ", list)
```

for the same code above, can also do as such:

```python
    numbers = input('please enter 3 numbers followed by a space, then enter when complete ').split(' ', 3)
    print(f"your new list is {numbers}")
```

### input a list using split() method & loop 
```python
    numbers = input('enter any amount of numbers followed by a space and press eneter when coplete: ').split()

    for x in range(0, len(numbers)):
        numbers[x] = int(numbers[x])

    print(f"your list of ints {numbers}")
```

## changing a list

```python
# ----- single item -----
list = [1, 2, 3]
list[1] = [4]
# list will now be [1, 4, 3]

# ----- multiple -----
list = [1, 2, 3, 4, 6, 7]
list[2:5] = [10, 11, 12]
# list will now be [1, 2, 10, 11, 12, 7]
# in python when the range is [x:y] it stops before y

# ----- insert() ------
list = [2, 3, 4, 5]
list.insert(2, 'b')
#list will now be [2, 3, 'b', 4, 5]
```

## removing items using remove(), pop(), del, and clear()
- `remove()` removes a specific item
- `pop()` removes an item at a specific index and _returns_ that same item
    - if nothing was specified in `pop()`, by default the last item will be removed
- `del` also removes from a specific index, but can also remove a whole list
- `clear` method can clear the list, but the list will still exist

## list comprehension
```python  
    list = ['Jane', 'Kathy', 'Frances', 'Karen', 'Francesca', 'Aileen']
    f_names = []
    for name in list:
        if 'F'in name:
            f_names.append(name)
    print(f_names)
```

the above can be written in one line: 
```python
    list = ['Jane', 'Kathy', 'Frances', 'Karen', 'Francesca', 'Aileen']
    f_names = [name for name in list if 'F' in name]
```

the syntax of one line is 
`list = [expression for item in iterable if condition]`
