Now that we have our List, Create and Update Views, we can create our missing View, The Detail view

The detail view is very similar to the list view, but instead of showing all the items, we just show one item in detail.

Django provides the generic class DetailView for exactly this purpose, Lets first create the new route for the detail view and then the rest

```python
path('tasks/<pk>' , TaskDetailView.as_view()),
```

Our class defenition will look like this

```python
class TaskDetailView(DetailView):
    model = Task
    template_name = "task_detail.html"
```

and our template will look like this

```html
<h2>Title</h2>
{{object.title}}
<h2>Description</h2>
{{object.description}}
<h2>Created At</h2>
{{object.created_date}}
```

The object refers to the selected object and is passed to the template.

Finally we can add the link to view the details of the object in the list view.

```html
<a href="tasks/{{ task.id }}">detail</a>
```

Now that the Detail view is implemented, we can look at the delete view, currently the delete operation is performed over the GET method, since the delete operation caused changes in models ( side effects ) we have to change it to POST.

But how do we do that ? we were using the anchor tag to create links to delete tasks. Remeber that links in anchor tags are GET requests, to create POST requests we need a form.

We could create forms inside the loop and create a view for the form, but instead we will use the DeleteView.

The Django delete view has a confirmation page that does not really delete anything, but just askes you to confirm the deletion before the item is deleted, that means that we can keep using the anchor tags in the list page.

The django delete view can be created like this

```python
class DeleteTaskView(DeleteView):
    success_url = "/tasks"
    model = Task
    template_name = "task_delete.html"
```

Like the other generic views, the DeleteView also takes in a model and generates a view that can delete objects.

and the template look like this

```html
<form method="post">
  {% csrf_token %}
  <p>Are you sure you want to delete "{{ object }}"?</p>
  <input type="submit" value="Confirm" />
</form>
```

We can show more details about the task here, but we will stick with just the task title for now.

The url route for the delete view is very similar to the update view,

```python
    path("tasks/<pk>/delete", DeleteTaskView.as_view()),
```

We'll also change the route in the tasks list page to call the new url route to delete tasks.

```html
<a href="tasks/{{ task.id }}/delete">delete</a>
```

and now if we try to hit the delete button it will redirect you to the confirm delete page and then delete it if you confirm. The delete view returns an HTML page with a form in the `GET` method and the `POST` method actually deletes the object.

< Show the source of the DeleteView if needed >

There are methods specifically made to delete and update objects in HTTP like the `DELETE` method or the `PUT`/`PATCH` method. but these methods do not work with forms, usually the logic to perform an action like delete is written in the delete method, but since our scope is restricted to browser based interactions, we will stay wth `GET` and `POST` for now.
