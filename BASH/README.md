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

### Handling the math expression
If we want to add `+`, `-` and `/` number we use `expr` command which treat the follow up args as expression
```bash
expr 30 + 50
```
We cannot write `expr 30+50`, we have to separate args with space to perform operation
For multiplication we use `expr 40 \* 3`, here `\*` is escape character, since `*` is wildcard in bash.

### Conditional Statements
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
## While Loop
It is used to statement until the statement is true
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

## Examples
**1. Script to update**
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