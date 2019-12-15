import os
import json
from apps.app_dnf import update_software
from apps.app_dnf import upgrade_software
from apps.app_dnf import install_software
from apps.app_yum import install_software_yum
from apps.app_snap import install_software_snap
from apps.app_manual import install_manual_software
import logging
#import sys
#sys.path.insert(1, '../config')
import config.settings

appsFile = "apps/apps.json"
f_null = open(os.devnull, 'w')
installer_text = "Status: install ok installed"


def install(software_installation_type, name, description, software_check, software, pre_commands, post_commands,
            software_url, software_extra_pre_argument, software_extra_post_argument, install_group):
    result = 0
    logging.info("Installing %s over %s", name, software_installation_type)
    if software_installation_type == 'manual':
        result = install_manual_software(software, software_url)
    elif software_installation_type == 'snap':
        result = install_software_snap(name, description, software_check, software, pre_commands, post_commands,
                                               software_extra_pre_argument, software_extra_post_argument)
    elif software_installation_type == 'yum':
        result = install_software_yum(name, description, software_check, software, pre_commands, post_commands,
                                             software_extra_pre_argument, software_extra_post_argument)
    else:
        result = install_software(name, description, software_check, software, pre_commands, post_commands,
                                         software_extra_pre_argument, software_extra_post_argument, install_group)
    return result


# install_software(vim_app, None, vim_app, None)

def install_apps():
    logging.info("Installing apps")
    """ Software """
    apps_file = open(appsFile)
    logging.debug("File %s get.", appsFile)
    applications = json.load(apps_file)
    logging.debug("File %s loaded on JSON format", appsFile)
    update_software()
    upgrade_software()
    for app in applications:
        name = app["name"]
        description = app["description"]
        software_check = app["software_check"]
        type_installation = app["type"]
        software = app["software"]
        pre_commands = app["pre_commands"]
        post_commands = app["post_commands"]
        url = app["url"]
        extra_pre_argument = app["extra_pre_argument"]
        extra_post_argument = app["extra_post_argument"]
        install_group = app["install_group"]
        install(type_installation, name, description, software_check, software, pre_commands, post_commands, url, extra_pre_argument, extra_post_argument, install_group)


install_apps()
