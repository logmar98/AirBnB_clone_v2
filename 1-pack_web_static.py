#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo'''

import os
import time
from fabric.api import local


def do_pack():
    '''generates a .tgz archive from the contents of the web_static'''

    creat_time = time.strftime("%Y%m%d%H%M%S")
    output_filename = f"versions/web_static_{creat_time}.tgz"

    os.makedirs("versions", exist_ok=True)
    
    if local("tar -cvzf {} web_static".format(output_filename)).failed is True:
        return None

    return output_filename
