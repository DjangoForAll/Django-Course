Standards in testing are always opinionated. Most probably every article you read will ask you to follow a different organizational style of writing tests.

I'll leave some articles for you to read and you can pick the best way to write tests on your own, Just make sure that you are writing tests no matter what style you follow!

[Django Tests Style Guide by J.V. Zammit](https://www.untangled.dev/2021/08/22/django-testing-style-guide/)  
[Mozilla Foundation](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)  

## Coverage

Tests are often evaluated with their coverage, Coverage refers to the code that is covered by the tests. Usually, the more coverage you have, the more stable your code is. We will quickly install coverage and check out the coverage of our project.

Let's first install a package called `coverage` which makes it easier to calculate the coverage of our project.

```bash
pip install coverage
```

Let's run the tests with coverage now

```bash
coverage run manage.py test
```

We are basically letting coverage run the tests, instead of invoking python directly.

Finally, you can run the following command to see the coverage report

```bash
coverage report
```

You can now see the coverage of each file in your project. Since we mostly use generic methods we don't really have any "custom code" in them, which makes the coverage pretty high. This is one of the cases where the coverage is not the best indicator of test quality, a high coverage need not mean that the code is perfect, it just means that the code is covered by the tests, not necessarily if all the edge cases and logical operations are working as expected.