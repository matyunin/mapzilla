#!/bin/bash

BASEDIR=$(dirname $0)/.

mkdir -p $BASEDIR/logs
mkdir -p $BASEDIR/tmp
mkdir -p $BASEDIR/db/mongo/

chmod +x $BASEDIR/tools/kill.sh
chmod +x $BASEDIR/tools/run.sh
chmod +x $BASEDIR/tools/mongo.sh

$BASEDIR/tools/kill.sh
sudo nginx -s reload >> $BASEDIR/logs/nginx.log
nohup $BASEDIR/tools/run.sh &
