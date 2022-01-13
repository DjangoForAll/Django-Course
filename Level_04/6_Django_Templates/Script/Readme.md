Writing HTML in python is extremely hard, especially when pages get really huge and complex. Django has a convenient solution for this called templates,
Templates are simply html or text file with some special syntax that describes how dynamic content should be made.

Templates are converted into HTML using template engines, Django comes with its own template system called Django Template Language (DTL).

DTL is not a replacement for HTML, DTL is used for creating Dynamic Content whether HTML, an email or even just plain text.

We'll create a new template with DTL and see how exactly it works.

Templates can be placed inside a folder called `templates`, these are usually placed in the root of the project, This is just a good practice and is not mandatory.

Lets create a template folder and a template file called `tasks.html` inside it, we'll also add some static content in it.

Now we have to let django know where we created the templates folder, we have already discussed that all configurations go inside the `settings.py` file.

This file also has default configurations on how to handle templates, we'll add the path to the template folder to the `TEMPLATE_DIRS` variable.

we wont look into the other configurations until we work with them.

Now we can render this template using the render function that ships with django, The render function can be imported from the `django.shortcuts` module.

Once imported we can create a response by passing the request and the name of the template file to the render function. The render function will then create an HTML response object from the given file. And we can return this response object to the client. Now we should be able to serve our template. Lets refresh the view and test it out.

Now we have static file rendering, lets make it more dynamic!

we can pass in data into the template by adding context to the render function, the context is a dictionary that can be used to pass in data into the template.

Now to access this value in the template we have to enclose the variable name in double curly braces, for example `{{ tasks }}` , when rendering django will look for the variable `tasks` in the context and replace it with the value. This is how DTL is written in HTML.

You can also do conditions, iterations and methods in DTL, we will look into some more aspects of the render function

Note that the first argument to the render function was the request object, This is used to get request context inside the template, the request context usually contains information like the logged in user name , the current path, parameter values etc.. we will take a quick example to see how this works.

lets try to fetch the value `request` inside the template, note that we dont really pass the value explicitly, it is added by django. we can see that the value is `<WSGIRequest: GET '/'>` this is the request object , lets go one step further and try to get `request.GET` which is a dictionary containing the GET parameters. Note that everything is case sensitive

Now we get an empty dictionary rendered, lets try and create some GET parameters, now we can see that the parameters are rendered in the template

You can even try to render a specific value in the template, for example `{{ request.GET.tasks }}` if the parameter does not exist it just does not render anything.

we can also create conditions inside the template, for example

```html
{% if request.GET.tasks %}
<h1>Yay We Have Values</h1>
{% else %}
<h1>No tasks</h1>
{% endif %}
```

The if statement here is called a tag in DTL, anything between the `{%` and `%}` is a tag. tags are more complex that simple variables, not all tags require a closing tag

In python we mark the end of a statement block using intendation, but HTML and DTL does not use intendation for any logical statements which is why we use endtags to mark the end of a DTL block. Most programming languages like java or C/C++ use brackets to contain statement blocks.

The for tag can be used to iterate over objects, let's pass a list in the context and try iterating over it.

```python
tasks = ["Complete Django Tutorial" , "Study Django Rest Framework"]

{% for task in tasks %}
    <li>{{ task }}</li>
{% endfor %}
```

We can also iterate over dictionaries , replace the tasks with request.GET and try it out.

Play around with templates and experiment what you learned.
