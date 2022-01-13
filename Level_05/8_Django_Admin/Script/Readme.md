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

To get to the admin interface you can visit the /manage route ( we changed this route earlier, we can change this route back to admin for the sake of consistency ), you will be presented with a login screen.

To get through the login screen you need to first create an account in your Django Project. To quickly create a new user lets run the following command.

```bash
python manage.py createsuperuser
```

Enter all the required information and hit enter, once the user is created, login to the admin panel with the newly created user.

Now you can see all the tasks that you have created, you can edit/delete them as well.

--

You can see that there are two other models that are registered in the admin interface, these are the User and Group models. Remember back when we were running the migrations we saw a bunch of migrations that we didnt create? Those were Django's migrations to create the User, Group and a bunch of other models.

Since Django already has a User model built in , lets try and add a relation to our user model.

```python
from django.contrib.auth.models import User

user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True ,blank=True)
```

The User model ships with django and is used to store the user related data.

The on_delete argument is used to specify the behaviour of the object when the foreign key (user here) is deleted.

Lets say that you created some tasks with the user field set to the user you created, after that you deleted the user, now the database does not know what value should be present in the user field, it cant store the id because the id no longer exists, so we can choose whether to cascade the delete ie delete the tasks when the user is deleted, set the value to null, or even `protect` which prevents deletion when there are objects referring to it.

The null and blank values tell the database that this field can have null values, if we dont allow null values then all our existing features will cease to work.

Lets now create the migrations and run them to add the changes in the database

Once the migrations are done, let's check the admin page and we can see that the user can also be set in the admin interface.
