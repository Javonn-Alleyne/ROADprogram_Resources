# How to fix a problem
## divergin branches
Occurs when trying to push to the main repo but your forked repo is behind in commints to the main repo
`git pull` should resolve issue

# if not then

`git config pull.rebase false`

# if not then

`git merge main` - merge different branch into main

make changes to files on your end - add or remove files in the forked repo to match the main repo

continue with the `git add`, `git commit -m`, `git push` process

