## Configure multiple SSH for different accounts
To configure multiple SSH keys for different GitHub accounts on a Linux system, follow these steps:

### 1. **Generate SSH Keys**
If you haven't already generated SSH keys for your accounts, do so now. You can generate separate keys for each account as follows:

```bash
ssh-keygen -t ed25519 -C "email@example.com"
```

Replace `"email@example.com"` with the email associated with your GitHub account. When prompted, name the key something distinctive like `id_ed25519_github_work` for a work account and `id_ed25519_github_personal` for a personal account. 

### 2. **Add the SSH Keys to the SSH Agent**
Start the SSH agent and add your newly created keys:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_github_work
ssh-add ~/.ssh/id_ed25519_github_personal
```

### 3. **Create or Modify the SSH Config File**
Next, create or modify the SSH config file to include your multiple identities.

```bash
nano ~/.ssh/config
```

Add the following configurations:

```plaintext
# Work GitHub account
Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github_work

# Personal GitHub account
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github_personal
```

### 4. **Cloning Repositories Using the Correct Identity**
When cloning a repository or setting the remote URL, specify the appropriate host alias you created in the SSH config file:

```bash
# Cloning a work repo
git clone git@github-work:username/work-repo.git

# Cloning a personal repo
git clone git@github-personal:username/personal-repo.git
```

### 5. **Updating Existing Repositories**
For existing repositories, you can update the remote URL to use the correct identity:

```bash
git remote set-url origin git@github-work:username/work-repo.git
```

or

```bash
git remote set-url origin git@github-personal:username/personal-repo.git
```

### 6. **Verify the Configuration**
You can verify which SSH key is being used by running:

```bash
ssh -T git@github-work
ssh -T git@github-personal
```

If everything is configured correctly, GitHub will respond with a success message corresponding to each account.

### 7. **Using Environment Variables for Git Configurations (Optional)**
If you want to ensure that commits are attributed to the correct GitHub account, you can configure Git to use different usernames and email addresses for different repositories:

```bash
cd /path/to/your/repository
git config user.name "Your Work Name"
git config user.email "your-work-email@example.com"
```

This setup allows you to manage multiple GitHub accounts on a single machine with minimal hassle.
