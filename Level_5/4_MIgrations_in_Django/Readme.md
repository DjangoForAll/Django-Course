In all projects, Database Schemas are sacred, even simple changes in them can break the whole application. Because of that, Django does not automatically sync the schema with the database, we have to manually ask django to keep the schema up to date.

Recording Schema changes are very important, imagine we have fields called `first_name` and `last_name` , we want to merge them together into one field called `name` , to do so we have to remove the original fields and create a new one, now if we remove the corresponding fields and sync the changes all the data that existed in the database will be lost with no traces of the old fields. Django solves these problems with Migrations, This might be a little tricky to understand but it is very important.

Migrations are a way to record changes in the database schema. you can think of it as git for database schema changes. It keeps track of the history, it allows us to move to a specific version of the schema as well.

Django has two main commands to manage migrations :

makemigrations : This is responsible for creating new migrations based on the changes you have made to your models.
migrate : This is when Django actually performs the schema changes in the Database. This command can also be used to move to a specific migration version.

All migrations in Django exist within the migrations folder inside the app. Its best that we dont modify anything inside the migrations unless we know exactly what we are doing.

Now that we have a basic understanding of how migrations work, lets create a new migration.

```shell
python manage.py makemigrations
```

Once we run the command we can see that django has detected the change and created a migration file for the same.

```txt
Migrations for 'tasks':
  tasks/migrations/0001_initial.py
    - Create model Task
```

In the response you can see that django has created the migration that creates the model Task, Django names migrations automatically so that you can refer them easily , in this case the migrations name is 0001_initial

Lets take a look at the migration file that django created, it contains information on what change was made on what model, the current migration specifies that a model has been created along with all the attributes that we specified, among the list you can also see a field called `id`, this is not something we added in the model, It is something that Django added for us.

In Databases it is required to have a unique value for each row so that each row can be uniquely identified. This is mandatory for most databases and Django autoamtically generates a primary key called `id` for any Schema that does not define one itself. Since we did not define one in our class, Django created one for us. The id field is an auto incremented number so it will automatically increment for each row, we wont have to manually specify it when adding new data.

> If our model has another fields with only unique values, we can use them as well, But it is reccomended to keep an autoincremented number as the primary key.

Now lets actually apply the migration by running

```shell
python manage.py migrate
```

Once you run it, you can see that a bunch of other migrations also got executed, These are migrations for Django's tables, Django also has its own models which it uses for its own bookkepping and management, we'll learn abou those later. For now we can see that our migrations have been applied, The schema has been created in the database

Now lets create a change in our model and see how Django's migration handles the change.

Lets add the following attribute in our model class

```python
created_date = models.DateTimeField(auto_now=True)
```

This attribute will store the date and time when the task was created, auto_now is a built in django attribute that will automatically update the created_date field whenever the task is created.

Now lets run makemigrations again, and see what it does

```bash
python manage.py makemigrations
```

running the command will create a new migration file for the change we made to our model.

```txt
Migrations for 'tasks':
  tasks/migrations/0002_task_created_date.py
    - Add field created_date to task
```

Django automatically figured out that we added a new field to the model Task and created a migration to handle that change.
the name of the migration is 0002_task_created_date , Django is smart enough to name its own files based on the name of the model and the changes we made!

Now we can migrate and and let the changes be reflected in the database

We can also create custom migrations in django, custom migrations are useful to handle cases where we need to write custom code to copy over data or perform other tasks.

To explain this in detail, lets take the case we described earlier , we have two columns `first_name` and `last_name` , we want to merge them into one field called `name`, to perform this operation we have to follow the following steps.

1. Add the field name to the model ( The `first_name` and `last_name` are not removed yet )
2. Create Migrations for this change
3. Create a custom migration that will copy the data from `first_name` and `last_name` to name
4. Remove the fields `first_name` and `last_name` from the Model
5. Create Migrations for this change
6. Migrate the changes

go ahead and try to recreate it and see what happens!

The Django Documentation provides excellent information on how to create custom migrations. View them [here](https://docs.djangoproject.com/en/3.2/topics/migrations/#data-migrations)

> Migrations are atomic in nature, ie if one change fails to be performed, the migrations are rolled back. the database is moved to the state it was in before the migration was applied.

You can do a lot more with django migrations, They are one of the reasons why Django is preffered over other Frameworks, Check out the [official documentation](https://docs.djangoproject.com/en/3.2/topics/migrations/) to learn more about migrations.
