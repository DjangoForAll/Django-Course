Here are some of the different ways to use Tailwind CSS in Django.

1) Use the Tailwind CDN:  
    This is the easiest method and usually required just one line addition in your template, The tailwind CSS is usually found at `https://cdn.jsdelivr.net/npm/tailwindcss/dist/tailwind.min.css`, just add this in the  `<head>` section of the template and you should be good to go.
    Example:
    ```html
    <head>
    <!-- -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss/dist/tailwind.min.css">
    <!-- -->
    </head>
    ```
    This method does not bring in all the features that Tailwind provides, but it should be good enough to get you going.
2) Using Django Tailwind:  
    This is a python package built to be used with Django to provide a comfortable way to use the Tailwind CSS framework with a Django project.  
    Instructions to set this project up can be found [here](https://django-tailwind.readthedocs.io/en/latest/installation.html)