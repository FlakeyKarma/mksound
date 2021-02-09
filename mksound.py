#!/bin/python2.7

import numpy as N
from scipy.io.wavfile import write
import threading,random,os

#Make note with the amplification level, frequency, duration(seconds), and number of samples per second to occur
def addNote(freq, wave_form=None, amp=1, duration=0.5, sampling_rate=44100):
    if wave_form is None:
        wave_form = []
    
    return N.append(wave_form, amp * N.sin(2 * N.pi * N.arange(duration * sampling_rate) * freq / sampling_rate))

#Finally, write to WAV file.
def fileWrite(wave_form):
    write('OUTPUT.wav', S, N.int16(wave_form * 32767))



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

def guitarTabz(fret, string_to_play, fret_count=19):
    #Guitar strings - credit: https://www.google.com/url?sa=i&url=http%3A%2F%2Fdanielchoy.blogspot.com%2F2017%2F02%2Fguitar-strings-frequency-chart-guitar.html&psig=AOvVaw076iywIyPiC7cB42Z3KWVJ&ust=1612553746158000&source=images&cd=vfe&ved=0CAMQjB1qFwoTCICwjo390O4CFQAAAAAdAAAAABAD
    '''
    guitar_strings = {
            'E':82.407,\
            'A':110.0,\
            'D':146.832,\
            'G':195.998,\
            'B':246.942,\
            'e':329.628
            }
    '''
    old_strings = {
            'E':112.407,\
            'A':140.0,\
            'D':176.832,\
            'G':225.998,\
            'B':276.942,\
            'e':359.628
            }
    guitar_strings = {}
    for i in old_strings:
        guitar_strings[i] = old_strings[i] + 64
    string_list = [guitar_string for guitar_string in guitar_strings]

    #Get frequency increase level
    f_inc = guitar_strings[string_list[string_list.index(string_to_play)+1]] - guitar_strings[string_to_play] + 20 if (string_to_play != 'e') else 102

    #Get estimated value by dividing the fret by the fret_count to get desired pitch, multiplying by f_inc to get increased value
    return ((fret/fret_count) * f_inc + guitar_strings[string_to_play])

def testRun(S):
    #Could be either randomly selected from chords in dict, or just randomly selected in Hz from 50Hz(Low) to 500Hz(High), just a general range. I recommend looking at speaker limits before entering personal ranges lol.
    #hz = chords[random.choice([i for i in chords])]
    hz = random.uniform(50.0, 500.0)

    #Duration
    D = random.uniform(0.2, 0.5)


    #Establish array based on duration and sampling rate
    sample_num = N.arange(D*S)

    WF = []

    #Set first value
    #WF = addNote(WF, 1, hz, D, S)

    #Random sound generation that intensifies with each iteration!
    for i in range(random.randint(9, 25)):
        #print(hz, D)
        hz = random.uniform(50.0, 500.0)
        D = random.uniform(0.2, 0.5)
        WF = addNote(wave_form=WF, amp=i, freq=hz, duration=D, sampling_rate=S)
    fileWrite(WF)

#Make a "song" based on frequency list, duration list, and amplification list
def makeSong(freq_list, duration_list, amp_list, repeatz=1):
    wave_form = []
    for i in range(repeatz):
        for j in range(len(freq_list)):
            wave_form = addNote(freq_list[j], wave_form, amp=amp_list[j], duration=duration_list[j])
    return wave_form

#freq_list is list of frequencies to go through, next repeatz is the number of times to repeat sequence. The point of this is to create a same-tempo audio sample list
def makeBeat(freq, duration=0.2, amp=0.5, repeatz=1):
    fl = []
    for i in range(repeatz):
        fl += [freq, 0.0]
    wave_form = makeSong(fl, [duration for i in range(repeatz*2)], [amp for i in range(repeatz*2)], repeatz)
    return wave_form 
#fileWrite(makeBeat(random.uniform(200.0, 500.0), repeatz=2)))

#Display problem and quit alarm when input is correct
def run():
    a_th = threading.Thread(target=alarmThread)
    p_th = threading.Thread(target=prblmThread)
    a_th.start()
    p_th.start()

#Alarm function to run
def alarmThread():
    while True:
        testRun(S)
        os.system("lame -b 320 OUTPUT.wav 1>/dev/null 2>/dev/null")
        os.system("mpg123 OUTPUT.mp3 1>/dev/null 2>/dev/null")

#Display problem
def prblmThread():
    while True:
        inc = raw_input('A> ')
        if inc == 'a':
            os.system("killall python2.7")
            os.system("killall mpg123")
            break

run()
