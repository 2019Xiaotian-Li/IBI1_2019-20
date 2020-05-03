# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 17:47:06 2020

@author: thinkpad
"""

s = input(r"Please input numbers to compute 24: (use ',' to divide them)")
num = []
for item in s.split(","):
   num.append(float(item))
flag = False
while flag == False:
    flag = True
    for item in num:
        if ((item > 23) or (item < 1)):
            flag = False
            print("Invalid number " + str(int(item)) + ", which should have been between integers 1 to 23.")
            s = input(r"Please input numbers to compute 24: (use ',' to divide them)")
            num = []           
            for item in s.split(","):
                num.append(float(item))
            break
            
   
# List all possible situations
def cal(l: int):
   return_list = []
   for i in list(range(l-1)):
      for j in list(range(i+1,l)):
          for k in range(6):
             return_list.append([i, j, k])
   return (return_list)
   


sc = [[], []]
for i in range(2, len(num) + 1):
   sc.append(cal(i))
   
all_sit = []
all_sit_tmp = []
sci = []
for i in range(len(num)):
   sci.append(sc[len(num) - i])
   
# Select one operation [] from one stage.  
def select_copy(l: list):
   l_copy = l.copy()
   if len(l_copy) == len(sci) - 1:
      all_sit.append(l_copy)
   for item in sci[len(l)]:
      l.append(item)
      select_copy(l)
      l.pop()
   
select_copy([])
 
# Apply
def f(i:int, j:int, k:int, l:list):
    if (k == 0):
        value = l[i] + l[j]
    elif (k == 1):
        value = l[i] - l[j]
    elif (k == 2):
        value = l[j] - l[i]
    elif (k == 3):
        value = l[i] * l[j]
    elif (k == 4) and (l[j] != 0) :
        value = l[i] / l[j]
    elif (k == 5) and (l[i] != 0):
        value = l[j] / l[i]
    else:
        value = 0
    if (value == 24):
        return (0)
    else:
        l[i] = value
        l.pop(j)
        return (-1)
    
a = 0   
n = 1
for item in all_sit:
   num_copy=num.copy()
   for jtem in item:
       if (f(jtem[0], jtem[1], jtem[2], num_copy) == 0 ) and a == 0:
          print("Yes")
          print("Time: " + str(n))
          a = -1
       else:
          n += 1
if a == 0:
    print("No")