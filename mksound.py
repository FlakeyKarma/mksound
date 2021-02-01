#!/bin/python2.7

import numpy as N
from scipy.io.wavfile import write
import random

#Samples per sec
S = 44100

#Frequency presets
chords = {
	'C0':16.35,\
	'D0':18.35,\
	'E0':20.6,\
	'F0':21.83,\
	'G0':24.5,\
	'A0':27.5,\
	'B0':30.87,\
	'C1':32.7,\
	'D1':36.71,\
	'E1':41.2,\
	'F1':43.65,\
	'G1':49.0,\
	'A1':55.0,\
	'B1':61.74,\
        'C2':65.41,\
	'D2':73.42,\
	'E2':82.41,\
	'F2':87.31,\
	'G2':98.0,\
	'A2':110.0,\
	'B2':123.47,\
	'C3':130.81,\
	'D3':146.83,\
	'E3':164.81,\
	'F3':174.61,\
	'G3':196.0,\
	'A3':220.0,\
	'B3':246.94,\
	'C4':261.63,\
	'D4':293.66,\
	'E4':329.63,\
	'F4':349.23,\
	'A' :440.0,\
	'B' :493.0,\
	'Bb':466.164,\
	'Cn':523.3,\
	'C' :261.6,\
	'Dn':587.4,\
	'D' :293.7,\
	'E' :329.7,\
	'F' :349.2,\
	'G' :392.0
}

#Could be either randomly selected from chords in dict, or just randomly selected in Hz from 50Hz(Low) to 500Hz(High), just a general range. I recommend looking at speaker limits before entering personal ranges lol.
#hz = chords[random.choice([i for i in chords])]
hz = random.uniform(50.0, 500.0)

#Duration
D = random.uniform(0.2, 0.5)


#Establish array based on duration and sampling rate
sample_num = N.arange(D*S)

WF = []

def makeNote(WF, amp, hz, D, S):
    return N.append(WF, amp * N.sin(2 * N.pi * N.arange(D * S) * hz / S))

#Set first value
WF = makeNote(WF, 1, hz, D, S)

#Random sound generation that intensifies with each iteration!
for i in range(random.randint(9, 25)):
    print(hz, D)
    hz = random.uniform(50.0, 500.0)
    D = random.uniform(0.2, 0.5)
    WF = makeNote(WF, i, hz, D, S)


WF_integerz = N.int16(WF * 32767)

#Finally, write to WAV file.
write('OUTPUT.wav', S, WF_integerz)
