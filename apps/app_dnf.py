import subprocess
import os
import logging

f_null = open(os.devnull, 'w')

check_installer = "rpm"
check_installer_arg_check = "-q"
check_installer_arg_install = "-i"

installer = "dnf"
installer_arg_install = "install"
installer_arg_group_install = "groupinstall"
installer_arg_update = "update"
installer_arg_upgrade = "upgrade"
installer_arg_forced_install = "-y"


def install_software(name, description, software_check, software, pre_commands, post_commands, software_extra_pre_argument, software_extra_post_argument,
                     install_group):
    logging.debug("Checking %s is installed on system", name)
    software_status = subprocess.call([check_installer, check_installer_arg_check, software_check], stdout=f_null,
                                      stderr=subprocess.STDOUT)
    if not software_status:
        logging.info("%s is already installed", name)
    else:
        installer_install = ""
        if install_group:
            installer_install = installer_arg_group_install
        else:
            installer_install = installer_arg_install

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
            install_status = subprocess.call([installer, installer_install, software])
        elif software_extra_pre_argument is None:
            install_status = subprocess.call(
                [installer, installer_install, software_extra_pre_argument, software])
        elif software_extra_post_argument is None:
            install_status = subprocess.call(
                [installer, installer_install, software, software_extra_post_argument])
        else:
            install_status = subprocess.call(
                [installer, installer_install, software_extra_pre_argument, software,
                 software_extra_post_argument])

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


def update_software():
    logging.info("Updating DNF local repositories from remote")
    result = subprocess.call([installer, installer_arg_update])
    if not result:
        logging.info("DNF local repositories updated successful")
    else:
        logging.error("Error found updating DNF local repositories")

    return result


def upgrade_software():
    logging.info("Upgrading system (over DNF repositories)")
    result = subprocess.call([installer, installer_arg_upgrade, installer_arg_forced_install])
    if not result:
        logging.info("System upgraded successful")
    else:
        logging.error("Error found upgrading system")

    return result
