Since some HTML tags will be used extensively through this course, we can take a look at them in detail.

### Forms and Inputs

Forms and Inputs are very important in web development. Without them, the web is just a collection of text and links.

The Read-only version of the internet was called [Web 1.0](techopedia.com/definition/27960/web-10)

Using Forms and Inputs the user can interact with the webpage and send data back to the server. This data can then be used to create dynamic web pages, In dynamic web pages, the pages are generated on the fly by a web server. For Example, let's say that you were displaying the tasks in a to-do list with an HTML page. This might be different for every user every time so the HTML page has to be created dynamically each time.

The form tag has two important attributes that are used to send back data to the server, the action attribute specifies the URL that the data will be sent to, and the method attribute specifies the method that will be used to send the data.

There are two main methods that we use to send data to the server, GET and POST. GET is used to send data encoded into the URL, and POST is used to send data to the server in the body of the request. Ultimately both of them achieve the same goal, POST over HTTPS is the most secure method. GET is used when the data is not sensitive.

We will take a short example and look at how each method works over a short video.

<Video>

### Quick History on GET vs POST

The inital version of the HTTP also called HTTP/0.9 was a very simple protocol that only supported the GET method. the internet at that point was simply requests to fetch documents ( ie That is what the method GET Implies, "GET" a document ), There was no room for anything else.

The web was being developed rapidly at the time and HTTP/0.9 simply could not meet every need, which led to a lot of independent experiments where servers would implement features and browsers would start to support them, these were not really structured until HTTP/1.0 came along to bring in more structure.

HTTP/1.0 Defines three standard methods including `GET` and `POST`. The actual usage for these methods can be read [here](https://datatracker.ietf.org/doc/html/rfc1945#section-8)

The HTTP/1.0 defines almost all of the terms we use in this course, view them [here](https://datatracker.ietf.org/doc/html/rfc1945) if you're intrested in the details.

> Quick Fact: We are current at HTTP/2.0 with HTTP/3.0 coming soon.

Getting back on track, forms supports GET and POST methods to transfer data from the client to the server, the GET method is the default method and send the data encoded in the URL which the POST method sends the data in the request body.

POST methods are prefered for most forms since it does not have a size limit ( relative to GET ) and it is more secure since the data is not stored in the URL. URL's are often logged by servers and proxies ( Internet providers ) so it is generally not a good idea to use GET methods to send any sensitive data.

However POST requests are more complex and is harder to create in plain HTML, we can create a simple redirect page with a get parameter by adding parameters to the URL. but the same is not possible with POST.

This opens up a lot of use cases for GET methods, for example, Bookmarking pages, Links with data in emails, links with tracking codes, region/language preferences and so on...

Now that you have a basic understanding of forms, try creating a form with different types of inputs and see how they work.

For examples visit this [link](https://www.w3schools.com/tags/tag_form.asp)
