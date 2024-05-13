## Bash Scripting

To determine which shell you are using in your distribution, execute the following command:
```bash
echo $SHELL
```

If you are not running bash, you can switch to bash by locating its path with the following command:
```bash
which bash
```
This command typically outputs something like `/usr/bin/bash`. Enter this in your terminal to switch to the bash shell.

To create a script file, first, create the file using a text editor such as `nano`. Execute the following command:
```bash
nano myscript.sh
```
Then, add your script content to the file. For example:
```bash
ls
```
To save the file, press `Ctrl` + `O`, then exit with `Ctrl` + `X`.

You must change the file's permissions to make it executable:
```bash
chmod +x myscript.sh
```
Now, you can run your first bash script with:
```bash
./myscript.sh
```
The standard convention for writing bash scripts is to include a shebang `#!/bin/bash` at the top of your script. This line specifies which interpreter to use to execute the script.
```bash
#!/bin/bash
echo "Hello World!"

echo "My current working directory is: "
pwd
```

## Variables

### Declaring Variables in Bash

Variables in bash are declared by specifying the variable name followed by `=` and its value, with no space between them. To access the value of a variable, prepend `$` before the variable name.
```bash
myname="realsanjeev"
echo $myname
```

When you exit the shell and open a new shell, the previous value of the variable is lost since in bash, the variable's scope is tied to the session.

**Double Quotes and Single Quotes**

To print out the value of a variable, use double quotes. If you don't want the variable's value to be interpreted, use single quotes.
```bash
myname=realsanjeev
echo "My name is $myname"
echo 'My name is $myname'
```
This will output:
```
My name is realsnjeev
My name is $myname
```

Variables are very useful when scripting since you can define and change their values in scripts for deployment and customization for different environments.

You can also assign the value of the output of another command to a variable:
```bash
files=$(ls)
```
Here, `$(ls)` is a subshell.

Variables are generally named using lowercase letters. UPPERCASE variables are typically reserved for system variables or environment variables of your system (e.g., USER is a system variable). It's best practice to use lowercase for local variables. You can view all system variables and session variables using the `env` command.

### Arguments in Bash

In Bash scripting, arguments are values provided to a script or a function when it is executed. These arguments allow scripts to accept input dynamically, making them more flexible and versatile.

In the provided script snippet:

```bash
#!/bin/bash

lines=$(ls -lh $1 | wc -l)

echo "You have $(($lines-1)) objects in the $1 directory."
```

- `$1` represents the first argument passed to the script.
- The script uses `$1` as the directory path argument to the `ls` command.
- `ls -lh $1` lists the contents of the directory specified by the first argument (`$1`), with human-readable sizes.
- `wc -l` counts the number of lines in the output of `ls`.
- The resulting count is stored in the variable `lines`.
- The script then echoes a message indicating the number of objects (files and directories) in the specified directory, derived from the count stored in `lines`.

### Handling the math expression
If we want to add `+`, `-` and `/` number we use `expr` command which treat the follow up args as expression
```bash
expr 30 + 50
```
We cannot write `expr 30+50`, we have to separate args with space to perform operation
For multiplication we use `expr 40 \* 3`, here `\*` is escape character, since `*` is wildcard in bash.

## Conditional Statements
Conditional statements allow us to execute commands only if certain conditions are met.

```bash
#!/bin/bash

mynum=200
if [ $mynum -eq 200 ]; then
    echo "mynum is equal to 200"
elif [ $mynum -gt 200 ]; then
    echo "mynum is greater than 200"
else
    echo "mynum is less than 200"
fi
```

In the `if` statement, the expression is enclosed in square brackets `[ ]`, with each expression separated by a space. Here, we check if the variable is equal to 200 using the `-eq` flag for equality.

Other comparison flags include:
- `-ne`: Not equal
- `-gt`: Greater than
- `-lte`: Less than or equal to

To check the existence of a file, we use `[ -f ~/file ]` in the expression. For directories, we use `-d` instead of `-f`.

### Exit Code
The exit code indicates whether a command was successful or not. It's an essential aspect of development since we often need to take different actions based on whether a command fails or succeeds. An exit code of `0` signifies success, while any non-zero value indicates failure.

For example:
```bash
#!/bin/bash

package=htop
sudo apt install $package
echo "The exit code for package installation is: $?"
```

We can also manually set the exit code in a script. When encountered, the script terminates, and we see the exit code of the terminated string.
```bash
#!/bin/bash

directory=/etc
if [ -d $directory ]; then
    echo "The directory $directory exists"
    exit 0
else
    echo "The directory $directory does not exist"
    exit 1
fi

echo "This statement will not run regardless of whether the condition of the above statement is true or not"
```

## Loop Statement
## While Loop
A while loop is used to repeat a statement until the specified condition becomes false.

```bash
#!/bin/bash

myvar=1
while [ $myvar -le 10 ]
do
    echo $myvar
    myvar=$((myvar + 1))
done
echo "This is after the while loop"
```

### For Loop
A for loop is used to iterate through a sequence of items.

```bash
#!/bin/bash

for current_num in {1..10}
do
    echo $current_num
    sleep 1
done

echo "This is outside of the for loop."
```

It can also be used to process files in a directory.

```bash
#!/bin/bash

# Iterate over the .log files in the logfiles directory
for file in logfiles/*.log
do
    tar -csvf $file.tar.gz $file
done
```

## Functions
In programing we donot want to repeat writing same code again and again. ,We write functions for reliablity and readability.
```bash
check_exit_status() {
    if [$? -ne 0 ]
    then 
        echo "An error occured, please check the $errorlog file."
    fi
}
```


## Other Commands
Here's a command to find all the files in the `/etc` directory:

```bash
find /etc -type f 
```

To suppress any error messages that may occur and prevent them from displaying on the console, we can redirect stderr (standard error) to `/dev/null`, which effectively discards any output sent to it. This is useful when we only want to see the successful output and not the error messages.

```bash
find /etc -type f 2> /dev/null
```

In the above command:
- `2` represents stderr (standard error).
- `>/dev/null` redirects stderr to `/dev/null`, ensuring that any error messages are not displayed on the console.

Conversely, if we want to see only the error messages and suppress the normal output, we can redirect stdout (standard output) to `/dev/null` instead:

```bash
find /etc -type f > /dev/null
```

In this command:
- `>` redirects stdout to `/dev/null`, effectively discarding any normal output.
- This means that only stderr (error messages) will be displayed on the console.

If we want to wrie std err and stdout in single file we can write `&` symbol after f as `find /etc -type f &> texts.txt`. If we want to send stdout to onefile and stderr in another file. Note that we donot have to erite 1 since 1 represents stdout which is by defalut what is shown if we donot write 1.
```bash
find /etc -type f 1>std_out.txt 2>std_err.txt
```


Take standard input from user
```bash
#!/bin/bash

echo "Please enter your name:"
read myname
echo "Your name is: $myname"
```
## Examples
**1. Script to update**
We can see our os information using `cat /etc/os-release`. This file is in almost all distro of linux system
```bash
#!/bin/bash

if [ -d /etc/pacman.d ]
then
    # The host is based on Arch, run the pacman update command
    sudo pacman -Syn
fi

if [ -d /etc/apt ]
then
    # The host is based on Debian or Ubuntu,
    # Run the apt version of the command
    sudo apt update
    sudo apt dist-upgrade
fi
```

Typically, we prefer not to store our scripts in the home directory or any publicly accessible directory. Instead, we opt for a location that is accessible to other users for execution but restricts their ability to update or modify the script. The commonly chosen location for this purpose is `/usr/local/bin`, and we often change the ownership of the script to the `root` user and `root` group for added security.

```bash
sudo mv update.sh /usr/local/bin/update
sudo chown root:root /usr/local/bin/update
```

In this example, we've renamed the file `update.sh` to `update`. In Linux, script files do not require a file extension to specify their type. After moving the script to `/usr/local/bin`, it can be executed simply by typing `update`. If executing the script using this command fails, we can resolve it by adding the `/usr/local/bin` directory to the `PATH` variable.

```bash
export PATH=/usr/local/bin:$PATH
```

By adding this line to our shell configuration file (e.g., `.bashrc` or `.profile`), we ensure that the `/usr/local/bin` directory is included in the `PATH` variable every time we log in, allowing us to execute scripts stored in that location without specifying their full path.

