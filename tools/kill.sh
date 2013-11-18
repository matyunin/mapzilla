#!/bin/bash

BASEDIR=$(dirname $0)/..

kill -9 $(ps -aux | grep uwsgi.*mapzilla | awk '{print $2}')
rm -rf $BASEDIR/tmp/mapzilla_uwsgi.sock
