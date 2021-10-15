## What is object oriented programming?

In python everything is an object, You can think of an object as something that holds a collection of data and methods that act on those data.
The objects are created from classes.

You can think of classes as blueprints for creating objects. You can think of objects as something that was created with those blueprints. you can create as many objects you want from a class.

By organizing code into classes, you can make your code more readable and easier to maintain. Unorganized code ( also known as spagetti code ) is extremely hard to debug, maintain or understand. One of your job as a software developer is to ensure that your codebase does not become a house of cards over time.

Now that you know what a class and object is, lets take a quick example of how they can be created and used.

```python
class Person: # This syntax creates a new class called Person
    name = "Person" # This is a class variable, it is shared by all instances of the class ( all objects )

# Note that the data and methods of a class are defined in the class block

john = Person() # This is the syntax used to convert a class into an objects
# Converting a class into an object is called instantiation, We create an instance of the class as an object
print(john.name) # Prints out Person
# We can access by using the dot notation : <obj_variable>.<class_variable>
```

- Note that class names are always in [UpperCamelCase](https://en.wikipedia.org/wiki/Camel_case)

Now we have a class but it doesen't really do anything, to add some functionality lets look into a method called constructor.

constructors are used to initialize the object, In the earlier example we created a person object and assigned it to a variable called john, but the value of the attribute name was not changed, it was just a default value. Constructors can recieve arguments and change attributes of the object during initialization.

In python constructor methods are called magic methods or dunder methods. They are prefixed and suffixed with two underscores ( since devs could not pronounce the underscores each time they started to call it dunder methods or double underscore methods ), The consstructor is called a magic method becasue we dont call it manually, it is called automatically when an object is created. The constructor in python is called \_\_init\_\_.

```python
class Person:
    full_name = "Person"

    def __init__(self, first_name , last_name): # This is a constructor
        full_name = first_name + last_name # This is an instance variable, it is unique to each instance of the class

john_doe = Person("John","Doe") # Pass the first and last name as arguments to the constructor
print(john_doe.full_name) # Prints John Doe
```

Notice that the first argument in the constructed was `self` , this is not an argument that we pass onto the constructor, it refers to the object that called the method, so if you wanted to access another attribute of the object you can use the self.<variable_name>

```python
class Person: # Create a new Class Person

    name = "Person" # Default Attributes
    salutation = "Hello"

    def __init__(self , name):# Note that name is both a parameter and a class attribute
        self.name = name # self.name refers to the class attribute and the other one refers to the parameter

    def greet(self): # Create another class method that returns a greeting
        return self.salutation + self.name # self is the object on which the method is called

john = Person("John Doe")
print(john.greet()) # Prints Hello John Doe
jane0 = Person("Jane Doe")
print(john.greet()) # Prints Jane Doe
```

note that the objects do not share any attributes.

To Quickly find out the class of an object we can use the built-in type function

```python
print(type(1)) # Prints <class 'int'>
print(type("123")) # Prints <class 'str'>
print(type([1])) # Prints <class 'list'>
print(type({"key" : "val"})) # Prints <class 'dict'>
```

Now that you have some idea about Object oriented Programming, lets take a look at all the features it provides along with examples
