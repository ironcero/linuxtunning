#! /bin/sh
echo "#################################################"
echo "########### Base Tunning Script #################"
echo "#################################################"

sh properties.sh

apt-get update
apt-get -y upgrade

wget -O git.sh $DIRECT_MASTER_DOWNLOAD_URL/git.sh
wget -O properties.sh $DIRECT_MASTER_DOWNLOAD_URL/properties.sh
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
