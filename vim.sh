#! /bin/sh

#Vim
echo "Checking if Vim is installed..."
if [ -z `dpkg -s vim | grep $INSTALLED_SUCCESS_TEXT` ]; then
    apt-get install -y vim
    if [ -z `dpkg -s vim | grep $INSTALLED_SUCCESS_TEXT` ]; then
        echo "Vim failed to install"
        exit 1
    else
        echo "Vim success to install"
    fi
else
    echo "Vim is already installed"
fi