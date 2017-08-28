#!/usr/bin/env python

import os
import sys

os.environ['THIS_APP_PATH'] = "/opt/app-root/src"

os.environ['web2py_path'] = os.path.join(os.environ['THIS_APP_PATH'], 'web2py')

sys.path.append(os.environ['web2py_path'])
sys.path.append(os.environ['web2py_path'], 'gluon'))

WEB2PY_LOG = os.path.join(os.environ['THIS_APP_PATH'], 'log', 'web2py.log')

from gluon.settings import global_settings
import gluon.main

application = gluon.main.appfactory(
    wsgiapp = gluon.main.wsgibase,
    logfilename = WEB2PY_LOG,
    profilerfilename = None
)
