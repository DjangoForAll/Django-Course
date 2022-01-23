Let's take a better look at the ORM using the Django shell, Django shell is simply the python interactive interpreter with Django configured, since Django is configured, you can interact with the Django ORM without any additional setup.

To run the Django shell run the following command in the root of the project:

```bash
python manage.py shell
```

Once this command executes, it should open up a python interactive shell, you can now start interacting with the ORM.

let's start with importing the Model Class we created earlier.

```python
from tasks.models import Task
```

### Making Queries

Once the Task model class is imported, we can start to run operations on it.

```python
Task.objects.all()
```

Running the above code snippet fetches all the tasks in the database as a queryset.

```python
print(Task.objects.all())

# We can also fetch all the values or specific values from the database using the values method.
Task.objects.values() # Returns a list of dictionaries with all the values as keys, Note that this fetches all the attributes of a task
Task.objects.values('title') # We can ask the ORM to fetch only the fields that we require only
Task.objects.values('title','completed') # We can also pass in a list of fields to fetch
```

Querysets are lazy in nature, as in they do not call the database unless you do something to evaluate the queryset.

```python

tasks = Task.objects.all() # This just creates a queryset, Do database operations are performed here

for task in tasks: # This is where the actual database operations are performed, The queryset is evaluated here
    print(task)
```

### Counting Rows

We can get the count of rows in the database with the count method on a queryset, Note that getting the count does not fetch all the data, the database only returns the data we ask for, in this case, the count of tasks in the database.

```python
tasks_count = Task.objects.all().count() # Fetches the Count of tasks in the database
print(tasks_count)
```

### Filtering data

We can filter tasks in the database using the filter method, the filter method also supports field lookups, more details are available [here](https://docs.djangoproject.com/en/4.0/ref/models/querysets/#field-lookups)

```python
tasks = Tasks.objects.filter(deleted=False) # Gets all the tasks that are not deleted
tasks = tasks.filter(completed=True) # Gets all the tasks that are completed
```

If you notice the above example, we are filtering based on two fields separately, this is called filter chaining, the resulting queryset will have all the tasks that are not deleted and are completed.

### Ordering Data

We can also let the database return ordered data, we can use the `order_by` method on a queryset to order the data.

```python
tasks = Task.objects.all()

tasks.order_by('created_at') # Orders the tasks by created_at in ascending mode
tasks.order_by('-created_at') # Orders the tasks by created_at in descending mode

tasks.order_by('completed','-created_at') # Orders the tasks by completed ascending and then for rows with the same completed value, use created_at in descending mode
```

### Slicing Querysets

Like slicing lists, we can also slice the queryset, Slicing data without an ordering method is not recommended as we may get different results each time. Negative indexing is not supported in the ORM, for more reading look [here](https://docs.djangoproject.com/en/4.0/topics/db/queries/#limiting-querysets)

```python
tasks = Task.objects.all()
tasks[0:5] # Gets the first 5 tasks
tasks[5:10] # Gets the next 5 tasks
```

### Checking if data exists

Sometimes it might be useful to check if there is any data in the database, we can use the `exists` method on a queryset to check if there is any data in the database against a given filter query.

```python
tasks = Task.objects.filter(completed=True)
tasks.exists() # Returns true if the row exists and false if not
# We can also ask the ORM to fetch the first row from the database, if the row does not exist the method will return None
tasks.first()
# This returns the first row that matches the query we have specified
```

### Playing with objects

Each object of the queryset is an object of the model class that we have created, This object can be manipulated if needed. 

```python

tasks = Tasks.obects.all()
task_obj = tasks[0] # Get one of the task as a task object
task_obj = tasks.first() # Another way to get a task object from a queryset, This particular method get the first row from the database

task_obj.completed = True # Set the completed field to True
task_obj.save() # Update all the changes that we have made into the database. In our case, it updates the completed field to True
# Django is not intelligent enough to understand that we have only changed the completed value, So instead it updates all the values with what it knows last, ie it updates all the values in the current task_obj to the database

task_obj.save(update_fields=["completed"]) # We can also explicitly ask Django to update only the fields we provide in this list, that way it does not have to update all the attributes to the database.

task_obj.user # This will return the user object that is associated with the task object, This object can again be manipulated and saved.
```

### Summary

Django has a very powerful ORM, almost everything you will ever need to do with data can be performed through the ORM, Learning the ORM and what it can do is a great way to learn the framework. I recommend everyone to go through the [official documentation](https://docs.djangoproject.com/en/4.0/ref/models/querysets/) to get a clear and concise idea of what the ORM is what its capabilities are.
