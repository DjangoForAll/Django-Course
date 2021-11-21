Till now we were using Function Based Views, to reiterate the view was the function that converted a Request into a Response

Classes allow us to easily inherit other classes and override certain required behaviour, which makes them better suited for reusing Django's views.

Lets first take a look at a simple Class-Based View

```python
from django.views import View

class TodoView(View):
    def get(self, request):
        return HttpResponse('Hello World')
```

Notice that we are inheriting the base class `View` and then overriding a method called `get`, the get method handles the `GET` request, similary `post` handles the `POST` request and so on.

Now we have to change our url defenition to point to our class based view, since we used to give views as the arguments in the urls, we have to convert our newly ceated class into a view, Django provides a built in method to convert a class into a view called `as_view`

we can update our url as follows

```python
from tasks.views import tasks_view , add_tasks_view ,delete_tasks_view , TaskView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks' , TaskView.as_view() ),
    path('add-tasks' , add_tasks_view ),
    path('delete-tasks/<int:index>' , delete_tasks_view)
]
```

Other than the change in url defenition, everthing else remains the same, you can try and port over our existing logic to the class based view and see how it works.

Function based views are still used if you want to quickly create a view that does not depend on anything else.

Now that we know what class based views are, lets take a look at something called Generic Views, Generic Views as their name suggests are built for a generic purpose, like listing something, viewing some objects details and so on. Generic Views are built to solve CRUD Operations , CRUD stands for Create Retrieve Update Delete. These are the most common operations in almost all applications you might make. Instead of creating these pages in every project, Django provides Generic views that solve the problem for you.

For example, Lets say that you want to list all the tasks in your application, you can create a generic `ListView` and pass in the model or the queryset you want to list. Django will render the template and create a response for you. We'll take a look at the `ListView` Class first.

```python
from django.views.generic.list import ListView

class TaskListView(ListView):
    model = Task
    template_name = 'tasks.html'
```

By default, django will pass in an object called `object_list` to the template, you can override this variable name by editing the attribute `context_object_name` of our class.

lets change our html template to accept the template variable `object_list` and now we have a generic view that can be used to list all the tasks.

In our generic class, we have an attribute called model, Django by default tries to get all the objcets from that model and pass them to the template.

We can edit that behaviour by passing in a queryset instead of a model

```python
class TaskListView(ListView):
    queryset = Task.objects.filter(deleted=False)
    template_name = 'tasks.html'
```

Now we only show the non-deleted tasks.

What about the search functionality? the search functionality is dynamic, ie the queryset changes based on the queryset, This is also something that can be done with generic views.

Almost all attributes in the class also has a corresponding `get_<attribute>` method that is used to dynamically fetch the value of the object.

Here we will use the same logic we had earlier to search for tasks, we will use the `get_queryset` method to dynamically fetch the queryset.

```python
class TasksListView(ListView):
    template_name = 'tasks.html'

    def get_queryset(self) :
        queryset = Task.objects.filter(deleted=False)
        search_term = self.request.GET.get("searchterm")
        if search_term:
            queryset = queryset.filter(title__icontains=search_term)
        return queryset
```

Now that we have a listing, what if we wanted pagination for our listing?

pagination is a feature that allows you to show a limited number of objects at a time, this is useful when you have a lot of objects and you want to show them in pages. Retrieving all objects from the database at the same time is usually not a good idea since there will be way too much data.

Lets add an attribute to our Class called `paginate_by` and set it to `5`, This will paginate the objects by 5 objects per page.

Now we need to edit our template to show the pages, Django handles pagination all by itself, we just have to show the page options in our template.

```html
{% for page in paginator.page_range %}
<li>
  <a href="?page={{ page }}&searchterm={{request.GET.searchterm}}"
    >{{ page }}</a
  >
</li>
{% endfor %}
```

paginator is a vairable that django provides, its a class that handles pagination, Here we are generating Anchor Tags for each page, each page is a redirection to the listing page with the page number, each route also has the serach term in the url, this is required since the page number wont make much sense without it.

Imagine you search for `milk` in the todo and select the second page, now if the search term is not applied to the second page, the second page would not make much sense right? Propogating the search term will provide the correct results.

Now that we have a page for listing tasks, lets see how we can add a task.
