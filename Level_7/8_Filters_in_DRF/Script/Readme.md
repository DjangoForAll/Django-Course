When we installed DRF, we installed another package along with it called `django-filter`, which is a library that helps us to filter the data based on the query parameters.

lets create some filters for our tasks api and see how it works.

```python
from django_filters.rest_framework import DjangoFilterBackend,FilterSet,CharFilter

class TaskFilter(FilterSet):
    title = CharFilter(lookup_expr="icontains")


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    permission_classes = (IsAuthenticated,)

    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter
```

We created a Filter class from the Filterset class that Django Filters provide and we defined what attribute we wanted to filter (title) , what types of data is expected (charfield) and what kind of expression to lookup with (icontains).

internally the filter set class will edit the queryset and add filters based on get parameters, if you think about it, its very straight forward. Check if the parameter is present in the query, if present then filter the queryset based on the value, this is exactly what we did in the search function in the previous level. the FilterSet class generalises it so that we dont have to handle it manually.

In DRF there is a concept of filter backends, FilterBackend are supposed to perform the filtering, DRF views can have more than one backends, when a view is called, DRF will call each of the backend with the current request and ask it to filter the queryset. Because of this we can have multiple filter backends that support multiple features.

DRF also has SearchFilters that can support searches over multiple fields, Ordering filters that control the ordering based on the request and so on!

The FilterBackends also implement the UI to be shown in the browsable API, if we take a look at the api in our browser you can see that there is another section called filters now which can be used to filter the data.

> Django Filters can also build dynamic forms for filtering in regular Django Views as well.

Now that we have filters, lets try to create a new feature in our task management app, lets create a status attribute that has fixed values, it could be PENDING, IN_PROGRESS, COMPLETED, CANCELLED and so on! this will increase our productivity even further!

In our Task model we can add a status attribute, but how do we ensure that the values are in the fixed list we have?

In Django ORM, we can create a list of choices for the value and Django ORM will validate and ensure that the value is present in the given list of items. These choices are often called enums, Python has classes just for managing enums, but we will skip that for now and focus on manually creating choices.

Lets see how we can create choices and use them as an attribute in a model class

```python
STATUS_CHOICES = (
    ("PENDING", "PENDING"),
    ("IN_PROGRESS", "IN_PROGRESS"),
    ("COMPLETED", "COMPLETED"),
    ("CANCELLED", "CANCELLED"),
)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

```

You can see that we have a predefined list called status_choices where we defined all the possible values for the status, the status options is a tuple that contains the value that is stored in the database and the value that is shown to the user.

If we are storing the Gender, we can skip storing the entire word Male and instead store an abbreviation like M internally, Django will map it back to the original value if needed, This is usually used to save space and to easily navigate databases.

you can see that the status attribute is still a CharField, Internally its still being stored as charecters, Django just makes sure that the values always match the choices that we provided it. Django is also smart enough to change forms that contain choices and automatically use select boxes instead of text fields so that only the avaiable options can be chosen.

We can make the migrations and migrate the database changes now. Once that is done take a look at the admin panel to check how the field is represented there. Similarly you can update the forms as well and check how django handles this model change.

Our DRF Viewsets can also adapt to this change automatically, lets add the status field to our serializer and visit the Browsable API page, the page renders a select option in the create form instead of free text now.

We can add a filter for the status as well

```python
status = filters.ChoiceFilter(choices=STATUS_CHOICES)
```

We could also use a CharFilter since internally its still being stored as charecters, the ChoiceFilter also contains meta information like the available choices so our filters UI can show options instead of a free text field.

Now we have added a new feature into our existing app with little to no changes!
