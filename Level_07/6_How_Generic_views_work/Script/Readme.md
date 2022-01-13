Lets breakdown the ModelSerializer Class

DRF comes packages with a Serializer Class, If we were to rewrite our task ModelSerializer with a regular Serializer it would look like this.

```python
class TaskSerializer(Serializer):
    task = serializers.CharField(max_length=100)
    description = serializers.CharField()

    def create(self, validated_data):
        title = validated_data.get('title')
        description = validated_data.get('description')
        return Task(title=title, description=description)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        return instance
```

Here we manually defined what the fields and its types , we also manually wrote the create and update methods, Note that the serializer we created just creates the objects, it does not actually save it to the database.

Model Serializer automatically fetches the model fields and their corresponding types , the create and update methods can easily be generated if we already know the field declarations. ModelSerializer also create the validation logic for us, Serializers like Forms support field level validations as well, lets create the same validation we created for the forms.

```python

```

To sum up everything, ModelSerializers can convert python native data types into Model Objects and vice versa.

The ModelViewset's job is to figure out what serializer should be called when a request is made, how should it be invoked, what authentication methods should be used etc..

Lets look at how DRF Defines the ModelViewset Class

```python
class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass
```

The ModelViewset is an empty class that inherits from a bunch of baseclassses, We have already learnt about mixins, Each of the mixins you see provide a particular functionality to the ModelViewset

The CreateModelMixin defines the .create() method, it is used to create a new object, if the request is a POST request, then the create() method is invoked. if the mixin was not added the request would be ignored.

You can also see a GenericViewSet at the end of the list, this is the base class that provides all the functionality common between all the mixins like figuring out what function to call based on the request method, route etc

Lets take a look at one mixin and study how it works, lets take the CreateModelMixin

```python
class CreateModelMixin:
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
```

This is the definition of the CreateModelMixin, the create() method is used to create objects when you perform a POST request

If you observe, all it does is create a new serializer class , pass in the data and validate the data, once validated it calls the `save` method to actually save the data to the database.

You must be wondering why there is a `perform_create` method, can't we just call the `save` method directly?

Well this is where things get interesting, These methods can be overridden to add custom logic into it, instead of completely rewriting the entire view to add changes, we can just override the perform_create method to add the logic.

Take a look at the other mixins and try to guess how they work!
