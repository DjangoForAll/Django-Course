Python comes packaged with a library called `unittests`, this library can be used to create simple tests, Lets take it for a quick test drive.

Lets create a new folder along with a python file ( lets call it `calculate_area.py` ), the python file can have the following method

```python

def calculate_square_area(side):
    """
    Calculates the area of a square, given a side
    """
    return side*side

```

Simple enough right? Lets create a simple test that check if the method actually works as intended and ensure that all edge cases are handled.

Lets create a new python file to write our tests, lets name this file `test_calculate_area.py`

```python
import unittest

from .calculate_area import calculate_square_area

class TestSquareArea(unittest.TestCase):
    def test_area_logic(self):
        self.assertEqual(calculate_square_area(2),4)
        self.assertEqual(calculate_square_area(3),9)
```

All test methods should start with test_ , this is how unittest knows that it is a test method.

All tests are a subclass of `unittest.TestCase`, this base class provides a lot of functionality when running tests, it helps keep tracks of tests that failed, printing pretty versions of the output and so much more.

Now that we have the tests written, lets run our test with the following command

```bash
python -m unittest test_calculate_area.py
```

Now that we can run our tests, lets add a new test to ensure that we handle strings as well.

```python
import unittest

from .calculate_area import calculate_square_area

class TestSquareArea(unittest.TestCase):
    def test_area_logic(self):
        """
        Ensure that our function has the correct logic
        """
        self.assertEqual(calculate_square_area(2),4)
        self.assertEqual(calculate_square_area(3),9)
    
    def test_handle_strings(self):
        """
        Convert strings to numbers and then calculate their area
        """
        self.assertEqual(calculate_square_area('2'),4)
        self.assertEqual(calculate_square_area('3'),9)
    
    def test_handle_non_numbers(self):
        """
        Ensure that we return -1 when the input cannot be converted into a number
        """
        self.assertEqual(calculate_square_area('a'),-1)
```

Now if we re-run our tests, most of them will fail because our method does not handle edge-cases or type conversions, go ahead and try to fix the issues by yourself, re-run the tests once you are done to confirm the results.

Python unittests are great for testing simple methods, to test more complicated web applications, Django provides its own testing framework, Django also uses python unittests in the background, in the next chapter we will take a look at testing our task management application.