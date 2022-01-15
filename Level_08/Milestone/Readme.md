In This milestone, you will be extending the functionality of the project we worked in the level.

The specification for this program is as follows,

## Specification

You are asked to build the same project we worked on in the level and add two new features to it.

1) Move all our code to use template blocks with a base template named `base.html`
2) Create a user-configurable report, The user can configure when he would like to receive his email reports ( in a day ) ( like 10PM or 11AM or any other valid time ) or if he wants to disable reports altogether. A background job would ensure that the user would get his reports at the specified time
3) The reports should contain a breakdown based on the task's status. ie, it should show the number of tasks with all the possible statuses

This milestone should be implemented with the Django ORM. All required model changes and migrations must be performed by yourself, make sure to include any migrations created in the submission.

The routes are not predefined, you can use any names for them.

The background jobs must be executed with the help of celery workers, Bounty points for identifying and resolving potential edge-cases

## Boilerplate code

Use the following repository as a starting point for this project: https://github.com/vigneshhari/GDC-Level-8-Milestone

to install the requirements for this project, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Submission

Once all the required features are implemented, push the code to a GitHub repository and submit the link to the repo.
