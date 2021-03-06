
### Static Files
These are files that are not generated, changed, or processed by the server ( These include CSS, images, js, etc that you use in your HTML files ), The server just serves them if needed. Django is terrible at static files management because it was never intended for it, There are packages like `whitenoise` that make it slightly better, but it is still a bad idea to let Django manage static files.

> Django is completely capable of serving static content, but it is not very efficient or very fast compared to tools that were built to solve this exact problem. To quote the Django docs, "This method is grossly inefficient and probably insecure, so it is unsuitable for production."

Usually, you will offload all the static files to external file storage to let them manage static content delivery themselves. The `STATIC_URL` setting in your settings file is prepended to all static files generated by Django, if we were to host the static files outside of Django, we simply change the `STATIC_URL` to point to the new location. for eg, let's say that your static content was served at `https://static.example.com/`, then we would change the `STATIC_URL` to `https://static.example.com/`, once changed, a static file like `/static/css/style.css` would be changed to `https://static.example.com/css/style.css`

For production deployments, you can use something like Digitalocean Spaces or AWS S3 to offload the static files to a remote location. You can also use a proxy in your deployment to offload the static files to another server. we won't be getting into these methods in detail, but you can find a lot of information about them on the internet.

Reference Articles:
- [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-set-up-object-storage-with-django)
- [Nginx](https://sayari3.com/articles/11-how-to-serve-djangos-static-files-using-nginx-on-localhost/)

Getting static files working in Django is a bit tricky and requires some trial and error, We'll be using a package called `whitenoise` that will let Django itself serve static files in production, this is usually preferred when there is very few static files or very small traffic to routes with static files

To learn more about static file deployment, read this [article](https://docs.djangoproject.com/en/4.0/howto/static-files/deployment/)

### Dynamic Files
These are files that are created on the go or uploaded by a user, examples are user profile pictures/images, user reports, etc. Since these are not static files they cannot be predetermined when the application is launched, handling Dynamic files is, therefore, more complicated than static files.

In Django Dynamic Files are often called media files, Django has lots of wrapper methods to handle media files, One way to handle media files is to write the file into the current application's media folder ( usually `/media` ) but this approach only works when there is a single instance of the application running, running more than one instance required a more complicated shared drive to be present.

The best way to handle Dynamic files is to not handle them ourselves, using external services like AWS S3 or Digital Ocean Spaces makes our life easier and lets all application instances share common media storage.

Reference Articles:
- [AWS](https://ordinarycoders.com/blog/article/serve-django-static-and-media-files-in-production)
- [Digital Ocean](https://testdriven.io/blog/django-digitalocean-spaces/)
