# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:15:28 2020

@author: thinkpad
"""
# Here is 4.1
a = int(input('please input a'))
b = int(str(a)+str(a))
c = b/7
d = c/11
e = d/13
print ('a=',str(a),'  e=',str(e))
if a == e :
    print ('a is equal to e')
elif a > e:
    print ('a is larger than e')
else:
    print ('a is smaller than e')

#explanation: For a three-digit number such as 123 and 321, write it twice equals to mutiply 1001
#             and 1001 = 7 * 11 * 13. So a = e.
    
    
# Here begins 4.2
# explanation: For a boolean variable, there are only 2 possible values : 0 and 1 (True and False)
#              if X!=Y, it means (X=1 and Y=0) or (X=0 and Y=1)
#              which equals (X and not Y) or (Y and not X)
#Script is here. (Modify directly on the text to change the import)
X = True
Y = False
Z = (X and not Y) or (Y and not X)
W = X!=Y
print ('Z=',Z,'  W=',W)
if Z == W :
    print ('Z is the same as W')