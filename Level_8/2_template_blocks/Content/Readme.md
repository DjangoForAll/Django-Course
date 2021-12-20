Template Inheritance is one of the most powerful featue of Django's template engine, Template inheritance allows you to create a template skeleton which can be reused in other tempalates.

Most applications have a common header/footer/menu in all templates. This is where template inheritance comes in handy.

Lets learn more with an example :

let's create a base template called `base.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>{% block title %}Default Title{% endblock %}</title>
  </head>
  <body>
    <div>
      <ul>
        <li><a href="/">Home</a></li>
      </ul>
    </div>
    <div>{% block content %}{% endblock %}</div>
  </body>
</html>
```

This template can be used as a base template for other templates that we create, lets create a new template to list tasks from the base template.

```html
{% extends 'base.html' %} 

{% block title %}View Tasks{% endblock %} 

{% block content %}
<h1>All the content should go here!</h1>
{% endblock %}
```

For any child template you must define which parent template you are extending from at the start of the file, we use the extends tag for extending a parent template, you can extend any template in django,
Once we specify the parent template, we can create blocks we want to override/modify in the child tempalate.

When rendering the page, Django will load up the parent template and replace the blocks with the child template. This means that anything that is not specified inside a block is ignored completely. This makes it really easy to structure web documents, and makes it easier to reuse HTML code.

Templates in Django can do a lot more stuff, take a look [here](https://docs.djangoproject.com/en/4.0/ref/templates/language/) for the complete documentation.