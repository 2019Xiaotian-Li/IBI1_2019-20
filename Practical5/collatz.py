# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:22:06 2020

@author: thinkpad
"""

n = int(input('please input n'))
print(n)
while n>1:
    if n % 2 == 0 :
        n = (n - n % 2) / 2
    else:
        n = 3 * n + 1
    print('n →', n)
    