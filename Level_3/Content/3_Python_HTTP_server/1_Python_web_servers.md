Now that we have a basic understanding on how a web page is created and styled, we have covered the basics of the Frontend side of an application, Now let's move to the backend!

We'll use python to build a simple web server. We'll start by creating a simple web server that will serve static files.

Seems really complicated right?

```shell
python -m http.server 8000
```

That's it, you just started a server that serves files from your directory. You can now open your browser and go to http://localhost:8000 to see the files.

8000 refers to the port number in your machine , 8000 is usually used for developing and testing web servers, but you are free to use any port number you want as long as no other app is using it.

Now, We have a server but it doesn't do anything.
