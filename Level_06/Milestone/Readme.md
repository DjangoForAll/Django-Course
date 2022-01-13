In This milestone, you will be extending the functionality of the project we worked in the level.

The specification for this program is as follows,

## Specification

You are asked to build the same project we worked on in the level and add some new features to it.

1) You have to create another field in the model to store the priority of a task, no two tasks can have the same priority, the listing views must always be sorted by priority. Adding a task with an existing priority should increment the existing task's priority by 1 ( Cascading )
2) Ability to mark tasks as completed
3) Ability to view completed tasks

This milestone should be implemented with the Django ORM.

All views must be implemented using Django's Generic View classes.
## Boilerplate code

Use the following repository as a starting point for this project: https://github.com/vigneshhari/GDC-Level-6-Milestone

to install the requirements for this project, run the following command in your terminal:

```bash
pip install -r requirements.txt
```


## Submission

Once all the required features are implemented, push the code to a GitHub repository and submit the link to the repo.


## Help

To understand how querysets can be ordered take a look [here](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#order-by) , you can use the exists method to check if an object already exists in the database, the exists method is documented [here](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#django.db.models.query.QuerySet.exists)
