Our current tasks application can add tasks, view them and delete any given task.

Your Task is to create another field to store the priority of a task, no two tasks should have the same priority, appropriate form validations should also be present, the listing views must always be sorted by priority.

The completed tasks features from the last level's submissions must be re-implemented with Django's generic views.

To understand how querysets can be ordered take a look [here](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#order-by), you can use the exists method to check if an object already exists in the database, the exists method is documented [here](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#django.db.models.query.QuerySet.exists)

The spec for the new pages are given below, ensure that your solution matches the spec. Run the test suite to check if the functionality is working as expected

`GET /completed_tasks` Should render an HTML page with all the completed Tasks  
`GET /completed_tasks/<task index>` should redirect to a page, with a confirmation to complete a task
`POST /completed_tasks/<task index>` should mark a task as completed

The Task model should have an attribute named `priority`

> Make sure that you do not change the name of the models and the routes. This is to ensure that the tests are working as expected.

Upload your solution to a public Github repository and submit the link to the repository to complete this milestone.
