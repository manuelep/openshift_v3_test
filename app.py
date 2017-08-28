#!/usr/bin/env python

import os
import sys

os.environ['WEB2PY_PATH'] = "/opt/app-root/src"

sys.path.append(os.path.join(os.environ['WEB2PY_PATH'], 'web2py'))
sys.path.append(os.path.join(os.environ['WEB2PY_PATH'], 'web2py', 'gluon'))

WEB2PY_LOG = os.path.join("/", 'web2py.log')

from gluon.settings import global_settings
import gluon.main

application = gluon.main.appfactory(
    wsgiapp = gluon.main.wsgibase,
    logfilename = WEB2PY_LOG,
    profilerfilename = None
)
