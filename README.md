# linuxtunning

Linux Scripts for tunning a Linux base system.

## Summary

Scripts must setup look configuration and add new software. All configuration and software will be orientated to a java development environment.

## Usage

1. Once you downloaded this repository you will need to setup the scripts. 
	* On config folder you can find only one file for setup: logger\_config.yml which lets you to setup logging options. But you could add a custom file named secrets.json if you need to add credential information. For example: [{"name":"oracle-jdk", "user":"SOME\_USER", "password":"SOME\_PASSWORD"}]
	* On apps folder you can find apps.json file. This file lets you change which application will be installed on your system. In further section you can find more information for this file.
	* On base folder you can find setupLinux.py. This file will change as your system looks and feels. You could change this file if you want a another style on your system.
2. After setup the scripts you could run it launching python tunningLinux.py on the base folder (on terminal).

## apps.json file
apps.json file is the heard of configuration for these scripts. This file lets you add, remove of change which application will be installed on your system. 4 types of installation have been added: manual, snap, yum and dnf (by default). Then, if you want to add a new dnf application you will need to setup as dnf type.

Here you could find one sample:

<pre><code>
{
    "name": "Visual Studio Code",
    "description": "Visual Studio Code is a source-code editor developed by Microsoft for Windows, Linux and macOS",
    "software_check": "code",
    "software": "code",
    "type": "default",
    "pre_commands": [
      [
        "rpm",
        "--import",
        "https://packages.microsoft.com/keys/microsoft.asc"
      ],
      [
        "cp",
        "vscode.repo",
        "/etc/yum.repos.d/vscode.repo"
      ],
      [
        "dnf",
        "check-update"
      ]
    ],
    "post_commands": null,
    "url": null,
    "extra_pre_argument": null,
    "extra_post_argument": null,
    "install_group": false
  }
</code></pre>

1. "name": This is the name that you put to application, not necessary the official name of application.
2. "description": Again, this is the description that you put to application.
3. "software\_check": This is the name used for test if this application has been installed on the system previously. Depends on the type of installation the script will check in one o other way. For example, for dnf type the script will check a command like this: <code>rpm -q software_check</code>
4. "software": This is the name used for install this application. Again, depends on the type of installation. For dnf type the script will install the application using a command like this: <code>dnf install -y software</code>
5. "type": This is the type of installation. You will need to put: manual, snap, yum or default (dnf).
6. "pre\_commands": Pre\_commands are a list of tasks which will be executed before your application will be installed.
7. "post\_commands": Post\_commands are a list of tasks which will be executed after your application will be installed.
8. "url": URL parameter will be used only for manual type installation. Is the URL where software will be downloaded.
9. "extra\_pre\_argument": These are a list of arguments which will be added before software word in the installation command. If you add "-t" parameter in these list, in example the result command will be: <code>dnf install -y -t software</code>
10. "extra\_post\_argument": These list is similar that the previous parameter ("extra\_pre\_commands"), but in this case the parameters will be added at the end. For example: <code>dnf install -y software -t</code>
11. "install_group": This parameter is special. Only works in dnf type and lets you change "install" to "groupinstall" on dnf command. It's necessary for some special software.

## Logs

## Linux version

