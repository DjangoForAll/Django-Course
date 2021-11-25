The page you saw earlier was the default landing page that django provides to ensure that everything is working properly.

Lets start learning django by creating a new url route, URL routes always exist within the urls.py file. if you take a look at our current urls.py file, you can see that we have a variable called urlpatterns in the root of the file.

The URL patterns is a list of routes that django will check against when processing a request , anything that does not match the urlpattern will be redirected to a 404 page. if you have multiple routes that match a pattern, django only selects the first matching route.

The first argument to the path function is the route that django will check against, the second argument is the view that django will call when the route is matched. We will discuss what a view is later on.

in the last level we looked at simple url routes, Django's URL Dispatcher ( This is what actually routes the url ) is cabable of handling much more complex routes, it can match patterns, link to other routes and do a lot of other stuff.

If you observe the current urls.py file, you can see that there is already a route for the admin panel, Django provides an admin panel by default, we wont be looking into this for now, we'll just verify that the admin panel is working. Lets head over to the admin route.

This login page is rendered in the admin route, Lets try changing the url route and try accessing it from the browser. Lets change admin to manager and save the file, now you can see that the admin route no longer works but if we try manager it will work.

\*\* Note that the server automatically restarts, these are features provided by the django development server.

Now lets head on to creating a view. Views are simply functions that return a web response when given a web request, the response can be an html page, a redirection, some staus code. a json response, an image or anything you can think of!, Normally we keep all views in the views.py file, but for huge projects it usually makes sense to create a folder for views and maintain all views in there.

we'll create a view right inside the urls file just to show out how it works.

we'll create a new function, i'll call it `tasks_view` for now and give it a parameter called request.

and i'll create a corresponding url pattern `tasks` , we'll map our newly created function to our route, This means that whenever this route is called, our function is called.

Lets try going to the route and see what happens.

Django is kind enough to tell us exactly what went wrong, Django Expected our tiny function to return an HTTP Response but it returned None or Nothing.

Lets fix that by returning a response back

Lets import the HTTPResponse class from the `django.http` module. we'll return an empty instance of the HTTPResponse class for now. We can see that our error has disappeared and now we have an empty page. The HTTPResponse class accepts an optional argument called `status`, this is the status code that will be returned to the client. We can quickly try that with 404 and see that it works, Now, Lets add some content to the response.

The response should be the first argument or we can use the keyword argument `content` to set the content of the response. we can write any html code here. lets test it our with a simple html tag. and Voila! we have our first working Django route!

Creating html pages in python is a bit of a challenge, In the next chapter we'll see better ways to solve this
