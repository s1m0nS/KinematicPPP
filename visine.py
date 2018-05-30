#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Primerjava višin

Nadmorske višine SitraNet in Tahimetrična izmera

h_prizme = 5.9 cm, vse višine tahimetra so preračuane na fazni center antene sprejemnika

"""
import matplotlib.pyplot as plt

#%% 1. BRANJE PODATKOV

file = open("tah1.txt", "r") 

e1 = []
n1 = []
h1 = []
st1 = []

vrstice1 = 0
for line in file:
    e1.append(float(line.split()[1]))
    n1.append(float(line.split()[2]))
    h1.append(float(line.split()[3]))
    st1.append(vrstice1)
    vrstice1 = vrstice1 + 1
file.close()

e2 = []
n2 = []
h2 = []
st2 = []

vrstice2 = 0
file2 = open("csrs1.txt", "r")

for line in file2:
    e2.append(float(line.split()[1]))
    n2.append(float(line.split()[2]))
    h2.append(float(line.split()[3]))
    st2.append(vrstice2)
    vrstice2 = vrstice2 + 1
file2.close()

#%% 2. PRIMERJAVA VIŠIN

avgh1 = sum(h1) / len(h1)
avgh2 = sum(h2) / len(h2)
avg = abs(float(avgh1 - avgh2))
print(avg)

#%% 3. GRAFIČNI IZRIS
plt.figure(num=1, figsize=(5,5),dpi=100,facecolor='w',edgecolor='k')
plt.title('Primerjava višin TAH in GNSS')
plt.grid(True)
plt.xlabel('Zaporedna številka opazovanj')
plt.ylabel('Nadmorska višina izmerjenih točk [m]')
plt.ticklabel_format(useOffset=False)
#TAH
plt.scatter(st1,h1,marker = '+',s=10.0,color='r',label='Tahimeter')
plt.plot(st1,h1,color='r') #povezave
#GNSS
plt.scatter(st2,h2,marker = 'o',s=10.0,color='g',label='GNSS')
plt.plot(st2,h2,color='g') #povezave
plt.xlim(xmin=-25)
plt.legend(loc=4)
plt.show()
