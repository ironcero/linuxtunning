import os
import subprocess
import json

f_null = open(os.devnull, 'w')

check_installer = "rpm"
check_installer_arg_check = "-q"
check_installer_arg_install = "-i"

installer = "dnf"
installer_arg_install = "install"
installer_arg_update = "update"
installer_arg_upgrade = "upgrade"
installer_arg_forced_install = "-y"

installer_snap = "snap"
installer_snap_arg_install = "install"

# adder_key="apt-key"
# adder_add_command="add"
downloader = "wget"
downloader_arg_output = "-O"
downloader_arg_quit = "-q"

installer_text = "Status: install ok installed"

def install_software(software, pre_commands, post_commands, software_extra_argument):
    software_status = subprocess.call([check_installer, check_installer_arg_check, software], stdout=f_null,
                                      stderr=subprocess.STDOUT)
    if not software_status:
        print(software + " allready installed")
    else:
        if pre_commands:
            for pre_command in pre_commands:
                error_extra_command = subprocess.call(pre_command, stdout=f_null, stderr=subprocess.STDOUT)
                if not error_extra_command:
                    print("Extra command of " + software + " executed")
                else:
                    print("Error found on " + software + ": " + str(error_extra_command))
                    return 1

        install_status = subprocess.call([installer, installer_arg_install, installer_arg_forced_install, software])
        software_status = subprocess.call([check_installer, check_installer_arg_check, software], stdout=f_null,
                                          stderr=subprocess.STDOUT)
        if not software_status:
            print(software + "installed")
        else:
            print("Problem was found on " + software + " installation")
            return 1
        if post_commands:
            for post_command in post_commands:
                error_extra_command = subprocess.call(post_command, stdout=f_null, stderr=subprocess.STDOUT)
                if not error_extra_command:
                    print("Extra command of " + software + " executed")
                else:
                    print("Error found on " + software + ": " + str(error_extra_command))
                    return 1
    return 0


def install_software_snap(software, pre_commands, post_commands, software_extra_argument):
    if software_extra_argument is None:
        install_status = subprocess.call([installer_snap, installer_snap_arg_install, software])
    else:
        install_status = subprocess.call(
            [installer_snap, installer_snap_arg_install, software, software_extra_argument])
    if post_commands:
        for extra_command in post_commands:
            error_extra_command = subprocess.call(extra_command, stdout=f_null, stderr=subprocess.STDOUT)
            if not error_extra_command:
                print("Extra command of " + software + " executed")
            else:
                print("Error found on " + software + ": " + str(error_extra_command))
                return 1
    return 0


def install_manual_software(software, software_url):
    software_status = subprocess.call([check_installer, check_installer_arg_check, software], stdout=f_null,
                                      stderr=subprocess.STDOUT)
    if not software_status:
        print(software + " already installed")
    else:
        download_status = subprocess.call([downloader, downloader_arg_output, software + ".deb", software_url])
        install_status = subprocess.call([check_installer, check_installer_arg_install, software + ".deb"])
        software_status = subprocess.call([check_installer, check_installer_arg_check, software], stdout=f_null,
                                          stderr=subprocess.STDOUT)
        if not software_status:
            print(software + "installed")
        else:
            print("Problem was found on " + software + " installation")
            return 1
    return 0


"""def install_thrid_party_software(software, software_key_file, software_key_url, repository_file, repository_url):
    software_status = subprocess.call([check_installer, check_installer_arg_check, software], stdout=FNULL,
                                      stderr=subprocess.STDOUT)
    if not software_status:
        print(software + " already installed")
    else:
        download_status = subprocess.call(
            [downloader, downloader_arg_quit, downloader_arg_output, software_key_file, software_key_url])
        install_key_status = subprocess.call([adder_key, adder_add_command, software_key_file])
        with open(repository_file, 'a') as file:
            file.write(repository_url)
        update_software()
        software_status = subprocess.call([check_installer, check_installer_arg_check, software], stdout=FNULL,
                                          stderr=subprocess.STDOUT)
        if not software_status:
            print(software + "installed")
        else:
            print("Problem was found on " + software + " installation")
            return 1
    return 0
"""


def update_software():
    return subprocess.call([installer, installer_arg_update])


def upgrade_software():
    return subprocess.call([installer, installer_arg_upgrade, installer_arg_forced_install])


def install(software_installation_type, software, pre_commands, post_commands, software_url, software_extra_argument):
    result = 0
    print("Installing " + software + " over " + software_installation_type)
    if software_installation_type is 'manual':
        result = install_manual_software(software, software_url)
    elif software_installation_type is 'snap':
        result = install_software_snap(software, pre_commands, post_commands, software_extra_argument)
    else:
        result = install_software(software, pre_commands, post_commands, software_extra_argument)
    return result


update_software()
upgrade_software()
# install_software(vim_app, None, vim_app, None)


print("Installing apps")


def install_apps():
    """ Software """
    apps_file = open("apps.json")
    apps = json.load(apps_file)
    # Chrome
    chrome_key_url = "https://dl-ssl.google.com/linux/linux_signing_key.pub"
    chrome_key_file = "chrome.key"
    chrome_app = "google-chrome-stable_current_amd64"
    chrome_repository_file = "/etc/apt/sources.list.d/google-chrome.list"
    chrome_repository_url = "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"
    chrome_url = "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
    for app in apps:
        type_installation = app["type"]
        software = app["software"]
        pre_commands = app["pre_commands"]
        post_commands = app["post_commands"]
        url = app["url"]
        extra_argument = app["extra_argument"]
        install(type_installation, software, pre_commands, post_commands, url, extra_argument)


# install(snap_installation_type, snap_app, snap_extra_command, snap_url, snap_extra_argument)
# install(pycharm_installation_type, pycharm_app, pycharm_extra_command, pycharm_url, pycharm_extra_argument)
# install_software(git_app, None, git_app, None)
# install_software(rabbitvcs_cli_app, None, rabbitvcs_cli_app, None)
# install_software(rabbitvcs_nautilus, None, rabbitvcs_nautilus, None)
# install_software(rabbitvcs_nautilux_app, None)
# install_manual_software(vscode_app, vscode_url)
# install_manual_software(chrome_app, chrome_url)
