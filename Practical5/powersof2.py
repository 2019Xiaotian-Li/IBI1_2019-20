# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:57:45 2020

@author: thinkpad
"""
# pseudocode:
# Purpose: Convert the number to binary
# input n
# repeat
#   a[j] = n mod 2
#   n = int(n / 2)
#   j = j + 1
# until n=1 (or n=0)  
# for i = j to 1
#   connect the remainder from back to front into string s
# output s
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
j = 0
n = int(input('please input n'))
s = str(n) + ' is '
while n>0:
   a[j] = n % 2
   n = ( n - a[j] ) / 2
   j+=1
s = s + '2**' + str(j-1)
for i in range (2,j+1):
      k = j - i
      if a[k] > 0 : s = s + ' + 2**' + str(k)
print (s)