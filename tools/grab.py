#!/usr/bin/env python

# Import base

import os
import sys

basedir = os.path.abspath(__file__ + '/../..')
sys.path.append(basedir)

from grabber.grabber import *

# Start grabbing and saving

grabber = MzGrabber()
grabber.grab()