Django has a lot of goodies built for create better and faster tests, Django creates a new database for running the tests and destroys the database once its done to ensure that your tests always produce the same result.

Django tests are placed in a folder labelled `tests` in the root of your app, each test file in the tests folder must begin with the word `test` , this is how django recognizes that it is a test file.

Lets create the required folder and create a new file 