# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:53:01 2015

@author: katarzyna

"""
   
import csv,scipy.io.wavfile
import numpy as np
import os
from play import play_sample, play_notes 

    
def play_track(XY, song):
    '''
    XY - for number of a track as a string of 2 characters.
    song - song name
    '''
    with open('freq.csv','r') as dest_f:
        data_iter = csv.reader(dest_f,
                               delimiter = ';', 
                               quotechar = '"')
        keys = dict([ [data[1],data[0]] for data in data_iter])
    f = open('defs.txt','r')
    defs = eval(f.read())
    bmp = defs['bmp']
    fs = 44100
#    t = fs*(60/bmp)  # time for one line
    filename = song+'/track'+XY+'.txt'
    with open(filename, 'r') as f:
        x = f.readline()
        x = x.split('\n')[0]
        if x == '# notes':
            track = play_notes(f,keys)
        else:
            track = play_sample(f,keys,bmp)
        scipy.io.wavfile.write('/var/tmp/test.wav',
                               fs,
                               np.int16(track/max(np.abs(track))*2767))
        os.system("aplay /var/tmp/test.wav")
 
if __name__ == '__main__':
    import sys
    if not 2 < len(sys.argv) < 4 :
        print('Pass arguments: XY - track number, song - song name')
        sys.exit(1)         
    else:
        play_track(sys.argv[1], sys.argv[2])
