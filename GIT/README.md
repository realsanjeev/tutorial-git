# Git Commands
## Configure Git
Use `--global` to set the username and e-mail for every repository on your computer(system level setup).
```bash
git config --global user.name '<username>'
git config --global user.email '<your@email.com>'
```
## Initialize git which you want to track
```bash
git init
```
Git now knows that it should watch the folder you initiated it on. Git creates a hidden folder to keep track of changes.
## Git help
See all possible commands in git. to quit from bash shell write `:q`
```bash
git help --all
```
See available option for specific command.
```bash
git <command> -help
```
## Git Status
Watch status of your changes in git repo.
```bash
git status
 ```
Files in your Git repository folder can any of 2 states:

- `Tracked` - files that Git knows about and are added to the repository
- `Untracked` - files that are in your working directory, but not added to the repository

To get status in short form
```bash
git status -s
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
```bash
git add --all
```
To add all file in git repo, we can also use `git add -A` OR `git add .`
To add only a file with filename `text.txt`, following code is executed
```bash
git add text.txt
```
### Stage change
Adding commits keep track of our progress and changes as we work. Git considers each `commit` a "change point" or "save point". Commit tag always written with message, so that we can see what changes were made in future

The `commit` command performs a commit, and the `-m` "message" adds a message.
```bash
git commit -m 'Message is added'
```
`-a` option will automatically stage every changed. It is generally not recommended. Since unwanted changes may be commited. (You donot need to specify file. It includes all file). It is same as `git add .` -> `git commit -m 'message the change'`
```bash
git commit -a -m 'Message is added'
```
## Git commit history
```bash
git log
```
To see log of remote repo use: `git log origin/master`


For more readable format in linewise.
It gives output in format `commit hash` and `commit message`
```bash
git log --oneline
```
## Git branch
Create branch in git repo, to work with. Branch name is usually meaningful which represent what is being done.
```bash
git branch first-branch
```
To see available branchs
- `git branch` : shows available branches in local git
- `git brach -a` : shows all braches in local as wel as remote repo
- `git brach -r` : shows all braches in remote repo only

**Switch the branch you are working with**
```bash
git checkout first-branch
```
Make changes in file in `first-branch`. When problem is solved switch to `master` or main branch.

**Merge changes in main branch**
```bash
git checkout master
git merge first-branch
```
Some-time when you change both files and want to merge. There may be merge conflct. For this `merge-conflict` of changed file should be resolved. And stage that change.

**Delete the branches**
After use of brach and `first-brach` donot have any uses. Delete that branch(local) using command.
```bash
git branch -d first-branch
```
To delete the remote branch you have to push it. Or use `-d` flag short form of `--delete`
```bash
git push origin --delete <branch-name>
```
`git remote prune origin`: Prunes (removes) remote-tracking references to branches that no longer exist on the remote repository named "origin."
## Git Stash

While working within a Git repository directory, you may need to save uncommitted changes without committing them. The `git stash` command allows you to temporarily store these changes and restore your working directory to a clean state.

**Save Your Changes**
To stash your current modifications:

```bash
git stash
```

By default, this saves both tracked and staged changes. Your working directory will revert to the last committed state.

You can also include a message to describe the stash:

```bash
git stash save "WIP: updating login feature"
```

**View Saved Stashes**
To see a list of all stashed changes:

```bash
git stash list
```

Example output:

```console
stash@{0}: WIP on main: 1234abcd Updating login feature
stash@{1}: WIP on feature/ui: 5678efgh Styling improvements
```

**Apply a Stash**
To reapply the most recent stash:

```bash
git stash apply
```

If you want to apply a specific stash from the list:

```bash
git stash apply stash@{1}
```

> **Note:** Applying a stash does *not* remove it from the stash list.
> To remove it after applying, use `git stash drop`.

**Remove a Stash**
Delete the most recent stash:

```bash
git stash drop
```

Or clear all stashes:

```bash
git stash clear
```

**Create and Apply in One Step**
If you want to stash your work and immediately apply it on another branch:

```bash
git stash pop
```

This applies the most recent stash and removes it from the stash list in one step.


## Git `.gitignore`
The `.gitignore` file tells Git which files or directories should not be tracked.
However, the `.gitignore` file itself is usually tracked so that other developers on the same project share the same ignore rules.
```bash
touch .gitignore
nano .gitignore
```
Example
```
# Ignore all .log files
*.log
# ignore all files in directory test in root.
test/*
```
It is also possible to **ignore files** without listing them in `.gitignore`.
You can do this by adding file patterns to:
> .git/info/exclude_file

### `.gitattributes` files
The `.gitattributes` file is used to configure how Git treats files based on their attributes. It allows you to specify attributes for paths and files in your Git repository.

Some common use cases for `.gitattributes` include:

1. **Text and Binary Files:** You can use `.gitattributes` to specify whether a file should be treated as text or binary. For example, you might want to ensure that certain file types (like images or binaries) are treated as binary to avoid line-ending conversions.

    ```plaintext
    # Treat all files with the '.jpg' extension as binary
    *.jpg binary
    ```

2. **End-of-Line (EOL) Settings:** You can control how Git handles end-of-line characters in text files. This is useful when collaborating on projects across different operating systems (Windows, Linux, macOS).

    ```plaintext
    # Set the EOL style to LF (Unix-style) for all '*.txt' files
    *.txt text eol=lf
    ```

3. **Git Merge Strategies:** You can specify different merge strategies for specific files or paths.

    ```plaintext
    # Use the 'ours' merge driver for files in the 'config/' directory
    config/** merge=ours
    ```

4. **Git Attributes for Linguist:** Linguist is a library used by GitHub to detect and highlight languages in repositories. You can use `.gitattributes` to override Linguist's language detection.

    ```plaintext
    # Override Linguist's language detection for a specific file
    filename linguist-language=Ruby
    ```

## Git Revert Reset and Amend
`git revert` is command we use when we want to take a previous commit point and add it as a new commit. But all log is still available.
Revert latest commit in repo
```bash
git revert HEAD --no-edit
```
To revert to an earlier commit, we use `git revert HEAD~x` where `x` is the number from latest commit to the specified commit. `x` is 0 for latest commit.

To undo revert command
```bash
git revert --abort
```
`git reset` is different from `git revert`. `git reset` takes us to a previous commit point and deletes all log following that point, while `git revert` keeps all log.

```bash
git reset <commit-hash>
```
You can get `<commit-hash>` from `git log --oneline`. It goes to the point of `<commit-hash>`.

`git amend` is used to modify the most recent commit.
To edit the most recent commit message, we use
```bash
git commit --amend -m "This is edited message from latest commit"
```

To add more files to the latest commit
```bash
git add <file>
git commit --amend --no-edit
```

To change the date of a commit
```bash
git commit --amend --date="YYYY-MM-DD HH:MM:SS"
```

Example
```bash
git commit --amend --date="2025-11-08 10:30:00"
```

We can also use environment variables before the commit command.

```bash
GIT_AUTHOR_DATE="2025-11-08 10:30:00" GIT_COMMITTER_DATE="2025-11-08 10:30:00" git commit --amend --no-edit
```

`GIT_AUTHOR_DATE` is the time when the commit was originally written.
`GIT_COMMITTER_DATE` is the time when the commit was actually made or last changed.

To change the date of older commits, we use interactive rebase
```bash
git rebase -i HEAD~x
```

Then change `pick` to `edit` for the commit we want to change and run
```bash
GIT_AUTHOR_DATE="YYYY-MM-DD HH:MM:SS" GIT_COMMITTER_DATE="YYYY-MM-DD HH:MM:SS" git commit --amend --no-edit
git rebase --continue
```



# Git and Github
Github is used to track changes in remote repo.
Create a repo in github and copy HTTPS url: `https://github.com/realsanjeev/tutorial-git.git`
Add remote repo to local git
```bash
git remote add origin https://github.com/realsanjeev/tutorial-git.git
```
**See how remote is set-up**
```bash
git remote -v
```
You can rename remote origin to upstream using 
```bash
git remote rename origin upstream
```
Push repo from local git to remote Github
```bash
git push --set-upstream origin master
```
You will get console to authenticate your github account.Fill your `github username` and in place of password write `personnal token` generated from git hub.

**To get personnal token.**
> Go to settings in profile > In developer settings > Go to personnal token access > In tokens(classic) > Generate token and save it for future use
## Git Pull and Push Essentials

In collaborative projects where multiple team members are contributing, it's crucial to keep the local and remote repositories synchronized. Here are the key commands for updating and pushing changes:

### Git Pull

When updates are made in the remote repository, use `git pull` to sync the local repository with the latest changes. This command is a combination of `git fetch` and `git merge`.

```bash
git pull origin
```

This is equivalent to:

```bash
git fetch origin
git merge origin/<branch>
```

To view differences between the remote master branch and the local master, use `git diff`:

```bash
git fetch origin master
git diff origin/master
```

### Git Push
To upload local changes to the remote repository, use the `git push` command:

```bash
git push origin
```

If a new branch, e.g., `<new-branch>`, is added locally and needs to be pushed to the remote repository, use:

```bash
git push --set-upstream origin <new-branch>
```

To track changes in a branch created on the remote repository, such as `second-branch`:

```bash
git checkout origin/second-branch
```

These commands ensure effective collaboration by maintaining a smooth flow of changes between local and remote repositories.

## Use SSH to connect GitHub
SSH(Secure Shell Protocal) is used for network management, remote file transfer and remote system access. SSH is used when you use unsecured network.
**Generate SSH key-pair**

`RSA(Rivest-Shamier-Adleman)` is public key cryptosystem whose typical key size is from 2948 to 4096. For this example, we use rsa to generate key.
```
ssh-keygen -t rsa -b 4096
```
You are opt to enter passphrase and location to store ssh-key. You can default storing location.You can add passphrase to d additional layer of security. For me, doing in kali linux `/home/kali/.ssh/id_rsa` is default location.
**Add SSH key-pair to SSH-Agent**
```
ssh-add /home/kali/.ssh/id_rsa
```
You will be opt to enter passphrase if any earlier.
copy public key to our clipboard which in location `/home/kali/.ssh/id_rsa.pub`
Then paste in github
> Go to profile setting > SSH > Add SSH > paste there
**Test SSH connection to Github**
```
ssh -T git@github.com
```
Add new GitHub SSH REmote to local repo
```
git remote add ssh-origin <ssh-url>
```
or convert our https connection to ssh
```
git remote set-url origin <ssh-url>
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
| Create `.gitkeep` file | Retain an empty directory for version control |
| Create `.gitattribute` file | Configure how Git treats files based on their attributes |
| `git clone https://<username>:<personal-token>@github.com:path/to/repo` | Clone a private repository that you have access to |
