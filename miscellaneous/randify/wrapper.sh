#! /bin/bash

rm -f rand_stuff.txt
python rand_line.py
cat rand_stuff.txt
RANDSHELL=`cat rand_stuff.txt`
./spotify play $RANDSHELL
