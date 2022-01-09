
### Static Files
These are files that are not generated, changed or processed by the server ( These include css,images,js etc that you use in your html files ) , The server just serves them if needed. Django is terrible at static files management because it was never intended for it, There are packages like `whitenoise` that makes it slightly better, but it is still a bad idea to let django manage static files.

Usually you will offload all the static files to an external file storage to let them manage static content delivery themselves. One of the easiest hack you can test yourself is to use the github's built in hosting feature, github hosts the content with their built in feature called pages for free. This is a great way to offload static files to github. The `STATIC_URL` setting in your settings file can be used to let django know that it is no longer handling static mangement, set the variables value to `"http://static.example.com/"` and now django will prepend the url to all static files, so the files are no longer served from django.

Uploading to github is just a hack, for production deployments you can use something like DigitalOcean Spaces or AWS S3 to offload the static files to a remote location. You can also use a proxy in your deployment to offload the static files to another server. we wont be getting into these methods in detail, but you can find a lot of information about them on the internet.

Getting static files working in django is a bit tricky and requires some trial and error, Learn more about `whitenoise` and how it can be used to make your life easier [here](https://devcenter.heroku.com/articles/django-assets)

To learn more about static file deployment, read this [article](https://docs.djangoproject.com/en/4.0/howto/static-files/deployment/)

### Dynamic Files
These are files that are created on the go or uploaded by a user, examples are user profile pictures/images, user reports etc. Since these are not static files they cannot be predetermined when the application is launched, handling Dynamic files is therefore a tad bit complicated than static files.

In Django Dynamic Files are often called media files, Django has lots of wrapper methods to handle media files, One way to handle media files is to write the file into the current application's media folder ( usually `/media` ) but this approach only works when there is a single instance of the application running, running more than one instance required a more complicated shared drive to be present.

The best way to handle Dynamic files is to not handle them ourselves, using external services like AWS S3 or Digital Ocean Spaces makes our life easier and lets all application instances share a common media storage.