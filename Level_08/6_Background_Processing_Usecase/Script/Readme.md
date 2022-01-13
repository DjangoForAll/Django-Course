Now that we have a basic understanding of Background jobs, lets try to build a tiny feature with background processes.

We will build a tiny task that will send emails out to the users at the end of the day with their pending tasks.

Now that we know what to build, lets get building.

Lets create a new file called `tasks.py` in our app directory. now lets create a new method called `send_email_reminder`.

first we will import the User model from django's built in authentication system and then iternate over the users.

For each user, we will query the pending tasks count and send a simple email to the registered email with the pending tasks count.

The send_mail is a method that django provides, it takes the arguments required for an email and actually send it. Django has a concept of Email Backends, The backend is what actually sends the email, we will use the Console backend for this tutorial, the console backend just prints the email to the console, no acutual email is sent.

To set the console email backend, set the following variable in `settings.py`

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

And thats it!, now we have created a background job that sends reports to all the users.
