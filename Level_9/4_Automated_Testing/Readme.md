Executing test usually gets more time taking and resource intensive1 as a project evolves, developers also need a method to ensure that untested code never gets deployed.

Testing code is usually a part of the CI/CD ( Continuous Integration/Deployment ) Pipeline, It is simply a bunch of scripts that are executed when a certain action is performed like a push being made to a repo or a new branch being created.

CI/CD piplines usually first test the code with a predefined environment and ensure that all the tests pass before moving on to the next step. The tests results are visible to all developers which makes it very transparent.

There can also be cases where the project needs to be tested on different types of machine (Mobile/Desktop), CI/CD pipelines can be configured to run the tests of different machines if required.

## Github Actions

Lets create a github action that will run our tests on every push to the github remote repo. We wont be learning in detail about github action's themselves, just enough to test our code.

First we will create a requirements file that will list out the dependencies of our project, this will help the CI to create the same virtual environment everytime for testing our code. We will discuss this concept in detail later in the course.

```bash
pip freeze > requirements.txt # Must be run in the root of the project
```

If you open up the requirements.txt file, you can see that it contains all the packages we use along with their versions.

Now that we have that done, Lets create a new folder in the root called ".github" and another folder called "workflows" inside it. This is the folder github will look into for finding workflows, these workflows are then executed by github actions.

Lets create a new file in the folder `.github/workflows` called django-test.yml and paste the following config in it.

```yaml
name: Django CI

on:
  push:
    branches: [master]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python Environment
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run Tests
        run: |
          python manage.py test
```

The config is really simple, It defines what branch the action should be run and a series of steps that must be taken in the pipeline.

The first step checks out the code from the branch, then it proceeds to create the Python Environment with the given python version and then installs the dependencies. Once the dependencies are installed the tests can be run.

Thats it! If you push the code and visit the actions tab in your github account, you can see the results of your tests. Github Actions can be used to create much more cooler pipelines, visit its [documentation](https://github.com/features/actions) to learn more 
