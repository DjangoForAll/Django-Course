## Encapsulation

Encapsulation is the process of wrapping the data and code together to prevent data from being accessed by other parts of the program. This is done so that we dont manually change the attributes of the object, which could cause unexpected results.

```python
class Person:
    name = "Person"

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

john = Person("John")
john.name = "Jane"
john.greet() # Hello, my name is Jane
```

Here we manually changed the value of an attribute and it caused the function to produce an unexpected result, Python does not enforce very strict rules to prevent accidental changes like these from happening, but there are standards that we can follow.

In Python there are protected members, which are members that can only be accessed by the class itself or its subclasses.

```python

class Person:
    _name = "Person"

    def __init__(self, name):
        self._name = name

    def greet(self):
        print("Hello, my name is " + self._name)
john = Person("John")
john.name = "Jane" # Creates a new attribute but does not edit the existing _name attribute
john.greet() # Hello, my name is John
```

Protected members are only a convention, and they are not enforced by Python. You can directly change the \_name value, Usually this is not a good idea.

Python also has a concept of private members, which are members that can only be accessed by the class itself, Even a base class cannot access these members.

```python
class Person:
    __name = "Person"

    def __init__(self, name):
        self.__name = name

    def greet(self):
        print("Hello, my name is " + __name)
john = Person("John")
john.__name = "Jane" # Creates a new attribute but does not edit the existing __name attribute
john.greet() # Hello, my name is John
```

Private members are also by convention only since these members can be accessed in the following format : object.\_<class_name><private_member_name> or in our case `john._Person__name`

Python does not really do any type of enforcement on private or protected members, but it is a convention to follow when desigining classes.

For the curious folk who want to know how python does this internally, check out this [link](https://docs.python.org/3/tutorial/classes.html#private-variables)

## Abstract Classes

An Abstract class is a class that contain blueprints for other classes to inherit from. An Abstract class does not contain any implementation but it defines a common interface for its subclasses.

Abstract classes are not used in our course so we'll leave it here, if you want to learn more about abstract classes and how to create them in python you can visit this [page](https://docs.python.org/3/library/abc.html)
