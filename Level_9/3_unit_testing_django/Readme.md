Django has a lot of goodies built for create better and faster tests, Django creates a new database for running the tests and destroys the database once its done to ensure that your tests always produce the same result.

Django tests are placed in a folder labelled `tests` in the root of your app, each test file in the tests folder must begin with the word `test` , this is how django recognizes that it is a test file.

Lets start by creating a folder called `tests` in the root folder, and then create a file called `test_task_manager.py` inside the tests folder.

We will write a simple testcase that checks if the tasks listing page returns a status code of `200` and if the page contains 