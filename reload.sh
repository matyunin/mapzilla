#!/bin/bash

mkdir -p ./logs

chmod +x ./tools/kill.sh
chmod +x ./tools/run.sh
chmod +x ./tools/mongo.sh

./tools/kill.sh
sudo nginx -s reload
nohup ./tools/run.sh &
