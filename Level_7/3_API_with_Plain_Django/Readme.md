Django can be used to create API's on its own, instead of returning HTML documents, we can return XML documents or JSON documents as response, lets try to create an API that returns the the tasks in our task management app

Lets first create the route for our API

```python
path('api/tasks' , ViewTasksAPIView.as_view()),
```

now that we have our route lets create the class based view

```python
from django.http.response import JsonResponse

class ViewTasksAPIView(View):

    def get(self,request):
        return JsonResponse({"Hello" : "World"})
```

This is how we return JSON objects from our view.

Now we have to convert our task model objects into data types that can be transfered and understood by the client, for eg JSON/XML ( you can think of it as a translation to a different type of data ), this process is called serialization.

Throughout this course serialization will be used to convert Model instances or other objects into native python datatypes (string, boolean , integer...), these datatypes can then be used to create a response.

Lets write a serializer by ourselves using the following code

```python
class ViewTasksAPIView(View):

    def get(self,request):
        tasks = Task.objects.filter(deleted=False)
        data = []
        for task in tasks:
            data.append({"title" : task.title})
        return JsonResponse({"tasks" : data})
```

We are querying the tasks that are not deleted and then iterating over each task object and creating a python list as serialized output, You can try to visit this page to get an idea on how the json output will look like. You can try adding more field into the serialization and see how the output changes.

This quickly gets out of hand, Deserialzation gets even more painful, we have to do even more work to keep all the endpoints RESTful.

To solve all these issues a bunch of folks created the Django Rest Framework, often called DRF ,DRF is an amazing open source library that provides the same generic functionality we had for Django views for API's

Django was built for HTML Applications, it can be used to write API applications as well, but DRF extends its capability massively, We'll take a quick look at how to install Django Rest Framework and how to get started with it
