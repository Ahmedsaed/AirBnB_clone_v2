#!/usr/bin/python3
"""
Fabric script that generates a tgz archive
from contents of the web_static folder of AirBnB Clone Repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a TGZ archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("version") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except:
        return None
