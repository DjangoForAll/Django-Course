# Introduction to Python

## Getting Started

### What is a Program ?

A program is a collection of statements that performs a specific task. or in simple words, it is an abstraction that takes some input and processes it to produce some output.
In python a program can be as simple as this `print("Hello World)` , This program does not take an input from the user, instead it prints `Hello World` as the output.

### What is python ?

Python is an interpreted, object oriented, high level programming language. These words might not make sense right away but we will explore each of python's features seperately in this course.

Before we get started with installing python on your computer, lets test drive python online.

You can use any of the following websites to run python online for free.  
[Official Python Website](https://www.python.org/shell/)  
[Alternative 1](https://www.online-python.com/)  
[Alternative 2](https://www.programiz.com/python-programming/online-compiler/)

You can run the sample code on any of these websites and see how the program execution changes when you try out your own experiments!

_Whenever you see code snippets anywhere, try and type it on your own, dont try to copy paste it directly, typing it on your own makes you think about what you are doing and train you to write better code_

### Variables and Data Types

lets try to build a program that doubles a given number.

```python
number = 5
print(number * 2)
```

in the above program we have defined a variable `number` and assigned it the value 5. Variables are used to store values. data stored in variables have types, in this case it is int ( short for integer ), some of the other data types in python are explain in the following program.

```python
ratio = 1.5 # float (short for floating point)
salutation = "Hello" # string
has_power = True # boolean
```

The `#` symbol is used to write comments in python, anything after the `#` symbol is ignored by python.

you can name the variables anything you want but the standard way to name variables is to use snake cases ( lowercase words seperated by underscores like snake_case ), this is the convention used by python.

variable names should be descriptive, they should be meaningful and easy to understand. they should not start with a number and they should not be a reserved keyword ( these are special words that python users like `print` naming variables with these names can cause unexpected results ).

### Converting Data Types

The process of converting one data type to another is called type conversion. type conversion can be Implicit or Explicit in python.

**Implicit Type conversions** are done automatically by python. for eg :

```python
num_a = 100 # int
num_b = 1.9 # float
print(numb_a + num_b) # implicit type conversion to float
```

To view the type of a variable you can use the `type()` function.

```python
some_variable = 1.6 # float
print(type(some_variable)) # prints <class 'float'>
```

The above program prints `<class 'float'>` which is the type of the variable `some_variable`.

---

Explicit type conversions are done manually in code, for eg :

```python
some_variable = 1.6
some_int = int(some_variable) # explicit type conversion
print(some_int * 2) # prints 2
```

The int() function converts a given data type into int, similarly float() converts a given data type into float.
similar functions exist for other data types like str(), bool(). the exact defenition and usage of functions will be explained later.

Trying to convert a string to an int will result in an exception.

```python
variable_a = "100" # string since the number is stored in string format
variable_b = int(variable_a) # int
print(variable_b) # prints 100
```

```python
variable_a = "zero" # string
variable_b = int(variable_a) # Raises Exception since zero cannot be converted to int
```

We will learn how to handle exceptions in the next section.

### Strings in Python

python has a lot of built in functions that can be used to manipulate functions, some of them are explained in the following program.

```python
some_string = "hello world, This is A test"
print(some_string.capitalize())  # Capitalizes the first character
print(some_string.count("a")) # Counts the number of times the character "a" occurs in the string
print(some_string.endswith("test")) # Returns True if the string ends with the substring "test"
print(some_string.find("gem")) # Returns the index of the first occurrence of the substring "gem" and -1 if it does not exist.
print(some_string.index("test")) # Returns the index of the first occurrence of the substring "test" and raises an exception if it does not exist.
print(some_string.upper()) # Returns a copy of the string in uppercase
print(some_string.title()) # Returns a copy of the string in title case
print(some_string.swapcase()) # Returns a copy of the string in swapcase
```

Try running this in your python interpreter and see what happens. A neat little hack in python to see all the functions available is to type `dir()` and see what functions are available.

```python
some_string = "hello world, This is A test"
print(dir(some_string)) # prints all the functions available with strings
```

now try each of the functions you get after running the snippet above and see what happens. you can try this with other types as well and see what happens.

### Functions in Python

Functions in python is a group of statements that may or may not take inputs and may or may not return values. Functions are usually used when you want to repeatedly call a piece of code without writing the same code over and over again.

```python
def greet(name): # this defines a function called greet with one parameter called name
    salutation = "Good Morning " + name # Note that the function body is indented, this is how python identifies the start of a python function
    return salutation # The return keyword returns the value of the function to the caller

print(greet("John")) # prints "Good Morning John"
print(greet("Jane")) # prints "Good Morning Jane"
# We only had to define the function once, we can call it as many times as we want
```

Take a note of the intendation structure of the code snippet, the functions body is always intended with a constant indentation of 4 spaces (or a tab).
Pythons function block ends when the code stops indenting, this is how python identifies the end of a function.

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

We have discussed about the boolean datatype earlier, we can leverage this datatype to create conditionals in python.

```python
print(1>2) # prints False
print(2*2 == 4) # prints True
print(True and False) # prints False
print( (2> 1) and (1 > 2) ) # prints False ( Evaluates to True and False )
(2 > 1) and print("2 is greater than 1") # prints 2 is greater than 1
(1 > 2) and print("1 is greater than 2") # prints nothing
```

This type of conditional statements are hard to read and make little to no sense, so we will use a different type of conditional statement called `if` statements. They are easier to handle and they can have multiple branching conditions as well.

```python
some_number = 5
if some_number > 1: # this is an if statement
    print("given number is greater than 1") # this is the body of the if statement
else: # this is the else statement
    print("given number is not greater than 1") # this is the body of the else statement
```

This is a very simple if statement, it has only one condition , if the condition evalues to True or 1 , then the body of the if statement is executed. if not the body of the else is executed. Try running this with different conditions to see what happens.

We can also write multiple branches of the same if statement by using elif.

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

### Python 2 vs Python 3

Throughout this course we will be using Python 3. In many machines python defaults to python 2 and it might cause issues when you try to run sample code, make sure that you are using python 3 (preferably the latest version) always.
