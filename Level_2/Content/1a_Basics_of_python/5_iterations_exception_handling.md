### Iterations in Python

Iterative statements are used to execute a block of code multiple times. usually, until a given condition has been reached. python has a few ways to do this, let's start with the `while` statement first.

```python
i = 10
while i > 0:
    print(i) # prints 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    i = i-1 # decrement i by 1
```

The simple program written above can be used to print the number from i to 0, be careful when working with loops because you can end up in an infinite loop. in the case above, if we were to remove the decrementing step, the code would print 10 forever ( like forever! ) in case you do end up in an infinite loop use `ctrl + c` key combination to stop the program execution.

We can also `break` out of a loop at any point. similarly, we can also cause the loop to skip over some code by using the `continue` statement.

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

When the while loops condition is always True like in the code snippet above, it will run forever. In such cases, we would have conditions inside the code that break out of the loop, in the case above we have a condition that breaks out of the loop when i is 0. Similarly, we also skip the code execution when i is 5 which causes it to skip it from printing.

Try the snippet above and see what happens.

Although while loops are extremely useful, python provides another iterative statement called `for`. for loops are used to iterate over a sequence (lists, dictionaries, string, or anything iterable).

```python
contact_list = ["John", "Jane", "Mary"]
for contact in contact_list:
    print("Hello" , contact) # prints Hello John, Hello Jane, Hello Mary
```

This for loop iterates over the list and prints the contact name with a greeting. similarly, we can loop over a string or a tuple or even a dictionary.

Python has a built-in function to build a list of numbers called `range`. `range(start, stop, step)` can be used to build a list of numbers to be iterated over.

```python
for i in range(0,10,2):
    # start value is included , end value is NOT included
    print(i) # prints 0, 2, 4, 6, 8
```

_Advanced Reading_ : _Python has a concept of iterators and generators. Iterators are objects that are used to iterate over a sequence. Generators are functions that return iterators. They are a bit hard to understand at first but once you get them you will understand them very well. You can find a full list of iterators and generators in the [Python documentation](https://docs.python.org/3/glossary.html#term-iterator)._

### Exceptions and Handling them

Errors are called Exceptions in the python world, Python provides a mechanism to handle errors in your code. This process is called exception handling.

More than often programs behaves in ways they are not supposed to, this might be caused by a bug in the code, wrong inputs given, missing files, or a wide variety of other reasons. if we don't have exception handling the execution stops right after the error and the program is not able to continue. Exception handling solves this issue and allows us to define the way we want the program to behave in case of an error.

```python
numerator = 5
denominator = 0
print(numerator/denominator) # Causes an Exception and stops the execution
print("This line will not be printed")
```

To solve the case above we can use the `try` and `except` block.

```python
try:
    numerator = 5
    denominator = 0
    print(numerator/denominator) # Causes an Exception and moves to the execute block
    print("This is still not printed")
except ZeroDivisionError:
    print("You cannot divide by zero")
print("This line will be printed")
```

The try block is the block that we want to execute, the except block is the code that we want to execute if an error occurs.

Note that the statements after the error in the try block are skipped, Once an error occurs the rest of the try block is skipped and the except block is executed immediately.

We can specify what kind of exceptions we want to handle in the except block and even define separate behavior for different types of exceptions by creating multiple except blocks.

We can also add generic exception handling by using the `except` keyword without specifying the exception type. This will handle all the exceptions that are not handled by the other `except` blocks. We can also add a `finally` block to the `except` block to execute code after the `try` block has been executed. The `finally` block is executed whether an error occurs or not.

Exceptions in python can also be raised by the programmer, this is done using the `raise` statement. This is useful when we want to force the execution to move to the except block. we can create new exceptions as well, we will learn about them in the next chapter

Here is an example of exception handling with all the concepts explained till now.

```python
try:
    numerator = 10
    denominator = 0 # Change this to see different execution flows
    if denominator > 100:
        raise ValueError("Denominator cannot be greater than 100")
    print("Answer is" , numerator/denominator)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("Value Error! Denominator Must be < 100") # Catches the Value Error
except:
    print("Something Happened")
finally:
    print("All operations have been completed")
```

Try the code above with multiple values for the denominator and observe what happens.
