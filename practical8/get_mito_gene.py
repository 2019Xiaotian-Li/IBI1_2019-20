# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 09:53:22 2020

@author: thinkpad
"""

Name = []
gene = []
s=''
count = 0
flag = False
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
for line in xfile:
    if line.startswith ('>'):
        if s!='':
            gene.append(s)
        s = line[1:8]
        Name.append(s)
        count = count + 1
        s = ''
    else:
        s = s + line 
gene.extend(s)

seq = input ('please input the gene name')
for i in range (count):
    if seq == Name[i]:
        print(gene[i])
        flag = True
        break
if flag == False:
    print ('No such sequence here')
    
try:
	xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
finally:
	if xfile:
		xfile.close()
fout = open('mito_gene.fa','w')
line1 = Name[i]
line2 = gene[i]
fout.write(line1)
fout.write(line2)
fout.close()

  