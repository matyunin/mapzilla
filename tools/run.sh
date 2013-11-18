#!/bin/bash

uwsgi --plugin python2 --socket ../tmp/uwsgi.sock --wsgi-file ../mapzilla.py --callable app --processes 4 --threads 2 --uid redneck --master
mkdir -p ../tmp
chmod 0665 ../tmp/uwsgi.sock
