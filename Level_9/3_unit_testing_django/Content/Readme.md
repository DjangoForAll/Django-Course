Django has a lot of goodies built to create better and faster tests, Django creates a new database for running the tests and destroys the database once it's done to ensure that your tests always produce the same result.

Django tests are placed in a file called `tests.py` in the root of your app, you can also create a folder labeled `tests` and then create more detailed test cases in it. The `tests.py` file is automatically created by Django for us when we created the app.

To test it out, let's create a simple test case that will always fail.

```python
from django.test import TestCase

class QuestionModelTests(TestCase):
    def test_always_fail(self):
        """
        This test will always fail ( for now )
        """
        self.assertIs(True, False)
```

To run this test, run the following command.

```bash
python manage.py test
```

The output shows a list of tests that failed and exactly what assertion failed, it also shows what caused it to fail, all these are features are borrowed from unittest, all Django tests are inherited from Python's unittest library, so anything you learned in the previous chapter can be implemented here.

Django performs a lot of operations behind the scenes to ensure that your tests are working as intended, one of these include creating a new database for each time you test and then destroying it once the test is done, read this [article](https://docs.djangoproject.com/en/4.0/topics/testing/overview/) to get a better overview of Django tests.

Now we'll create a test that checks if the listing page can be viewed by an unauthenticated user, we'll try to get the task listing page and see what happens

```python

class QuestionModelTests(TestCase):
    def test_authenticated(self):
        """
        Try to GET the tasks listing page, expect the response to redirect to the login page
        """
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/user/login?next=/tasks")

```

Go ahead and run this test.

The test above will pass, we try to get the tasks listing page, but since we are not authenticated, we will be redirected to the login page. 302 is the status code for a redirect, the URL represents the URL we are redirecting to, we expect that to be the login page.

With this test implemented, at any point if we accidentally delete the authentication constraint for this route, the test would fail and we would know exactly what is going wrong.

Django's client emulates a complete request-response cycle, each request goes through the URL router, middleware, and everything that stands between the request and the response, This method has its merits and demerits, we'll look at another type of test that Django has

Django Request Factory, as the name suggests, Django Request Factory creates requests which we can manually pass into the views we created and expect them to provide a response, This is very useful when you just want to test out the logic without worrying about the request cycle. We'll see an example of a test written with the Django Request Factory.

```python
from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase

from .views import GenericTaskView

class QuestionModelTests(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="bruce_wayne", email="bruce@wayne.org", password="i_am_batman")

    def test_authenticated(self):
        """
        Try to GET the tasks listing page, expect the response to redirect to the login page
        """
        # Create an instance of a GET request.
        request = self.factory.get("/tasks")
        # Set the user instance on the request.
        request.user = self.user
        # We simply create the view and call it like a regular function
        response = GenericTaskView.as_view()(request)
        # Since we are authenticated we get a 200 response
        self.assertEqual(response.status_code, 200)

```

The setup method is called once before running all the tests, the setUp method is usually used to do one-off operations that might be required like adding dummy data, creating users, and so on.

Django has excellent documentation on testing, Read more about the `client` [here](https://docs.djangoproject.com/en/4.0/topics/testing/tools/) and the `RequestFactory` [here](https://docs.djangoproject.com/en/4.0/topics/testing/advanced/)

Django can test rendered templates, but it cannot test the _behavior_ of the web pages ( Javascript code ), But Django provides a number of tools to make it easier, to read more about these types of tests, look into [selenium](https://www.selenium.dev/)

Django Rest Framework provides some additional features on top of the standard Django Test Client and Request Factory, refer to the following [article](https://www.django-rest-framework.org/api-guide/testing/) to get a better understanding of the features. 