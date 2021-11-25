Now that we have our List, Create and Update Views, we can create our missing View, The Detail view

The detail view is very similary to the list view, but instead of showing all the items, we just show one item in detail.

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

the object refers to the selected object and is passed to the template.

Finally we can add the link to view the details of the object in the list view.

```html
<a href="tasks/{{ task.id }}">detail</a>
```
