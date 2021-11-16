Django loves modularising things, as in converting everything into smaller modules which can be reused, these modules can be published as packages which can be used in different projects. Django calls these small modules apps.

Apps are usually created by logically grouping actions/data, for example if you are building an e commerce web application then your apps might be user, product, cart, checkout, payment, shipping, etc. these apps together make up our e commerce web application.

If you might want to build a new task management app you can reuse the user app which we created for e commerce, this way django prevents you from reinventing the wheel.

There is no defenitive way to decide what constitutes an app, you can even build your entire application inside of a single app, you can also split it into a 100 ones!, generally apps should “Do one thing and do it well.” ( This is also one of the [UNIX Philosophies](https://en.wikipedia.org/wiki/Unix_philosophy#Do_One_Thing_and_Do_It_Well) ) !

To create an app you can run the command `python manage.py startapp <app_name>` , the app name should always be in lower cases, I personally tend to name apps in their plural form ( users , posts , blogs etc.. ), there is no standard for this, you can follow what makes the most sense to you.

Lets create a new app called tasks, everything task related is going to come under this app.

```bash
python manage.py startapp tasks
```

running this command should create a new folder called tasks in your root project folder

if you try to view the files inside the `tasks` folder you can see that there are multiple files created for us

The app we created is not yet linked to the django project, to link it to the project we need to add the name of our new app to the end of the `INSTALLED_APPS` list in the `settings.py` file.

You installed apps should look like this now

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "tasks"
]
```

> Note that djano's own apps are also declared here, you can see them listed before our app.
