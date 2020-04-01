# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 09:22:15 2020

@author: thinkpad
"""
s1 = ''
seq = input('please input the DNA sequence')
#seq = 'ATGCGACTACGATCGAGGGCCAT'
for i in range(len(seq)):
#get the reserve DNA sequence 
    if seq[i] == 'A':
        s1 = 'T' + s1
    elif seq[i] == 'C':
        s1 = 'G' + s1
    elif seq[i] == 'G':
        s1 = 'C' + s1
    elif seq[i] == 'T':
        s1 = 'A' + s1
    else:
        print('It is not a DNA sequence')
        break
if len(seq)==len(s1):
    print(s1)