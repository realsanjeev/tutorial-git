# Git Commands
## Configure Git
Use global to set the username and e-mail for every repository on your computer.
```
$ git config --global user.name '<username>'
$ git config --global user.email '<your@email.com>'
```
## Initialize git which you want to track
```
$ git init
```
Git now knows that it should watch the folder you initiated it on. Git creates a hidden folder to keep track of changes.
## Git help
See all possible commands in git. to quit from bash shell write `:q`
```
$ git help --all
```
See available option for specific command.
```
$ git <command> -help
```
## Git Status
Watch status of your changes in git.
```
$ git status
 ```
Files in your Git repository folder can any of 2 states:

- Tracked - files that Git knows about and are added to the repository
- Untracked - files that are in your working directory, but not added to the repository

To get status short form
```
$ git status -s
```
Common Short status flags are:
|   Flags     | Description |
| ----------- | ----------- |
| ??     | Untracked files     |
| A    | Files added to stage|
|M     |  Modified files    |
|  D    | Deleted files|
 
## Add file And stage Change
### Add file
To add all file in git repo
```
$ git add --all
```
To add all file in git repo, we can also use `git add -A` OR `git add .`
To add only a file with filename `text.txt`, following code is executed
```
$ git add text.txt
```
### Stage change
Adding commits keep track of our progress and changes as we work. Git considers each `commit` a "change point" or "save point". Commit tag always written with message, so that we can see what changes were made in future

The `commit` command performs a commit, and the `-m` "message" adds a message.
```
$ git commit -m 'Message is added'
```
`-a` option will automatically stage every changed. It is generally not recommended. Since unwanted changes may be commited. (You donot need to specify file. It includes all file). It is same as `git add .` -> `git commit -m 'message the change'`
```
$ git commit -a -m 'Message is added'
```
## Git commit history
```
$ git log
```
To see log of remote repo use: `$ git log origin/master`
For more readable format in linewise.
It gives output in format `commit hash` and `commit message`
```
$ git log --oneline
```
## Git branch
Create branch in git repo, to work with. Branch name is usually meaningful which represent what is being done.
```
$ git branch first-branch
```
To see available branchs
- `$ git branch` : shows available branches in local git
- `$ git brach -a` : shows all braches in local as wel as remote repo
- `$ git brach -r` : shows all braches in remote repo only

**Switch the branch you are working with**
```
$ git checkout first-branch
```
Make changes in file in `first-branch`. When problem is solved switch to `master` or main branch.
**Merge changes in main branch**
```
$ git checkout master
$ git merge first-branch
```
Some-time when you change both files and want to merge. There may be merge conflct. For this `merge-conflict` of changed file should be resolved. And stage that change.
After use of brach and `first-brach` donot have any uses. Delete that brac using command.
```
$ git branch -d first-branch
```
# Git and Github
Github is used to track changes in remote repo.
Create a repo in github and copy HTTPS url: `https://github.com/realsanjeev/tutorial-git.git`
Add remote repo to local git
```
$ git remote add origin https://github.com/realsanjeev/tutorial-git.git
```
**See how remote is set-up**
```
git remote -v
```
Push repo from local git to remote Github
```
$ git push --set-upstream origin master
```
You will get console to authenticate your github account.Fill your `github username` and in place of password write `personnal token` generated from gt hub.
To get personnal token.
> Go to settings in profile > In developer settings > Go to personnal token access > In tokens(classic) > Generate token and save it for future use

## Git pull
When changes are made in github repo using `edit` option. We need to sync remote repo and local repo to keep repo in local computer up-to-date
`git pull` is combination of `git fetch` and `git merge`
```
$ git fetch origin
$ git merge origin/master
```
is equivalent to 
```
$ git pull origin
```
To see difference in file from remote master branch and local master. You can use `git diff` as 
`$ git fetch origin master` then, `$ git diff origin/master`
## Git push
To push changes in remote repo from local git.
```
$ git push orign
```
If new brach is added in local repo and we want to push changes in remote repo by creating brach first brach. Use this command:
```
$ git push --set-upstream origin first-branch
```
To track changes in brach of remote repo. If you create brach in remote repo `second-branch`
`$ git checkout origin/second-branch`

## Git .gitignore
`.gitignore` file includeitself is being ttracked. file that you donot want to be tracked. But `.gitignore` file itself is being tracked.
```
$ touch .gitignore
$ nano .gitignore
```
Example
```
# ignore all .config file
*.log
# ignore all files in directory test in root.
test/*
```
It is also possible to gnore files and directory and not been shown in .gitignore file. For this specify file to be ignored in
> .git/info/exclude_file

## Git Revert Reset and Ammend
