import this
import os
import subprocess

""" Comentario """
# Comentario

FNULL = open(os.devnull, 'w')

print("Tunning linux system")

check_installer="dpkg"
check_installer_arg_check="-s"
check_installer_arg_install="-i"
installer="apt-get"
installer_arg_install="install"
installer_arg_update="install"
installer_arg_forced_install="-y"
adder_key="apt-key"
adder_add_command="add"
downloader="wget"
downloader_arg_output="-O"
downloader_arg_quit="-q"


installer_text="Status: install ok installed"

""" Software """
# Git
git_app="git"
# RabbitVCS
rabbitvcs_cli_app="rabbitvcs-cli"
rabbitvcs_nautilux_app="rabbitvcs-nautilus"
#Vim
vim_app="vim"
#Visual Studio Code
vscode_url="https://go.microsoft.com/fwlink/?LinkID=760868"
vscode_app="code"
#Chrome
chrome_key_url="https://dl-ssl.google.com/linux/linux_signing_key.pub"
chrome_key_file="chrome.key"
chrome_app="google-chrome-stable_current_amd64"
chrome_repository_file="/etc/apt/sources.list.d/google-chrome.list"
chrome_repository_url="deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
chrome_url="https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"


def install_software( software ):
    software_status=subprocess.call([check_installer, check_installer_arg_check, software], stdout=FNULL, stderr=subprocess.STDOUT)
    if not software_status:
        print(software + " allready installed")
    else:
        install_status=subprocess.call([installer, installer_arg_install, installer_arg_forced_install, software])
        software_status=subprocess.call([check_installer, check_installer_arg_check, software], stdout=FNULL, stderr=subprocess.STDOUT)
        if not software_status:
            print(software + "installed")
        else:
            print("Problem was found on " + software + " installation")
            return 1;
    return 0;

def install_manual_dpkg_software( software, software_url ):
    software_status=subprocess.call([check_installer, check_installer_arg_check, software], stdout=FNULL, stderr=subprocess.STDOUT)
    if not software_status:
        print(software + " allready installed")
    else:
        download_status=subprocess.call([downloader, downloader_arg_output, software+".deb", software_url])
        install_status=subprocess.call([check_installer, check_installer_arg_install, software+".deb"])
        software_status=subprocess.call([check_installer, check_installer_arg_check, software], stdout=FNULL, stderr=subprocess.STDOUT)
        if not software_status:
            print(software + "installed")
        else:
            print("Problem was found on " + software + " installation")
            return 1;
    return 0;

def install_thrid_party_software( software, software_key_file, software_key_url, repository_file, repository_url ):
    software_status=subprocess.call([check_installer, check_installer_arg_check, software], stdout=FNULL, stderr=subprocess.STDOUT)
    if not software_status:
        print(software + " allready installed")
    else:
        download_status=subprocess.call([downloader, downloader_arg_quit, downloader_arg_output, software_key_file, software_key_url])
        install_key_status=subprocess.call([adder_key, adder_add_command, software_key_file])
        with open(repository_file, 'a') as file:
            file.write(repository_url)
        update_software()
        software_status=subprocess.call([check_installer, check_installer_arg_check, software], stdout=FNULL, stderr=subprocess.STDOUT)
        if not software_status:
            print(software + "installed")
        else:
            print("Problem was found on " + software + " installation")
            return 1;
    return 0;

def update_software():
    return subprocess.call([installer, installer_arg_update]);

update_software();
install_software(git_app);
install_software(rabbitvcs_cli_app);
install_software(rabbitvcs_nautilux_app);
install_manual_dpkg_software(vscode_app, vscode_url);
install_manual_dpkg_software(chrome_app, chrome_url);