Now that we have a basic understanding of Background jobs, lets try to build a tiny feature with background processes.

We will build a tiny task that will send emails out to the users with a summary of their tasks.

Now that we know what to build, lets get building.

Lets create a new file called `tasks.py` in our app directory. now lets create a new method called `send_email_reminder`.

```python
@periodic_task(run_every=timedelta(seconds=10))
def send_email_reminder():
    print("Starting to process Emails")
    for user in User.objects.all():
        pending_qs = Task.objects.filter(user=user, completed=False, deleted=False)
        email_content = f"You have {pending_qs.count()} Pending Tasks"
        send_mail("Pending Tasks from Tasks Manager", email_content, "tasks@task_manager.org", [user.email])
        print(f"Completed Processing User {user.id}")
```

first we will import the User model from django's built in authentication system and then iternate over the users.

For each user, we will query the pending tasks count and send a simple email to the registered email with the pending tasks count.

The send_mail is a method that django provides, it takes the arguments required for an email and actually send it. Django has a concept of Email Backends, The backend is what actually sends the email, we will use the Console backend for this tutorial, the console backend just prints the email to the console, no acutual email is sent.

To set the console email backend, set the following variable in `settings.py`

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

And thats it!, now we have created a background job that sends reports to all the users.

Now that we know how scheduled jobs work, we'll also take a look at jobs triggered dynamically without a specific schedule.

Here you can see a simple example of a method that print 1 to 10 with a delay of 1 second between each print, this method is simulating a request that can take 10 seconds to complete, If this is run directly in a view the response would take 10 seconds to return, we'll try doing exactly that first.

```python
import time

def test_background_jobs():
    print("This is from the bg")
    for i in range(10):
        time.sleep(1)
        print(i)
```

This method will block the request handler for 10 seconds and the user has to wait until the method completes.

To complete this method with celery, we can use the task decorator, this registers the method as a celery tasks and allows the method to be called as a celery task and exected asyncronously in the background.

Lets try to do that now

```python
from task_manager.celery import app

@app.task
def test_background_jobs():
    ...

test_background_jobs.delay()
```

Now this method is executed in the background and the web request is responded back before the method has completed execution, This is usually used when the method takes a lot of time to complete.

You can play around with celery and try creating more complex tasks.