# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:11:41 2020

@author: thinkpad
"""

import numpy as np
import matplotlib.pyplot as plt

#t is the time
t = [0]
#n is popularity
n = 10000
β = 0.3
γ = 0.05
time = 1000
for j in range (0,11):
    t = [0]
    #suspectible
    sus = [int(n - 1 - (n * j / 10))] 
    #infected
    inf = [1]
    #recovered
    rec = [0]
    if sus[0] < 0:
        sus = [0]
        inf = [0]
    for i in range (0,time):
        a = np.random.choice(range(2),sus[i],p=[1-β*(inf[i]/n),β*(inf[i]/n)])
        num1 = np.sum(a == 1)
        b = np.random.choice(range(2),inf[i],p=[1-γ,γ])
        num2 = np.sum(b == 1)
        sus.append (sus[i] - num1)
        inf.append (inf[i] + num1 - num2)
        rec.append (rec[i] + num2)
        t.append (i)
    inf_1 = inf
    lab = str(j * 10) +'%'
    plt.plot(t, inf_1, label=lab)
    plt.legend(loc = 'upper right')

#show the plot
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model with different vaccination rates')
plt.show
plt.savefig('SIRmodel', type='png' )
