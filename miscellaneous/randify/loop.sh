#! /bin/bash

set $SPOT_STATUS=`./spotify status`
if SPOT_STATUS="Spotify is currently paused."
then
rm -f rand_stuff.txt
python rand_line.py
cat rand_stuff.txt
RANDSHELL=`head -c 5 rand_stuff.txt`
./spotify play artist $RANDSHELL
else
  sleep 45
fi
