You must have heard this term in a lot of projects or courses, What exactly is REST?

REST stands for Representational State Transfer , It is a standard or a design pattern that is used when developing web application API's.

API's that follow the REST standard are often called RESTful web applications or RESTful APIs.

Lets understand REST better with an example, lets take our task management app for now

We can perform a variety of operations on the tasks, the major ones are CREATE,RETRIEVE,UPDATE,DELETE (CRUD Operations)

REST forms guidelines on how these operations are performed, for example HTTP has a method called `GET` The GET method must always be used to retrieve or READ data as per the REST guidelines, similarly POST must be used to perform CREATE operations , `PATCH` and `PUT` for update operations and finally `DELETE` for delete operations.

So instead of having routes like `create-tasks` , `delete-tasks` and so on .. we will have one route for tasks `/task` and then all operations are done with different http methods, this makes the API much easier to understand to us and the folks using our API

REST does not mean just using the http methods as well, it has a bunch of properties and constraints ( 6 to be exact ), we will take a look at some of them.

- Statelessness
  Imagine you have 10 servers running your application, if a client sends a request it may end up in any one of those servers, if the response does not change no matter what server we connect to, then the application is called stateless, it simply means that no information is retained by the receiver

- Client-Server Architecture
  This means that the client and the server act independently, they interact with requests, The server does not respond without a request, it waits until a request is received to return a response

For the full defenition of REST, take a look [here](https://en.wikipedia.org/wiki/Representational_state_transfer)
