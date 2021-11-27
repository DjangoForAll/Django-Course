DRF uses a different type of url router, this was introduced to create routes dynamically instead of us having to write them all out, For all API related views we will stick to the router provided by DRF and for everything else we will use the "Django way"

Here is how a router is defined in DRF:

```python
# urls.py
from rest_framework import routers
from django.urls import include

router = routers.SimpleRouter()

urlpatterns = [
    # The Django Routes go here
    path('api/v1/', include(router.urls)),
]
```

The include function is used to "include" more url routes within the same base route, lets say that all your urls have a base route of `/api/`, you can then create a route and include all the other patterns inside it as a modules, you can use the include function to clean up your routes and organize them into different files or folders. The files that contain a urlpatterns variable are usually called as URLconf modules.

The router is simply a class that generates routes based on our views, instead of defining each route and the corresponding view, we can let the router handle the logic for us, DRF even lets us create custom sub routes inside our views, the router will create new routes as needed as we start to build our logic, we will take a look into this in detail later in this level.

Lets now create a Generic view in Django

```python
from rest_framework.viewsets import ModelViewSet

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

The queryset as usual is the queryset that we want to render in the list view and retrieve view.
the serializer_class is the serializer we created earlier

ViewSet simply means a bunch of views, ModelViewSet is a viewset that is based on a Model, the ModelViewset class automatically implements all REST Operations on this model

To register the model with the router we created earlier, use the following code,

```python
router.register("task", TaskViewSet)
```

And that's it! You have a working REST API, you can Create/Retrieve/Update/Delete tasks via API! try it out in your browser.

That wasn't too hard right? When code gets this generic there is always a downside to it, we have a working API but absolutely no clue what is happening behind the scenes. Which leads to a very steep learning curve, To master DRF, we need to understand how it works internally.
