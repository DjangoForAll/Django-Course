Currently, our application works great in our local environment, In this chapter, we will try to showcase our project to everyone with Heroku. 

We have already learned the basics of what Heroku does, in this chapter we will learn how to deploy our project to Heroku. 

Before we get started, follow the following instructions

1) Sign up for a [Heroku account](https://signup.heroku.com/devcenter).

2) Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

3) Log in to Heroku from the CLI, run the following command in your terminal to log in to Heroku.

```bash
heroku login
```

1) Navigate to your applications root directory and run the following command
   
```bash
heroku create <application-name> # Replace <application-name> with the name of your choosing, note that Heroku application names cannot be duplicated across accounts, try something like <github_username>-<project_name> for the sake of consistency - You can only use dashes, numbers, and letters, the name should start and end with a letter
```

This command will create a new Heroku application with the name you specified, and add a new remote to your local git repository, this remote will be called `heroku` and will point to a git instance on Heroku. Once you are done with your work, you can push your changes to the remote `heroku`. This will let Heroku know that you are trying to deploy your application and it will do that.

We can run `git push origin heroku` and Heroku will take our current application and deploy it. But it does not really work yet, We currently run our application with the `manage.py` file, which is used for creating local development servers and not production-grade servers. We will be using an HTTP server called gunicorn to run our application. Django has already created a `wsgi.py` file that will interact with the gunicorn HTTP server. WSGI stands for web server gateway interface, it contains an application callable which the application server (Gunicorn) will use to communicate to your code.

To install gunicorn, we can run the following command in our terminal

```bash
pip install gunicorn
```

Now that we have installed gunicorn, make sure that you have updated the requirements file with the current requirements and that the requirements file is present at the root of the project.

Now that we have the application setup, we need a way to let Heroku know how to run our application. We can do this by creating a `Procfile` file at the root of the project.

Let's create a new file called `Procfile` ( No Extensions ) and add the following content to it.

```Procfile
web: gunicorn task_manager.wsgi
```

before deployment, run the following command to let Django know that static files need not be collected

```bash
heroku config:set DISABLE_COLLECTSTATIC=1
```

Now that all our application config has been completed, let's push the changes to the Heroku remote.

```
git push heroku master
```

This might take some time, once Heroku is done deploying, it should provide a link to your deployment. You can visit the link to view your webpage.

If you try to view your page now, you'll get an error that says `DisallowedHost at /`, there are two issues here,

1) Django has a built-in locking mechanism that blocks the request unless they are from a list of allowed hosts, this setting can be found under the `settings.py` file in the `ALLOWED_HOSTS` variable. ( Host is the fully qualified domain name of the website. )
2) Django is explicitly pointing out the error along with stack traces to our code, these pretty error pages are rendered by Django because we have set the `DEBUG` variable in the settings file to `True`. This lets Django know that we are in the development environment and that we don't care about security. The debug mode should NEVER be turned on in production.

Let's fix the first issue by finding the `ALLOWED_HOSTS` variable in the settings file and updating it like this
```python
ALLOWED_HOSTS = ["<application_name>.herokuapp.com"] # you can also do ALLOWED_HOSTS = ["*"] to allow all hosts
```

To solve the second issue, find the `DEBUG` variable in the settings files and update it to `False`

Commit your changes and push to Heroku again to ensure that everything is working as expected.

Even though our application is working, there are some issues with our application: 

1) We have not set up a dedicated database yet, The database we currently use (SQLLite) is not used in production applications, SQLLite is a file-based database, you must have seen a file called `db.sqlite3` in the root of your project, this is the database we were using till now, Continuing with databases like this is a terrible idea, we will be using a different type of databases like `MySQL` or `PostgreSQL` in production.
2) Static files are not being served by our application yet, we either need to configure a different server for serving static files or we need to let our application server know that it needs to serve static files.

