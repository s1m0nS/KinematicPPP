#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

#%% 0. BRANJE PODATKOV

# CSRS
file1 = open("csrs.txt", "r")

e1 = []
n1 = []
h1 = []

for line in file1:
    e1.append(float(line.split()[0]))
    n1.append(float(line.split()[1]))
    h1.append(float(line.split()[2]))
file1.close()

file2 = open("apps.txt")

e2 = []
n2 = []
h2 = []

for line in file2:
    e2.append(float(line.split()[0]))
    n2.append(float(line.split()[1]))
    h2.append(float(line.split()[2]))
file2.close()

# magicGNSS

file3 = open("magic.txt", "r")
e3 = []
n3 = []
h3 = []

for line in file3:
    e3.append(float(line.split()[0]))
    n3.append(float(line.split()[1]))
    h3.append(float(line.split()[2]))
file3.close()

#GLAB - igs efemeride
file4 = open("gLAB.txt", "r")

e4 = []
n4 = []
h4 = []

for line in file4:
    e4.append(float(line.split()[0]))
    n4.append(float(line.split()[1]))
    h4.append(float(line.split()[2]))
file4.close()

#RTKLIB - igs efemeride
file5 = open("rtklib.txt", "r")

e5 = []
n5 = []
h5 = []

for line in file5:
    
    e5.append(float(line.split()[0]))
    n5.append(float(line.split()[1]))
    h5.append(float(line.split()[2]))

file5.close()


# %% 2. IZRIS GNSS

#Koordinate stebrov
fgg124e = [460878.787,460938.078,460888.287]
fgg124n = [100784.216,100811.610,100763.782]

plt.figure(num=1, figsize=(20,20),dpi=100,facecolor='w',edgecolor='k')
plt.title("Točke GNSS")
plt.grid(True)
plt.autoscale(enable = True, axis = 'both')
plt.ylabel("n [m]")
plt.xlabel("e [m]")
plt.ticklabel_format(useOffset=False)
plt.scatter(fgg124e,fgg124n,marker = 'o',s=10.0,color = 'k') #FGG1 in FGG2
plt.text(fgg124e[0],fgg124n[0], "FGG1",color = 'k',style = 'italic',fontsize = 11)
plt.text(fgg124e[1],fgg124n[1], "FGG2",color = 'k',style = 'italic',fontsize = 11)
plt.text(fgg124e[2],fgg124n[2], "FGG4",color = 'k',style = 'italic',fontsize = 11)

#Izris GNSS - spreminjaj izris z odkomentiranjem vrstic
#plt.scatter(e1,n1,marker = 'o', s=5.0, color = 'g',label='CSRS') 
plt.scatter(e2,n2,marker = 'o', s=5.0, color = 'g',label='APPS')
#plt.scatter(e3,n3,marker = 'o', s=5.0, color = 'g',label='magicGNSS')
#plt.scatter(e4,n4,marker = 'o', s=5.0, color = 'g',label='gLAB')
#plt.scatter(e5,n5,marker = 'o', s=5.0, color = 'g',label='RTKLIB')
plt.legend()
plt.gca().set_aspect('equal',adjustable='box')
plt.show()
