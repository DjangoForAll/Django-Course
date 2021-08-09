# Introduction to Version Control Systems ( VCS )

Version control systems are vital to almost every development workflow, we'll take a quick look at why it exists and how to start using it for development.

_If you are already familiar with version control systems like git, you can take this time to undetstand exactly how it works internally._

## The Problem

To understand the value of VCS lets take a short example,
One day, your class teacher divided your class into small groups to prepare a long report on something old (probably), You being the _technical guru_ of the group suggested that your group complete the whole thing with computers and share the works over email, sounds really cool right? ...fast forward some weeks and now you have a million emails and no idea on who contributed what or which one is the latest copy.

Now think of organizations with thousands of employees working on the same project, thousands of changes being made everyday, there has to be some system to keep track of changes to ensure that things dont turn into lava overnight. This is where version control systems shine.

Now that we have a general idea of why we need Version Control Systems, lets dive a little deeper and understand exactly what else can it provide.

## Git

It is one of most widely used version control system in the world, it is developed by the same guy who built the Linux operating system kernel ( Linus Torwarlds ) and it is an essential prerequisite for almost all development related jobs out there.

### Installing git

This is already covered in the previous sections, if you still havent configured it view [this article](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to get you upto speed

### Learning Git

Assuming the same example as the section above, we'll see how git would have helped in your group project.

Lets assume for now that just you are working on this project, and you wanted to track the changes you made to your report as you complete it,

To start with lets create a new folder called `learning-git` , you can create this folder wherever you want.

now that you have your folder created, open up a terminal/command-prompt and navigate to your current directory, once you are inside your newly created folder run the following command.

`git init`

\*_if this command returns an error then git has not been configured in your system, look back at earlier sections and make sure that git is installed correctly._

This command creates a new git _Repository_, a Repository is similar to a project ( with version control ), now your unversioned project is a git repository.  
if you look closely you will see a new hidden folder `.git` created inside your folder, git uses this folder for all its bookeeping, unless you are a git wizard don't try to edit anything in there.

Now we have a really cool version controlled project but its kinda empty, so lets create a new file in it, you can use your favourite code editor or linux commands to create a new file in your folder. for the sake of consistency lets create a file called `cats.txt` containing the following text

`Cats : A Brief Summary`

Now that the file is created, we can take a look the capabilties of git.
