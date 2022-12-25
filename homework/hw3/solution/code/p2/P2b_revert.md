1. No.  The conflict happens because both developers modified the same hunk in
   the file.
2. Developer B modifies a different hunk in the file:
   a.) No.  Git can resolve this merge since common ancestor is clear
   b.) Yes.  Git *cannot* resolve this conflict because the common ancestor is
   not clear and work might be lost.
