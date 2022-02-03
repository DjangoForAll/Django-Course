Here are a few tips on solving the milestone. I recommend reading them only if you are completely stuck, most of the content can be found with simple internet searches.

### Styling

Since Django renders the forms for us, modifying attributes and structure of input elements start to get complicated, especially when using front-end styling frameworks that require special classes to be added to the form elements. Enclosing the form elements in separate divs is also made harder.

Here are some of the solutions for this problem

- Adding Styles in the Form 
    In Django, each of the form element/input element is called a [widget](https://docs.djangoproject.com/en/4.0/ref/forms/widgets/#widget) and we can modify the behavior of the widget when a form class is initialized.

    ```python
    class TaskForm(ModelForm)

        class Meta:
            model = Task

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['title'].widget.attrs['class'] = 'my_class'
    ```
    `self.fields` is a dict that maps all the input elements as a Widget Object to the field name, we can select the input element and then add a class to it, we are not limited to a class name change here, any HTML attribute of a form element can be edited in this way.

- Restructuring Forms
    This is documented extensively in the [Django Docs](https://docs.djangoproject.com/en/4.0/topics/forms/#working-with-form-templates)

These are not the only ways to solve the problem, there might be tons of packages out there that can solve these types of problems, but for the milestone, we can focus on using plain Django.

### Handling Priority Logic

- The priority cascading logic can be written in a lot of methods, The most common method is to override the `form_valid` method in form-based generic views. The `form_valid` method is called when valid data is submitted to the form and the validations have been completed. Check the following [Django Doc](https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/) for more information.


### General Tips
    - Try to document your approach.
    - Try to build the logic in the easiest way possible.
    - Using methods like `exists`, `count`, `get`, `save`, etc on ORM objects cause queries to the database, try to minimize them as much as possible.
    - Read about bulk operations that Django provides to optimize your code, Read about them [here](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#bulk-update)
    - Try thinking about concurrency based problems that might arise ( Brownie Points )
    - Make sure that the design exactly matches the provided mockup.
    - Ensure that the priority cascade logic handles form updates as well.
    - Keep things DRY (DRY = Do Not Repeat Yourself)