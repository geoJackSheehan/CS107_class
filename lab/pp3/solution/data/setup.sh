#!/usr/bin/env bash
# File       : setup.sh
# Description: Create Git repositories for exercise 2 (PP3).
# Copyright 2022 Harvard University. All Rights Reserved.
dst='exercise_2'
rm -rf ${dst}
mkdir -p ${dst}
cd ${dst}
mkdir remote A B
(cd remote && git init --bare)
(cd A && git init && git branch -M main && git remote add origin ../remote)
(cd B && git init && git branch -M main && git remote add origin ../remote)
for dev in A B; do
    cd ${dev}
    cat <<EOF >>.git/config
[user]
    name = Developer ${dev}
    email = developer.${dev}@harvard.edu
EOF
    cd ..
done
cd A
cat <<'EOF' >goat.py
#!/usr/bin/env python3
# File       : goat.py
# Description: pp3 exercise 2
# Copyright 2022 Harvard University. All Rights Reserved.

def main():
    goat = 4 * ["🖤 Developer A is the greatest of all time! 🖤"]
    print('\n'.join(goat))

if __name__ == "__main__":
    main()
EOF
git add goat.py
git commit -m 'Initial commit'
git push -u origin main
sed -i 's/of all time/for all eternity/' goat.py
git commit -am 'I like it better this way'
cd ../B
git pull origin main
sed -i 's/Developer A/Developer B/' goat.py
sed -i 's/4 \*/100 */' goat.py
git commit -am 'I disagree 100 times'
git push -u origin main
