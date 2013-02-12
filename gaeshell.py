# -*- coding: utf-8 -*-
"""
cd ~/tools
/usr/local/google_appengine/remote_api_shell.py --secure calpdev-hrd

remote_shell> import gaeshell
remote_shell> gaeshell.show_acl_feed(...)

"""
import os
import sys
sys.path.insert(0, os.environ['HOME'] + '/dev/rakumo')
sys.path.insert(0, os.environ['HOME'])

import appengine_config
import fasti.core
fasti.core.startup()

from fasti.login.user import User









