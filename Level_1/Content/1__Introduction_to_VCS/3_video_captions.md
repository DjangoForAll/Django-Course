In this level we will be introducing git for version control

version control is used to efficiently manage and track all changes made to a project, this allows us to understand when or who made a change and how to revert it to previous state

git is the standard tool for version control across the software industry

we'll be taking a look at some of the git commands and how to version control a simple project

before continuing make sure that you have git installed, if you havent yet The instructions to install git are present in the course content

to get started lets create a folder named study-git, i am using the mkdir command to create the folder

Now lets try to view the status of git in this folder, This can be done at any point to know quick stats about the current state of the git repository using the command git init

This error pops up becuase our folder is not a git repository yet , to convert it lets run the command git init

git init converts an unversioned folder into a git version controlled repository

If we quickly run the command git status we can see that the folder is now a git repository

if we try to list all the files and folders in this folder including hidden files, we can observet that have a .git folder created now, git uses this folder for all its bookeeping and its best that we dont meddle with it

Now we have a git repository we can view the status of the repository and it shows all the information related to it

Now lets create a file called README in this folder,

we can create this file using the touch command.

on viewing the status of the repository we can see that the file is not tracked by git, to add the file to the git repo we can run the command git add README or git add .

Once this is added we can view the status and we can see that the file is now tracked by git, git also tells us that the file is not commited yet,

commits are logical chunks of change, ideally associated with a commit message, the message is a summary of everything that was done in that commit, this usually helps in debugging versions and choosing the right one.

Once the file is committed we can view the log to see the history of commits

Now lets make some changes to the file and look at how git views the differences,

we can use any code editor to make changes, i am using gedit for now.

we can do this by running the command git diff

lets add this file commit again and look at the logs

now you have a basic idea of how git works locally , try variations of these commands, in the next chapter we will learn how to sync these changes with github.
