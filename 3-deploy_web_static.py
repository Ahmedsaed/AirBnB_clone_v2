#!/usr/bin/python3
# fabric file create and distribute an archive to web server

from datetime import datetime
from fabric.api import local,env,put,run
import os.path
from os.path import isdir


def do_pack():
    """generates a TGZ archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("version") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
    
def do_deploy(archive_path):
    """Distributes archive to web server"""
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -c /data/web_static/releases/{}/".format(file,name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web/web_static/release/{}/".format(name,name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed is True:
        return False
    return True


def deploy():
    """Create & distribute an archive to a web server"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
