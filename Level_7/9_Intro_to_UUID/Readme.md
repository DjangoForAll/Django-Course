In the earlier level we got to know why integer id's perform poorly when used as the sole identifier for an object, To solve this problem we will use UUID's

UUID's stands for Universally unique identifier , its also called GUID sometimes (Globally Unique Identifier)

There are various versions of UUID, The current and latest version is 4, Version 4 of UUID's are completely random, the probability that you'll get the same one is almost impossible, in total 2^122 (5.3 undecillion) possible version-4 UUID's , that's a lot of UUID's.

This is what a regular UUID looks like `639a75cf-de3f-42a2-91ff-294bb60426a3`
They are 32 charecters long (8-4-4-4-12) and each charecter you see here is a hexadecimal ( they can be any number from 0-9 or a charecter from A-F ) , ie 16 possible values for each charecter.

Now we know what UUID's are, lets see how to make one in python

Python ships with a library called `uuid` which makes it easy to generate new UUID's

to create a new uuid in python we can follow the following code snippet,

```python
from uuid import uuid4
print(uuid4())
```

That's it, Now lets add it to our model

```python
external_id = models.UUIDField(default=uuid4, unique=True, db_index=True)
```

usually id refers to an internal id, regular id's are autoincremented integers that is used internally and not exposed to the end users, external_id's on the other hand are random non incremented values that are exposed to the end users, external id's are hard to guess and is generally more secure.

> you might be thinking why create an external_id, why not just id's ? its perfectly fine to use one type of id and keep that type as the primary key, however we will continue to use both the integer and a UUID for now.

UUIDField is used to store UUID Values only and contains the validations to reject invalid values

The default argument can be a callable ( functions can be called hence they are callable ) or just constant values, if the value is a callable then Django will call the callable function each time a new raw is created without a value for the given attribute to get the default value.

the unique argument ensures that there is exactly one row with the given attribute value in the given table. note that this check is performed in the database and not in django.

indexing is a way to optimise performance, think of phone books/textbooks where indexes massively save time instead of searching page by page. Similarly indexes in databases provide a faster way to process queries. since the external id is going to be used for almost all queries, we will add an index to it. indexing by itself is really intresting, you can read about it [here](https://www.essentialsql.com/what-is-a-database-index/) once you are done with the course content

if you try to create migrations and run the migrations, you will run into an issue, a unique constraint issue specifically, we are trying to create a new field in the database, this field will initially have null values for all existing rows, since we have a unique constraint it will restrict same values to exist in multiple rows and thereby produce an error.

There are two ways to solve this,

1. Delete the migration, Remove the unique constraint , create migrations and migrate , write a custom migration to add the unique UUID's, add back the unique constraint and then create and run the migrations. This is pretty complicated
2. Delete all existing data, When there is no data there are no unique constraint issues. Clearly this is only applicable to us, since we dont have any real data yet. Any instance with real data would have to go in the first route, that also gives a lot of control over the process.

For now lets delete all the existing data, This is a good time to introduce the django shell, the django shell is just a python interpreter but we can interact with django ORM within the shell.

to start a django shell we can run

```shell
python manage.py shell
```

Once inside the shell we can import the Task model and delete all data

```python
from tasks.models import Task
Task.objects.all().delete()
```

You can also test out anything you want in the shell

Now, we can rerun our migrations and complete it

Now we can create a couple of tasks and check the admin interface to confirm if the UUID's are generated

We will add external_id to the serializer so that the api responds the unique id as well, we will update the serializer as follows,

```python
from rest_framework.serializers import ModelSerializer, UUIDField

class TaskSerializer(ModelSerializer):

    user = UserSerializer(read_only=True)
    id = UUIDField(source="external_id", read_only=True)

    class Meta:
        model = Task
        fields = ["title", "description", "user", "status", "id"]
```

we create a new attribute called `id` , the source attribute is used to denote where the value is fetched from, now if we refresh our browsable API, we will see the id's for each task created,

Finally we have to edit the routes to enure that the UUID's can be used to get to the detail views.

DRF provides a really simple way to do it, just add the `lookup_field = "external_id"` attribute to our viewsets and DRF will take care of the rest, no need to change the routes or anything like that, the DRF router will figure out what is the field type and change the url pattern generated accordingly.

That's it now we are all set to use UUID's in our REST API's
