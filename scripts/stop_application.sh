#!/usr/bin/env bash

touch /home/ec2-user/stop_application

tee -a /home/ec2-user/stop_application <<EOF
Server Stoppped
EOF
