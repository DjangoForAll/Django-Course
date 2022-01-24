Lets start a project with cookiecutter.

To start off lets install cookiecutter itself

```bash
python3 -m pip install cookiecutter
```
Once that is installed lets start a new project

```bash
cookiecutter https://github.com/cookiecutter/cookiecutter-django
```

The project name can be anything you want, the slug is just a version of your project name that can be put into a url

The description and author_name can filled in as required

domain_name can be any fake domain you want, we'll change this later on.

Version and email can be left to the default values.

Lets select MIT for the open source license, since it is the most "Free" License

Leave timezone as UTC for now, 

windows, pycharm and docker can be set to N/default

Select the default postgres version and disable the js task runner

we'll set the cloud provider as None [3]

Most email providers will provide email services for free, we'll keep using Mailgun for now.

we wont be using async views in this project

DRF is required [y]

Custom bootstrap compilation is not required, so we'll leave it as N/default

We will disable compression for now.

we can enable celery dev, and disable mailhog (Mailhog is used for testing emails)

We'll disable sentry for now, sentry is a free open source error reporting tool, which i highly reccomend looking into.

We'll enable whitenoise for serving static files in heroku and enable heroku itself.

We can leave CI to None Now. and let the env local option be set to the default value.

Debug can be set to y

Finally you should see a success message and a new project should be created in the current directory