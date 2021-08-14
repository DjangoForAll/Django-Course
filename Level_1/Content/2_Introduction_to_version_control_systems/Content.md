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

Now that you have created a new file, we can take a look the capabilties of git.

### Working Directory, Staging Area and Repository

A git development environment consists of three sections

1. Working Directory
   This is simply the current state of files and folders inside your current folder, these changes are _not_ yet recognized by git and are _not_ tracked yet.
2. Staging Area
   This is a temporary location for your files before they are saved to a repository. you can add more than one file to the staging area.
3. Repository
   This is where your actual work and its history lies. you can sync repositories to other computers and expect the same copies to be present.

To get a better view lets explain this concept with a example.
You wanted to purchase some groceries for your home ( working directory ) so you go to the supermarket and add a couple of things to your shopping cart ( Staging Area ) and finally when you are done you purchase everything in your cart, and bring them back home ( Repository ). ( And the bill is the log ).

To view the current status of our git repository run the following command

`git status`

Once you run the command, git will inform you that you have created a new file. this file is still in the working directory.

To stage the file with git we can run the following command

`git add cat.txt`

This command will add the file `cat.txt` into the git staging area, alternatively you can also do `git add .` which will add all files in your folder into the git staging area ( when you dont want to manually specify each file )

If you are still confused about the staging area, its importance will be become clear as you progess.

Once the files have been staged, they have to be moved to the repository, this is called a commit, commits are usually a logical chunk of change, you dont have to commit for every change you make to the file, in our example youi can commit the file once you have completed a section of the report. Commits create snapshots of the repository, you can restore your your repository to any historical commit at any time.

Commits are always ( ideally ) associated with a commit message, the commit message makes it easier to understand the intent of the change, this is incredibly useful if you wanted to restore the repository into an earlier commit you made.

The following command is used to create a commit in git

`git commit -m "Started to create a report on cats"`

This command will take all the files in staging and commit them to the git repository. Once you have commited running `git status` again will let you know that you no longer have any changes, (Your working directory and the git repository are in sync now). Commiting clears the staging area so that you can start working on your new changes.

To view all your past commits you can use the log command

`git log`
( use q to exit the command )

This command will show all the commits made in your repository along with who made the change.

Now, make some changes to your report , you can add new content , delete existing content or even create new files. Once you are done , run `git diff` this will show what all changes you have made in your working directory.

Now you have a basic idea on what git is and how to perform basic actions in git, Try making more changes in your folder and try to record those changes with commits to get familiar with git.
