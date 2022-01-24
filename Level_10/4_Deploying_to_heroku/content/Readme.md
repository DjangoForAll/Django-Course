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

We can run `git push origin heroku` and Heroku will take our current application and deploy it. But it does not really work yet, We currently run our application with the `manage.py` file, which is used for creating local development servers and not production-grade servers. The web server shipped with Django has not gone through any security audits or performance tests which makes it a poor choice as a production web server. Quoting the official Django documentation: _We’re in the business of making web frameworks, not web servers, so improving this server to be able to handle a production environment is outside the scope of Django_

We will be using an HTTP server called `gunicorn` to run our application in Heroku. Django has already created a `wsgi.py` file that will interact with the gunicorn HTTP server. WSGI stands for web server gateway interface, it contains an application callable which the application server (Gunicorn) will use to communicate to your code.

Let's just break down what we talked about before moving ahead, Python has set a standard called [PEP-3333](https://www.python.org/dev/peps/pep-3333/) that specifies a standard interface between web servers and Python web applications or frameworks to ensure that servers and applications communicate in a standard manner. The standard requires an application callable (a callable is anything that can be called). The application should be callable with a standard set of arguments passed by the web server and the application should return a response.  ( checkout the WSGI file inside your project and you should be able to get to the application that it creates. )

Visit this [article](https://www.fullstackpython.com/green-unicorn-gunicorn.html) for more details regarding gunicorn and Django

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

To handle static files, Django comes built-in with a [collectstatic](https://docs.djangoproject.com/en/4.0/ref/contrib/staticfiles/#collectstatic) command, this command will collect all the static files that are required for the application to run and place them in a predefined folder.

The collect static command requires a folder to be defined so that the static files can be placed in, lets add this configuration in the settings file

```python
STATIC_ROOT = BASE_DIR / "staticfiles"
```

This places all static files in the `staticfiles` folder in the root, you can try running the command locally to test it out, just ensure that the collected files are not committed to git!

Now that all our application config has been completed, let's push the changes to the Heroku remote.

```
git push heroku master
```

This might take some time, once Heroku is done deploying, it should provide a link to your deployment. You can visit the link to view your webpage.

If you try to view your page now, you'll get an error that says `DisallowedHost at /`, there are two issues here,

1) Django has a built-in mechanism that blocks the request unless they are from a list of allowed hosts, this setting can be found under the `settings.py` file in the `ALLOWED_HOSTS` variable. ( Host is the fully qualified domain name of the website. )
2) Django is explicitly pointing out the error along with stack traces to our code, these pretty error pages are rendered by Django because we have set the `DEBUG` variable in the settings file to `True`. This lets Django know that we are in the development environment and that we don't care about security. The debug mode should NEVER be turned on in production.

Let's fix the first issue by finding the `ALLOWED_HOSTS` variable in the settings file and updating it like this
```python
ALLOWED_HOSTS = ["<application_name>.herokuapp.com"] # you can also do ALLOWED_HOSTS = ["*"] to allow all hosts
```

To solve the second issue, find the `DEBUG` variable in the settings files and update it to `False`

Commit your changes and push to Heroku again to ensure that everything is working as expected.

Even though our application is working, there are some issues with our application: 

1) We have not set up a dedicated database yet, The database we currently use (SQLite) is not used in production applications, SQLite is a file-based database, you must have seen a file called `db.sqlite3` in the root of your project, this is the database we were using till now, Since SQLite is a file-based database, if the file is deleted, all our data is lost, it also makes it really hard to share the data with other instances running on other machines.
Heroku uses an [ephemeral filesystem](https://devcenter.heroku.com/articles/dynos#ephemeral-filesystem) that means that the changes made to the filesystem only last until that instance is running, if the instance is shut down or restarted the filesystem is also reset, this means that all our data is also lost in the process. Heroku calls its instances [dynos](https://devcenter.heroku.com/articles/dynos) and they are restarted once every day and whenever you deploy/make changes to the env.
We will need a dedicated database to store our data, we will be using a database called `Postgres` in our Heroku instance.
2) Since Django disables static file serving in production, we either need to configure a different server for serving static files or we need to install packages like `whitenoise` that lets us handle static files in production.

We'll see how we can solve these issues in the next lesson.
