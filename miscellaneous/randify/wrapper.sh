#! /bin/bash

rm -f rand_stuff.txt
python rand_line.py
cat rand_stuff.txt
unset RAND_NUM
unset RANDSHELL
RAND_NUM=$((( RANDOM % 2 ) + 1 ))
if [ "$RAND_NUM" = 2 ]; then
RANDSHELL=`head -c 5 rand_stuff.txt`
else
RANDSHELL=`tail -c 5 rand_stuff.txt`
fi
./spotify play $RANDSHELL
sleep 4
./spotify status
