A simple http server does not really let us create content on the go, It just lists everything in the current folder.

Lets create a custom server in python that can serve dynamic content.

## Start with a new python file.

I'll be pasting this snippet to save time typing it out

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
class MyServer(SimpleHTTPRequestHandler):
    pass
address = "127.0.0.1"
port = 8080
server_address = (address, port)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()
```

we are creating an empty class from the `SimpleHTTPRequestHandler` class from the http.server module

Once we have a class we can start python to start listening on a port and address and invoke the class we created for requets.

Once we run the file,we can see that the same directory listing page is up again,

We have learned about inheritance and overriding in the previous level, Here we have created a new class from the BaseClass, to create new functionality we have to override some its methods

lets first try overriding the `do_GET()` method, this method is invoked when the client sends a GET request to the server.
when we override the method, we can place custom logic and control how the page is rendered.

after overriding the do_GET() method, we can see that we get an error instead of the directory listing, this is because we have not implemented the logic to handle the request.

Every HTTP Request Response should have a status code, this status code is used to indicate the status of the request. Clients can then use this information to determine if the request was successful or if any further action is needed.

If a request is successfull, then the status code should be 200, This is not something that we decide for each project , HTTP response code are a standard and should be followed strictly in all projects

Lets add a status code to our current server and see what happens.

```python
self.send_response(200)
self.end_headers()
```

Now our page is rendered empty, without any errors, the error has been fixed. Lets try changing the status code and see how the page rendering changes.

Lets change it to infamous 404 error, This error code indicates that the requested resource was not found.
Similaryly, we can change the status code to 500 to indicate that the server encountered an error.

Generally the 200 series of status codes indicate success, the 300 series indicate that the client should take an action to resolve the issue like redirecting to the login page when you try to access a reosource, and the 400 series indicate that the request was malformed and the 500 series indicate that the server encountered an error.

I will leave a link with all the available status codes in HTTP. You can try to render each one and see what happens.

Apart from the status code, the server also sends some metainformation along with the response, these are called header. For the scope of this level we will be looking into the content type header, this header specifies what kind of content we are sending back to the client, for example, if we are sending a html page, then the content type header should be set to text/html, if we are sending text files, the content type should be set to text/plain, and so on.

Lets set the header to text/html and see what happens.

```python
self.send_header("Content-type", "text/html")
```

Nothing happens when the load the page becuase there is no content to render yet!

Now lets create some html and try sending that back to the client.

```python
content = "<h1>Hello World!</h1>"
self.wfile.write(content.encode())
```

self.wfile.write() is a method that sends the response back to the client. decode() is a string method that converts the string to bytes since the response is in bytes.

Now lets view our page again and see what happens.

There you go, we have created our very own server!

Lets Make this a bit more dynamic, Lets add the current time to the response

Lets import the datetime module and add the current time into the response

```python
from datetime import datetime
content = f"<h1>Hello World!, The Current Time is, {datetime.now()}</h1>"
```

And now we have our very own dynamic page!

Play around with the server and see what happens.
