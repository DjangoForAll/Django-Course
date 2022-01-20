We have already seen the flow of a request that hits a django server, lets take an example and create a new middleware in django.

Lets create a middleware that will add the current time to the request and response.

```python
class CustomMiddleware(object):
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        response = self.get_response(request)
        return response
```

The get_response method is passed by django and it contains logic to execute the next middleware in order, you can think of this as a recurvive call that calls all of the middleware before it actually responds back. in the final middleware the get_response will actually invoke the view based on the route figured out, the response from this view is then available to every middleware which can decide to perform some logic or return it without any changes.

Middleware are extremely useful in implementing security features, with just one line we can plugin a middleware that implements a specific feature and our core logic remains unchanged.

To demonstrate middlewares, lets add a simple feature with middlewares, lets set an attribute that stores the current time to the request object and try to print it out in the html template.

```python
from datetime import datetime

class CustomMiddleware(object):
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        request.current_time = datetime.now()
        response = self.get_response(request)
        return response
```

now we can easily refer to {{request.current_time}} in our template to refer to the current time, this is accessible across all the views written in django. This particular use case was just shown as an example.