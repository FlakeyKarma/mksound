#!/bin/bash

for i in {1..10}; do
	./bin/python2.7 mksound.py;
	lame -b 320 OUTPUT.wav 1>/dev/null 2>/dev/null;
	mpg123 OUTPUT.mp3 1>/dev/null 2>/dev/null;
	echo "Done with $i";
done;
