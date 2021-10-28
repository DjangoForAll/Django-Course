We have a server that can render dynamic content, but it can only render one page, most websites have multiple pages that you can navigate to, Dynamic routing enables you to render content based on what path the user currently is in.

To get the current path the user is in, we can use the path attribute of the class

```python
print(self.path)
```

Once you have the path, you can setup different routes and change html contnet based on that

```python
if(self.path == "/home"):
    html = "<h1>Home</h1>"
elif(self.path == "/time"):
    html = "<h1>The current time is</h1>"
else:
    html = "<h1>404</h1>"
```

Now on visiting different paths you get different html content

You can play around with this to create more examples.
