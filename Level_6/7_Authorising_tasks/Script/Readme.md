Currently all tasks can be viewed by everyone, there is no Authorisation for tasks, if i create a task, it can be viewed by anyone who visit the lists page. which is kinda terrible since it can only be used by one person currently.

Lets change that to store the user who created the task within the task object and only list the tasks that were created by the user.

We already created a model attribute called user, a Foreign key to the User table that Django has. Now we will populate the user when a user saves the task.

Before getting into that lets quickly create a function based view to see how we can access the currently logged in user, we will reuse our session management view for this.

```python

def learn_sessions_view(request):
    total_views = request.session.get("total_views", 0)
    request.session["total_views"] = total_views + 1
    print(request.user)
    return HttpResponse(f"Total Views is {total_views}")
```

We added a print statement for printing the current user, Django automatically checks if the session has a logged in user and then sets the user attribute of the request with the logged in user.

When we try to logout and view the same page, Django sets the current user to `AnonymousUser`, we can use the `is_authenticated` attribute to quickly check if the user is logged in or not.

Since the user object is accessible from the request object, we can use it in our templates to create a quick greetings line as well, we can add this into our dashboard like so.

```
<h3>Welcome! {{request.user}}</h3>
```

This will render a welcome message just for the user when he visits a page.

Now in the create view, we can override the `form_valid` method, the form valid method saves the object when the form is valid

The regular `form_valid` method looks like this

```python
def form_valid(self, form):
    """If the form is valid, save the associated model."""
    self.object = form.save()
    return HttpResponseRedirect(self.success_url)
```

It creates an object from the values submitted by the form and returns to the success_url that we defined

we will create our own version of the `form_valid` method and update the object and save the user into it

```python
def form_valid(self, form):
    """If the form is valid, save the associated model."""
    self.object = form.save() # Self.object refers to a model object
    self.object.user = self.request.user # We can directly set the value to the object
    self.object.save() # the save method of the model class saves the object to the database
    return HttpResponseRedirect(self.success_url)
```

Now in the listing view we can filter out tasks that are created by the currently logged in user

```python
def get_queryset(self):
    queryset = Task.objects.filter(deleted=False , user=self.request.user)
    search_term = self.request.GET.get("searchterm")
    if search_term:
        queryset = queryset.filter(title__icontains=search_term)
    return queryset
```

Adding the filter will allow authenticated users to view their tasks, what about unauthenticated users? Django will throw an error in those cases

we will define permissions on a class level which restricts the access to the view based on certain conditions

Django has a mixin to prevent unauthenticated users from accessing a view, lets see how we can configure it

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class TasksListView(LoginRequiredMixin, ListView):
...
```

If an unauthenticated user tries to visit the tasks listing page, it will redirect the request to the Login Url, The login url must be defined in the settings.py file with the variable `LOGIN_URL`, otherwise it will redirect to Django's default login page

You can add the mixin to all the views you were using to completely secure your application.

Now you have an application that users can login to and save their tasks.
