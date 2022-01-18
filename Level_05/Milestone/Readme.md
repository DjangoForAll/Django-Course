In This milestone, you will be extending the functionality of the project we worked in the level.

The specification for this program is as follows,

## Specification

You are asked to build the same project we worked on in the level and add two new features to it.

1) A new route to mark tasks as completed. ` GET /complete_task/<Task Id> `
2) A new route to view completed tasks. ` GET /completed_tasks `

Completed tasks should no longer be visible in the existing tasks view.

For the other functionality, the URL routes should be exactly the same as the ones used in the level.

For bounty points, implement another route `GET /all_tasks` that renders pending and completed tasks on a single page.

This milestone should be implemented with the Django ORM. the model is already present in the boilerplate code, no changes should be made to the model.
## Boilerplate code

Use the following repository as a starting point for this project: https://github.com/DjangoForAll/GDC-Level-5-Milestone

to install the requirements for this project, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

Also, migrate the database changes so you can use the model:
```bash
python manage.py migrate
```

## Testing

Run the following command to test your application.

```bash
python manage.py test
```

## Submission

Once all the tests are passing, push the code to a GitHub repository and submit the link to the repo.
