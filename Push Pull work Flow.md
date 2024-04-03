# Push Pull Work Flow
Allows for asynchronous work to be done. Allows for work to be done on multiple branches

## Why work with branches
can make changes without destroying the main build.
if errors occur on the main build, it would have to be revert or scrapped.
branches avoid this problem

# How To?
## first check status
- git status - status on branch
- git checkout "branch name" - to switch branches (only if switching to branch)

## Create a new branch on the repository
- git checkout -b “branch name” (no spaces) - creates a new branch
- git status - to see the status on new branch

## Pushing files to repo
- git add . - adds current files in the present working directory
- git commit  -m “_**type message here**_” - creates a snapshot in time on the changes made to the files being added to the repo
- git push - push to the repository
- Copy - git push --set-upstream origin "new branch name" - allows the branch to be seen on Github

## Github
- Create pull request on the new branch to sync the branches
- merge new branch with main branch

# Extra help
[here](https://medium.com/@Ariobarxan/recovering-a-lost-commit-in-git-103a48bf8a16)

