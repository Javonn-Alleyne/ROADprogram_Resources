# SSH KEY-GEN
1. Ssh -T git@github.com - check status on ssh key

# From root cd to `.ssh` dir
1. Ssh-keygen -t ed25519 -C “email used for GitHub account”
1. `Eneter`
1. `Enter` - enter twice to skip password requirements

1. `ls` - look into the `.ssh` folder
2. `cat` filename.pub
3. copy and paste the string of numbers ans letters into github account under the `SSH KEYS` section
4. `ssh -T git@github.com`

# Git clone error - not cloning repo
1. Ssh-add ~/.ssh/github
