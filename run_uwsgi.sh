#!/bin/sh
kill -9 `cat /tmp/menuentry.pid`
uwsgi --ini ./menuentry/uwsgi.ini
