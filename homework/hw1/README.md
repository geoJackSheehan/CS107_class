# Homework 1

* Git repository setup
* Command line
* Markdown
* Working with Git

<https://canvas.harvard.edu/courses/108118/assignments/607987>

# Submission instructions

Homework must be submitted in your private Git repository hosted in the CS107
organization at <https://code.harvard.edu/CS107>. Only commits before or at the
due date are considered for grading. The homework due date is indicated on the
problem sheet and displayed in the
[schedule](https://harvard-iacs.github.io/2022-CS107/pages/schedule_static.html).

Please see the [homework
tutorial](https://harvard-iacs.github.io/2022-CS107/pages/tutorials.html#tutorial-hw)
for the correct submission procedure.  The summarized steps are:

1. Checkout a new branch called `hw1`.  This branch should be based off your
   `main` or `master` branch.
2. Solve the homework on the `hw1`.  Commit often and logically.
3. Your final work must be submitted in the directory
   `homework/hw1/submission` in your private Git repository.
4. Create an open pull request to merge your `hw1` branch into your `main` or
   `master` branch (you could also do this after step 1).  The last commit on or
   just before the deadline in the *open* pull request will graded.  *Do not
   merge the open pull request before we have graded your work.*
5. Zip your `submission` directory and submit it on Gradescope:
   [https://canvas.harvard.edu/courses/108118/external_tools/89451](https://canvas.harvard.edu/courses/108118/external_tools/89451)


# Some Unix references and more examples

This extra set of exercises is for your reference in case you don't have much
experience with Unix/Linux.  *Please* do your best to become comfortable with
the command line throughout the semester.  There are plenty of resources
available on learning how to use the command line efficiently.  Here is one to
get you started:
[http://linuxcommand.org/lc3_learning_the_shell.php#contents](http://linuxcommand.org/lc3_learning_the_shell.php#contents).

MacOSX comes with a command line app (terminal.app) and since Macs are similar
to [Unix](https://en.wikipedia.org/wiki/Unix), the terminal commands are pretty
much the same as those in [Linux](https://en.wikipedia.org/wiki/Linux)
distributions.  Windows is a bit different and you should consider installing
the Windows Subsystem for Linux and possibly Docker.  See the
[Windows](https://harvard-iacs.github.io/2022-CS107/pages/resources.html#windows)
section in the resources page of the class.

It is true that there are various options for using `git` from the Desktop (e.g.
see [GitHub Desktop](https://desktop.github.com)).
However, it is more useful for you to be able to do things from the command
line.  The reasons for this are that the command line is not going anywhere any
time soon and it can't be predicted what GUI your future company/group will want
you to use.  You'll be much more versatile using the command line.

What this means is that you need to learn a little bit about how to navigate
with the command line.  There are a few essential commands that you absolutely
**must** know.  You'll pick up the rest as you go.  Here are
the essential ones:

* **ls**: list the contents of the current directory
* **cd**: change to a new directory
* **mv**: rename a directory or file OR move a directory or file to a new location
* **cp**: copy a directory or file
* **pwd**: print the working directory
* **mkdir**: create a new directory
* **rm**: remove a file (you can remove a directory with rm -r)

Let's try to work with these a bit.  In the following steps, you should hit the
`Return` key after typing each command.

1. Open up a terminal and type `pwd`.  The output should be your home directory.
2. Next type `ls`.  You should see all the files and directories in your home
   directory.  Notice that if you type `ls -l` you get a list with more
   information where the files and directories are ordered alphabetically.
   Typing `ls -lt` sorts the list by date/time created with the most recent
   file/directory at the top.  `ls -ltr` just reverses the order of the sort;
   now the most recent file/directory is at the bottom.
3. Now type `mkdir mydir`.  Voila!  You have just created a new directory.  Try
   `ls` again.  Do you see the new directory?
4. To enter that directory type `cd mydir`.  You just changed into your new
   directory.  Type `pwd` to see where you are.
5. Now that you're inside your new directory, let's create a file in there.
   * Type `echo 'Hello world!' > newfile.txt`
   * Type `ls`.  You should see the next text file!
   * To see the contents of the file, type `cat newfile.txt`.
6. Suppose you now want to rename `newfile.txt` to `README.txt`.  Just execute
   `mv newfile.txt README.txt`.  Type `ls` again if you wish.
7. Maybe you really wanted to keep a copy of `newfile.txt`.  Just do `cp
   README.txt newfile.txt`.  As usual, `ls` will show you what you want to see.
8. What if `newfile.txt` should actually be in a different directory?  Let's do
   the following:
   * `mkdir newdir`
   * `mv newfile.txt newdir/`
   * Alternatively, you could give the entire path of the new directory (not
     necessary here).  Here's how you would do that:
     - `pwd` (just to see the current path)
     - `mv newfile.txt path_from_pwd/newdir/`
9. That was fun, but this directory is completely useless to use now.  Let's
   delete it.
   * First, you need to get out of the current directory.  You can't delete a
     directory from within it!
   * To go up one directory, just type `cd ..`.
      - **Unix Note:** In Unix, `.` stands for the current directory and `..`
        stands for the parent directory (that is, the directory containing the
        current directory.  Hence, `cd ../` changes to the parent directory of
        the current directory.
      - **Unix Note:** If you want to go up two directories, just do `cd ../../`.
        You can use the same pattern for $n$ directories.
  * Now type `rm mydir`.  You should see the message `rm: mydir/: is a
    directory`. `rm` cannot be used to remove directories as-is.  It can only
    remove files.
  * To remove the directory type `rm -rv mydir`.  The `-r` option says to
    recursively remove the directory and any contents.  The `-v` option says to
    be verbose while removing files.  You don't really need the `-v` option, but
    I like use it so I can see progress.

That was a whirlwind tour through a few of the more useful Unix commands.  It
won't take you long to use them effectively, but *you must use them*.

**Note:** If you want more information about any command, just type `man
command_name` into the terminal.  This will bring up the manual page for that
command. You will see all sorts of information. To scroll down, just hit the
`space bar`. To exit the `man page` just type `q` (for quit). Here's an example
of a portion of the `man page` for the `rm` command:

```bash
$ man rm
RM(1)                          User Commands                          RM(1)

NAME
       rm - remove files or directories

SYNOPSIS
       rm [OPTION]... [FILE]...

DESCRIPTION
       This  manual  page documents the GNU version of rm.  rm removes each
       specified file.  By default, it does not remove directories.

       If the -I or --interactive=once option is given, and there are  more than
       three  files  or the -r, -R, or --recursive are given, then rm prompts
       the user for whether to proceed with the  entire  operation. If the
       response is not affirmative, the entire command is aborted.

       Otherwise,  if  a  file is unwritable, standard input is a terminal, and
       the -f or --force option is not given, or the -i  or --interactive=always
       option is given, rm prompts the user for whether to remove the file.  If
       the response is  not  affirmative,  the  file  is skipped.
```

#### Bonus Command

Suppose you want to copy a file from a different location to your current
directory.  Well, recall that the current directory is represented by the `.`
object.  Here are a few things you can do:

* `cp path_to_file/file .`: Will copy file to your current location
* `cp path_to_file/file ./sub_dir`:  Will copy file to the directory `sub_dir`
  in your current location
* `cp ../file .`:  Will copy file from the parent directory to your current
  location

There are other, similar patterns to accomplish roughly the same thing.
