#!/bin/bash
#
#  $1 scp file (train/eval/valid) 
#  $2 target location for a wav file
#  $3 output rate (resample!)
#
#

sox -t raw -r 16000 -b 16 -e signed-integer $1 -t raw -r 8000 -c 1 -b 16 --encoding signed-integer $2 speed $3

