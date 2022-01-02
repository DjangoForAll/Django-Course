Unit Testing is one of the ways we can ensure that our application continues to work as intended over time as we introduce changes.
It keeps our application in a stable state and ensures that we don't break any of the functionality. It is a very important part of the development process.

Unit testing can also save time by cutting down on manual testing and quickly find bugs.

> Jacob Kaplan-Moss, one of Django’s original developers, says __“Code without tests is broken by design.”__

Now we have the an idea on why we should always test our code. But how do we get about doing it? 

There are some stategies that we can learn to implement tests in our project, One of them is test driven development, In this strategy we first create tests that abstract the feature we are trying to implement, and then create the code that fixes the test. This might seem counter intuitive at first, but it tries to model a real world scenario where we would have a high level view of a problem and then a developer can implement logic to actually make it work.

Testing can also be performed the other way round, where the logic is written first and the tests just ensure that the logic works as expected.

There are a couple of other strategies that we can use to test our code as well, we will focus on how we can write tests in our project and then you can follow any strategy you want!