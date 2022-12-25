# Basic Shell Programming


The first line that you will write in bash script files is called `shebang`. This line in any script determines the script's ability to be executed like a standalone executable without typing sh, bash, python, php etc beforehand in the terminal.

## 1. Variables

Creating variables in bash is similar to other languages. There are no data types. A variable in bash can contain a number, a character, a string of characters, etc. You have no need to declare a variable, just assigning a value to its reference will create it.

Example:
```bash
str="hello world"
echo $str   # hello world
```

In bash, we can assign the output text of a command to a variable directly.
Example
```bash
$now=`date`
```

Example:
```bash
var = hi
echo $var # hi
echo Good$var # Goodhi
echo $varhello # empty
echo ${var}hello # hihello
```
### Difference between "$var" and $var
```bash
var="foo bar"
for i in "$var"; do # Expands to 'for i in "foo bar"; do...'
    echo $i         #   so only runs the loop once
done
# foo bar

var="foo bar"
for i in $var; do # Expands to 'for i in foo bar; do...'
    echo $i       #   so runs the loop twice, once for each argument
done
# foo
# bar
```

https://stackoverflow.com/questions/18135451/what-is-the-difference-between-var-var-and-var-in-the-bash-shell

## 2. Functions
As in almost any programming language, you can use functions to group pieces of code in a more logical way or practice the divine art of recursion. Declaring a function is just a matter of writing function my_func { my_code }. Calling a function is just like calling another program, you just write its name.

```bash
function name() {
    # $1 the 1st parameters，$N the N-th parameters
    # $# num of parameters
    # $0 the name of the shell or shell script.
    # $@ all parameters
    # $* all parameters, type is string
    shell commands
}
```

Example:
```bash
#!/bin/bash
function hello {
   echo world!
}
hello

function say {
    echo $1
}
say "hello world!"
```
#### Exit code
```Bash
#!/bin/bash

exit 0   # Exit the script successfully
exit 1   # Exit the script unsuccessfully
echo $?  # Print the last exit code
```

## 3. Conditionals

The conditional statement in bash is similar to other programming languages. Conditions have many form like the most basic form is `if` expression `then` statement where statement is only executed if expression is true.

Expression Examples:

```bash
statement1 && statement2  # both statements are true
statement1 || statement2  # at least one of the statements is true

str1=str2       # str1 matches str2
str1!=str2      # str1 does not match str2
str1<str2       # str1 is less than str2
str1>str2       # str1 is greater than str2

-a file         # file exists
-d file         # file exists and is a directory
-e file         # file exists; same -a
-f file         # file exists and is a regular file (i.e., not a directory or other special type of file)
-r file         # you have read permission
-s file         # file exists and is not empty
-w file         # you have write permission
-x file         # you have execute permission on file, or directory search permission if it is a directory
-N file         # file was modified since it was last read
-O file         # you own file
```

Example
```bash
test -e a.sh; echo $? # find the return value of the last executed command 
test -r a.sh; echo $?
test -w a.sh; echo $?
test -x a.sh; echo $?
```
```bash
file1 -nt file2     # file1 is newer than file2
file1 -ot file2     # file1 is older than file2

-lt     # less than
-le     # less than or equal
-eq     # equal
-ge     # greater than or equal
-gt     # greater than
-ne     # not equal
```

### if 
```bash
if [ expression ]; then
    will execute only if expression is true
else
    will execute if expression is false
fi
```

```bash
if [ "$varname" = "abc" ]; then
    echo "this is abc"
elif [ "$varname" = "123" ]; then
    echo "this is 123"
else
    echo "neither"
fi
```

```bash
if [ $val -gt 11 ] && [ $val -lt 12 ]; then
    echo "the value is  between 11 and 12"
fi
```

### case
```bash
case expression in 
    pattern1 )
        statements ;;
    pattern2 )
        statements ;;
    * )
        otherwise ;;
esac
```

## 4. Loops

There are three types of loops in bash. `for`, `while` and `until`.

### while 
```bash
while condition; do
    statements
done
```

```bash
i=1
while [ $i -le 10 ]; do
    echo $i; 
    i=$(expr $i + 1)
done
```

### for
```bash
for i in {1..10}; do
    echo $i
done
```
```bash
for name [in list]; do
    statements
done
```
list files in a directory
```bash
for f in /home/*; do 
    echo $f
done
```

```bash
for (( initialisation ; ending condition ; update )); do
    statements
done

for ((i = 0; i < 10; i++)); do 
    echo $i; 
done
```

```Bash
#!/bin/bash
for number in `seq 1 1 10`
do
    total=$(($total + $number))
done
echo $total
```

### until 
```bash
until condition; do
    statements
done
