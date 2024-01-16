# Git Commands
## Configure Git
Use `--global` to set the username and e-mail for every repository on your computer(system level setup).
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

**Delete the branches**
After use of brach and `first-brach` donot have any uses. Delete that branch(local) using command.
```
$ git branch -d first-branch
```
To delete the remote branch. Or use `-d` flag short form of `--delete`
```
$ git push origin --delete <branch-name>
```
`git remote prune origin`: Prunes (removes) remote-tracking references to branches that no longer exist on the remote repository named "origin."

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
`git revert` is command we use when we want to take a previous commit point and add it as new commit. But all log is still available
Revert latest commit in repo
```
$ git revert HEAD --no-edit
```
To revert to earlier commit, we use `$ git revert HEAD~x` where `x` is number from latest commit to specified commit. x is 0 for latest commit
To undo revert command
```
$ git revert --abort
```
`Git reset` is different from `git revert`. `git reset` takes us to previous commit point and delete all log following that point. While `git revert` has all log.
```
$ git reset <commit-hash>
```
You can get `<commit-hash>` from `$ git log --oneline`. It gors to point of `<commit-hash>`
`git ammend` is used to modify most recent commit.
To edit most latest commit, we use
```
$ git commit -m 'This is edited message from latest commit`
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
You can rename remote origin to upstream using 
```
$ git remote rename origin upstream
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

## Use SSH to connect GitHub
SSH(Secure Shell Protocal) is used for network management, remote file transfer and remote system access. SSH is used when you use unsecured network.
**Generate SSH key-pair**

`RSA(Rivest-Shamier-Adleman)` is public key cryptosystem whose typical key size is from 2948 to 4096. For this example, we use rsa to generate key.
```
$ ssh-keygen -t rsa -b 4096
```
You are opt to enter passphrase and location to store ssh-key. You can default storing location.You can add passphrase to d additional layer of security. For me, doing in kali linux `/home/kali/.ssh/id_rsa` is default location.
**Add SSH key-pair to SSH-Agent**
```
$ ssh-add /home/kali/.ssh/id_rsa
```
You will be opt to enter passphrase if any earlier.
copy public key to our clipboard which in location `/home/kali/.ssh/id_rsa.pub`
Then paste in github
> Go to profile setting > SSH > Add SSH > paste there
**Test SSH connection to Github**
```
$ ssh -T git@github.com
```
Add new GitHub SSH REmote to local repo
```
$ git remote add ssh-origin <ssh-url>
```
or convert our https connection to ssh
```
$ git remote set-url origin <ssh-url>
```

# CheetSheet For Git
| **Command** | **Description** |
|-------------|-----------------|
| `git init` | Initialize a new Git repository |
| `git clone <repository_url>` | Clone a repository |
| `git status` | Check the status of your working directory |
| `git add <file_name>` | Add changes to the staging area |
| `git add .` | Add all changes to the staging area |
| `git commit -m "Commit message"` | Commit changes to the repository |
| `git branch <branch_name>` | Create a new branch |
| `git checkout <branch_name>` | Switch to an existing branch |
| `git checkout -b <branch_name>` | Create and switch to a new branch |
| `git merge <branch_name>` | Merge branches |
| `git branch -d <branch_name>` | Delete a branch |
| `git remote add <remote_name> <repository_url>` | Add a remote repository |
| `git fetch <remote_name>` | Fetch changes from a remote repository |
| `git pull <remote_name> <branch_name>` | Pull changes from a remote repository |
| `git push <remote_name> <branch_name>` | Push changes to a remote repository |
| `git checkout -- <file_name>` | Discard changes in the working directory |
| `git reset HEAD <file_name>` | Unstage changes |
| `git commit --amend` | Amend the last commit |
| `git revert <commit_hash>` | Revert a commit |
| `git log` | View commit history |
| `git remote -v` | View remote repositories |
| *Create `.gitignore` file* | Ignore files and directories |
| `git config --global user.name "Your Name"` | Configure global user name |
| `git config --global user.email "your.email@example.com"` | Configure global user email |
|`.gitkeep` file|Keep the empty directory for version control|
