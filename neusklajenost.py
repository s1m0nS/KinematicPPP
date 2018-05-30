#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Odprava neusklajenosti koordinatnih sistemov med TAH in GNSS
"""

import numpy as np

#%% 2. Odprava neusklajenosti koordinatnih sistemov TAH in GNSS


#TAHIMETER!
file = open("tah3.txt",'r') 

tahe = []
tahn = []
tahH = []

for line in file:
    tahe.append(float(line.split()[1]))
    tahn.append(float(line.split()[2]))
    tahH.append(float(line.split()[3]))
    
file.close()


#GNSS!
file = open("rtklib3.txt",'r') 

gnsse = []
gnssn = []
gnssH = []

for line in file:
    gnsse.append(float(line.split()[1]))
    gnssn.append(float(line.split()[2]))
    gnssH.append(float(line.split()[3]))
    
file.close()
#-----------------------------------------------------------------------------#

fgg2_tah = [460938.078,100811.610,321.116] #FGG2 TAH
fgg4_tah = [460888.291,100763.788,321,110] #FGG4 TAH

#fgg2_gnss = [460938.592,100812.090,321.406] #1
#fgg2_gnss = [460938.199,100812.160,321.393] #2

fgg4_gnss = [460887.868,100764.140,321.253] #3
#fgg4_gnss = [460887.837,100764.145,321.117] #4

#Razlika GNSS-TAH FGG2
#re = fgg2_gnss[0] - fgg2_tah[0]
#rn = fgg2_gnss[1] - fgg2_tah[1]
#rH = fgg2_gnss[2] - fgg2_tah[2]

#Razlika GNSS-TAH FGG4
re = fgg4_gnss[0] - fgg4_tah[0]
rn = fgg4_gnss[1] - fgg4_tah[1]
rH = fgg4_gnss[2] - fgg4_tah[2]

print(re,rn,rH)
re = abs(re)
print(re,rn,rH)

#Usklajene koordinate GNSS s koordinatami TAH
uE = np.array(gnsse) - re
uN = np.array(gnssn) - rn
uH = np.array(gnssH) - rH

a = np.size(uE)
b = np.size(uN)
c = np.size(uH)
print("Test vrstic:",a,b,c)

#IME 
#ime = np.full((1,a),'KIN', dtype=str)

np.savetxt('urtklib3.txt',np.c_[uE,uN,uH],fmt='%.3f',delimiter='    ')
