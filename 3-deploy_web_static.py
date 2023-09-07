#!/usr/bin/python3
# creates and distributes an archive to the web servers
from datetime import datetime
from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import local
from os.path import isfile, isdir
import os

env.hosts = ["34.202.157.122", "100.27.2.78"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_pack():
    """generates a TGZ archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    if isdir("version") is False:
        if local("mkdir -p versions").failed is True:
            return None
    file_name = "versions/web_static_{}.tgz".format(date)
    if local(f"tar -cvzf {file_name} web_static").failed is True:
        return None
    return file_name


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False

    return True


def deploy():
    """creates and distributes an archive to the web servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
