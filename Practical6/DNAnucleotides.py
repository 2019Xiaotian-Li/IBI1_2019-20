# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:44:15 2020

@author: thinkpad
"""
#reset the variables
A = 0
C = 0
G = 0
T = 0
s = input()
# input s
n = len (s)
# for i = 0 to n-1
# count(A,C,G,T)
for i in range (0,n):
    c = s[i-1]
    if c == 'A':
        A = A + 1
    elif c == 'C':
        C = C + 1
    elif c == 'G':
        G = G + 1
    elif c == 'T':
        T = T + 1
    else:
        print('It is not a DNA sequence')



import matplotlib.pyplot as plt
# set parameters
labels = ['A' , 'G' , 'C' , 'T']
sizes = [A , G , C , T]
explode = (0 , 0 , 0 , 0) 
colors = ['red', 'yellow', 'blue', 'green',]
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90,colors=colors)
plt.axis('equal')
plt.title('Counting	DNA	nucleotides')
print (' A = ', A,' , G = ',G, ' , C = ',C,' , T = ', T) 
plt.show()