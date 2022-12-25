# Why is the commit SHA1 different for two commits with identical content

The reason is that commit objects also take into account the date and time when
a commit has been created.  It is therefore not possible that an earlier commit
can be identical to a later commit, even if the content is identical.  Commit
objects are *unique* and *immutable*.
