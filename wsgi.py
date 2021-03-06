#!/usr/bin/env python

import os
import sys

os.environ['THIS_APP_PATH'] = "/opt/app-root/src"

os.environ['web2py_path'] = os.path.join(os.environ['THIS_APP_PATH'], 'wsgi', 'web2py')

sys.path.append(os.environ['web2py_path'])
sys.path.append(os.path.join(os.environ['web2py_path'], 'gluon'))

WEB2PY_LOG = os.path.join(os.environ['THIS_APP_PATH'], 'log', 'web2py.log')

from gluon.settings import global_settings
from gluon.main import appfactory

application = appfactory(logfilename = WEB2PY_LOG)
