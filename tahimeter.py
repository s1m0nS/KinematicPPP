#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''Analiza koordinat terestrične in GNSS izmere
   Simon Šanca
'''

import matplotlib.pyplot as plt
import numpy as np
import math

#%% 0. BRANJE PODATKOV

#x, y = np.loadtxt('dat.txt', delimeter='    ',unpack=True)

file = open("tah_neorientirano.txt", "r")

#points = [] #x,y,H
e = []
n = []
h = []

for line in file:
    e.append(float(line.split()[1]))
    n.append(float(line.split()[2]))
    h.append(float(line.split()[3]))
    
file.close()

#%% FUNKCIJE; za uporabo

def dol(y1:float,x1:float,y2:float,x2:float): #iz kooridnat
    dolzina = math.sqrt((y2-y1)**2 + (x2-x1)**2)
    return dolzina

def ni(y1:float, x1:float, y2:float, x2:float):
    
    #FUNKCIJA
    delY = y2-y1
    delX = x2-x1

    if (delY > 0) and (delX > 0): #1. kvadrant
        ni = math.atan(((delY/delX)))
    elif (delY > 0) and (delX < 0): #2. kvadrant
        ni = math.atan(((delY/delX))) + math.pi
    elif (delY < 0) and (delX < 0): #3. kvadrant
        ni = math.atan(((delY/delX))) + math.pi
    elif (delY < 0) and (delX > 0): #4. kvadrant
        ni = math.atan(((delY/delX))) + 2*math.pi
    elif delY == 0 and delX < 0:
        ni = math.pi
    elif delY > 0 and delX == 0:
        ni = math.pi/2
    elif delY < 0 and delX == 0:
        ni = (3/2)*math.pi
    elif delY == 0:
        ni = print("Smerni kot ne obstaja!!!")
    elif delX == 0:
        ni == 0

    #nist = nidms(ni)
    #print("ni[dms] = {:3.4f}".format(nist))
    #print()
	
    return ni
    
def rad2dms(rad):
    dms = math.degrees(rad)
    return dms
    
def dms2rad(dms):
    rad = math.radians(dms)
    return rad

#%% 2. ROTACIJA KOORDINAT TAHIMETRA na pravo območje
#                    FGG1               #FGG2           
niF1F2 = ni(460878.787,100784.216,460938.078,100811.610)
skot_dms = rad2dms(niF1F2)

print(skot_dms)
#ni = dms2rad(0.1) #- spreminjaj kot
ni = niF1F2

#Rotacija v 2D, upoštevamo smerni kot niFGG1_FGG2

er = []
nr = []

for i in e,n,h:
    
    #0. Napaka zaradi napačnega vnosa koordinat v instrument, odštejemo razliko FGG1-FGG2, razlika v E - koordinati za 10 m
    
    pravi_e = np.array(e) + 10
    pravi_n = np.array(n) #pustiš kot je!
      
    #1. Središčna točka rotacije - FGG1: 460878.787 100784.216
    rce = float(460878.787)
    rcn = float(100784.216)
    
    #2. Odštejemo odstopanja od središčne točke
    se = np.array(pravi_e) - rce
    sn = np.array(pravi_n) - rcn
    
    #3. Rotacija za smerni kot ni okoli središčne točke FGG1
    er = np.array(se) * math.cos(ni) + np.array(sn)*math.sin(ni)
    nr = -np.array(se)*math.sin(ni) + np.array(sn)*math.cos(ni)
    
    #4. Postavimo koordinate na pravo mesto
    re = er + rce
    rn = nr + rcn
    
    #5. Prištejemo višinam,  h-prizme = 5,9 cm
    pravi_h = np.array(h) + 0.059

    break


#%% 2.1 IZPIS POPRAVLJENIH KOORDINAT v txt

file = open("tah_prave.txt","w")

for i in range(len(re)):
    file.write('{}    {:6.4f}    {:6.4f}    {:3.3f}\n'.format('KIN',re[i],rn[i],pravi_h[i]))

file.close()

#%% 3. GRAFIČNI IZRIS

#FGG1:   460878.787    100784.216    321.115
#FGG2:   460938.078    100811.610    321.116
#FGG4:   460888.287    100763,782    321.115

fgg124e = [460878.787,460938.078,460888.287]
fgg124n = [100784.216,100811.610,100763.782]

#Izris koordinat stebrov + koordinat točk TAH, vse serije
fig = plt.figure(1)
plt.figure(num=1, figsize=(50,50),dpi=100,facecolor='w',edgecolor='k')
plt.title("TOČKE TAHIMETRIČNE IZMERE")
plt.grid(True)
plt.autoscale(enable = True, axis = 'both')
plt.ylabel("n [m]")
plt.xlabel("e [m]")
plt.scatter(fgg124e,fgg124n,marker = 'o',s=10.0,color = 'k',label='FGG1,FGG2,FGG4') #FGG1 in FGG2
plt.text(fgg124e[0],fgg124n[0], "FGG1",color = 'k',style = 'italic',fontsize = 11)
plt.text(fgg124e[1],fgg124n[1], "FGG2",color = 'k',style = 'italic',fontsize = 11)
plt.text(fgg124e[2],fgg124n[2], "FGG4",color = 'k',style = 'italic',fontsize = 11)
#plt.scatter(e,n,marker = '+') # neorientirane, pogrešene zaradi stojišča
plt.scatter(re,rn,marker = '.', s=1.0, color = 'r',label='Tahimeter') #ostale popravljene in rotirane merjene točke
plt.legend()
plt.gca().set_aspect('equal',adjustable='box')
plt.show()

#%% IZRIS TAHIMETRIČNIH TOČK PO SERIJAH

file = open("tah4.txt",'r') #spremeni tah1.txt,tah2.txt,tah3.txt,tah4.txt - odvisno od serije

e1 = []
n1 = []
h1 = []

for line in file:
    e1.append(float(line.split()[1]))
    n1.append(float(line.split()[2]))
    h1.append(float(line.split()[3]))
    
file.close()

#Izris serij
plt.figure(num=2, figsize=(20,20),dpi=100,facecolor='w',edgecolor='k')
plt.title("TOČKE TAHIMETRIČNE IZMERE")
plt.grid(True)
plt.autoscale(enable = True, axis = 'both')
plt.ylabel("n [m]")
plt.xlabel("e [m]")
plt.ticklabel_format(useOffset=False)
#plt.scatter(e1,n1,marker = 'o',s=3.0,color = 'r') #FGG1 in FGG2
plt.gca().set_aspect('equal',adjustable='box')
plt.show()