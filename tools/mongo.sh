#!/bin/bash

BASEDIR=$(dirname $0)/..
MONGO_PATH="/Applications/mongodb-osx-x86_64-2.4.8/bin"
MONGO_PID=$(ps -a | grep mongod | awk '{print $1}')

echo "Stoping MongoDB..."

kill -2 $MONGO_PID

echo "Running MongoDB..."

$MONGO_PATH/mongod --nojournal --dbpath $BASEDIR/db/mongo/ >> $BASEDIR/logs/mongo.log &