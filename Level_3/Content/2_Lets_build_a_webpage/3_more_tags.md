Html provides a lot of standard tags for building webpages.  
You can visit the following link to see a list of all the tags and how they can be used

[MDN Mozilla Html Reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

Since some tags will be used extensively through this course, we can take a look at them in detail.

### Forms and Inputs

Forms and Inputs are very important in web development. Without them the web is just a collection of text and links.

The Read only version of the internet was called [Web 1.0](techopedia.com/definition/27960/web-10)

Using Forms and Inputs the user can interact with the webpage and send data back to the server. This data can then be used to create dynamic web pages, In dynamic web pages the pages are generated on the fly by a web server. For Example, lets say that you were displaying the tasks in a todo list with an html page. This might be different for every user every time so the html page has to be created dynamically each time.

The form tag has two important attributes that are used to send back data to the server, the action attribute specifies the url that the data will be sent to, and the method attribute specifies the method that will be used to send the data.

There are two main methods that we use to send data to the server, GET and POST. GET is used to send data encoded into the url, and POST is used to send data to the server in the body of the request. Ultimately both of them achieve the same goal, POST over https is the most secure method. GET is used when the data is not sensitive.

We will take a short example and look at how each method works over a short video.
