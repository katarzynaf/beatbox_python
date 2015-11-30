# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:05:37 2015

@author: katarzyna
"""

from play_track import play_track

def play_song(utwor):
    song = open(utwor+'/song.txt', 'r')
    for track in song:
        track = track.split()[0]
        play_track(track,utwor)
        
if __name__ == '__main__':
    import sys,re
    if len(sys.argv) != 2 :
        print('Pass a song name')
        sys.exit(1)         
    else:
        if not bool(re.search('.zip', sys.argv[1])):
            play_song(sys.argv[1])
        else:
            from tools import unzipto
            s = sys.argv[1]
            song_name = s.split('.',1)[0]
            unzipto(sys.argv[1])
            play_song('/var/tmp/'+song_name)
