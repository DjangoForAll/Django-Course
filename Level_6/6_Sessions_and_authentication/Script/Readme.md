Lets create a new function based view to test how session storage works

```python
def session_storage_view(request):
    total_views = request.session.get('total_views', 0)
    request.session['total_views'] = total_views + 1
    return HTTPResponse(f"Total Views is {total_views}")
```

lets create a route to test it out and see how it works

This simple view returns the number of times a user has visited the page in a single session, refreshing the page will increment the count.

Things start to get intresting when you try to view this page from an incognito window, You can see that the view count has been reset to 0. This is because incognito windows usually do not keep the session data from the normal window. we can try to view the actual cookie that stores the session id and see what happens if we delete it.

Django recretes a new session for us and all the data in the previous session is lost.

Django also uses the session to store information about the currently logged in user. Whenever a user logs into a Django server it links the session to the user.

lets use django's built in user management system to build a simple login and signup page.

Lets start with the signup page

```python
from django.contrib.auth.forms import UserCreationForm

class UserCreationView(CreateView):
    form_class = UserCreationForm
    template_name = "user_create.html"
    success_url = "/user/login"
```

Django provides the UserCreationForm class to help us create a form that will create a new user. We have already learned about what CreateView does so lets skip it for now.

Lets also create a route to handle this view.

```python
path("user/signup", UserCreationView.as_view()),
```

Now you can visit the route to get to the signup page. But after successfully submitting the form it redirects to the login page, which is not defined yet, so you will get an error. lets fix that by implementing the login page.

```python
from django.contrib.auth.views import LoginView

class UserLoginView(LoginView):
    template_name = "user_login.html"
```

And a route to handle this view

```python
path("user/login", UserLoginView.as_view()),
```

We have not set the success_url yet, instead of the success_url we will set the setting `LOGIN_REDIRECT_URL` , this will ensure that no matter how we login we always end up on the same url.

we'll add this config to the bottom of the settings file

```
LOGIN_REDIRECT_URL="/tasks"
LOGIN_URL="/user/login
```

The LOGIN_URL is used by django to redirect users to the login page if someone tried to access a restricted route.

We can also add a Logout View as well

```
from django.contrib.auth.views import LogoutView

path("user/logout", LogoutView.as_view()),
```

since the LogoutView does not need a template, we can use the Class as-is without any changes, The logout redirects you to the default logout page currently, that behaviour can be changed by setting the `LOGOUT_REDIRECT_URL` setting.

and now you have a working authentication system with a login page, signup page and logout page.
