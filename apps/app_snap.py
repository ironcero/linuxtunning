import subprocess
import os
import logging

f_null = open(os.devnull, 'w')

installer_snap = "snap"
installer_snap_arg_install = "install"

check_installer = "snap"
check_installer_arg_check = "info"


def install_software_snap(name, description, software_check, software, pre_commands, post_commands,
                          software_extra_pre_argument, software_extra_post_argument):
    logging.debug("Checking %s is installed on system", name)
    software_status = subprocess.call([check_installer, check_installer_arg_check, software_check], stdout=f_null,
                                      stderr=subprocess.STDOUT)
    if not software_status:
        logging.info("%s is already installed", name)
    else:
        if pre_commands:
            logging.debug("Executing commands before installation of %s", name)
            for pre_command in pre_commands:
                error_extra_command = subprocess.call(pre_command, stdout=f_null, stderr=subprocess.STDOUT)
                if not error_extra_command:
                    logging.info("Extra command %s executed", pre_command)
                else:
                    logging.error("Error found executing command %s: %s", pre_command, error_extra_command)
                    return 1

        if software_extra_post_argument is None and software_extra_pre_argument is None:
            install_status = subprocess.call([installer_snap, installer_snap_arg_install, software])
        elif software_extra_post_argument is None:
            install_status = subprocess.call(
                [installer_snap, installer_snap_arg_install, software_extra_pre_argument, software])
        elif software_extra_pre_argument is None:
            install_status = subprocess.call(
                [installer_snap, installer_snap_arg_install, software, software_extra_post_argument])
        else:
            install_status = subprocess.call([installer_snap, installer_snap_arg_install, software_extra_pre_argument,
                                              software, software_extra_post_argument])

        software_status = subprocess.call([check_installer, check_installer_arg_check, software_check], stdout=f_null,
                                          stderr=subprocess.STDOUT)

        if not software_status:
            logging.info("%s was installed successful", software)
            if post_commands:
                logging.debug("Executing commands after installation of %s", name)
                for post_command in post_commands:
                    error_extra_command = subprocess.call(post_command, stdout=f_null, stderr=subprocess.STDOUT)
                    if not error_extra_command:
                        logging.info("Extra command %s executed", post_command)
                    else:
                        logging.error("Error found executing command %s: %s", post_command, error_extra_command)
                        return 1

        else:
            logging.error("Error found installing %s ", software)
            return 1

    return 0
