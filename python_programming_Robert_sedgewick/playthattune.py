# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 15:31:12 2024

@author: Lenovo
"""
import sys
sys.path.append('C:\\Users\\Lenovo\\Downloads\\introcs-1.0')
import math 
import stdarray 
import stdaudio 
import stdio
import numpy

SPS = 44100 
CONCERT_A = 440.0
while not stdio.isEmpty(): 
    pitch = stdio.readInt() 
    duration = stdio.readFloat() 
    hz = CONCERT_A * (2 ** (pitch / 12.0)) 
    n = int(SPS * duration) 
    samples = stdarray.create1D(n+1, 0.0) 
    for i in range(n+1): 
        samples[i] = math.sin(2.0 * math.pi * i * hz / SPS) 
    stdaudio.playSamples(samples) 
stdaudio.wait()