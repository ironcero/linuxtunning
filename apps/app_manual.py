import subprocess
import os
import logging

f_null = open(os.devnull, 'w')

check_installer = "rpm"
check_installer_arg_check = "-q"
check_installer_arg_install = "-i"

downloader = "wget"
downloader_arg_output = "-O"
downloader_arg_quit = "-q"


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
