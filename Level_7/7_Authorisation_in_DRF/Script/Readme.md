In our regular views, only the person who created the tasks could see them, lets add the same logic in the API View as well.

we have to override the get_queryset method so that the data is always filtered, and the save method to save the user who created the task.

```python
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

This might look very similar to the code in the regular view, we edited the queryset method to dynamically filter based on the user.

When performing a create operation, we also store the user who created the task in the user field. This also answers the question on why perform_create was a seperate method from the save method

finally we also added an attribute called permission_classes, which is a list of permissions that the view will use. the view will call each of the permission classes in the given list and check if the action is allowed. IsAuthenticated simply checks if the user is authenticated or not.

now you can go ahead and visit the api url and perform all actions on them, Now you have a working REST API for our tasks.

currently our serializer only serializes the fields realated to the task, lets say that we wanted to know a bit about the user who created them as well, in that case we can create a nested serializer, lets look at how we can create one.

```python
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class TaskSerializer(ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ["title", "description", "user"]
```

we created a new serializer that can serialize a user model and then created an attribute in the task serializer called user and assigned it to the user serializer.

Now when the TaskSerilizer tries to serilize the user attribute, it will call the UserSerializer to do so.

We passed in read_only so that no one will try to edit the user value.

we can check our API output again and see that the user field is now serialized. if we remove the user attribute here, you can see that it will give the id of the user instead which is not really useful.

you can also have a serializer within the user serializer if needed, the only thing to keep in mind is that in the background all these are creating complex queries to the database, so it is better to keep them as simple as possible.
