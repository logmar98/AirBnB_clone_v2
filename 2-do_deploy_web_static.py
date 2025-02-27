#!/usr/bin/python3
'''Write a Fabric script that distributes an archive to your web servers'''

import os
from fabric.api import env
from fabric.api import put
from fabric.api import run


env.hosts = ['54.158.192.143', '54.152.58.19']


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): path of archive to distribute.
    Returns:
        If file doesn't exist at archive_path or error occurs - False.
        Otherwise - True.
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        return False
