Python Operators like `+` , `-` can be overloaded to perform different operations based on what object is being operated on. To make things clearer lets view an example

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # Overloading the `+` operator
        return Point(self.x + other.x, self.y + other.y)
    # Self is the object on the lhs and other is the object on the rhs

    def __sub__(self, other): # Overloading the `-` operator
        return Point(self.x - other.x, self.y - other.y)

    # This is called when the object is printed or converted to a string
    def __str__(self): # Overloading the `str` operator
        return f"({self.x}, {self.y})"

point_a = Point(1, 2)
point_b = Point(3, 4)
print(point_a + point_b) # Output: (4, 6)
print(point_a - point_b) # Output: (-2, -2)
```

Note that the results from the operations are new objects and not the original objects. Lets see a short example to understand this behaviour

```python
var_a = 1
var_b = 2
print(var_a + var_b) # Output: 3
```

In the above example the value of var_a and var_b are not changed. The result of the operation is a new object with the result. Similarly when the overrode the `+` and `-` operators we return a new object instead of editing the original object. This is the expected behaviour.

Note that the function \_\_sub\_\_ , \_\_add\_\_ are magic or dunder methods , we dont manually invoke these functions, python calls them when needed.

We can also override comparison operators, bitwise operators and logical operators. The entire list along with the documentation can be found [here](https://docs.python.org/3/reference/datamodel.html#special-method-names)

Try overriding different methods and see what happens.
