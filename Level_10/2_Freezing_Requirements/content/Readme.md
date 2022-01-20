We've already seen how to get the installed packages from pip in the 9th Level, Now we'll take a look at its advanced use cases.
### Handling Requirements

Usually, all python projects will have a file called `requirements.txt` at the root that contains a list of all the packages that are required to run the project. To create it, simply run the following command.

```bash
pip freeze > requirements.txt
```

This command will freeze the requirements and save them in a file called `requirements.txt` at the root of the project. This file can then be used by pip to install all the required packages. To specify a requirements file in pip you can use the `-r` flag.

```bash
pip install -r requirements.txt
```

pip will install all the required packages once this command is run. 
### Configuring Different Environments

It is also common to have a `requirements-dev.txt` as well, this file would contain extra requirements that are only required for development and testing. These packages need not be installed in the remote environment so they are maintained in a separate file. 

Some examples of packages that are used in dev only are the following: 
- [Django Debug ToolBar](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
    This is a package that adds an overlay to the server rendered page which makes development and debugging easier
- [Black](https://djangopackages.org/packages/p/black/)
    Auto Formatting in Django
- [Django Silk](https://github.com/jazzband/django-silk)
    Silk is a live profiling and inspection tool for the Django framework

These packages are usually used only in the dev environment, keeping these packages in production might not make much sense, this is why its usually good to have a seperate requirements that contains just the dev requirements.

When running the application in different environments, It also makes sense to create multiple settings.py files so that we can have different configurations for different environments.

You can inherit reqruiements from other requirements files if needed

```requirements
# requirements-dev.txt

-r requirements.txt # Inherits everything from the regular requirements to run the application

black==X.Y # Adds dev packages on top of the regular requirements
```