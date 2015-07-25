#!/bin/bash
#export LANG=C.UTF-8

# A monitor script for bot that restarts bot if it crashes. Only for production use.

control_c() {
    kill -9 $PID
    exit
}

trap control_c SIGINT

until python bot.py; do
    PID=$!
    echo "'bot.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
