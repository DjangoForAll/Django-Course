### Blocks in Python

Python programs get structured through indentation, i.e. code blocks are defined by their indentation. it's a language requirement, not a matter of style. This principle makes it easier to read and understand Python code.
All statements with the same distance to the right belong to the same block of code, The block ends at a line less indented or the end of the file. If a block has to be more deeply nested, it is simply indented further to the right.

### Functions in Python

Functions in python are a group of statements (code block) that may or may not take inputs and may or may not return values. Functions are usually used when you want to repeatedly call a piece of code without writing the same code over and over again.

```python
def greet(name): # this defines a function called greet with one parameter called name
    salutation = "Good Morning " + name # Note that the function body is indented, this marks the start of the code block
    return salutation # The return keyword returns the value of the function to the caller

print(greet("John")) # prints "Good Morning John"
print(greet("Jane")) # prints "Good Morning Jane"
# We only had to define the function once, we can call it as many times as we want
```

Functions can not return a value as well, In those cases `None` is the value returned by the function.

we can also specify default values to the function parameters when we define the function.

```python
def greet(name, greeting = "Good Morning"): # this defines a function called greet with two parameters called name and greeting
    return greeting + " " + name

print(greet("John")) # prints "Good Morning John"
print(greet("Jane", "Good Afternoon")) # prints "Good Afternoon Jane"
print(greet(name="John")) # we can also pass parameters to the function by name, that way we can change the order of the parameters
```

### Conditionals in Python

We have discussed the boolean datatype earlier, we can leverage this datatype to create conditionals in Python.

```python
print(1>2) # prints False
print(2*2 == 4) # prints True
print(True and False) # prints False
print(not False) # prints True
print( (2 > 1) and (1 > 2) ) # prints False ( Evaluates to True and False )
(2 > 1) and print("2 is greater than 1") # prints 2 is greater than 1
(1 > 2) and print("1 is greater than 2") # prints nothing
```

These types of conditional statements are hard to read and make little to no sense, so we will use a different type of conditional statement called `if` statements. They are easier to handle and they can have multiple branching conditions as well.

```python
some_number = 5
if some_number > 1: # this is an if statement
    print("given number is greater than 1") # this is the body of the if statement
else: # this is the else statement
    print("given number is not greater than 1") # this is the body of the else statement
```

This is a very simple if statement, it has only one condition, if the condition evaluates as `True` or 1, then the body of the if statement is executed. if not the body of the else is executed. Try running this with different values to see what happens.

We can also write multiple branches of the same if statement by using `elif`.

```python
given_number = 5
if given_number > 1: # this is an if statement
    print("given number is greater than 1") # this is the body of the if statement
elif given_number < 1: # this is an elif statement
    print("given number is smaller than 1") # this is the body of the elif statement
else: # this is the else statement
    print("given number is 1!") # this is the body of the else statement
```

Once one of the conditions in the if statement is satisfied, the rest of the statements are not executed. Complicated branching logic can be simplified by using `if` statements efficiently.

Now that you have some basic knowledge about python, try to create a function that takes a user's name, age, and some basic information and prints out a fake profile. Try constructing different types of portfolios based on the user's age and other variations to try out what you learned
