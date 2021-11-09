Till now we were using libraries that were packaged with the standard python installation ( `htttp.server` ), Now we will be looking at a package manager for python called pip. pip will allow us to install external libraries ( libraries that developer by other folks ) with ease.

Python packages are usually hosted at [PyPI](https://pypi.org/), PyPI is free and anyone can upload their own package into it, Packages from PyPI can be installed using pip.

Python packages are versioned, Versioning allows us to keep track of the changes in the code, this becomes very useful when we are working with large libraries that are updated frequently. We can force pip to install a specific version of the library so that even if newer versions of the library are released, we can still use the old version which works with our project.

You might be asking why we would possibly want to keep the old version of the package, Newer is better right!
This is true for some cases, but sometimes upgrades change the way the library works and some of the features it supported earlier might not work now. This would cause our project to break. To solve such issues, we keep track of the exact versions of the libraries we are using, these are usually called requirements or dependencies.

The libraries we use can also have their own dependencies, pip finds out exactly who needs what and installs them correctly.

pip is shipped with all standard python installations by default, if its not installed by default, you can install it from this [tutorial](https://pip.pypa.io/en/stable/installation/#ensurepip) or this [tutorial](https://www.makeuseof.com/tag/install-pip-for-python/)

To check if pip is intalled on your system, you can use the following command on your terminal:

```bash
pip freeze
```

This command lists all the packages that are installed on your system, note that each package is listed with its current version as well.

The packages are listed in the following format: `package_name==version` ( `==` is the separator for the version number ).

To install a python package, you can use the following command:

```bash
pip install package_name
```

we can specify restrictions in the version by using

```bash
pip install package_name==version
pip install package_name>=version # installs a version greater than or equal to the specified version
```
