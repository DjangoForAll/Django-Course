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

A dictionary in python is simply a collection of key value pairs, what are key value paris ? in real life this is like a contact name and a phone number they are always mapped together and given the contact name you can find out the phone number.

```python
contact_details = {
    "John": "1234567890",
    "Jane": "0987654321",
}
print(contact_details["John"]) # prints 1234567890
```

Dictionaries like lists have a lot of methods that can be performed on them, you can find a full list of methods in the [Python documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-dictionaries).

```python
contact_details = {
    "John": "1234567890",
    "Jane": "0987654321",
}
print(contact_details.keys()) # prints ["John", "Jane"]
print(contact_details.values()) # prints ["1234567890", "0987654321"]
print(contact_details.get("Jane")) # prints 0987654321
print(contact_details.get("Mary", "Not found")) # prints Not found
```

### Iterations in Python

Itertive statements are used to execute a block of code multiple times. usually until a given condition has been reached. python has a few ways to do this, lets start with the `while` statement method first.

```python
i = 10
while i > 0:
    print(i) # prints 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    i = i-1 # decrement i by 1
```

The simple program written above can be used to print the number from i to 0, be careful when working with loops because you can end up in an infinite loop. in the case above , if we were to remove the decrementing step, the code would print 10 forever ( like forever forerver! ) in case you do endup in an infinite loop use `ctrl + c` keys to stop the program.

We can also `break` out of a loop at any point. similarly we can also cause the loop to skip over some code by using `continue`.

```python
i= 10
while True:
    i = i -1
    if i == 5:
        continue
    if i == 0:
        break
    print(i)
```

When the while loops condition is always True like in the code snippet above, it will run forever. In such cases we would have conditions inside the code that break out of the loop, in the case above we have a condition that breaks out of the loop when i is 0. Similarly we also skip the code when i is 5 which causes it to skip it from printing.

Try the snippet above and see what happens.

Although while loops are extremely useful, python provides another iterative statement called `for` . for loops are used to iterate over a sequence of items.

```python
contact_list = ["John", "Jane", "Mary"]
for contact in contact_list:
    print("Hello" , contact) # prints Hello John, Hello Jane, Hello Mary
```

This for loop iterates over the list and prints the contact name with a greeting. similarly we can loop over a string or a tuple or even a dictionary.

python has a built in function to build a list of numbers called `range`. range(start, stop, step) can be used to build a list of numbers.

```python
for i in range(0,10,2):
    # start value is included , end value is NOT included
    print(i) # prints 0, 2, 4, 6, 8
```

_Advanced Reading_ : _Python has a concept of iterators and generators. Iterators are objects that are used to iterate over a sequence. Generators are functions that return iterators. They are bit hard to understand at first but once you get them you will understand them very well. You can find a full list of iterators and generators in the [Python documentation](https://docs.python.org/3/glossary.html#term-iterator)._

### Exceptions and Handling them
