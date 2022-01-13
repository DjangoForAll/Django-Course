Now that we have a basic understanding of HTML and CSS, lets take a look at building our first web server with python.

Python ships with a simple web server implementation, We will use this implementation to look at exactly what a web server is and how we can create one.

To get the simplest web server running, lets run the following command:

```bash
python3 -m http.server 8000
```

Here the -m refers to running a library or a module in python and the http.server is the module that we want to run. 8000 is the port number that we want the server to run on.

Ports are used by various applications to communicate, 8000 is usually the port number for python dev servers, feel free to use any valid port number you like.

Now that we have our server running, open up your browser and navigate to localhost:8000 and you should see a simple web page.

The webpage shows all the current files in the folder we started the server in, Since there are no files in that folder the web server does not list anything, Lets create a txt file in this folder and then refresh the page.

Now you can see that the file can be browsed directly from here.

Similarly lets try it with an html file,

Note that when i select html in vs code i get emmet abbreviations as i start typing, these help me skip redundant parts of an html page.

We can add some sample text into our html page and then refresh our directory listing, Now we can see our html page as well, Clicking on the html page renders the page instead of showing the text.

There you have it, a simple http server that can be used to render html files. You can use this to test out how your html code renders.

Try creating different types of files and see how the browser renders them.
