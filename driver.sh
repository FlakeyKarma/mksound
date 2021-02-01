#!/bin/bash

./bin/python2.7 mksound.py 2>/dev/null
lame -b 320 OUTPUT.wav 2>/dev/null
mpg123 OUTPUT.mp3
