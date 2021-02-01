#!/bin/bash

for i in {0..10}; do
	echo "Starting $i";
	./bin/python2.7 mksound.py # > "SOUND_LIST_$(date  | cut -d' ' -f5,6,7)$i.txt";
	lame -b 320 OUTPUT.wav 1>/dev/null 2>/dev/null;
	mpg123 OUTPUT.mp3 1>/dev/null 2>/dev/null;
	echo "Done with $i";
done;
