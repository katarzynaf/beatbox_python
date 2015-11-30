# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:34:40 2015

@author: katarzyna
"""

import scipy.io.wavfile, re
import numpy as np
from tools import key_frequencies, sound

def play_notes(f, keys):
    '''
    play musical notes
    '''
    track = []
    for line in f:
        line = line.split('\n')[0]
        notes = line.split()
        fr = key_frequencies(int(keys[notes[0]]))
        track = np.append(track, sound(fr,2/int(notes[1])))
            
    return(track)
    
def play_sample(f, keys,bmp):
    '''
    play the track
    '''
    t = 44100*60/bmp
    data = f.readlines()
    arr = np.zeros(0)
    n,k = t*len(data), len(data[0].split())
    arr.resize(n, k)
    i=0
    for line in data:
        samples = line.split()
        j=0
        for sample in samples:
            if sample == '--':
                arr[(i*t):((i+1)*t), j] += np.zeros(t)
            else:
                if not bool(re.findall(r'[A-Z]+', sample)):
                    fs,y = scipy.io.wavfile.read('sample/'+sample+'.wav')
                    y = np.mean(y,axis=1)
                    y /= 12767
                else:
                    fr = key_frequencies(int(keys[sample]))
                    y = sound(fr,60/bmp*2)
                arr[(i*t):(len(y)+(i*t)), j] = y[:t*(len(data)-i)]
            j += 1
        i += 1
    track = arr.sum(axis=1)
    return(track)
