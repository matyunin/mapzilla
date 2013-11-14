#!/bin/bash
kill -9 $(ps -aux | grep uwsgi.*mapzilla | awk '{print $2}')
rm -rf /tmp/mapzilla_uwsgi.sock
