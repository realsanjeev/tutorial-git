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
For multiplication we use `expr 40 \* 3`, here `\*` is escape ccharacter, since `*` is wildcard in bash.