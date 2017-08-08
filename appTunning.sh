#! /bin/sh
echo "#################################################"
echo "########### Base Tunning Script #################"
echo "#################################################"

TEMPORAL_APP_FOLDER=/tmp/appTemporalFolder
INSTALLED_SUCCESS_TEXT="install ok installed"

apt-get update
apt-get -y upgrade

echo "Making temporal folder ($TEMPORAL_APP_FOLDER)..."
if [ -d "$TEMPORAL_APP_FOLDER" ]; then
    echo "$TEMPORAL_APP_FOLDER exists"
else
    echo "$TEMPORAL_APP_FOLDER doesn't exist. Creating..."
    mkdir $TEMPORAL_APP_FOLDER
    echo "$TEMPORAL_APP_FOLDER was created"
fi



wget X
sh vscode.sh
sh vim.sh