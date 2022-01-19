# Environment Variables (MAC OS)

Environment variables are like "system-wide" variables.  
 They can be used by any program on the computer.  
 You can create them in the terminal or in files like `.zshenv`.

<br>

 ## Creating an environment variable
 ---

 In the terminal, type: 
 - `export VAR="hello world"`  
 
 or simply:
 - `VAR="hello world"`  

 >Where VAR is the name of the environment variable.  
 >Notice no spaces before or after the equals sign.  

 The environment variable can now be used.  

 Type `echo $VAR` to print it to the standard output.
 > Notice the `$` in front of the variable name. This denotes that you are calling an environment variable and must immediately precede the name of the environment variable.  

 An environment variable created this way will be automatically deleted when the terminal session ends. To create an environment variable permanently, the same code should be written in a shell configuration file (e.g. .zshenv) so that the environment variable is created whenever a terminal session starts up.

<br>

## Misc info
---

 To see a list of all currently defined environment variables, simply type the command `env` in a terminal session.  

 Arguably the most important / common environment variable is `$PATH`.  
 This variable lets the terminal know what directories to look in when a command is typed. The terminal finds the shell script (executable file) whose name matches the name of the command entered and runs the file.

<br>

[Article with more info](https://opensource.com/article/19/8/what-are-environment-variables)