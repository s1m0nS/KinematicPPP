#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#%% 1. BRANJE PODATKOV

praz1 = [] #csrs
praz2 = [] #apps
praz3 = [] #magic
praz4 = [] #glab
praz5 = [] #rtklib

#2D
file = open("csrs2D.txt", "r")

for line in file:
    praz1.append(line.split()[1])
praz1 = np.array(praz1)
praz1 = praz1.astype(np.float)

file.close()

file = open("apps2D.txt", "r")

for line in file:
    praz2.append(line.split()[1])
praz2 = np.array(praz2)
praz2 = praz2.astype(np.float)

file.close()

file = open("magic2D.txt", "r")

for line in file:
    praz3.append(line.split()[1])
praz3 = np.array(praz3)
praz3 = praz3.astype(np.float)

file.close()

file = open("glab2D.txt", "r")

for line in file:
    praz4.append(line.split()[1])
praz4 = np.array(praz4)
praz4 = praz4.astype(np.float)

file.close()

file = open("rtklib2D.txt", "r")

for line in file:
    praz5.append(line.split()[1])
praz5 = np.array(praz5)
praz5 = praz5.astype(np.float)

file.close()

#VISINE

dH1 = [] #csrs
dH2 = [] #apps
dH3 = [] #magic
dH4 = [] #glab
dH5 = [] #rtklib

file = open("csrs_dH.txt", "r") #Spreminjaj prebrano datoteko!

for line in file:
    dH1.append(line.split()[1])
dH1 = np.array(dH1)
dH1 = dH1.astype(np.float)

file.close()

file = open("apps_dH.txt", "r") #Spreminjaj prebrano datoteko!

for line in file:
    dH2.append(line.split()[1])
dH2 = np.array(dH2)
dH2 = dH2.astype(np.float)

file.close()

file = open("magic_dH.txt", "r") #Spreminjaj prebrano datoteko!

for line in file:
    dH3.append(line.split()[1])
dH3 = np.array(dH3)
dH3 = dH3.astype(np.float)

file.close()

file = open("glab_dH.txt", "r") #Spreminjaj prebrano datoteko!

for line in file:
    dH4.append(line.split()[1])
dH4 = np.array(dH4)
dH4 = dH4.astype(np.float)

file.close()

file = open("rtklib_dH.txt", "r") #Spreminjaj prebrano datoteko!

for line in file:
    dH5.append(line.split()[1])
dH5 = np.array(dH5)
dH5 = dH5.astype(np.float)

file.close()

#%% 2. SKUPNA STATISTIČNA ANALIZA

praz = praz1.astype(np.float) #Spremeni praz1,praz2,praz3,praz4,praz5
dH = dH1.astype(np.float) #spremeni dH1,dH2,dH3,dH4,dH5

praz_2 = praz**2
dH_2 = dH**2

#HZ - koordinate
praz_povp = np.mean(praz)
praz_min = np.min(praz) #min
praz_max = np.max(praz) #max
praz_std = np.std(praz) #standardni odklon
praz_var = np.var(praz) #varianca
praz_rms = np.sqrt(np.mean(praz_2)) #rms

#VISINE
dH_povp = np.mean(dH) #povprecje visinske razlike
dH_min = np.min(dH) #min
dH_max = np.max(dH) #max
dH_std = np.std(dH) #standardni odklon
dH_var = np.var(dH) #varianca
dH_rms = np.sqrt(np.mean(dH_2)) #rms

#%% 3. IZPIS REZULTATOV

dec = "{:.4f}"
filestat = open("skupstat.txt","w")

#HZ-koordinate
filestat.write("Statistika primerjave HZ koordinat:\n")
filestat.write("Povprecje:      "+str(dec.format(praz_povp))+"\n")
filestat.write("Minimum:        "+str(dec.format(praz_min))+"\n")
filestat.write("Maksimum:       "+str(dec.format(praz_max))+"\n")
filestat.write("St. odklon:     "+str(dec.format(praz_std))+"\n")
filestat.write("Varianca:       "+str(dec.format(praz_var))+"\n")
filestat.write("RMS:            "+str(dec.format(praz_rms))+"\n")
filestat.write("\n")
#VISINE
filestat.write("Statistika primerjave visin:\n")
filestat.write("Povprecje:      "+str(dec.format(dH_povp))+"\n")
filestat.write("Minimum:        "+str(dec.format(dH_min))+"\n")
filestat.write("Maksimum:       "+str(dec.format(dH_max))+"\n")
filestat.write("St. odklon:     "+str(dec.format(dH_std))+"\n")
filestat.write("Varianca:       "+str(dec.format(dH_var))+"\n")
filestat.write("RMS:            "+str(dec.format(dH_rms))+"\n")

filestat.close()

#%% 4. IZRIS PORAZDELITVE NAPAKE MED IZMERO - barchart, matplotlib

st_op1 = [] #csrs
vrstice1 = 0 
for i in praz1: #Spreminjaj glede na izris!
    st_op1.append(vrstice1)
    vrstice1 = vrstice1 + 1


st_op2 = [] #apps
vrstice2 = 0
for i in praz2: #Spreminjaj glede na izris!
    st_op2.append(vrstice2)
    vrstice2 = vrstice2 + 1
    
st_op3 = [] #magic
vrstice3 = 0
for i in praz3: #Spreminjaj glede na izris!
    st_op3.append(vrstice3)
    vrstice3 = vrstice3 + 1
    
st_op4 = [] #glab
vrstice4 = 0
for i in praz4: #Spreminjaj glede na izris!
    st_op4.append(vrstice4)
    vrstice4 = vrstice4 + 1
    
st_op5 = [] #rtklib
vrstice5 = 0
for i in praz5: #Spreminjaj glede na izris!
    st_op5.append(vrstice5)
    vrstice5 = vrstice5 + 1
#-----------------------------------------------------------------------------#
#Prikaži vsako serijo v drugačni barvi - komentiraj vse če nočeš tega!

#CSRS
sc1 = st_op1[0:307]
sc2 = st_op1[307:397]
sc3 = st_op1[397:597]
sc4 = st_op1[597:864]

#APPS - samo 2 seriji
sa1 = st_op2[0:318] 
sa2 = st_op2[318:444] 

#magicGNSS
sm1 = st_op3[0:238]
sm2 = st_op3[239:326]
sm3 = st_op3[326:462]
sm4 = st_op3[462:632]

#gLAB
sg1 = st_op4[0:19]
sg2 = st_op4[19:24]
sg3 = st_op4[24:36]
sg4 = st_op4[36:51]

#RTKLIB
sr1 = st_op5[0:286]
sr2 = st_op5[286:383]
sr3 = st_op5[383:556]
sr4 = st_op5[556:822]

width = 1.0 #sirina stolpca
widthglab = 0.2 #sirina stolpca

#2D
plt.figure(num=1,figsize=(15,10),dpi=100,facecolor='w',edgecolor='k')
plt.subplot(3,1,1) #CSRS
plt.text(30,0.95,'CSRS',ha='left',va='top',fontsize='14',fontstyle='oblique')
plt.grid(True)
plt.title('PRIKAZ ODSTOPANJ HORIZONTALNIH POLOŽAJEV')
#plt.scatter(st_op1,praz1,marker = 'o',s=10.0,color='g',label='CSRS')
#plt.plot(st_op1,praz1,color='g') #povezave
plt.bar(sc1,praz1[sc1],width,color='g',edgecolor='g',label='1. serija')
plt.bar(sc2,praz1[sc2],width,color='b',edgecolor='b',label='2. serija')
plt.bar(sc3,praz1[sc3],width,color='r',edgecolor='r',label='3. serija')
plt.bar(sc4,praz1[sc4],width,color='y',edgecolor='y',label='4. serija')
plt.legend(loc=1,ncol=2,bbox_to_anchor=(1.005,1.241),fontsize='10')
#plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.00), shadow=True, ncol=4)
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])

plt.subplot(3,1,2) #APPS
plt.text(15,0.95,'APPS',ha='left',va='top',fontsize='14',fontstyle='oblique')
plt.grid(True)
plt.ylabel('Odstopanje horizontalnih položajev GNSS od horizontalnih položajev tahimetra [m]',fontsize='12')

#plt.scatter(st_op2,praz2,marker = 'o',s=10.0,color='g',label='APPS')
#plt.plot(st_op2,praz2,color='g') #povezave
plt.bar(sa1,praz2[sa1],width,color='g',edgecolor='g')
plt.bar(sa2,praz2[sa2],width,color='b',edgecolor='b')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])

plt.subplot(3,1,3) #gLAB
plt.text(2,0.95,'gLAB',ha='left',va='top',fontsize='14',fontstyle='oblique')
plt.grid(True)
#plt.scatter(st_op4,praz4,marker = 'o',s=10.0,color='g',label='gLAB')
#plt.plot(st_op4,praz4,color='g') #povezave
plt.bar(sg1,praz4[sg1],widthglab,color='g',edgecolor='g')
plt.bar(sg2,praz4[sg2],widthglab,color='b',edgecolor='b')
plt.bar(sg3,praz4[sg3],widthglab,color='r',edgecolor='r')
plt.bar(sg4,praz4[sg4],widthglab,color='y',edgecolor='y')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])
plt.xlabel('Število opazovanj',fontsize='12')
plt.show()

#%%
plt.figure(num=2,figsize=(15,10),dpi=100,facecolor='w',edgecolor='k')
plt.subplot(2,1,1) #magicGNSS
plt.title('PRIKAZ ODSTOPANJ HORIZONTALNIH POLOŽAJEV')
plt.text(15,0.95,'magicGNSS',ha='left',va='top',fontsize='14',fontstyle='oblique')
plt.grid(True)
#plt.scatter(st_op3,praz3,marker = 'o',s=10.0,color='g',label='magicGNSS')
#plt.plot(st_op3,praz3,color='g') #povezave
plt.bar(sm1,praz3[sm1],width,color='g',edgecolor='g',label='1. serija')
plt.bar(sm2,praz3[sm2],width,color='b',edgecolor='b',label='2. serija')
plt.bar(sm3,praz3[sm3],width,color='r',edgecolor='r',label='3. serija')
plt.bar(sm4,praz3[sm4],width,color='y',edgecolor='y',label='4. serija')
plt.legend(loc=1,ncol=2,bbox_to_anchor=(1.005,1.150),fontsize='10')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])

plt.subplot(2,1,2) #RTKLIB
plt.text(25,0.95,'RTKLIB',ha='left',va='top',fontsize='14',fontstyle='oblique')
plt.grid(True)
#plt.scatter(st_op5,praz5,marker = 'o',s=10.0,color='g',label='RTKLIB')
#plt.plot(st_op5,praz5,color='g') #povezave
plt.bar(sr1,praz5[sr1],width,color='g',edgecolor='g')
plt.bar(sr2,praz5[sr2],width,color='b',edgecolor='b')
plt.bar(sr3,praz5[sr3],width,color='r',edgecolor='r')
plt.bar(sr4,praz5[sr4],width,color='y',edgecolor='y')
plt.ylabel('                                                                                  Odstopanje horizontalnih položajev GNSS od horizontalnih položajev tahimetra [m]',fontsize='12')
plt.xlabel('Število opazovanj',fontsize='12')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])

plt.show()

#%% VISINA
plt.figure(num=3,figsize=(15,10),dpi=100,facecolor='w',edgecolor='k')
plt.subplot(3,1,1) #CSRS
plt.title('PRIKAZ ODSTOPANJ VIŠIN')
plt.text(30,0.95,'CSRS',ha='left',va='top',fontsize='14',fontstyle='oblique')
plt.grid(True)
#plt.scatter(st_op1,dH1,marker = 'o',s=10.0,color='g',label='CSRS')
#plt.plot(st_op1,dH1,color='g') #povezave
plt.bar(sc1,dH1[sc1],width,color='g',edgecolor='g',label='1. serija')
plt.bar(sc2,dH1[sc2],width,color='b',edgecolor='b',label='2. serija')
plt.bar(sc3,dH1[sc3],width,color='r',edgecolor='r',label='3. serija')
plt.bar(sc4,dH1[sc4],width,color='y',edgecolor='y',label='4. serija')
plt.legend(loc=1,ncol=2,bbox_to_anchor=(1.005,1.24),fontsize='10')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])

plt.subplot(3,1,2) #APPS
plt.text(15,0.95,'APPS',ha='left',va='top',fontsize='14',fontstyle='oblique')
plt.grid(True)
#plt.scatter(st_op2,dH2,marker = 'o',s=10.0,color='g',label='APPS')
#plt.plot(st_op2,dH2,color='g') #povezave
plt.bar(sa1,dH2[sa1],width,color='g',edgecolor='g')
plt.bar(sa2,dH2[sa2],width,color='b',edgecolor='b')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])
plt.ylabel('Odstopanje višin GNSS od višin tahimetra [m]',fontsize='14')

plt.subplot(3,1,3) #gLAB
plt.text(2,0.95,'gLAB',ha='left',va='top',fontsize='14',fontstyle='oblique')
plt.grid(True)
#plt.scatter(st_op4,dH4,marker = 'o',s=10.0,color='g',label='gLAB')
#plt.plot(st_op4,dH4,color='g') #povezave
plt.bar(sg1,dH4[sg1],widthglab,color='g',edgecolor='g')
plt.bar(sg2,dH4[sg2],widthglab,color='b',edgecolor='b')
plt.bar(sg3,dH4[sg3],widthglab,color='r',edgecolor='r')
plt.bar(sg4,dH4[sg4],widthglab,color='y',edgecolor='y')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0])
plt.xlabel('Število opazovanj',fontsize='14')

plt.show()

#%% VISINA MAGIC IN RTKLIB - posebej zaradi velikih odstopanj v višini od ostalih
plt.figure(num=4,figsize=(15,10),dpi=100,facecolor='w',edgecolor='k')
plt.subplot(2,1,1) #magicGNSS
plt.title('PRIKAZ ODSTOPANJ VIŠIN')
plt.text(15,2.1,'magicGNSS',ha='left',va='top',fontsize='14',fontstyle='oblique')
plt.grid(True)
#plt.scatter(st_op3,dH3,marker = 'o',s=10.0,color='g',label='magicGNSS')
#plt.plot(st_op3,dH3,color='g') #povezave
plt.bar(sm1,dH3[sm1],width,color='g',edgecolor='g',label='1. serija')
plt.bar(sm2,dH3[sm2],width,color='b',edgecolor='b',label='2. serija')
plt.bar(sm3,dH3[sm3],width,color='r',edgecolor='r',label='3. serija')
plt.bar(sm4,dH3[sm4],width,color='y',edgecolor='y',label='4.serija')
plt.legend(loc=1,ncol=2,bbox_to_anchor=(1.005,1.15),fontsize='10')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2])

plt.subplot(2,1,2) #RTKLIB
plt.text(35,2.1,'RTKLIB',ha='left',va='top',fontsize='14',fontstyle='oblique')
plt.grid(True)
#plt.scatter(st_op5,dH5,marker = 'o',s=10.0,color='g',label='RTKLIB')
#plt.plot(st_op5,dH5,color='g') #povezave
plt.bar(sr1,dH5[sr1],width,color='g',edgecolor='g')
plt.bar(sr2,dH5[sr2],width,color='b',edgecolor='b')
plt.bar(sr3,dH5[sr3],width,color='r',edgecolor='r')
plt.bar(sr4,dH5[sr4],width,color='y',edgecolor='y')
plt.xlabel('Število opazovanj',fontsize='14')
plt.ylabel('                                                     Odstopanje višin GNSS od višin tahimetra [m]',fontsize='14')
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2])
plt.show()