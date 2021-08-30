## Other Data Types in Python

### Lists

As the name suggests, a list is a collection of items. these items can be of any data type. lists are very flexible you can add/remove items in a list if needed, lists are mutable as in you can change the value of an item in a list.

```python
list_with_numbers = [1, 2, 3, 4, 5]
list_with_strings = ["a", "b", "c", "d", "e"]
list_with_mixed_data_types = [1, "a", "b", "c", "d", "e"]
length_of_list = len(list_with_numbers) # This will return the length of the list
```

Lists are indexed starting from 0. so to the get the first element you have to ask from the 0th element.

```python
list_with_numbers = [1, 2, 3, 4, 5]
print(list_with_numbers[0]) # prints 1
```

Lists can be sliced ( create a new sublist from the list ) like this `list_variable[start:end]` (note that the start is included and the end is excluded).
Lists can also be negatively indexed ie -1th index is the last element.

You can combine all these together to do a lot of things with lists.

```python
list_with_numbers = [1, 2, 3, 4, 5]
print(list_with_numbers[0:2]) # prints [1, 2]
print(list_with_numbers[:2]) # prints [1, 2] not specifying a start index will start from the beginning
print(list_with_numbers[2:]) # prints [3, 4, 5] not specifying an end index will end at the end
print(list_with_numbers[-1]) # prints 5
print(list_with_numbers[-3:]) # prints [3, 4, 5] ( the last three items with the start included)
```

Lists like strings comes with a bunch of methods like `.count()`, `.index()`, `.append()`, `.pop()`, `.remove()`, `.reverse()`, `.sort()` etc. You can find a full list of methods in the [Python documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists). Explaining everything in detail is beyond the scope of this tutorial.

```python
list_with_numbers = [1, 2, 3, 4, 5]
list_with_numbers.append(6) # adds 6 to the end of the list
list_with_numbers.insert(2, 7) # inserts 7 at index 2
list_with_numbers.remove(3) # removes the first 3 from the list ** Based on the value not the index
list_with_numbers.pop() # removes the last item from the list
list_with_numbers.pop(0) # removes the first item from the list
list_with_numbers.reverse() # reverses the order of the list, note that this function does not return anything
list_with_numbers.sort() # sorts the list , note that this function does not return anything
list_with_numbers.sort(reverse=True) # sorts the list in reverse order
```

As you saw with strings try the dir() function with lists to see if you want to try everything first hand ( for the adventurous folks! )

### Fun with lists

given a list we can define a function and have python call the function with every item in the list. This is performed using the map function.

```python
some_names = ["John", "Jane", "Mary"]
def say_hello(name):
    return "Hello " + name
print(list(map(say_hello, some_names))) # prints ["Hello John", "Hello Jane", "Hello Mary"]
```

This is just the tip of the iceberg!

_Python comes with an immutable version of lists called `tuple`. Tuples do not support changes once initialised._

### Dictionaries

### Iterations in Python

### Exceptions and Handling them
