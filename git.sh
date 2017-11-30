#! /bin/bash

#Vim
echo "Checking if Git is installed..."
git_installed=`dpkg -s git | grep "$INSTALLED_SUCCESS_TEXT"`
if [ -z "$git_installed" ]; then
    apt-get install -y git
    git_installed=`dpkg -s git | grep "$INSTALLED_SUCCESS_TEXT"`
    if [ -z "$git_installed" ]; then
        echo "Git failed to install"
        exit 1
    else
        echo "Git success to install"
        git clone $BASE_RESPOSITORY.git
    fi
else
    echo "Git is already installed"
fi
