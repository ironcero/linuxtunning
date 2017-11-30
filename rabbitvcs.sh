#! /bin/bash

#RabbitVCS-cli
echo "Checking if RabbitVCS-cli is installed..."
if [ -z `dpkg -s rabbitvcs-cli | grep $INSTALLED_SUCCESS_TEXT` ]; then
    apt-get install -y rabbitvcs-cli
    if [ -z `dpkg -s rabbitvcs-cli | grep $INSTALLED_SUCCESS_TEXT` ]; then
        echo "RabbitVCS-cli failed to install"
        exit 1
    else
        echo "RabbitVCS-cli success to install"
    fi
else
    echo "RabbitVCS-cli is already installed"
fi

#RabbitVCS-Nautilus
echo "Checking if RabbitVCS-Nautilus is installed..."
if [ -z `dpkg -s rabbitvcs-nautilus | grep $INSTALLED_SUCCESS_TEXT` ]; then
    apt-get install -y rabbitvcs-nautilus
    if [ -z `dpkg -s rabbitvcs-nautilus | grep $INSTALLED_SUCCESS_TEXT` ]; then
        echo "RabbitVCS-Nautilus failed to install"
        exit 1
    else
        echo "RabbitVCS-Nautilus success to install"
    fi
else
    echo "RabbitVCS-Nautilus is already installed"
fi
