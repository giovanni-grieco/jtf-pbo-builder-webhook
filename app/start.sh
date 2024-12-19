#!/bin/bash
git config --global user.email "$GIT_EMAIL"
git config --global user.name "$GIT_USERNAME"
echo "https://$GIT_USERNAME:$GIT_PASSWORD@$(echo $GIT_REPO | sed -e 's,https://,,')" > ~/.git-credentials
git config --global credential.helper 'store --file ~/.git-credentials'

git clone $GIT_REPO

python main.py