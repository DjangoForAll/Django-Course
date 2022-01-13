The delete function deletes a row from the database permanently. usually, applications dont necessarily do a full delete, instead they perform soft deletion.

soft deletion is a way to mark a row as deleted, we'll have a boolean field that is set to true when a row is deleted.

soft deletion is useful when we want to keep a record of a deleted row, like an audit trail or when other tables depend on this row ( We'll see this later) .

Lets implement soft deletion in our task management app.

Lets first create a new field called `deleted` in our Model Class

```python
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```

Now run `makemigrations` and then `migrate` to complete the change process

Now we will rewrite our list and delete view to support soft deletion

we will rewrite our delete view as :

```python
def delete_tasks_view(request,index):
    Task.objects.filter(id=index).update(deleted=True)
    return HttpResponseRedirect("/tasks")
```

Instead of the delete method, we are calling the update method on the queryset, the update method will update the value of the given attributes on all the selected rows with the new value, in this case the deleted value to True.

Now we will rewrite our list view to only show the tasks that are not deleted.

```python
def tasks_view(request):
    all_tasks = Task.objects.filter(deleted=False)
    search_term = request.GET.get("searchterm")
    if search_term:
        all_tasks = all_tasks.filter(title__icontains=search_term)
    return render(request,"tasks.html", {"tasks" : all_tasks})
```

Instead of the `all` method that returns all the rows, we are calling the `filter` method with the condition `deleted=False` that only fetches rows that are not deleted.

> ORM Queries are chained, so if you have two filter methods, both of them are applied to the queryset.

And Now our application support soft deletion as well!
