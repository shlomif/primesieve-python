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
container = client.containers.run(
    'fedora:40',
    "bash -c 'set -x ; sleep 10'",
    detach=True,
)
listt = client.containers.list()
print(listt)
assert len(listt) > 0
