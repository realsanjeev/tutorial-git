##Git SSH Clone

To clone a Git repository using SSH, you need to follow these steps:

1. Ensure you have an SSH key pair:
   - If you don't have an SSH key pair, you can generate one using the following command:
     ```
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
     ```
   - Press Enter to accept the default file location and provide a passphrase if you wish.

2. Add your SSH key to the SSH agent:
   - Start the SSH agent:
     ```
     eval "$(ssh-agent -s)"
     ```
   - Add your SSH private key to the agent:
     ```
     ssh-add ~/.ssh/id_rsa
     ```
   
3. Copy the SSH public key:
   - Display your public key:
     ```
     cat ~/.ssh/id_rsa.pub
     ```
   - Copy the displayed key.

4. Add the SSH key to your Git hosting service:
   - For GitHub, go to your account settings, then "SSH and GPG keys," and add the SSH key.

5. Clone the Git repository using SSH:
   - Copy the SSH URL of the Git repository. It typically looks like `git@github.com:username/repo.git`.
   - Run the following command to clone the repository:
     ```
     git clone git@github.com:username/repo.git
     ```
   
Make sure to replace `username` with your actual username and `repo` with the name of the repository you want to clone. If you are using a different Git hosting service, replace the URL accordingly.