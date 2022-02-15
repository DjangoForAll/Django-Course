Standards in testing are always opinionated. Most probably, every article you read will ask you to follow a different organizational style for writing tests.

I'll leave some articles for you to read, and you can pick the best way to write tests on your own. Just make sure that you are writing tests no matter what style you follow!

[Django Tests Style Guide by J.V. Zammit](https://www.untangled.dev/2021/08/22/django-testing-style-guide/)  
[Mozilla Foundation](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)  

## Coverage

Tests are often evaluated with their coverage. Test Coverage refers to the percentage of code that is covered by the tests. Usually, the more coverage you have, the more stable your code is. We will quickly install `coverage` and check out the coverage of our project.

Let's first install a package called `coverage` which makes it easier to calculate the coverage of our project.

```bash
pip install coverage
```

Let's run the tests with coverage now

```bash
coverage run --source='.' manage.py test
```

We are basically letting coverage run the tests, instead of invoking Python directly. The source attribute is used to specify which files should be checked for coverage. We only need the coverage reports for our current project.

Finally, you can run the following command to see the coverage report.

```bash
coverage report
```

You can now see the coverage of each file in your project. Since we mostly use generic methods, we don't really have any "custom code" in them, which makes the coverage pretty high. This is one of the cases where the coverage is not the best indicator of test quality. High coverage need not mean that the code is perfect. It just means that the code is covered by the tests. It does not necessarily ensure that all the edge cases and logical operations are working as expected.

Coverage can also create more detailed reports in different formats, refer to this [article](https://www.codemag.com/article/1701081/Improve-Code-Quality-Using-Test-Coverage) to read more about them.  

Since your repository is public, you can also use fancy tools like [CodeCov](https://about.codecov.io) to generate reports and badges for your project.