Before we start with creating the new view , lets first move the task creation view into a seperate template, so it's easier to understand, To move to a seperate template, lets create a template called task_create.html and create a new view to render the form.

We already learned about get and post methods, usually its convention to use the get method to render the form and the post method to accept the data from the form, that way all the realated views fall under the same route, This again is not a requirement, but it makes the view easier to understand.

Lets start by creating the new template task_create.html

```html
<h4>Create a new Task</h4>
<form action="" method="post">
  <input type="text" name="task" />
  <button type="submit">Add Task</button>
</form>
```

Now let's create a new url route called create-task and create a corresponding class based view to render the form

```python
path('create-task' , CreateTaskView.as_view() )
```

> Note that all classnames are written in camelcases where every word's first letter is capitalized

The Class will have the following defenition

```python
class CreateTaskView(View):

    def get(self,request):
        return render(request , "task_create.html")

    def post(self,request):
        new_task = request.GET.get("task")
        Task(title=new_task).save()
        return HttpResponseRedirect("/tasks")
```

Now if we head over to the url /create-task, we will see the form rendered, however if we submit the form we'll recieve an error page.
`CSRF token missing or incorrect.` Django will not accept the form submission, because it is missing the csrf token.

so what exactly is the CSRF Token?

Lets say that you created a really cool task management web app, lets say you hosted this at the url awesome-task-manager.app,
One of the users in your app was casually looking over the internet ( something completely different ) and stumbles upon a form, Lets say that the form said "Enter your details to win a FREE Prize"! so he fills it out and submits it.
If the form's action attribute is set to your awesome-task-manager.app then our app will think that some legitimate user is trying to submit the form and accept the form submission.

So the user created a task even he never intended to create a task, now think of a much more serious situation where your banking app is involved and the form tried to create a transaction that transfers money from one account to another! Since the user does not look at each forms action attribute, they will click on a rather random form and submit it! but the consequences can be deadly!

These types of attacks are called Cross-site request forgery (CSRF) attacks. and django has a very clever way to prevent these attacks.

Django create a random token for every request that renders a form and remembers the token when the data is sent back, so the server can verify that the request is legitimate, and not a CSRF attack.

If you wanted to add a task to your task management app, when you get to the task create page, Django will add a hidden value to the form called `csrfmiddlewaretoken`, this value is sent over along with the data in the form, when Django recieves a POST request, it will check if the token is present and valid, if a random form is submitted, it wont have the token and hence Django will reject the request.

To add a csrf token to the form, you can edit the html as follows,

```html
<h4>Create a new Task</h4>
<form action="" method="post">
  <input type="text" name="task" />
  {% csrf_token %}
  <button type="submit">Add Task</button>
</form>
```

The `{% csrf_token %}` will render into a hidden input tag, once you are done , view the source of your task creation page and see how it looks like, you will see that an input tag has replace the csrf_token tag.

Now the form submission works as expected and the user can create a task.
