#!/bin/bash

BASEDIR=$(dirname $0)/..

uwsgi --plugin python2 --socket $BASEDIR/tmp/uwsgi.sock --wsgi-file $BASEDIR/mapzilla.py --callable app --processes 4 --threads 2 --uid redneck --master

chmod 0665 $BASEDIR/tmp/uwsgi.sock
