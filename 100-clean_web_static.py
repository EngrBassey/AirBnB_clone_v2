#!/usr/bin/python3
'''delete clean'''

import os
from datetime import datetime
from fabric.api import *
from os.path import exists
env.user = 'ubuntu'
env.hosts = ['35.153.66.4', '100.25.118.56']

def do_clean(number=0):
    '''clean'''

    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "webstatic" in a]
        archives = sorted(archives)
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
