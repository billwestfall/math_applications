#! /bin/bash

rm -f rand_stuff.txt
python rand_line.py
cat rand_stuff.txt
unset RAND_NUM
unset RANDSHELL
unset RAND_ALB
# add in random chance to take characters from head or tail of term
RAND_NUM=$((( RANDOM % 2 ) + 1 ))
if [ "$RAND_NUM" = 2 ]; then
RANDSHELL=`head -c 5 rand_stuff.txt`
else
RANDSHELL=`tail -c 5 rand_stuff.txt`
fi
# add in one out of twenty chance to play whole album
RAND_ALB=$((( RANDOM % 20 )))
if [ "$RAND_ALB" = 15 ]; then
./spotify play album $RANDSHELL
else
./spotify play $RANDSHELL
fi
sleep 2
./spotify status
