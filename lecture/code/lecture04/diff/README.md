# Steps to patch file `branch_B/hello.py`

1. Create a patch file from a diff:
```bash
diff --color=never -u branch_B/hello.py branch_A/hello.py >fix.patch
```
2. Change into `branch_B/` and apply the patch to the file `hello.py`.  Check
   the contents of the file *before* you apply the patch and once more after.
   To apply the patch:
```bash
patch -p1 <../fix.patch
```
