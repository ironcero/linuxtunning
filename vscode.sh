#! /bin/sh

#VS CODE
VSCODE_APP_FILE="vscode.deb"
VSCODE_APP_URL="https://go.microsoft.com/fwlink/?LinkID=760868"

if [ -z `dpkg -s code | grep $INSTALLED_SUCCESS_TEXT` ]; then
    echo "Downloading VS Code installer..."
    wget -O $VSCODE_APP_FILE $VSCODE_APP_URL
    if [ -f $TEMPORAL_APP_FOLDER/$VSCODE_APP_FILE]; then
        echo "VS Code installer downloaded"
        echo "Installing VS Code..."
        dpkg -i $TEMPORAL_APP_FOLDER/$VSCODE_APP_FILE
        echo "Installing VS Code dependencies..."
        apt-get install -f -y
        if [ -z `dpkg -s code | grep $INSTALLED_SUCCESS_TEXT` ]; then
            echo "VS Code failed to install"
            exit 1;
        else
            echo "VS Code success to install"
        fi
    else
        echo "VS Code installer failed to download"
        exit 1;
    fi
else
    echo "VS Code is already installed"
fi
