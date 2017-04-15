#!/bin/bash

echo "starting virtual env"
. ./venv/bin/activate

echo "starting mongod"
mongod --fork --config /usr/local/etc/mongod.conf

echo "starting flask"
./run.py
