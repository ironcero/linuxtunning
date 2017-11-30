#! /bin/sh
echo "#################################################"
echo "########### Base Tunning Script #################"
echo "#################################################"

INSTALLED_SUCCESS_TEXT="install ok installed"
BASE_RESPOSITORY=https://github.com/ironcero/linuxtunning
DIRECT_MASTER_DOWNLOAD_URL=$BASE_RESPOSITORY/raw/master

apt-get update
apt-get -y upgrade

wget -O git.sh $DIRECT_MASTER_DOWNLOAD_URL/git.sh
wget -O properties.sh $DIRECT_MASTER_DOWNLOAD_URL/properties.sh

sh properties.sh

if [ -f git.sh ]; then
    sh git.sh
else
    echo "git.sh not found"
    exit 1;
fi

if [ -f appTunning.sh ]; then
    sh appTunning.sh
else
    echo "AppTunning.sh not found"
    exit 1;
fi
