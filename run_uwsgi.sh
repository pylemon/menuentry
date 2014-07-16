#!/bin/sh
kill -9 `cat /tmp/menuentry.pid`
/home/ubuntu/Envs/menuentry/bin/uwsgi --ini ./menuentry/uwsgi.ini --static-map /static=/home/ubuntu/menuentry/static/
