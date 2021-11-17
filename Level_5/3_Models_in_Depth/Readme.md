When we created the new app, Django created a bunch of files and a folder for us, Amoung these files all Database/Schema related code resides in models.py

When you want to store data in a database ( relational database ) the structure of the data should be predefined, you can think of creating a user table with the attributes name,email,age . we cannot add data with another structure into this table. for eg in the table we mentioned earlier has no address column, trying to add this data will result in an error. The predefined table structure is often called as a schema, it is more or less the blueprint of how the database/table is constructed.

Django allows us to model schemas by creating classes, in django a model is any class that inherits from the `django.db.models.Model` class, if you create a class from this base class then Django maps it into a database table automatically, it then allows us to perform all kinds of operations by calling methods on this class.

It is important to note that django does not store the data, django just converts what you want to store/query into a query understandable by the database. The actual storing/querying is done by the databse, Django provides this layer of abstraction so that we can create better applications without spending time with the specifics.

Lets start creating our first Django Model!

First lets create a new class called `Task` , this class will represent a task

```python
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
```

Here we created a class `Task` from the subclass `Model` The `Task` Class represents how the table is going to be structured, each attribute in the model represents a field in the database, Django manages this conversion for us so we dont have to write a single line of SQL.

If you notice every attribute in this class is assigned a field type, when the attribute `title` is assigned `models.CharField` we are letting Django know that this field is a `CharField` ie a Charecter Field that can store any charecter and the `max_length` ie the maximum length of the data in this field is 100 characters. Django understands that this is a database field and will create the schema accordingly with the given options

> The max_length is a required parameter and is enforced by most databases, if the maximum value of a field is known beforehand the database can optimize the storage size, this was a big deal back in the day when memory was really expensive.

Similar to CharFields we have a bunch of other fields, You can take a look at all the different types of fields and their allowed paramaeters [here](https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types)

Similar to the `CharField`, The `TextField` is used to store charecters but `TextField` does not impose any restrictions on the size of the data, Boolean Fields store boolean values (True/False) , the default parameter can be used in any field to set the default value of the field.

Now that we have a model created, we need to ask django to sync the schema with the database,

> Note that you can have as many models as you want, You can try creating multiple classes if needed
