Here are a few tips on solving the milestone. I recommend reading them only if you are completely stuck, most of the content can be found with simple internet searches.

### Placing Logic
The milestone requires the creation of a new Django Model ( TaskHistory ) that can track all the changes being made to a given Task object. The logic for the creation of the history object can be placed in different methods, lets take a look at each one
- Overriding the standard API Viewset/Serializer : This feels the most natural way to implement the logic, in this method we just override the method that used to save the task object and add our our logic there. Although this is simple to implement it opens up loopholes like, what is the task object is saved via the form? do we replicate our logic there? What happens if the task is created in some other contexts? how long do we keep copying our logic? ( Same goes to the priority cascade logic as well )
- Overriding the save method : This is another common approach to solve the problem, Our logic to create task history objects are more concerned about the model than the medium that we are interacting with ( API, Form, etc ) and it makes more sense to place the logic in the model than the view. that way anytime the object is saved, all logic pertaining to the model is evaluated. This solves some of the loopholes mentioned above. Implenting this approach is pretty straightforward, we override the save method in our model and call the super method once we are done with our logic.
- Using Django Signals : This is one of the best approaches to solve the problem, this is virtually the same as overriding the save method, but this approach is more flexible and easy to read/understand to other developers. Django creates signals whenever some actions are performed on a model, We can define recievers or handlers that can recieve a signal, we can use these to handle our logic to create task history objects. Read more about Django signals [here](https://docs.djangoproject.com/en/4.0/topics/signals/)

### Authentication vs Authorisation
This is one of the key areas where a lot of folks struggle, Authentication proves that you are who you say you are, Authorisation ensures that you access only what should be accessible by you!
If i create a task, i expect only myself to access those tasks. In other words, the tasks should not be accessible to anyone else.
Both Authentication and Authorisation should be implemented in all views you create in this milestone.

### Read Only Views
Since the history objects are created on task updates, the history endpoint does not need Create/Update/Delete endpoints, it should be read-only. Look into [ReadOnlyModelViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#readonlymodelviewset) for more information.

### General Tips
    - Try to move all your API logic into a seperate file to make it more readable
    - Remove all other unnecessary code from the views before submitting
