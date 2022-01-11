Over the course of this course, we've used a couple of packages, but we haven't noted down what these packages are or what version of them we are using.

When deploying an application, it is crucial that the deployment environment has exactly the same packages running the same versions. Any deviation can cause unexpected behaviors

### Introduction Requirements

Usually, all python projects will have a file called `requirements.txt` at the root that contains a list of all the packages that are required to run the project. To create it, simply run the following command.

```bash
pip freeze > requirements.txt
```

This command will freeze the requirements and save them in a file called `requirements.txt` at the root of the project. This file can then be used by pip to install all the required packages. To specify a requirements file in pip you can use the `-r` flag.

```bash
pip install -r requirements.txt
```

pip will install all the required packages once this command is run. It is also common to have a `requirements-dev.txt` as well, this file would contain extra requirements that are only required for development and testing. These packages need not be installed in the remote environment so they are maintained in a separate file. 

### Configuring Different Environments

When running the application in different environments, It also makes sense to create multiple settings.py files so that we can have different configurations for different environments.
