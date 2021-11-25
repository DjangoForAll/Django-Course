Now that we have an Basic Understanding of realtional databases we can talk about what makes them "Relational".

The dictionary defenition of a relational database is : a database structured to recognize relations between stored items of information.

Lets first get some context as to why relations are required.

Lets say that we are building a task management app which requires the user to login first. That means that all the tasks that are created should be visible to the created user, Only the created user. That means our database must also account for this change. our instinct tells us to add another field to the tasks that store the email of the user who created the task. That works but it is not a good idea. what happens if the user changes his email, what happens if the user is deleted? what if we want to create a username field for the users as well?

To create this table with relations , we would have 2 tables, one that describes the task ( Task ) which can be our existing table, and then another table that describes the user , we can store all the users information like their name , email and anything you can think of! in the User Table , Instead of duplicating the user's information in every row of the task table, we store it once in the user table and create a relationship from the Task table to the User Table.

We'll take an example with data to get a better idea

Lets imagine the Tasks Table has the following data

| id  | title        | completed | deleted | user_id |
| --- | ------------ | --------- | ------- | ------- |
| 1   | Buy Milk     | False     | False   | 1       |
| 2   | Learn Django | False     | False   | 1       |
| 3   | Buy Bread    | False     | False   | 2       |

and the User table has the following data

| id  | Name         | Email               |
| --- | ------------ | ------------------- |
| 1   | Vignesh Hari | hey@vigneshhari.dev |
| 2   | Gigin C      | hey@gigin.dev       |

Here user_id points to the id ( Primary Key ) of the user who created the task, This is called a Foreign Key Index. The Foreign key links table with the primary key of the other table, in this case the user table.

While querying we can join both the data together, ( technically we can join data even without the foreign key index, but it is not a good idea as it slows down the query ) During a join the database finds the corresponding data in the other table and joins it to create a bigger table.

Lets checkout what the joined table will look like

| id  | title        | completed | deleted | user_id | id  | Name         | Email               |
| --- | ------------ | --------- | ------- | ------- | --- | ------------ | ------------------- |
| 1   | Buy Milk     | False     | False   | 1       | 1   | Vignesh Hari | hey@vigneshhari.dev |
| 2   | Learn Django | False     | False   | 1       | 1   | Vignesh Hari | hey@vigneshhari.dev |
| 3   | Buy Bread    | False     | False   | 2       | 2   | Gigin C      | hey@gigin.dev       |

Its literally a table created by joining the two tables together.

Why Relations? If you observed the actual value was only stored once in the user table, even if you create a million tasks , the email is only stored once. If the user wanted to change the email address or name , there would only be one update required.

Duplicating data leads to inconsistencies and Multiple sources of truth, these are huge problems when designing databases.

Generally databases are designed in depth before they implemented, Database design is usually what differentiates a sub par college project from a real life professional project.

Database Design consists of a really important step known as Normalization.

Read more about Normalization [here](https://docs.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description)

Creating Relations in Django is extremely simple and straight forward. which makes our life a lot easier.
