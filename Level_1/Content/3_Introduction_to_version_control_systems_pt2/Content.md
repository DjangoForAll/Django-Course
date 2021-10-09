# Introduction to Version Control Systems ( VCS ) - Part 2

Now that you know the basic functioning of git, lets learn some advanced concepts.

### Collaboration

This is one of the main reasons why we are learning git, git allows multiple developers to share a repository and work on the same project without losing any changes. The same concepts that you have learnt till now can be extended to work with multiple developers/(Project Collaborators)

In real world scenario having the repository on your machine wont make much sense since your team members would also need to access the repository, Services like Github, Gitlab solve that problem ( Github and git are two different things , Github is an online service that lets you manage your git repositories )

Git also lets you work on your project without the internet since you only need the internet to sync your repository, Even if github is down you can continue working on your project, To learn some of the advanced concepts of git we will connect to a github repository and try running some git commands.

### Creating a Repository in Github

Signin/Signup to Github and click on New repository ( usually this page is hidden under the + icon close to the profile picture ) , On the Create form give a name for your repository , you can name it anything you want for now ( Use \_ or - instead of spaces ).
Public repositories are available to anyone on the internet, private repositories are only visible to you and the folks you choose to share it with. Lets go with the public repository option for now.
Uncheck Readme Files and any other option for now and create the repository

### Linking your local repo to a Github repo

\*_repo is short for repository_

Now that you have a Github repository, we need to link your local github repository to github so that it can sync the changes, to do this we need to locate the URL of your github Repository, you can use the HTTP address/URL of your newly created github repo for now. the URL will be of the form <https://github.com/>`github_username`/`repository_name`

Once you have the url the following command will link the local repository to the remote repository

`git remote add origin https://github.com/github_username/repository_name`

Here the word origin is not a keyword, you can name it anything you want, usage of the word origin is just standard convention.

### Basics of Git Branches

Branching is a feature in git which allows you to isolate your work and work on multiple changes simultaneously. you can switch between branches without creating multiple development environments, branches are extremely useful when you want to work on different parts of the project simultaneously. to know what is the current branch you can execute the `git status` command we used earlier, the first line of its output will tell you what branch you are on.

By default you will be in the master or main branch of your repository ( master used to be the default branch in github but recently it was changed to main )

### Syncing Repositories

now that you have linked the Github repository you can pull ( move changes in github into your local repo ) or push ( move local changes from your local repo into github's repo ) changes , since we already have changes made in local we can push the changes into github with the following command

`git push origin main`

Origin is a reference to the url we added earlier and main is the branch we want to push to

Similarly we can also pull changes from the remote repository with the following command

`git pull origin main`

### Merges and Conflicts

When multiple developers work on a single project and make changes to the same file, the changes made by each developer are not merged together, instead they are kept in separate branches. Git allows seperate branches to be merged together, if the changes are not conflicting git will automatically figure out a way to merge the branches together. But if there are conflicts that need to be resolved, git will not automatically merge the branches

Usually, When multiple developers have made changes to the same file in multiple branches, you have a conflict. We have to manually resolve the conflict and select the version that we want to keep.

### Forking

Forking is a feature in git that allows you to create a copy of your repository on your own account. This is useful when you want to work on a project that you have not created yourself. Forking allows you to create a copy that you can freely experiment with, without affecting the original repository.

Forking is usually used to propose changes to the original repository, and then merge those changes into the original repository.

In github, with every repo you have option to fork it from the UI, Once the fork is created you can make changes into it.

### Pull Requests

A pull request is a request to merge a branch into another branch, or a fork into the main repository, it lets the maintainers of the project know that you wish to merge your code into their project. Pull requests are often used to propose changes to a repository, Which is a great way to share code with others.

Once a pull request is made, you can discuss and review the potential problems and limitation of the changes with the folks who maintain the project, You can continue adding commits to the pull request until you are satisfied with the changes.

_To complete this lesson, we'd like you to practise using git by working through the ._ [Git-it Guide](http://jlord.us/git-it/)

### Tips/Tricks for Git

It is incredibly easy to mess-up a git repository and the best way to learn how not to do it is to keep experimenting, trying out various techniques and finding the sweetspot.  
Whatever happens, do **not** try copy pasting git code unless you know exactly what its doing **( There is only pain down that path ! )**  
Commit messages and Branch Names should always make sense, Otherwise years later you'll blame yourself **( Thats what i did )**  
There is a sea of open source software out there, try to find something intresting and contribute, Thats the reccomended way to become a better developer!
