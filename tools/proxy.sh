#!/usr/bin/env python

# Import base

import os, sys, sh, datetime

# Setup environment

basedir = os.path.abspath(__file__ + '/../..')
sys.path.append(basedir)

git = sh.git.bake(_cwd='%s/db/proxy' % basedir)
git.init()

time = datetime.datetime.now()

# Import proxy classes

from grabber.proxies.hidemyass import *

# Start grabbing and saving

print 'Getting proxy list from HideMyAss.com'

proxy = MzProxyHidemyass()
print proxy.get_json_path()
proxy.parse()
proxy.save_json()

# Fix changes

git.add('.')
git.commit(m='Update for HideMyAss.com at %s' % time)