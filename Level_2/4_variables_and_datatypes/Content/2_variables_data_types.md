### Variables and Data Types

let's try to build a program that doubles a given number.

```python
number = 5
print(number * 2)
```

in the above program, we have defined a variable `number` and assigned it the value 5. Variables are used to store values. data stored in variables have types, in this case, it is int ( short for integer ), some of the other data types in Python are explained in the following program.

```python
ratio = 1.5 # float (short for floating point)
salutation = "Hello" # string
is_even = True # boolean
```

you can name the variables anything you want but the standard way to name variables is to use [snake cases](https://en.wikipedia.org/wiki/Snake_case) ( lowercase words separated by underscores like snake_case ), this is the convention used by python.

variable names should be descriptive, they should be meaningful and easy to understand. they should not start with a number and they should not be a [reserved keyword](https://docs.python.org/3.9/reference/lexical_analysis.html?highlight=reserved#keywords) ( these are special words that python users like `print` naming variables with these names can cause unexpected results ).

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
some_int = int(some_variable) # explicit type conversion ( Value is floored )
print(some_int * 2) # prints 2
```

The int() function converts a given data type into an integer, similarly, float() converts a given data type into float.
similar functions exist for other data types like str(), bool(). the exact definition and usage of functions will be explained later.

- Note that converting a float to an int will truncate the decimal part of the number. (Flooring the number)

Trying to convert a non-numeric string to an int will result in an exception.

```python
variable_a = "100" # string since the number is stored in string format
variable_b = int(variable_a) # int
print(variable_b) # prints 100
```

```python
variable_a = "john" # string
variable_b = int(variable_a) # Raises Exception since john cannot be converted to int
```

### Strings in Python

python has a lot of built-in functions that can be used to manipulate functions, some of them are explained in the following program.

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

### F strings

F strings are a relatively new addition to python ( since 3.6 ), they are a way to format strings in python.

here are some examples of f strings :

```python
some_variable = "john"
print(f"hello {some_variable}") # prints hello john
print(f"{some_variable.upper()}") # prints JOHN
print(f"{1+2-3}") # prints 0
```

F strings make string formatting easier and more readable.

- Note that all F strings start with `f` right before the start of the quotation marks
- Expressions have to be surrounded with a curly brace `{}` to be replaced by their value
