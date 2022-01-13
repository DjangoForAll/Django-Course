Till now we were creating forms manually, but Django provides a way to abstract the form creation as well, lets see how that works.

Similar to `ListView` which we saw earlier to abstract the listing of objects, CreateView abstracts object creation.

Lets create a class based view for the `Task` model.

```python

from django.views.generic.edit import CreateView

class CreateTaskView(CreateView):
    model = Task
    fields = ("title","description" , "completed")
    template_name = "task_create.html"
    success_url = '/tasks'
```

The model refers to the model we want to create a new object for. the fields refer to the fields we want to display in the form, anything that is not in the fields will not be displayed in the form and the user wont be able to edit them even if he wants to.
An excellent example for this is the created_date, since the field is not added to the fields variable the user wont be able to edit it, even if they want to.

The template name as usual refers to the template that we created for this view, The template name is actually optional, the default template name is always `<model_name_lowercase>_<action>` where action is list, form etc.

The success url is simply the url to be routed to after the form is successfully submitted. if there are errors in validation then the errors are displayed in the form and the user is redirected to the same page.

Now lets edit the html form

```html
<h4>Create a new Task</h4>
<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" value="Save" />
</form>
```

That's it! `form.as_p` converts the form object that django created into html, so that we can display the form in the template.

Django has a very Useful Form Class, Form Classes are not necessarily connected to a model, they can be used to describe regular forms as well.

Lets actually create a form class to see what is happening behind the scenes

```python

from django.forms import ModelForm

class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title","description","completed"]

class CreateTaskView(CreateView):
    form_class=TaskCreateForm
    template_name = "task_create.html"
    success_url = '/tasks'
```

Here instead of letting django create a form on its own, we first created a Form and then passed it on to the CreateView, This performs the exact same task as the previous snippet, but this time we can write our own logic inside the form class.

Lets say that our tasks must be atleast 10 characters long! we need to send an error back whenever it is not the case.

To build something like that we can write field validations in the form class.

```python

class TaskCreateForm(ModelForm):

    def clean_title(self):
        title = self.cleaned_data["title"]
        if(len(title) < 10):
            raise ValidationError("The value must be atleast 10 charecters")
        return title

    class Meta:
        model = Task
        fields = ["title","description"]

```

The form class dynamically searches for methods with the name `clean_<fieldname>` and calls them when the form is validated. The clean methods should return the cleaned value, Lets say that you wanted to keep the title in uppercase, you could do operations like that here.

Raising Validation Errors won't actually stop execution here, instead Django forms will catch it and display the error in the form.

Similar to the clean methods, the form class also has a couple of methods that are called when the form is submitted, I'll leave documentation regarding all the possible methods in the text.

Placing the right logic in the right method allows you to reuse the same form for multiple usecases, lets try and create an update view for our tasks.

lets create a new route for the update view `tasks/<pk>/update` and create a new view for it. pk stands for primary key, since our primary key is an integer the `<pk>` can be replaced with any integer.

The routes for the same will be

```python
path('tasks/<pk>/update' , UpdateTaskView.as_view()),
```

The UpdateTaskView Class will have the following defenition

```python
class UpdateTaskView(UpdateView):
    model=Task
    form_class = TaskCreateForm
    template_name = "task_create.html"
    success_url = '/tasks'
```

UpdateView is a generic baseclass that django provides us that allows us to edit an object given its PK (Primary Key)

Lets finally add the update button to the list page

```html
<a href="tasks/{{ task.id }}/update">update</a>
```

Now lets revisit the listing page and try the update button. And it works as expected!

Any logic you had in the create view is now shared in the update view as well.

The beauty of generics comes during changes in models and structures, if you decide to add a new field to the model, you just need to specify if the field needs to be updated or not and django takes care of the rest!
