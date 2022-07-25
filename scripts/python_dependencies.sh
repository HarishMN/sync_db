#!/usr/bin/env bash
chown ec2-user:ec2-user /home/ec2-user/www
python3 -m venv /home/ec2-user/www/env
chown ec2-user:ec2-user /home/ec2-user/www/env
chown ec2-user:ec2-user /home/ec2-user/www/env/*
source /home/ec2-user/www/env/bin/activate
