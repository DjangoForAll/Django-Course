# What is object oriented programming?

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

Now we have a class but it doesen't really do anything, to add some functionality lets look into a method called constructor.

constructors are used to initialize the object, In the earlier example we created a person object and assigned it to a variable called john, but the value of the attribute name was not changed, it was just a default value. Constructors can recieve arguments and change attributes of the object during initialization.

```python

```

# Classes in Python

# Principles in Object Oriented Programming

# Inheritance and Mixins
