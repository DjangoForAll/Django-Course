Lets start by creating migrations for the model we created earlier

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

In Databases it is required to have a unique value for each row so that each row can be uniquely identified. This is mandatory for most databases and Django automatically generates a primary key called `id` for any Schema that does not define one itself. Since we did not define one in our class, Django created one for us. The id field is an auto incremented number so it will automatically increment for each row, we wont have to manually specify it when adding new data.

> If our model has other fields with only unique values, we can use them as well, But it is reccomended to keep an autoincremented number as the primary key.

Now lets actually apply the migration by running

```shell
python manage.py migrate
```

Once you run it, you can see that a bunch of other migrations also got executed, These are migrations for Django's tables, Django also has its own models which it uses for its own bookkepping and management, we'll learn about those later. For now we can see that our migrations have been applied, The schema has been created in the database

Now lets create a change in our model and see how Django handles the change.

Lets add the following attribute in our model class

```python
created_date = models.DateTimeField(auto_now=True)
```

This attribute will store the date and time when the task was created, auto_now is an argument that will automatically update the created_date field whenever the task is created.

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
