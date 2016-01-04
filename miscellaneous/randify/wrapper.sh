#! /bin/bash

rm -f rand_stuff.txt
python rand_line.py
cat rand_stuff.txt
RANDSHELL=`head -c 6 rand_stuff.txt`
./spotify play $RANDSHELL
