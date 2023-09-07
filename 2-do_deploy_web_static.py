#!/usr/bin/python3
# Fabric file to distribute archive to a web server
import os.path
from fabric.api import env,put,run

env_hosts = ["34.202.157.122","100.27.2.78"]

def do_depoly(archive_path):
    """Distributes archive to web server"""
    if os.path.isfile(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, f"/tmp/{file}").failed is True:
        return False
    if run(f"rm -rf /data/web_static/releases/{name}/").failed is True:
        return False
    if run(f"mkdir -p /data/web_static/releases/{name}/").failed is True:
        return False
    if run(f"tar -xzf /tmp/{file} -c /data/web_static/releases/{name}/").failed is True:
        return False
    if run(f"rm /tmp/{file}").failed is True:
        return False
    if run(f"mv /data/web_static/releases/{name}/web_static/* "
           f"/data/web_static/release/{name}/").failed is True:
        return False
    if run(f"rm -rf /data/web_static/releases/{name}/web_static").failed is True:
        return False
    if run(f"rm -rf /data/web_static/current").failed is True:
        return False
    if run(f"ln -s /data/web_static/releases/{name}/ /data/web_static/current").failed is True:
        return False
    return True
