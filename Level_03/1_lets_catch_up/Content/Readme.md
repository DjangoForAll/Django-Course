The aim of this chapter is to get you familiar with the basics of the internet and some associated terminology. This will make it easier to follow the rest of the course.

## Dynamic and Static Web Pages

When browsing the web you might see pages that don't change no matter who views them or where you view them from, these are called static web pages, we'll learn how to make static web pages at this level
Most of the pages you visit will be dynamic, these are pages that are generated just for you, they are newly generated just for you by servers ( specifically web servers ).

## FrontEnd vs BackEnd

Front End is the part of the web that is seen by the user, they are also called client-side. Back End is the part of the web that is not seen by the user, they are also called server-side.

The backend contains the logic that makes your application work, if you are making a todo app, the todo items will be stored in the backend, while the frontend focuses on styling and making the website look and feel better for the end-user. Splitting the app into different parts makes it easier to manage and update. It also allows developers to create different versions of the application like a mobile version, a desktop version, a version for a tablet, etc without much hassle.

In this course, we will be focusing on the backend primarily.

## API's and JSON

In modern applications, the Front End and Back End are developed and maintained separately, They often use APIs to communicate with each other, In the previous section we talked about backend and frontend, the frontend usually communicates with the backend using HTTP requests and responses.

In the context of a Todo App, the frontend might perform API calls to fetch existing todo's, create a new todo item, mark an item as completed, etc. These API requests perform a certain action.

Now that we know that the frontend and backend communicate, we can talk about the data that is being sent and received. Usually, when the frontend requests data from the backend, the backend sends back data in the form of JSON. Note that JSON is not the only way for data interchange, you can also use XML, or even just plain text. JSON is the most common format for data interchange in modern applications.

JSON Stands for JavaScript Object Notation, it was based on a subset of the Javascript Programming language. Even though JSON is based on Javascript, it is a language-independent data format, as in it can be used in any programming language.

Let's look at a JSON Response for a Todo App.

```json
{
  "todos": [
    {
      "id": 1,
      "title": "Learn Python",
      "completed": false
    },
    {
      "id": 2,
      "title": "Learn HTML",
      "completed": false
    }
  ]
}
```

This is a JSON response, it contains a list of to-do items, each to-do item has an id, title, and completed status.

The reason why we have standard interchange formats like JSON is that HTTP only allows transferring plaintext data, Plaintext data does not have any kind of structuring, it is just a bunch of characters. Formats like JSON or XML bring formatting and structure to the data, which makes it easier for us developers and machines to understand it better.

JSON might look like a python dictionary but it is not, JSON is a format that is used to send data over the internet.

API's are not just used for data interchange between the frontend and the backend, it can be used for machine communication ( backend to backend ) as well, an example might be another service that reads your pending todo items to perform certain actions.
