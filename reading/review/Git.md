# Git

## What is Git? 

### Snapshots, Not Differences
- `The major difference between Git and any other VCS is the way Git thinks about its data.`

Conceptually, most other systems store information as a list of file-based changes. **(diff)**
These other systems think of the information they store as a set of files and the changes made to each file over time
(this is commonly described as delta-based version control).

- `Git thinks of its data more like a series of` **(snapshots)**. 

With Git, every time you commit, or save the state of your project, Git basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot. 
To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file it has already stored. Git thinks about its data more like a stream of snapshots.

### Nearly Every Operation Is Local
- `Most operations in Git need only `**local files** `and resources to operate` 
generally no information is needed from another computer on your network. 

## Why do we need git add, git commit, git push etc ?

### The Three States
- `Git has three main states that your files can reside in:` **modified, staged, and committed**:

**Modified** means that you have changed the file but have not committed it to your database yet.

**Staged** means that you have marked a modified file in its current version to go into your next commit snapshot.

**Committed** means that the data is safely stored in your local database.

This leads us to the three main sections of a Git project: **the working tree, the staging area, and the Git directory**.

**The working tree** is a single checkout of one version of the project. These files are pulled out of the compressed database in the Git directory and placed on disk for you to use or modify.

**The staging area** is a file, generally contained in your Git directory, that stores information about what will go into your next commit. Its technical name in Git parlance is the “index”, but the phrase “staging area” works just as well.

**The Git directory** is where Git stores the metadata and object database for your project. This is the most important part of Git, and it is what is copied when you clone a repository from another computer.

#### The basic Git workflow goes something like this:
```diff
+You modify files in your working tree.

+You selectively stage just those changes you want to be part of your next commit, 
+which adds only those changes to the staging area.

+You do a commit, which takes the files as they are in the staging area and 
+ stores that snapshot permanently to your Git directory.
```
If a particular version of a file is in the Git directory, it’s considered committed. If it has been modified and was added to the staging area, it is staged. And if it was changed since it was checked out but has not been staged, it is modified. 


## Git Internals - Git Objects

```diff
- What's the complex combination of number and abcde... ?
```
the core of Git is a **simple key-value data store**. 

What this means is that you can insert any kind of content into a Git repository, 
for which Git will hand you back a unique key you can use later to retrieve that content.

Git takes some data, stores it in your .git/objects directory (the object database), 
and gives you back the unique key that now refers to that data object.

``` diff
- I don't get it 
```
```diff
+ A Git blob (binary large object) is the object type used to store the contents of each file in a repository. 
+The file's SHA-1 hash is computed and stored in the blob object. 
```

```diff
+ A Git commit is a snapshot of the hierarchy (Git tree) and the contents of the files (Git blob) in a Git repository

+ A Git tree object creates the hierarchy between files in a Git repository. 
+ (You can use the Git tree object to create the relationship between directories and the files they contain)
```
