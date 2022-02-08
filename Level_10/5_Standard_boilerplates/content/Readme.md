Django comes built-in with a boilerplate template generator, we already learned how to use it to create our first Django project. The term "boilerplate" simply means anything that is repeated over and over again, Boilerplate projects save us time in creating a skeletal version of a project that can be used to build anything.

The official Django boilerplate only covers a handful of features, we'll learn about a better boilerplate template generator.

We'll be working with [Django CookieCutter](https://github.com/cookiecutter/cookiecutter-django)

Cookiecutter itself is a package that allows the creation of projects from templates, The Django cookiecutter is just a template for the cookiecutter package, Which also means that you can create your own version of a cookiecutter with everything that you feel is required for a Django project.

The installation instructions for cookiecutter are present in its Github repository.

-- Video 1

If you are confused about the options, you can always refer to the [cookiecutter documentation](https://cookiecutter-django.readthedocs.io/en/latest/project-generation-options.html) to get more information.

Django cookiecutter by default, uses another type of database called Postgres, The ORM code we wrote remains the same, but we have to install and configure Postgres to run our project.

Follow this [tutorial](https://www.postgresguide.com/setup/install/) to install and configure Postgres in your system. Once Postgres is installed, create a new database by following these instructions, make sure that the database has the exact same name as your Django project.

Once you have configured Postgres, you can create a new virtual environment and install all the required packages, The cookiecutter project comes with a set of requirements, to install them run the following command.

```bash
pip install -r requirements/local.txt
```

We need to configure one more variable before we can start our server, head over to the `config/settings/base.py` file, and change the `CELERY_BROKER_URL` variable to the following line.

```python
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://localhost:6379")
```

If this line is not set, it expects the value to be present in the current environment and throws an error if it's not found. We have set a default value for the variable so that it does not throw that error.

Once you have configured the project, you can run all the migrations that are required and then start the server to test if everything is working as intended, Cookiecutter by default includes a login/register page and an extensible user model, and a lot of other features as well, Feel free to explore the features and see what you can find.

### Deploying to Heroku


-- Video 2

### Configs in Heroku


| Key                    | Config                               |
| ---------------------- | ------------------------------------ |
| DJANGO_ADMIN_URL       | admin                                |
| DJANGO_ALLOWED_HOSTS   | application_domain_name_here         |
| DJANGO_SECRET_KEY      | Generate one at https://djecrety.ir/ |
| DJANGO_SETTINGS_MODULE | config.settings.production           |
| MAILGUN_API_KEY        | Get from MailGun                     |
| MAILGUN_DOMAIN         | Get from MailGun                     |