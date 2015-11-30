# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 02:27:09 2015

@author: katarzyna
"""

import numpy as np
import scipy.io.wavfile,scipy.signal    

def unzipto(zip_file):
    '''
    temporarily unzipping
    '''
    import zipfile
    with zipfile.ZipFile(zip_file) as zf:
        zf.extractall('/var/tmp/')
        
def key_frequencies(n):
    '''
    calculating frequencies of musical notes
    n - key number (see freq.csv)
    '''
    f = 2**((n-49)/12)*440 # Hz
    return(f)

def sound(f, T, a=.05, d=.05):
    '''
    make a T-sec noise with the f - frequency of waves.
    '''
    n = T*44100
    t = np.linspace(0, T, n)
    y = np.sin(2*np.pi*f*t+.1)+1*scipy.signal.sawtooth(2*np.pi*f*t)
    y[0:int(n*a)] *= np.linspace(0,1,int(n*a))
    y[-int(n*d):-1] *= np.linspace(1,0,int(n*d)-1)
    return(y)
