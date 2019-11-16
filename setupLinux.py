import os
import subprocess

user = "ironcero"


def setup_wallpaper():
    # Setup wallpaper
    wallpaper_path = "/home/" + user + "/wallpapers"
    wallpaper_file_name = "fedoraWallpaper.png"
    if not os.path.isdir(wallpaper_path):
        subprocess.call(["mkdir", wallpaper_path])
    if not os.path.isfile(wallpaper_path + "/" + wallpaper_file_name):
        subprocess.call(["cp", wallpaper_file_name, wallpaper_path + "/."])

    subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri",
                               "file://" + wallpaper_path + "/" + wallpaper_file_name])
    print("Wallpaper modified")
    return 0


def setup_screenlock():
    # Setup wallpaper
    wallpaper_path = "/home/" + user + "/wallpapers"
    wallpaper_file_name = "fedoraWallpaper.png"
    if not os.path.isdir(wallpaper_path):
        subprocess.call(["mkdir", wallpaper_path])
    if not os.path.isfile(wallpaper_path + "/" + wallpaper_file_name):
        subprocess.call(["cp", wallpaper_file_name, wallpaper_path + "/."])

    subprocess.call(["gsettings", "set", "org.gnome.desktop.screensaver", "picture-uri",
                               "file://" + wallpaper_path + "/" + wallpaper_file_name])
    print("Screen Lock modified")
    return 0


def setup_maximize_buttons():
    subprocess.call(["gsettings", "set", "org.gnome.desktop.wm.preferences", "button-layout",
                     '":minimize,maximize,close"'])
    print("Buttons modified")


def setup_title_height():
    gtk_file_name = "gtk.css"
    gtk_file_path = "/home/" + user + "/.config/gtk-3.0/"
    subprocess.call(["sudo", "-u", user, "cp", gtk_file_name, gtk_file_path + "/."])
    print("Title bar modified")
    print("Press 'ALT' + 'F2' and type 'R' + 'Enter'")


def setup():
    print("Setting up linux system")
    setup_wallpaper()
    setup_screenlock()
    setup_maximize_buttons()
    setup_title_height()


setup()
