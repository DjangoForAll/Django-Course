In all projects, Database Schemas are sacred, even simple changes in them can break the whole application. Because of that, Django does not automatically sync the schema with the database, we have to manually ask django to keep the schema up to date.

Recording Schema changes are very important, imagine we have fields called `first_name` and `last_name` , we want to merge them together into one field called `name` , to do so we have to remove the original fields and create a new one, now if we remove the corresponding fields and sync the changes all the data that existed in the database will be lost with no traces of the old fields. Django solves these problems with Migrations, This might be a little tricky to understand but it is very important.

Migrations are a way to record changes in the database schema. you can think of it as git for database schema changes. It keeps track of the history, it allows us to move to a specific version of the schema as well.

Django has two main commands to manage migrations :

makemigrations : This is responsible for creating new migrations based on the changes you have made to your models.
migrate : This is when Django actually performs the schema changes in the Database. This command can also be used to move to a specific migration version.

All migrations in Django exist within the migrations folder inside the app. Its best that we dont modify anything inside the migrations unless we know exactly what we are doing.

Now that we have a basic understanding of how migrations work, lets create a new migration.

-- Video --

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

> Migrations are atomic in nature, ie if one change fails to be performed, all the migrations are rolled back. the database is moved to the state it was in before the migration was applied.

You can do a lot more with django migrations, They are one of the reasons why Django is preferred over other Frameworks, Check out the [official documentation](https://docs.djangoproject.com/en/3.2/topics/migrations/) to learn more about migrations.
