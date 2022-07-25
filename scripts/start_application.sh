#!/usr/bin/env bash

touch /home/ec2-user/server_file

tee -a /home/ec2-user/server_file <<EOF
leave me here
EOF
