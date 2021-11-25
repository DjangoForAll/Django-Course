Lets get started with installing Django

Django is a python package, so it is installed using pip like regular pacakges.

```bash
pip install django
```

This command installs the latest version of Django along with all its dependencies.

Now that we have django installed we need to create a project. To create a new project in django, we use the django-admin command, this command is installed along with the django package.

```bash
django-admin startproject my_project
```

Running this command creates a new folder `my_project` in the current folder with a sample django project. we can quickly look at the current structure of the project by looking inside the folder.

```
my_project/
    manage.py
    my_project/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

Lets look at each file and see what their function in our project is,

- `manage.py` : remember in the last level's milestone we had a file called `tasks.py`, we invoked this file to start the server, create tasks and so on.. Similarly manage.py is a command line utility to interact with the project, ie to start the server, run commands and so on.

- `settings.py` : this file contains all the settings for the project, we can change the settings in this file to change the behaviour of the project.

- `urls.py` : this file contains the url patterns for the project, in the last level we had a simple if condition that changed the html content when we visited different url's in our project, these conditions can get very complex when we have huge projects, so all url patterns are defined in urls.py file.

-- `__init__.py` : This is a python file without any content, if this file is present then python treats the folder as a package.

-- `asgi.py`/`wsgi.py` : These files are used to run the project in a production environment. we'll not edit these files for now, we'll revisit them once we get a good grasp on django

There are a lot of other standard files that are not yet created, we'll create them as we go along.

Finally, lets start the development server and see what it does!

a development server is usually used only for testing by the developer, to start it we can use the manage.py file we talked about earlier

```bash
python manage.py runserver
```

This starts a development server at localhost:8000 , let's visit the page and see what happens!

Now that Django is up and running lets modify some of the files and try to create some content.
