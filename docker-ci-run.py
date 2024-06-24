#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2024 Shlomi Fish < https://www.shlomifish.org/ >
#
# Licensed under the terms of the MIT license.

"""

Work-in-Progress docker-based CI program.

"""

import docker
client = docker.from_env()
images = client.images
if False:
    image = images.pull('fedora:40')
    images.prune(image)
bash_code = """
set -e -x
# sudo -H bash -e -x -c 'dnf install -y git'
seq 1 10
expr 12 + 12
dnf install -y git
git clone https://github.com/shlomif/primesieve-python
"""
if True:
    ret = client.containers.run(
        'fedora:40',
        ["bash", "-c", bash_code, ],
        detach=False,
        stream=True,
    )
else:
    pass
    # ret = container.exec_run(
    # ["bash", "-c", bash_code], stdout=True, stderr=True, )
print(ret.output.decode('utf-8'))
print(ret)

listt = client.containers.list()
print(listt)
