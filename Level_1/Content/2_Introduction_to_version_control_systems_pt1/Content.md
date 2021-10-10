# Introduction to Version Control Systems

Version control systems are vital to almost every development workflow, we'll take a quick look at why it exists and how to start using it for software development.

_If you are already familiar with version control systems like git, you can take this time to understand exactly how it works internally._

## The Problem

To understand the value of VCS lets take a short example,
For a class project report, your teacher divided your class into small groups, You being the _technical guru_ of the group suggested that your group complete the whole thing with computers and share the works over email, sounds really cool right? ...fast forward some weeks and now every team member has a different version of the project, tons of emails, and no idea on who contributed what or which one is the latest copy.

Now think of organizations with thousands of employees working on the same project, thousands of changes being made every day, there has to be some system to keep track of changes to ensure that things don't break overnight. This is where version control systems shine.

Now that we have a general idea of why we need Version Control Systems, let's dive a little deeper and understand exactly what it provides.

## Git

It is one of the most widely used version control system in the world, it is developed by the same guy who built the Linux operating system kernel ( Linus Torwarlds ) and it is an essential prerequisite for almost all software development related jobs out there.

### Installing git

This is already covered in the previous sections, if you still haven't configured it view [this article](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to get you up to speed

### Learning Git

Assuming the same example as the section above, we'll see how git would have helped in your group project.

Let's assume for now that just alone is working on this project, and you wanted to track the changes you made to your report as you complete it,

To start with let's create a new folder called `learning-git` , you can create this folder wherever you want.

now that you have your folder created, open up a terminal/command prompt and navigate to your current directory, once you are inside your newly created folder run the following command.

```git
git init
```

\*_if this command returns an error then git has not been configured in your system, look back at earlier sections and make sure that git is installed correctly._

This command creates a new git _Repository_, a Repository is similar to a project ( with version control ), now your unversioned project is a git repository.  
if you look closely you will see a new hidden folder `.git` created inside your folder, git uses this folder for all its bookkeeping, unless you are a git wizard don't try to edit anything in there.

Now we have a really cool version-controlled project but its kinda empty, so let's create a new file in it, you can use your favorite code editor or Linux commands to create a new file in your folder. for the sake of consistency let's create a file called `cats.txt` containing the following text

`Cats: A Brief Summary`

Now that you have created a new file, we can take a look at how we can track its changes with git.

### Working Directory, Staging Area and Repository

A git development environment consists of three sections

1. **Working Directory**  
   This is simply the current state of files and folders inside your current folder, these changes are **_not_** yet recognized by git and are **_not_** tracked yet.
2. **Staging Area**  
   This is a temporary location for your files before they are saved to a repository. you can add more than one file to the staging area.
3. **Repository**  
   This is where your actual work and its history lies. you can sync repositories to other computers and expect the same copies to be present.

To view the current status of our git repository run the following command

```git
git status
```

Once you run the command, git will inform you that you have created a new file. ( the file is still in the working directory )

To stage the file with git we can run the following command

```git
git add cat.txt
```

This command will add the file `cat.txt` into the git staging area, alternatively, you can do `git add .` which will add all files in your folder into the git staging area ( when you don't want to manually specify each file )

Once the files have been staged, they have to be moved to the repository, this is called a commit, commits are usually a logical chunk of change, you don't have to commit for every change you make to the file, in our example, you can commit the file once you have completed a section of the report or such. Commits create snapshots of the repository, you can restore your repository to any commit at any time.

Commits are ideally associated with a commit message, the commit message makes it easier to understand the intent of the change, this is incredibly useful if you wanted to restore the repository into an earlier commit you made.

The following command is used to create a commit in git

```git
git commit -m "Started to create a report on cats"
```

This command will take all the files in staging and commit them to the git repository. Once you have committed, running `git status` again will let you know that you no longer have any changes, (Your working directory and the git repository are in sync now). Committing clears the staging area so that you can start working on your new changes.

To view all your past commits you can use the log command

```git
git log
```

( use q to exit the command )

This command will show all the commits made in your repository along with who made the change.

Now, make some changes to your report, you can add new content, delete existing content or even create new files. Once you are done, run `git diff` this will show all changes you have made in your working directory.

Now you have a basic idea of what git is and how to perform basic actions in git, Try making more changes in your folder and try to record those changes with commits to get familiar with git.
