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
#suspectible
sus = [n- 1]
#infected
inf = [1]
#recovered
rec = [0]
for i in range (0,time-1):
    a = np.random.choice(range(2),sus[i],p=[1-β*(inf[i]/n),β*(inf[i]/n)])
    num1 = np.sum(a == 1)
    b = np.random.choice(range(2),inf[i],p=[1-γ,γ])
    num2 = np.sum(b == 1)
    sus.append (sus[i] - num1)
    inf.append (inf[i] + num1 - num2)
    rec.append (rec[i] + num2)
    t.append (i)


#show the plot
plt.plot(t, sus, color='green', label='suspectible')
plt.plot(t, inf, color='red', label='infected')
plt.plot(t, rec, color='skyblue', label='recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model')
plt.legend(loc = 'upper right')
plt.show
plt.savefig('SIRmodel', type='png' )
