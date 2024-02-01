#!/usr/bin/python3
'''Write a Fabric script that distributes an archive to your web servers'''

import os
from fabric.api import env
from fabric.api import put
from fabric.api import run


env.hosts = ["54.158.192.143", "54.152.58.19"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): path of archive to distribute.
    Returns:
        If file doesn't exist at archive_path or error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    file_name = file.split(".")[0]

    try:
        put(archive_path, "/tmp/{}".format(file))
        run("rm -rf /data/web_static/releases/{}/".
            format(file_name))
        run("mkdir -p /data/web_static/releases/{}/".
            format(file_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file, file_name))
        run("rm /tmp/{}".format(file))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".
            format(file_name, file_name))
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(file_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(file_name))
        return True
    except Exception as e:
        return False
