Here are a few tips on solving the milestone. I reccomend reading them only if you are completely stuck, most of the content can be founbd with simple internet searches.

### Styling

Since Django renders the forms for us, styling becomes an issue, especially when using front end styling frameworks which require special classes to be added to the form elements. Enclosing the form elements in seperate divs is also made harder.

Here are some of the solutions for this problem

- Adding Styles in the Form 
    In Django each of the form element/input element is called a [widget](https://docs.djangoproject.com/en/4.0/ref/forms/widgets/#widget) and we can modify the widgets behaviour when a form class is initialised.

    ```python
    class TaskForm(ModelForm)

        class Meta:
            model = Task

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['title'].widget.attrs['class'] = 'my_class'
    ```
    self.fields is a dict that contains all the input elements as a Widget Object, we can select the input element and then add a class to it, we are not limited to a class here, any HTML attribute of a form element can be edited in this way.

- Restructuring Forms
    This is documented extensively in the [Django Docs](https://docs.djangoproject.com/en/4.0/topics/forms/#working-with-form-templates)

These are not the only ways to solve the problem, There might be tons of packages out there which can solve these types of problems, but for the milestone, we can focus on using plain Django.

### Handling Priority Logic

- The priority cascading logic can be written in a lot of methods


### General Tips
    - Try to document your approach.
    - Try to build the logic in the easiest way possible.
    - Using methods like `exists`,`count`,`get`,`save`,etc on ORM objects cause queries to the database, try to minimise them as much as possible.
    - Read about bulk operations that django provides to optimise your code, Read about them [here](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#bulk-update)
    - Try thinking about concurrency based problems that might arise ( Brownie Points )
    - Make sure that the design exactly matches the provided mockup.
    - Ensure that the priority cascade logic handles form updates as well.
    - Keep things DRY (DRY = Do Not Repeat Yourself)