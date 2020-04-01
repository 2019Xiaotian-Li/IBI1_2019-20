# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 09:53:22 2020

@author: thinkpad
"""

Name = []
gene = []
leng = []
s=''
count = 0
length = 0
flag = False
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
for line in xfile:
    if line.startswith ('>'):
        if s!='':
            gene.append(s)
            leng.append(length)
        s = line[1:8]
        length = 0
        Name.append(s)
        count = count + 1
        s = ''
    else:
        s = s + line 
        length = length + len(line)
gene.append(s)

seq = input ('please input the gene name')
l = int(input('please input the gene length'))
for i in range (count):
    if seq == Name[i]:
        print(gene[i])
        flag = True
        break
if flag == False:
    print ('No such sequence here')
    
fout = open('mito_gene.fa','w')
line1 = Name[i] + '   ' + str(leng[i]) + '\n'
line2 = gene[i]
fout.write(line1)
fout.write(line2)

try:
	xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
finally:
	if xfile:
		xfile.close()
fout.close()

  