Static files are files that are not changed when the application is running, these include the CSS files, images, javascript files, and any other type of files that are not dependent on the application logic.

Django provides a very simple way to handle static files.

1) Let's first create a new folder called static at the root of our project. This folder will contain all the static files that are used in our application.

2) Now, add an image to our static folder, this could be any image, let's call it `test_image.png`

3) let's create a new template called `test_static.html` , and then create a route called `/test_static/` that renders this template.

4) To reference the static file inside a Django template, we need to let Django know that we are serving a static file and let it handle the route to the static file.

```html
<!-- templates/test_static.html -->
{% load static %} <!-- This tag should be at the top of the HTML document and must only be defined once. -->
<img src="{% static 'test_image.png' %}" alt="Test Image">
```

Instead of manually specifying the URL route to the image, we are letting Django handle the URL creation, this way if decide on moving all static files to a separate server, we do not need to change all the static URL's in our template, we can let Django take care of it. Letting Django handle the static files also opens the door to a lot of packages to build more features on top.

This method is applicable to any static file, not just images, we can use the static tag to load our CSS files, js files, etc.

> Note that the load static tag has to be the first tag in the template and it should only be defined once.
