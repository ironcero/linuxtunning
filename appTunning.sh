#! /bin/bash
echo "#################################################"
echo "########### Base Tunning Script #################"
echo "#################################################"

TEMPORAL_APP_FOLDER=/tmp/appTemporalFolder

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

sh vscode.sh
sh vim.sh
sh rabbitvcs.sh
