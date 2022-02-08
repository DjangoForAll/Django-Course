Unit Testing is one of the ways we can ensure that our application continues to work as intended over time as we introduce changes.
It keeps our application in a stable state and ensures that we don't break any of the functionality. It is a very important part of the development process.

Unit testing can also save time by cutting down on manual testing and quickly finding bugs.

>__“Code without tests is broken by design.”__ - Jacob Kaplan-Moss, one of Django’s original developers

To understand the need for unit testing clearly, let's take an example. 
Let's take the case of our task manager app we have built earlier, the app works fine, for now, sometime later we decided to rewrite the tasks listing view to show the tasks in a different way( maybe added some optimizations as well ), but while implementing the feature, the user-level filter was not added, that meant that anyone could view anyone's tasks, if we are manually testing with a single user, everything would have been working as intended and would be okay to be deployed. This is one of the cases where unit tests step in to help, the unit tests would have been written to test access of the lists and those tests would have failed. This helps us quickly pinpoint the error and understand what all have been affected by the change that we made without manually testing everything every time.

Now we have a basic understanding of why testing is required, But how do we get about doing it?

There are some strategies that we can learn to implement tests in our project, One of them is test-driven development, In this strategy, we first create tests that abstract the feature we are trying to implement, and then create the code that fixes the test. This might seem counterintuitive at first, but it tries to model a real-world scenario where we would have a high-level view of a problem and then a developer can implement logic to actually make it work.

Testing can also be performed the other way round, where the logic is written first and the tests just ensure that the logic works as expected.

There are a couple of other strategies that we can use to test our code as well, we will focus on how we can write tests in our project, and then you can follow any strategy you want!