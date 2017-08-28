#!/usr/bin/env python

import os
import sys

virtenv = os.environ['APPDIR'] + '/virtenv/'
os.environ['web2py_path'] = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'web2py') 

sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'web2py'))
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'web2py', 'gluon'))
sys.path.append(os.path.join(virtenv, 'lib/python2.6/site-packages'))

WEB2PY_LOG = os.path.join(os.environ['OPENSHIFT_LOG_DIR'],'web2py.log')
#SQLITE_DIR = os.path.join(os.environ['OPENSHIFT_DATA_DIR'],'databases')
NEWRELIC_INI = os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'web2py', 'newrelic.ini')

os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.6/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')

try:
    execfile(virtualenv, dict(__file__=virtualenv))
except:
    pass


from gluon.settings import global_settings
import gluon.main

application = gluon.main.appfactory(wsgiapp=gluon.main.wsgibase,
                                    logfilename=WEB2PY_LOG,
                                    profilerfilename=None)

#NewRelic Monitoring
#import newrelic.agent 
#newrelic.agent.initialize(NEWRELIC_INI)

#application = newrelic.agent.wsgi_application()(application)
