#!/bin/bash

git config --global user.email "$GIT_EMAIL" && git config --global user.name "$GIT_USERNAME" && git config --global user.password "$GIT_PASSWORD" && git config --global credential.helper store

git clone $GIT_REPO