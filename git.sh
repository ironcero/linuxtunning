#! /bin/bash

#Vim
echo "Checking if Git is installed..."
if [ -z `dpkg -s git | grep "$INSTALLED_SUCCESS_TEXT"` ]; then
    apt-get install -y git
    if [ -z `dpkg -s git | grep "$INSTALLED_SUCCESS_TEXT"` ]; then
        echo "Git failed to install"
        exit 1
    else
        echo "Git success to install"
        git clone $BASE_RESPOSITORY.git
    fi
else
    echo "Git is already installed"
fi
