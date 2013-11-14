#!/bin/bash
./kill.sh
sudo nginx -s reload
nohup ./run.sh &
