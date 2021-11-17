-- Video Only

Now that we have a Model and its schema updated in the database, we can start learning the ORM.

The Django ORM is a clever piece of engineering that lets you interact with the database in a very natural way, no complicated languages or libraries required.

Lets learn how the ORM works by building our Tasks management app.

Before we get started, lets move all of our views from the urls.py file into the views.py file inside our app, views.py is where all the view related logic should reside.

After moving the views we will import the views into the urls.py file.

We'll start the server and check if the app is working fine as before.

Now we will modify the create tasks view to use the ORM to save the task to the Database

We'll start by importing the model at the top of the document.

```python
from tasks.models import Task
```

and instead of appending to the global variable we will rewrite it with the ORM.

```python
def add_tasks_view(request):
    new_task = request.GET.get("task")
    Task(title=new_task).save()
    return HttpResponseRedirect("/tasks")
```

And that's it! Just one line changed and we are now writing to a database. if you observe what we are doing here, you can see that we are creating a new object from the class Task with the values as parameters (note that they are named parameters) and then on the newly created object we are calling the save() method.

Django in the background checks the data is correct, and if everything is good, it will generate an SQL query to insert data into the tasks table and run the query on the database.

and now to retrieve the data from the database we can overwrite the get_tasks_view function.

```python
def tasks_view(request):
    all_tasks = Task.objects.all()
    return render(request,"tasks.html", {"tasks" : all_tasks})
```

Notice the statement `Task.objects.all()` , this is how we write an ORM query, Every model has a model manager that is responsible for the ORM queries. the `Task.objects` represents the Model manager for the Task model. the all method is a type of query that returnns all the objects in the database.

The output of this query is called a QuerySet. Querysets are iterable objects ( can be iterated in a loop ) that contain the data that is returned from the database.

In our example the queryset is passed into the template as a variable called tasks, When we try to view the page, we get something wierd, instead of the tasks being displayed we get something like `Task object (1)`, this is because each item in the queryset is an object of the Task Class. when we try to print or render an object, it will call the `__str__` method, which is the method of the class that converts a given object to a string. lets create this method in the Task Class and see what happens.

```python
def __str__(self):
    return self.title
```

Now if you refresh the page, you will see the tasks are displayed as usual.

There is another way to solve this issue, In our html template, we can specify which attribute to render. lets try that method as well.

```html
{% for task in tasks %}
<h2>
  {{ forloop.counter }} {{ task.title }} - {{ task.created_date }}
  <a href="delete-tasks/{{ forloop.counter }}">delete</a>
</h2>
{% endfor %}
```

This way we are explicitly asking to print the title attribute of the task object along with the time of creation.

What if we wanted to search for a particular task? Lets try that.

Lets create a new search bar in out html template and add a search button. we'll make it using regular html forms. we'll reuse the list view we created earlier.
We'll leave the action empty because we want to use the same url.

Our view should filter based on the search term if its present, if not it should return all the tasks.

Lets first fetch the term from the request. and then filter the data based on the term.

```python
search_term = request.GET.get("searchterm")
if search_term:
    all_tasks = all_tasks.filter(title=search_term)
```

all_tasks is the variable that stores the current queryset, we then applied a filter to it, filtering the data based on the search term. currently we check if the term is exactly the same as title.

This is kinda useless becuase we have to search for the exact term to fetch it, lets build a better version of the serach.

Lets change the part where we filter the data based on the search term.

```python
all_tasks = all_tasks.filter(title__icontains=search_term)
```

This performs a contains search instead of a exact search. The `i` in the `icontains` is to make the serach case insensitive. `title__icontains=search_term` is used when you want a case sensitive search.

Now if we try it out, we can see that the search works just fine!

In the last method we deleted the task from the database with the use of an loop index, With databases a loop index is not going to work ( It may work but it will make the whole process a lot more complex ) , instead we will use the objects primary key or the id.

we will change the html to send over the id instead of the loop index

```html
{% for task in tasks %}
<h2>
  {{ forloop.counter }} {{ task.title }} - {{ task.created_date }}
  <a href="delete-tasks/{{ task.id }}">delete</a>
</h2>
{% endfor %}
```

Now we can uniquely idenity the task to be deleted

In the delete view we can fetch the row of data with the id and then delete it from the database

we can rewrite the delete view like this

```python
def delete_tasks_view(request,index):
    Task.objects.filter(id=index).delete()
    return HttpResponseRedirect("/tasks")
```

`delete` is a method of the queryset class that deletes the row from the database, we first filtered the data to match the id and then deleted it.

Thats it! Our Application is now working with databases.
