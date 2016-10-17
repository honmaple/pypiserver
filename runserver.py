#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: runserver.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-09-29 16:10:33 (CST)
# Last Update:THURSDAY 2016-9-29 16:25:24 (CST)
#          By:
# Description:
# **************************************************************************
import pypiserver
from os.path import join

base_path = '/home/arch/pypiserver'
conf = pypiserver.default_config(
    root=join(base_path, 'packages'),
    host='127.0.0.1',
    port=8080,
    password_file=join(base_path, 'password'),
    log_file=join(base_path, 'logs/info.log'),
    welcome_file=None)
application = pypiserver.app(**conf)
