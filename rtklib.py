#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#%% 1. BRANJE PODATKOV

praz1 = [] #magicGNSS

#2D
file = open("rtklib2D.txt", "r")

for line in file:
    praz1.append(line.split()[1])
praz1 = np.array(praz1)
praz1 = praz1.astype(np.float)

file.close()

#VISINE

dH = [] #csrs

file = open("rtklib_dH.txt", "r")

for line in file:
    dH.append(line.split()[1])
dH = np.array(dH)
dH = dH.astype(np.float)

file.close()

#%% 2. IZRIS PORAZDELITVE NAPAKE MED IZMERO - barchart, matplotlib

st_op1 = [] #spremeni, ko prebereš drugo datoteko
vrstice1 = 0 
for i in praz1: #Spreminjaj glede na izris!
    st_op1.append(vrstice1)
    vrstice1 = vrstice1 + 1

s1 = st_op1[0:286]
sop1 = st_op1[0:286]

s2 = st_op1[286:383]
sop2 = st_op1[0:97]

s3 = st_op1[383:556]
sop3 = st_op1[0:173]

s4 = st_op1[556:822]
sop4 = st_op1[0:266]


#%% 3. GRAFIČNI IZRIS

#%% HZ
width = 1.0
width1 = 0.6

plt.figure(num=1,figsize=(16,8),dpi=100,facecolor='w',edgecolor='k')
plt.title('RTKLIB 1. serija',fontsize='24')
plt.ylabel('Odstopanja [m]',fontsize='24')
plt.xlabel('Zaporedno število opazovanj [m]',fontsize='24')
plt.grid(True)
plt.bar(sop1,praz1[s1],width,color='g',edgecolor='g',label='1. serija')
plt.xticks(fontsize='24')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0],fontsize='24')

plt.figure(num=2,figsize=(16,8),dpi=100,facecolor='w',edgecolor='k')
plt.title('RTKLIB 2. serija',fontsize='24')
plt.ylabel('Odstopanja [m]',fontsize='24')
plt.xlabel('Zaporedno število opazovanj [m]',fontsize='24')
plt.grid(True)
plt.bar(sop2,praz1[s2],width1,color='g',edgecolor='g',label='2. serija')
plt.xticks(fontsize='24')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0],fontsize='24')

plt.figure(num=3,figsize=(16,8),dpi=100,facecolor='w',edgecolor='k')
plt.title('RTKLIB 3. serija',fontsize='24')
plt.ylabel('Odstopanja [m]',fontsize='24')
plt.xlabel('Zaporedno število opazovanj [m]',fontsize='24')
plt.grid(True)
plt.bar(sop3,praz1[s3],width,color='g',edgecolor='g',label='3. serija')
plt.xticks(fontsize='24')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0],fontsize='24')

plt.figure(num=4,figsize=(16,8),dpi=100,facecolor='w',edgecolor='k')
plt.title('RTKLIB 4. serija',fontsize='24')
plt.ylabel('Odstopanja [m]',fontsize='24')
plt.xlabel('Zaporedno število opazovanj [m]',fontsize='24')
plt.grid(True)
plt.bar(sop4,praz1[s4],width,color='g',edgecolor='g',label='4. serija')
plt.xticks(fontsize='24')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0],fontsize='24')

#%% VIŠINE

plt.figure(num=5,figsize=(16,8),dpi=100,facecolor='w',edgecolor='k')
plt.title('RTKLIB 1. serija',fontsize='24')
plt.ylabel('Odstopanja [m]',fontsize='24')
plt.xlabel('Zaporedno število opazovanj [m]',fontsize='24')
plt.grid(True)
plt.bar(sop1,dH[s1],width,color='r',edgecolor='r',label='1. serija')
plt.xticks(fontsize='24')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0,1.2],fontsize='24')

plt.figure(num=6,figsize=(16,8),dpi=100,facecolor='w',edgecolor='k')
plt.title('RTKLIB 2. serija',fontsize='24')
plt.ylabel('Odstopanja [m]',fontsize='24')
plt.xlabel('Zaporedno število opazovanj [m]',fontsize='24')
plt.grid(True)
plt.bar(sop2,dH[s2],width1,color='r',edgecolor='r',label='2. serija')
plt.xticks(fontsize='24')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0],fontsize='24')

plt.figure(num=7,figsize=(16,8),dpi=100,facecolor='w',edgecolor='k')
plt.title('RTKLIB 3. serija',fontsize='24')
plt.ylabel('Odstopanja [m]',fontsize='24')
plt.xlabel('Zaporedno število opazovanj [m]',fontsize='24')
plt.grid(True)
plt.bar(sop3,dH[s3],width,color='r',edgecolor='r',label='3. serija')
plt.xticks(fontsize='24')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2],fontsize='24')

plt.figure(num=8,figsize=(16,8),dpi=100,facecolor='w',edgecolor='k')
plt.title('RTKLIB 4. serija',fontsize='24')
plt.ylabel('Odstopanja [m]',fontsize='24')
plt.xlabel('Zaporedno število opazovanj [m]',fontsize='24')
plt.grid(True)
plt.bar(sop4,dH[s4],width,color='r',edgecolor='r',label='4. serija')
plt.xticks(fontsize='24')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6],fontsize='24')