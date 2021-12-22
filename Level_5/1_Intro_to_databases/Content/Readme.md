In the previous levels, we used two methods to store data, first, we used a text file and then as a global variable, Although these work well for small amounts of data and in a test environment, they are not suitable for anything above that.

The text document we saved had no structure, it was just a bunch of text, and every time we had to update the text file we had to rewrite the entire file, imagine rewriting gigabytes of text files just to change one line! this method will also start to get slower as the amount of data increases.

Thankfully we are not the first people to stumble upon this problem, in fact, the standards that we use were first created back in [1986](https://archive.org/details/federalinformati127nati/page/4/mode/2up), There is enough content about databases that can fit an entire course or ten! But we won't go into its detail since Django does a very good job of abstracting away the details about databases and how they work. We'll focus on how to get it working with Django rather than the details of the database itself.

Almost every time you see dynamic content on the web, the data must be coming from a database.

There are different types of databases out there, most classifications are based on how the data is stored and how it is accessed. The type of databases we will learn about are called relational databases.

Relational databases store data in tables,

You can think of relational databases as a really complex version of excel or google spreadsheets.

You can visualize relational tables as a bunch of columns and rows. columns are called attributes or fields and rows are called records.

For example, we can have a table called users with the following columns or attributes: name, email, age
then the rows would be the actual data that is stored in the table. like ("John","john@gmail.com",24),("Doe","doe@gmail.com",18) and so on

Databases also allow us to perform queries on the data, for example, we can ask the database to give us all the users that are older than 18, or all the users that are younger than 18 or any condition you can think of, you can also delete rows, join tables and so on.

There are a couple of different implementations of relational databases out there, Most of them are free and open-source like SQLite, Postgresql, Mysql, etc...Databases use SQL ( Structured Query Language ) which is a standardized programming language that's used to interact with the database, raw SQL will not be covered in this course, instead, we will focus on Django ORM ( Object Relational Mapping ) which is a library that allows us to interact with databases using Python.

Django ORM is also smart enough to work with many types of databases, full list [here](https://docs.djangoproject.com/en/3.2/ref/databases/#third-party-notes)

Throughout this course we will use SQLite, We are using SQLite because it is the simplest database to set up, It comes pre-configured with Django so there is nothing to set up. SQLLite is only recommended for testing or development, for actual production applications we will look at Postgresql or Mysql ( These will be covered at the end of the course )
