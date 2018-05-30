#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simon Šanca: Primerjava tahimetrične in GNSS izmere
"""
import matplotlib.pyplot as plt
import math
import numpy as np

#%% 1. PRIMERJAVA VIŠIN:  A-Tahimeter, G-GNSS

def dol(y1:float,x1:float,y2:float,x2:float): #iz kooridnat
    dolzina = math.sqrt((y2-y1)**2 + (x2-x1)**2)
    return dolzina

def pravokotnaRazdalja(p1,p2,p3): #Pravokotna razdalja
    pravokotnaRazdalja = np.linalg.norm(np.cross(p2-p1, p1-p3))/np.linalg.norm(p2-p1) #cross - vektorski produkt norm - norma
    return pravokotnaRazdalja 
 
def tockaNaPravokotnici(p1,p2,p3): #Pravokotna razdalja - preureditev iz Matlab funkcije
    p = [p2[0] - p1[0],p2[1] - p1[1]] #vektor B-A
    dAB = p[0]*p[0] + p[1]*p[1]  #dolzina AB
    if(dAB == 0):
        return [0,0]
    u = float(((p3[0]-p1[0])*p[0]+(p3[1]-p1[1])*p[1]))/float(dAB) #skalarni produkt (AB*AT)/dAB
    point = [p1[0] + u*p[0],p1[1] + u*p[1]] #point = A+v*AB
    return point

def resi(A,G,AH,GH): #G - GNSS, A-tahimeter, AH - H-tah, GH - H-gnss
    
    pravokotneTockeX = []
    pravokotneTockeY = []
    izrisPravokotnihCrt = [] #za graf
    praz = []
    tah1H = []
    tah2H = []
    gnssH = []

    file = open("rezultati.txt","w") #Izpis rezultatov
    file.write("A(tahimeter),  B(tahimeter),  GNSS,  Tocka pravokotnice, Razdalja do pripadajoce premice TAH\n")
    for k in range(len(G)): #sprehod cez vse GNSS
        i = 0 #prva tocka za vektor na katerega projekciramo
        j = 1 #druga tocka za vektor na katerega projekciramo
        print(k) #st. iteracije
        Ai = i
        Aj = j
        minP = G[k] 
        minDol = math.inf; #najmanjsa oddaljenost od premice
        while j < len(A): #cez vse TAH
    
            p = tockaNaPravokotnici(A[i],A[j],G[k]) #(A,B,T)
            if(A[i][0] <= A[j][0]): #katera manjsa po x osi
                
                if p[0] >= A[i][0] and p[0] <= A[j][0]: #ce je pravokotna tocka znotraj intervala na x osi
                    if(k == 87): print(G[k],p)
                    if(A[i][1] <= A[j][1]): #katera je manjsa po y osi
                        if(p[1] >= A[i][1] and p[1] <= A[j][1]): # pravokotna tocka znotraj intervala na y osi
                            d = pravokotnaRazdalja(A[i],A[j],G[k]) #izračun pravokotne razdalje na premico
                            if(d < minDol): #trenutna dolzina < najmanjse dolzine
                                minP = p
                                minDol = d 
                                Ai = i
                                Aj = j
                    elif(A[i][1] > A[j][1]): #ce je vecja po y osi
                        if(p[1] <= A[i][1] and p[1] >= A[j][1]):
                            d = pravokotnaRazdalja(A[i],A[j],G[k]) #izračun pravokotne razdalje na premico
                            if(d < minDol):
                                minP = p
                                minDol = d
                                Ai = i
                                Aj = j
                    
            elif(A[i][0] > A[j][0]): #ce je vecja po x osi
                if p[0] <= A[i][0] and p[0] >= A[j][0]:
                    if(A[i][1] <= A[j][1]):
                        if(p[1] >= A[i][1] and p[1] <= A[j][1]):
                            d = pravokotnaRazdalja(A[i],A[j],G[k]) #izračun pravokotne razdalje na premico
                            if(d < minDol):
                                minP = p
                                minDol = d
                                Ai = i
                                Aj = j
                    elif(A[i][1] > A[j][1]):  #ce je vecja po y osi - enako kot zgoraj
                        if(p[1] <= A[i][1] and p[1] >= A[j][1]):
                            d = pravokotnaRazdalja(A[i],A[j],G[k]) #izračun pravokotne razdalje na premico
                            if(d < minDol):
                                minP = p
                                minDol = d
                                Ai = i
                                Aj = j
                           
            i = i+1 #vzame naslednji dve TAH tocki
            j = j+1
        if(minDol != math.inf): #ce minDol ni enaka neskoncnosti --> najmanjsa pravokotna tocka na premico AB
            if (minDol < 1): #Vecjih dolzin od 1 m ne shranjujemo med rezultate ker so posledica izgube signala GNSS med izmero
                
                #FORMAT izpisa na 3 decimalna mesta
                dec = "{:.4f}" #koordinate x,y 
                #TAH
                tah1x = dec.format(A[Ai][0])
                tah1y = dec.format(A[Ai][1])
                tah2x = dec.format(A[Aj][0])
                tah2y = dec.format(A[Aj][1])
                visinaTAH1 = dec.format(AH[Ai]) #A
                visinaTAH2 = dec.format(AH[Aj]) #B
                #GNSS
                gnss_x = dec.format(G[k][0])
                gnss_y = dec.format(G[k][1])
                visinaGNSS = dec.format(GH[k])
                #Tocka pravokotnice
                prav_x = dec.format(minP[0])
                prav_y = dec.format(minP[1])
                #Dolzina
                prav_dol = dec.format(minDol)
            
                file.write("("+str(tah1x)+","+str(tah1y)+","+visinaTAH1+")  ("+str(tah2x)+","+ str(tah2y)+","+visinaTAH2+")  ("+str(gnss_x)+","+str(gnss_y)+","+visinaGNSS+")  ["+str(prav_x)+","+ str(prav_y)+"]  " + str(prav_dol)+"\n")
                if(minDol < 1 ): #uporabimo za izris pravokotnih crt, dolge ne izrisujemo
                    izrisPravokotnihCrt.append([G[k][0],G[k][1],minP[0],minP[1]]) #v tabelo shranimo podatke o tem katera pravokotna tocka pripada kateri gnss tocki
                pravokotneTockeX.append(minP[0]) #za izris pravokotnih tock
                pravokotneTockeY.append(minP[1])
                tah1H.append(AH[Ai])
                tah2H.append(AH[Aj])
                gnssH.append(GH[k])
                praz.append(minDol)
                
    file.close()
    
    return [pravokotneTockeX,pravokotneTockeY,praz,izrisPravokotnihCrt,tah1H,tah2H,gnssH]
#%% 2. BRANJE PODATKOV

A = [] #TAH
AH= [] #Visine TAH
Ax = []
Ay = []

G = [] #GNSS
GH = [] #Visine GNSS
Gx = []
Gy = []

#TAH
file = open("tah1.txt", "r") #Spreminjaj prebrano datoteko za primerjavo

for line in file:
    x = float(line.split()[1])
    y = float(line.split()[2])
    A.append([x,y])
    AH.append(float(line.split()[3]))
    Ax.append(x)
    Ay.append(y)
    
A = np.array(A)

file.close()

#GNSS
file = open("csrs1.txt","r") #Spreminjaj prebrano datoteko za primerjavo

for line in file:
    x = float(line.split()[0])
    y = float(line.split()[1])
    G.append([x,y])
    GH.append(float(line.split()[2]))
    Gx.append(x)
    Gy.append(y)
    
G = np.array(G)

file.close()

#RESITEV PRIMERJAVE:
resitev = resi(A,G,AH,GH) #(TAH,GNSS,H-tah,H-GNSS)

print("------------------------------------------------------------------------")
print("Konec primerjave!")
print("Rezultati primerjave horizontalnih položajev TAH in GNSS so v datoteki rezultati.txt, v isti mapi!")
print("Sledi statistična analiza!")
print("Rezultati statistične analize so v datoteki statistika.txt, v isti mapi!")
print("Sledi grafični izris!")
print("Graf 1 - Primerjava HZ položajev")
print("Graf 2 - Primerjava višin")
print("Za naslednjo analizo spremenite imena vhodnih datotek in znova zaženite program!")
print("------------------------------------------------------------------------")


#%% 3. PRIMERJAVA VISIN

"""
Nadmorske visine SitraNet in Tahimetricna izmera
h_prizme = 5.9 cm, vse visine tahimetra so preracuane na fazni center antene sprejemnika
"""
praz = np.array(resitev[2]) #razdalja med premico TAH in GNSS
tahH1 = np.array(resitev[4]) #A
tahH2 = np.array(resitev[5]) #B
gnssH = np.array(resitev[6]) #GNSS
tahHi = (tahH1 + tahH2)/2 #povprecje A-B potrebno za izris

st_op = [] #stevilo opazovanj
vrstice = 0 #

for i in resitev[4]: 
    st_op.append(vrstice)
    vrstice = vrstice + 1

praz_2 = (praz)**2
tahH = (tahH1 + tahH2)/2 #povprecje A-B
dH = abs(tahH - gnssH) #razlike v visini TAH-GNSS
dH_2 = (dH)**2 # dH^2


#%% 4. STATISTIČNA ANALIZA - za vsako serijo posebej

#%% 4.1 HZ KOORDINATE

praz_povp = np.mean(praz) #povprecje
praz_min = np.min(praz) #min
praz_max = np.max(praz) #max
praz_std = np.std(praz) #standardni odklon
praz_var = np.var(praz) #varianca
praz_rms = np.sqrt(np.mean(praz_2)) #rms

#%% 4.2 VISINE

dH_povp = np.mean(dH) #povprecje visinske razlike
dH_min = np.min(dH) #min
dH_max = np.max(dH) #max
dH_std = np.std(dH) #standardni odklon
dH_var = np.var(dH) #varianca
dH_rms = np.sqrt(np.mean(dH_2)) #rms

#%% 4.3 IZPIS REZULTATOV

dec = "{:.4f}"
filestat = open("statistika.txt","w")

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

#IZPIS RAZLIK VISIN
dHizpis = dH.tolist()
filedH = open("rtklib_dH.txt","a")
for i in range(len(dH)):
    filedH.write('{}    {:.4f}\n'.format('dH',abs(dH[i])))

filedH.close()

#%% 5. GRAFIČNI IZRIS

#%% 5.1 HZ-koordinate TAH in GNSS

#Koordinate stebrov
fgg124e = [460878.787,460938.078,460888.287]
fgg124n = [100784.216,100811.610,100763.782]

##IZRIS
plt.figure(num=1,dpi=100,facecolor='w',edgecolor='k')
plt.title('Primerjava 2D položajev: TAH in GNSS')   
plt.grid(True)                                     
plt.autoscale(enable = True, axis = 'both')
plt.ylabel('n [m]')
plt.xlabel('e [m]')
plt.ticklabel_format(useOffset=False)

#STEBRI
plt.scatter(fgg124e,fgg124n,marker = 'o',s=10.0,color = 'k') #FGG1 in FGG2
plt.text(fgg124e[0],fgg124n[0], "FGG1",color = 'k',style = 'italic',fontsize = 11)
plt.text(fgg124e[1],fgg124n[1], "FGG2",color = 'k',style = 'italic',fontsize = 11)
plt.text(fgg124e[2],fgg124n[2], "FGG4",color = 'k',style = 'italic',fontsize = 11)

#TAH
plt.scatter(Ax,Ay,marker='+',color='r',label='TAH')
plt.plot(Ax,Ay,color='r') #poveži

#GNSS
plt.scatter(Gx,Gy,marker='o',color='g',label='GNSS')
plt.plot(Gx,Gy,color='g')

#Pravokotne tocke x,y
plt.scatter(resitev[0],resitev[1],marker="*",color="b",label='PravT')

#Pravokotne crte, ki povezujejo GNSS s premico TAH - odstopanja med trajektorijama
for tocke in resitev[3]:
    plt.plot([tocke[0],tocke[2]],[tocke[1],tocke[3]], color='b')
        
plt.legend(loc=2)
plt.gca().set_aspect('equal',adjustable='box')
plt.show()

#%% 5.2 Visine TAH in GNSS
plt.figure(num=2, figsize=(10,6),dpi=100,facecolor='w',edgecolor='k')
plt.title('Primerjava višin TAH in GNSS')
plt.grid(True)
plt.xlabel('Zaporedna številka opazovanj')
plt.ylabel('Nadmorska višina izmerjenih točk [m]')
plt.ticklabel_format(useOffset=False)
#TAH
plt.scatter(st_op,tahHi,marker = '+',s=10.0,color='r',label='Tahimeter')
plt.plot(st_op,tahHi,color='r') #povezave
#GNSS
plt.scatter(st_op,gnssH,marker = 'o',s=10.0,color='g',label='GNSS')
plt.plot(st_op,gnssH,color='g') #povezave
plt.xlim(xmin=-5)
plt.legend(loc=1)
plt.show()

print("Konec izrisa!")