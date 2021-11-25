Lets first install the Django Rest Framework with pip, DRF like Django is also a python package.

```shell
pip install djangorestframework
pip install django-filter  # Filtering support
```

We will install djangorestframework along with django filters, django filters is a handy library that will help us with adding filters, we will talk about this later in the course

Once we have both the packages installed, lets add the packages to the list of installed apps in django, only after adding it in `INSTALLED_APPS` would django recognize it as a package and import its contents

append the following lines into the `INSTALLED_APPS` variable in settings.py

```python
INSTALLED_APPS = [
    ... # Dont edit anything else that is already in the list
    'rest_framework',
    'django_filters',
]
```

Once this is done we are good to go!

DRF Provides a different version of the `View` Class that Django provides, `APIView` is a class specifically written for API's in DRF

> If you look inside the implementation of APIView, you can see that it inherits from the `View` class, the Rest Framework does not rebuild everything from scratch, it just enhances what Django already has for API based Development.

Lets convert the API we wrote earlier to APIView

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class ViewTasksAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.filter(deleted=False)
        data = []
        for task in tasks:
            data.append({"title": task.title})
        return Response({"tasks": data})
```

Notice that the only changes were the BaseClass and the Response class, the APIView works exactly like a regular View and Response works just like the `JsonResponse` class we observed earlier, These are equivalents from the rest framwork package.

now if we visit the api url again, the whole UI has changed, now we get a pretty UI that shows us the output and gives us some capability to perform actions.

If you observe the code snippet above, you can observe that we haven't really changed any logic, let's use DRF's built in serializer to serialize the data.

```python
from rest_framework.serializers import ModelSerializer

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["title", "description"]


class ViewTasksAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.filter(deleted=False)
        data = TaskSerializer(tasks, many=True).data
        return Response({"tasks": data})
```

We are using the ModelSerializer class from DRF to serialize the data, the serializer might look very similar to Forms in Django, That's because it works very similar to the ModelForm we saw earlier.

The ModelSerializer is a special type of serializer that will automatically map the fields of the model and convert the data to the correct format. The ModelSerializer also needs a list of fields that are to be serialized, With this information it can start to convert the data from querysets.

Notice that we passed the data into the serializer along with a parameter called `many` , this parameter is used to let the serializer know that we'll be passing more than one Task Object (Queryset) into the serializer

The data attribute of the serializer provides the reprsentation of the input data as native python datatypes, since we had **many** inputs, the output will be a list of dictionaries. if only one object was passed in, then the data attribute would be a python dictionary

The ModelSerializer takes in the fields to serialize along with the model and translates the object into a python dictionary, this can then be sent in the response back to the client.

The ModelSerializer is capable of much more! , lets take a look at other DRF Features to correctly understand serializers and how it works.
