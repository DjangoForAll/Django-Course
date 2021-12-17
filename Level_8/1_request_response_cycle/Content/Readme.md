A web application usually revolves around requests and responses, the application logic somehow converts the request into an appropriate response, There are a lot of stages before the request is reached to the view that we create, these steps are usually called as middleware. we wont be discussing in detail about middlewares, we'll just touch base on why they are important in django.

Roughly speaking a django request goes through the following flow,
Request -> Request Middleware -> URL Router -> Views -> Response Middleware -> Response

Lets start with the actual request, The request refers to the HTTP request made by the client to the server. Once the request is recieved by the server, the request is passed through a series of middlewares, the middleware usually takes care of functionality that is common to the entire project, for example the user object was automatically populated when the user was logged in, this object was populated by a middleware, similarly POST requests made without a CSRF token were automatically rejected, this logic was also handled by a middleware. Middleware are declared in the settings file and each middleware entry is called squentially in series.

take a look at the `MIDDLEWARE` variable in your `settings.py` file to see exactly what all the middleware are.

Once all the middlewares are run, Django will resolve the url and determine which view to call, If there are no matching routes, the dispatcher renders the standard 404 page. Once the corresponding view is resolved, it is invoked with the request.

The view contains all our business logic, the view itself may have seperate flows internally to best suite the business logic.

Once the corresponding view is found out, the view is again passed through the middlewares and then the view is invoked with the request object.

The view performs the required business logic and returns a response object or raises an exception, unhandled exceptions are handled by the exception handler middlewares. and the responses are passed back through the middlewares, the responses are passed in the reverse order of the middlewares.

And that completes the request response cycle. Middlewares make it incredibly simple to "plugin" new handlers into an existing request response cycle.
