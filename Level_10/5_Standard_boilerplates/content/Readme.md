Django comes built-in with a boilerplate template generator, we already learned how to use it to create our first Django project. The term "boilerplate" simply means anything that is repeated over and over again, Boilerplate projects save us time in creating a skeletal version of a project that can be used to build anything.

The official Django boilerplate only covers a handful of features, we'll learn about a better boilerplate template generator.

We'll be working with [Django CookieCutter](https://github.com/cookiecutter/cookiecutter-django)

Cookiecutter itself is a package that allows the creation of projects from templates, The Django cookiecutter is just a template for the cookiecutter package, Which also means that you can create your own version of a cookiecutter with everything that you feel is required for a Django project.

The installation for cookiecutter is present in the Github repository, When creating a project with cookiecutter, you will be asked a bunch of questions, which will be used to configure the project, If you are not aware of what these options are, or you are confused about what they mean, you can always refer to the [cookiecutter documentation](https://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html)

Make sure that you have enabled the following options when creating a project with cookiecutter :

```bash
use_drf [n]: y
use_celery [n]: y
debug [n]: y
```

for the rest of the options, you can leave it to the default values.

Django cookiecutter by default, uses another type of database called Postgres, The ORM code we wrote remains the same, but we have to install and configure Postgres to run our project.

Follow this tutorial to install and configure Postgres in your system, If you don't want to install Postgres, you can continue using SQLite by pasting the following code in the `config/settings/base.py` file

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ROOT_DIR / 'db.sqlite3',
    }
}
```

the existing database configuration must be removed before using this. to remove the configuration, simply delete the `DATABASES` variable from the file.

Once you have installed Postgres, you can create a new virtual environment and install all the required packages, The cookiecutter project comes with a set of requirements, to install them run the following command.

```bash
pip install -r requirements/
```

Once you have configured the project, you can run all the migrations that are required and then start the server to test if everything is working as intended, Cookiecutter by default includes a login/register page and an extensible user model, and a lot of other features as well, Feel free to explore the features and see what you can find.
