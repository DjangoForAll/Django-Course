Python packages are global by default. That means that if you install a package in your machine, this package is availiable in all projects you have on your machine. Although this sounds really good, it limits projects with conflicting dependencies ( Say you were working on two projects which used different versions of the same package ) To solve this issue we can use virtualenvs.

Virtualenvs create an isolated environment where you can install packages and experiment freely without affecting the rest of your machine. You can create as many virtualenvs as you want. Another advantage of virtualenvs is that they dont require permissions to install packages, installing global packages usually required you to have root access.

> Virtualenv is not the only solution for this problem, there are multiple ways to create virual environments like pipenv, venv ( and a bunch more!) but for the sake of the course we will stick to virtualenv.

Now that we know what virutalenvs are, lets create one!

```bash
pip install --user virtualenv
```

Virtualenv itself is a package that is installed with pip, This command installs the virtualenv package.

```bash
virtualenv .env
```

This command will create a new virtual environment under the .env folder, This is usually where the environment resides , feel free to name it something other than .env

At this point you can take a look at your current folder and you should see a folder called .env ( or whatever you named it ), this is the folder where your virtual environment will reside.

To activate your virtual environment run the following command:

```
source .env/bin/activate
```

Once you run the command you'll see the the environment name is displayed in the terminal, this means that the virtual environment is active.

To confirm the virtual environment is active you can run the following command:

```bash
which python
```

The `which` command tells you where the given command is located. In this case the python interpreters location. If the virtual environment is active the python interpreter will be located in the .env/bin folder.

You can deactivate the virtual environment by running the following command:

```bash
deactivate
```

Try running the `which` commnand to make sure that the virtual environment is no longer active.

Make sure that you are always activating the **right** environment before you start working on your project.
