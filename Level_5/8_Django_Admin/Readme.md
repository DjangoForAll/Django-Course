-- Video --

Django comes with a lot of handy features that help you focus on what you do best! One of this is the admin interface.

Django can create admin interfaces for your models, from the UI you can create/update/delete/view your models.

Django does not register all models created in your project, you have to manually let Django know that you want to use the admin interface for your model.

In your appp's folder there should be a file called admin.py , this is where all your Model registrations should reside.

Open it up and add the following code:

```python
from django.contrib import admin
from tasks.models import Task

admin.sites.site.register(Task)
```

Thats it! Now you can access your models from the admin interface.

To get to the admin interface you can visit the /admin route, you will be presented with a login screen.

To get through the login screen you need to first create an account in your Django Project. To quickly create a new user lets run the following command.

```bash
python manage.py createsuperuser
```

enter all the required information and hit enter, once the user is created, login to the admin panel with the newly created user.

Now you can see all the tasks that you have created, you can edit/delete them as well.

You can see that there are two other models that are registered in the admin interface, these are the User and Group models. Remember back when we were running the migrations we saw a bunch of migrations that we didnt create? Those were Django's migrations to create the User, Group and a bunch of other models.

Since Django already has a User model built in , lets see how we can add that to our existing Task Model
