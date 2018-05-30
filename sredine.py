#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simon Šanca: Analiza GNSS in tahimetrične izmere

"""

import numpy as np

#%% 1. Računanje aritmetičnih sredin statičnih opazovanj

file = open("gLAB.txt","r")

fi = [] #enako za e,n,h
la = []
h = []

fi.append([])
la.append([])
h.append([])

jePrvicKin = False;
prejsna = "FGG2";
stevec = 0;

for line in file:
    oznaka = line.split()[0]
    if(prejsna != oznaka and oznaka != "FGG2" and oznaka != "FGG4"):
        jePrvicKin = True;
    if(oznaka == "FGG2" or oznaka == "FGG4"):
        fi[stevec].append(float(line.split()[1]))
        la[stevec].append(float(line.split()[2]))
        h[stevec].append(float(line.split()[3]))
    if(jePrvicKin):
        stevec = stevec + 1;
        fi.append([])
        la.append([])
        h.append([])
        jePrvicKin = False;
    prejsna = oznaka;
    
file.close()
    
fiav = []
laav = []
hav = []

for i in range(stevec):
    
    fi = np.array(fi)    
    la = np.array(la)
    h = np.array(h)
    fiav.append(np.average(fi[i])) #np.average() np.mean() - vseeno
    laav.append(np.average(la[i]))
    hav.append(np.average(h[i]))
    
#FORMATIRANJE IZPISA za izračunane koordinate
dec = "{:.9f}" # fi,lam
dech = "{:.4f}" # h

print("FGG2_1",dec.format(fiav[0]),dec.format(laav[0]),dech.format(hav[0]))
print("FGG2_2",dec.format(fiav[1]),dec.format(laav[1]),dech.format(hav[1]))
print("FGG4_1",dec.format(fiav[2]),dec.format(laav[2]),dech.format(hav[2]))
print("FGG4_2",dec.format(fiav[3]),dec.format(laav[3]),dech.format(hav[3]))

