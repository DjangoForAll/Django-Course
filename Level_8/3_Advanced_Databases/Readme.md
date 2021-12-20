We learned general principles of databases earlier, now we'll talk a little bit more on how to efficiently design and use databases.

Databases are usually designed before you start programming, Schema changes after designing an application can be tedious to handle and even more painful if the application is in use.

Before you start developing a web application, you need to have a general idea on what you are trying to solve and what kind of data we will be handling.

Once you have a general idea, we start designing a database to store our data, ER Diagrams are usually used to visualise a database desingn, ER Diagram stands for Entity Relationship Diagram.

An ER Diagram simply represents different tables and how they connect to each other, it also lists out the attributes and datatypes of each tables. We can take a look at our task management application's ER Diagram to quickly understand the database design.

-- ER

As you can see, we only have 2 tables, one table to store our tasks and another table to store our users. A task can have only one user association, this is also known as a many to one relationship. Similary a user can have many tasks, this is also known as a one to many relationship.

There can also be one to one relationships, eg. when you want to store all of the users details in a seperate table, you can create a one to one relationship between the user and user profile tables. Because of the one to one relationship a given user can have only one user profile ( or none ).

The last type of relationship is a many to many relationship, lets say that you want to create multiple tags for each task, so one task can have many tags and tags can be connected to many tasks as well. which creates a many to many relationship

Many to Many relationships cannot be created without creating a through table, Imagine the example we talked about earlier, Connecting multiple tasks to multiple tags, We cant have a field in the task table , since for each value of the tag we will have to duplicate the task data, Same goes with the tag table as well. This is where a through table comes in, It is a table that simply connects two tables together. Lets see an example of such a table.

-- ER

As you can see, for every tag associated to a task, there needs to be another entry in the through table, no data is duplicated anywhere.

Now that we have a general idea of relationships, we can move over to the implementation.

[This Django doc](https://docs.djangoproject.com/en/4.0/topics/db/models/#relationships) explains each of the relationship in detail

For examples on each relationship type, visit this [url](https://docs.djangoproject.com/en/4.0/topics/db/examples/)
