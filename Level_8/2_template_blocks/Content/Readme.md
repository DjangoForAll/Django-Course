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
    <div id="sidebar">
      <ul>
        <li><a href="/">Home</a></li>
      </ul>
    </div>

    <div id="content">{% block content %}{% endblock %}</div>
  </body>
</html>
```

This template can be used as a base template for other templates that we create, lets create a new template to list tasks from the base template.

```html

```
