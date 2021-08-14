# Introduction to Version Control Systems ( VCS ) - Part 2

Now that you know the basic functioning of git, lets learn some advanced concepts.

### Collaboration

This is one of the main reasons why we are learning git, git allows multiple developers to share a repository and work on the same project without losing any changes. The same concepts that you have learnt till now can be extended to work with multiple developers/(Project Collaborators)

In real world scenario having the repository on your machine wont make much sense since your team members would also need to access the repository, Services like Github, Gitlab solve that problem ( Github and git are two different things , Github is an online service that lets you manage your git repositories )

These services also let you work on your project without the internet since you only need the internet to sync your repository, Even if github is down you can continue working on your project, To learn some of the advanced concepts of git we will connect to a github repository and try running some git commands.

### Creating a Repository in Github

Signin/Signup to Github and click on New repository ( usually this page is hidden under the + icon close to the profile picture ) , On the Create form give a name for your repository , you can name it anything you want for now.
Public repositories are available to anyone on the internet, private repositories are only visible to you and the folks you choose to share it with. Lets go with public for now.
Uncheck Readme Files and any other option for now. and create the repository

### Linking your local repo to a Github repo

\*_repo is short for repository_

Now that you have a Github repository, we need to link your local github repository to github so that it can sync the changes, to do this we need to locate the URL of your github Repository, you can use the HTTP address of your newly created github repo for now. the URL will be of the form <https://github.com/>`github_username`/`repository_name`

Once you have the url the following command will link the local repository to the remote repository

`git remote add origin https://github.com/github_username/repository_name`

Here the word origin is not a keyword, you can name it anything you want, usage of the word origin is just standard convention.

### Branches

Branching is a feature in git which allows you to isolate your work and work on multiple changes simultaneously.

### Syncing Repositories

now that you have linked the Github repository you can pull ( move changes in github into your local repo ) or push ( move local changes to git ) changes , since we already have changes made in local we can push the changes into github with the following command

`git push origin master`

git pull
forking
Pull Requests
Merging code
Milestone
