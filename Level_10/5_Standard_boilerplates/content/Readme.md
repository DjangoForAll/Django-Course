Django comes built-in with a boilerplate template generator, we already learned how to use it to create our first Django project. The term "boilerplate" simply means anything that is repeated over and over again, Boilerplate projects save us time in creating a skeletal version of a project that can be used to build anything.

The official Django boilerplate only covers a handful of features, we'll learn about a better boilerplate template generator.

We'll be working with [Django CookieCutter](https://github.com/cookiecutter/cookiecutter-django)

Cookiecutter itself is a package that allows the creation of projects from templates, The Django cookiecutter is just a template for the cookiecutter package, Which also means that you can create your own version of a cookiecutter with everything that you feel is required for a Django project.

The installation instructions for cookiecutter is present in its Github repository.

-- Video 1

If you are confused about the options, you can always refer to the [cookiecutter documentation](https://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html) to get more information.

Django cookiecutter by default, uses another type of database called Postgres, The ORM code we wrote remains the same, but we have to install and configure Postgres to run our project.

Follow this [tutorial](https://www.postgresguide.com/setup/install/) to install and configure Postgres in your system. Once postgres is installed, create a new database by following these instructuions, make sure that the database has the exact same name as your django project.

Once you have configured Postgres, you can create a new virtual environment and install all the required packages, The cookiecutter project comes with a set of requirements, to install them run the following command.

```bash
pip install -r requirements/local.txt
```

Once you have configured the project, you can run all the migrations that are required and then start the server to test if everything is working as intended, Cookiecutter by default includes a login/register page and an extensible user model, and a lot of other features as well, Feel free to explore the features and see what you can find.

### Deploying to Heroku


-- Video 2