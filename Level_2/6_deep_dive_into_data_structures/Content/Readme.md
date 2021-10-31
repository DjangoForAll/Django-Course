## Lists

As the name suggests, a list is a collection of items. these items can be of any data type. lists are very flexible you can add/remove items in a list if needed, lists are mutable as in you can change the value of an item in a list.

```python
list_with_numbers = [1, 2, 3, 4, 5]
list_with_strings = ["a", "b", "c", "d", "e"]
list_with_mixed_data_types = [1, "a", "b", "c", "d", "e"]
length_of_list = len(list_with_numbers) # This will return the length of the list
```

Lists are indexed starting from 0. so to get the first element you have to start from the 0th element.

```python
list_with_numbers = [1, 2, 3, 4, 5]
print(list_with_numbers[0]) # prints 1
```

Lists can be sliced ( create a new sublist from the list ) like this `list_variable[start:end]` (note that the start is included and the end is excluded).
Lists can also be negatively indexed ie -1 index is the last element.

You can combine all these together to do a lot of operations with lists.

```python
list_with_numbers = [1, 2, 3, 4, 5]
print(list_with_numbers[0:2]) # prints [1, 2]
print(list_with_numbers[:2]) # prints [1, 2] not specifying a start index will start from the beginning
print(list_with_numbers[2:]) # prints [3, 4, 5] not specifying an end index will end at the end
print(list_with_numbers[-1]) # prints 5
print(list_with_numbers[-3:]) # prints [3, 4, 5] ( the last three items with the start included)
```

Lists like strings comes with a bunch of methods like `.count()`, `.index()`, `.append()`, `.pop()`, `.remove()`, `.reverse()`, `.sort()` etc. You can find a full list of methods in the [Python documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists). Explaining everything in detail is beyond the scope of this tutorial.

Some examples of methods that can be used with lists are:

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

We can split a string into a list by using the split method.

```python
some_string = "This is a test"
list_of_words = some_string.split(" ") # The argument to the split function is used to split the words by.
print(list_of_words) # prints ['This', 'is', 'a', 'test']
```

Lists can be joined back into a string with the join method.

```python
list_of_words = ["This", "is", "a", "test"]
joined_string = "-".join(list_of_words) # The argument to the join function is used to join the words by.
print(joined_string) # prints "This-is-a-test"
```

Lists can have all sorts of data types in them. You can even have lists inside of lists.

```python
list_cordinates = [[1,0] , [2,0], [3,0]]
```

## Fun with lists

given a list, we can define a function and have python call the function with every item in the list. This is performed using the map function.

```python
some_names = ["John", "Jane", "Mary"]
def say_hello(name):
    return "Hello " + name
print(list(map(say_hello, some_names))) # prints ["Hello John", "Hello Jane", "Hello Mary"]
```

This is just the tip of the iceberg!

_Python comes with an immutable version of lists called `tuple`. Tuples do not support changes once initialized._

## Dictionaries

A dictionary in python is simply a collection of key-value pairs, what are key-value pairs? in real life, this is like a contact name and a phone number they are always pairs mapped together, and given the contact name you can find out the phone number.

> Note that this is a one-way mapping so given the key you get a value back, but you cant get the value back from the key. ( This is possible although not recommended )

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

Dictionary values can be of any datatype , even dictionaries themselves!

```python
contact_details = {
    "Mary": {
        "address": "123 Main Street",
        "state": "NY",
        "phone": ["1234567890" , "9876543210"]
    }
}
```
