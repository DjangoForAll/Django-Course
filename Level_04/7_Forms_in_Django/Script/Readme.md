Now that we know how to render dynamic content, we can start building forms to create complex web applications.

Lets create a simple web application that allows users to manage tasks.

To keep things simple lets keep the data in memory ( creating a global variable called tasks ).
Global variables are usually never used in real life for storing data, we will figure out better ways to store data in the next level, for now lets use it to understand concepts in forms clearly.

we'll go over the implementation in detail

Lets first create a form in html with one input field and one button

Let the action be the url `/add-task`, to keep things simple lets use the GET method for the data transfer

```html
<form action="add-task" method="get">
  <input type="text" name="task" />
  <button type="submit">Add Task</button>
</form>
```

If we refresh our page you can see that it displays the form, when we try to add a task we can see the django 404 page, this is expected since we did not define the url route `add-task`

lets go ahead and create a new function called `add_task_view` that will handle the data, and then create the required url route, now if we try submitting our form again, it no longer gives an error, now lets write the logic to add the item.

lets fetch the data from the request, we have already seen that the `request.GET` is a dictionary that contains all the query parameters, lets fetch the `task` key to get the task name. Now that we have the task in hand, we have to somehow store it. since we are just testing django out, we can just store it in a global variable, lets create a global variable called `tasks` and assign it an empty list.

In python anything created in the main body is global and can be accessed anywhere in the program. the variable is defined at the start of the server, which means that when the server restarts, we will lose all data. This is fine since we are testing the application out.

Now lets append the task to the tasks list, we will also redirect the user back to the tasks view page so that they can see their tasks, we can use the `HttpResponseRedirect` from the `django.http` library to redirect the user to the tasks view page.

The `HttpResponseRedirect` accepts a route as an argument.

Finally we can change the tasks view function to render the tasks variable we created. Thats it! Now we have a working web application.

Now lets add a delete functionality to make our tasks management application more useful.

Before getting there, lets first add an index to our html page, since the tasks in the list can be duplicated, the only way we can select a task is by using the index. The index value is available with the variable `{{forloop.counter}}` we can update our html to display the index value as well.

Now that we have a unique index for each item, lets add a link with each task to delete it. We can use the `<a>` tag to create a link. lets redirect to `delete-task/1` where 1 represents the index of the task to be deleted. Now the page renders with links to delete the item as well, but all links delete the item with index 1, we have to change it so that it deletes the item with the corresponding index `delete-task/{{ forloop.counter }}` can be used to dynamically generate a link with the correct index.

Now that we have creating a delete link, lets add a delete functionality to our application. If you observed, the url changes based on the index of the item, the index is not a query parameter, its part of the url. that means we have to create entries for every index number possible! , Luckily Django provides a neat way to solve this problem, `delete-task/<int:index>` with a route of this pattern, django will check if the url matches this pattern and extract the index out of the url for us!

we can create a new view function called `delete_task_view` and pass the index also as an argument, django will automatically pass the extracted index value to this view. Now that we have the index. Lets delete the item and redirect back to the tasks view. You can delete the item using the `del` keyword or the `pop` method in the list class

`tasks.pop(index-1)` is the same as `del tasks[index-1]` we subtract one from the index because the index in the DTL started at 1 while the indexs in python start at 0

And thats it! Now we have a working web application that allows us to manage tasks. We can even deploy the application at this point and have it working. But our data is volatile, anytime the server restarts or crashes we lose all the data. We can leverage databases which are tools which are specifically designed to store data in a reliable way. we'll take a look at what they are and how to leverage them efficiently in the next level.
