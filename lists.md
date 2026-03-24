# Lists Basics

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





