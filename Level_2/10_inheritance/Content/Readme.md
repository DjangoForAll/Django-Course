# Inheritance

One of the most important features of OOP is inheritance. Inheritance is a way to create new classes from existing classes. This is done by using the `class` keyword followed by the name of the new class and the name of the existing class. The new class inherits all the methods and attributes of the existing class. The new class can also have its own methods and attributes. The new class is called a subclass while the existing class is called a superclass. The subclass can also override attributes and methods from a superclass ( create its own versions of attributes and methods ).

Let's look at an example.

```python
class LivingThing:
    def breathe(self):
        print("I am alive")

class Plant(LivingThing): # We are inheriting from LivingThing
    def speak(self):
        print("I am a plant")

class Animal(LivingThing): # We specify the parent class in parenthesis
    def move(self):
        print("I am moving")

class Dog(Animal):
    def speak(self):
        print("Woof?")

my_doggo = Dog()
my_doggo.breathe() # I am alive
my_doggo.move() # I am moving
my_doggo.speak() # Woof?
```

The above code creates a new object from the class Dog. The Dog class inherits all the methods and attributes from the Animal class. The Dog class also has its own methods. The Dog class is called a subclass while the Animal class is called a superclass.

The Animal Class in turn inherits from the LivingThing class. The LivingThing class has a method called `breathe` which prints out the string `I am alive`.

This is called inheritance. Specifically, In this case, Multi-Level Inheritance.

Classes can also override methods in their parents, this is used to redefine the behavior of a method.

for example

```python
# Continuation from existing code
class Turtle(Animal):
    def move(self): # Overrides Animal's move method
        print("I am moving, but kinda slowly!")

my_turtle = Turtle()
my_turtle.move() # I am moving, but kinda slowly!
my_turtle.breathe() # I am alive
```

Similarly, you can create attributes in the subclass and override them as well.

like multilevel inheritance, python also supports multiple inheritance. This is used when we want to inherit from multiple classes.

```python
class A:
    def print_a(self):
        print("A")

class B:
    def print_b(self):
        print("B")

class AB(A,B): # This class inherits from both A and B
    def print_ab(self):
        print("AB")

ab = AB()
ab.print_a() # A
ab.print_b() # B
ab.print_ab() # AB
```

Each python object has a method resolution order ( MRO ) which is a list of classes that are used to resolve the method. The MRO is used to determine which class to call when a method is called. Let's say that each of the inherited classes has the same function, to identify which method is called we use the MRO.

```python
# Continue from the above example

print(ab.mro()) # [<class '__main__.AB'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# The MRO is [AB, A, B, object] so the AB class is checked first then the A class and then the B class.
```

## Mixins

When developing applications you might come across common functionality that is shared between a number of classes, in python each feature can be built into different classes and then combined together to create a new class with the functionality required.

In the above examples we created classes and defined functionality in them, another approach is to create classes with functionality and combine them together to create a new class.

```python

class RunnableMixin:
    def run(self):
        print("Can Run")

class WalkableMixin:
    def walk(self):
        print("Can Walk")

class TalkingMixin:
    def talk(self):
        print("Can Talk")

class Animal(RunnableMixin, WalkableMixin):
    pass

class Human(RunnableMixin, WalkableMixin, TalkingMixin):
    pass

```

Each of the feature classes is called a Mixin. Mixins are extremely useful in web development to add new features to existing classes.
